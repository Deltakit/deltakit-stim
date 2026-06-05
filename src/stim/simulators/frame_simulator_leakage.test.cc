// Copyright 2021 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "stim/simulators/frame_simulator.h"

#include "gtest/gtest.h"

#include "stim/circuit/circuit.test.h"
#include "stim/gen/gen_surface_code.h"
#include "stim/mem/simd_word.test.h"
#include "stim/util_bot/test_util.test.h"

using namespace stim;

TEST_EACH_WORD_SIZE_W(FrameSimulatorLeakage, configuration_with_leakage, {
    auto circuit = Circuit(R"CIRCUIT(
        LEAKAGE(0.01) 0 1 2 3 4 5 6 7 8 9 10 11
    )CIRCUIT");
    auto circuit_stats = circuit.compute_stats();
    FrameSimulator<W> frame_sim(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 0, INDEPENDENT_TEST_RNG());
    const size_t batch_size = 500;
    frame_sim.configure_for(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, batch_size);
    ASSERT_EQ(frame_sim.leakage_table, simd_bit_table<W>(circuit_stats.num_qubits, batch_size));
})

TEST_EACH_WORD_SIZE_W(FrameSimulatorLeakage, leakage_table_is_cleared_at_the_start_of_each_run, {
    auto circuit = Circuit(R"CIRCUIT(
        LEAKAGE(0.1) 0 1 2 3 4 5 6 7 8 9 10 11
    )CIRCUIT");
    auto circuit_stats = circuit.compute_stats();
    FrameSimulator<W> frame_sim(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 0, INDEPENDENT_TEST_RNG());
    frame_sim.configure_for(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 10);
    frame_sim.do_circuit(circuit);
    circuit = Circuit(R"CIRCUIT(
        CZ 0 1 2 3 4 5 6 7 8 9 10 11
    )CIRCUIT");
    frame_sim.reset_all();
    frame_sim.do_circuit(circuit);
    ASSERT_EQ(frame_sim.leakage_table, simd_bit_table<W>(circuit_stats.num_qubits, 10));
})

TEST_EACH_WORD_SIZE_W(FrameSimulatorLeakage, leakage_state_manipulated_via_leakage_channel, {
    auto circuit = Circuit(R"CIRCUIT(
        LEAKAGE(0.01) 0 1 2 3 4 5 6 7 8 9 10 11
    )CIRCUIT");
    auto circuit_stats = circuit.compute_stats();
    FrameSimulator<W> frame_sim(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 0, INDEPENDENT_TEST_RNG());
    const size_t n = 10'000;
    frame_sim.configure_for(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, n);
    frame_sim.do_circuit(circuit);

    // All qubits have been targetted by the leakage channel so the expectation is that each
    // qubit will have been leaked in 1% of the shots
    for (size_t q = 0; q < circuit_stats.num_qubits; ++q) {
        int num_hits = 0;
        for (size_t k = 0; k < n; ++k) {
            num_hits += frame_sim.leakage_table[q][k];
        }
        EXPECT_NEAR(n * 0.01, num_hits, n * 0.005);
    }

    // Test case where leakage only affects a subset of the qubits in the circuit. In this case
    // only qubits 0, 1 and 7 should have been leaked 1% of the time.
    circuit = Circuit(R"CIRCUIT(
        R 0 1 2 3 4 5 6 7 8 9 10 11
        LEAKAGE(0.01) 0 1 7
    )CIRCUIT");
    frame_sim.reset_all();
    frame_sim.do_circuit(circuit);
    for (size_t q = 0; q < circuit_stats.num_qubits; ++q) {
        int num_hits = 0;
        for (size_t k = 0; k < n; ++k) {
            num_hits += frame_sim.leakage_table[q][k];
        }
        if (q == 0 || q == 1 || q == 7) {
            EXPECT_NEAR(n * 0.01, num_hits, n * 0.005);
        } else {
            ASSERT_EQ(num_hits, 0);
        }
    }
})

TEST_EACH_WORD_SIZE_W(FrameSimulatorLeakage, leakage_is_accompanied_by_an_immediate_dep1_event, {
    auto circuit = Circuit(R"CIRCUIT(
        LEAKAGE(0.01) 0 1 2 3 4 5 6 7 8 9 10 11
    )CIRCUIT");
    auto circuit_stats = circuit.compute_stats();
    FrameSimulator<W> frame_sim(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 0, INDEPENDENT_TEST_RNG());
    const size_t n = 20'000;
    frame_sim.configure_for(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, n);
    frame_sim.do_LEAKAGE(circuit.operations[0]);

    for (size_t q = 0; q < circuit_stats.num_qubits; ++q) {
        int num_x_flips = 0;
        int num_z_flips = 0;
        for (size_t k = 0; k < n; ++k) {
            num_x_flips += frame_sim.x_table[q][k];
            num_z_flips += frame_sim.z_table[q][k];
        }
        EXPECT_NEAR(n * 0.5 * 0.01, num_x_flips, n * 0.5 * 0.005);
        EXPECT_NEAR(n * 0.5 * 0.01, num_z_flips, n * 0.5 * 0.005);
    }

    circuit = Circuit(R"CIRCUIT(
        R 0 1 2 3 4 5 6 7 8 9 10 11
        LEAKAGE(0.01) 0 1 7
    )CIRCUIT");
    frame_sim.x_table.clear();
    frame_sim.z_table.clear();
    frame_sim.do_LEAKAGE(circuit.operations[1]);
    for (size_t q = 0; q < circuit_stats.num_qubits; ++q) {
        int num_x_flips = 0;
        int num_z_flips = 0;
        for (size_t k = 0; k < n; ++k) {
            num_x_flips += frame_sim.x_table[q][k];
            num_z_flips += frame_sim.z_table[q][k];
        }
        if (q == 0 || q == 1 || q == 7) {
            EXPECT_NEAR(n * 0.5 * 0.01, num_x_flips, n * 0.5 * 0.005);
            EXPECT_NEAR(n * 0.5 * 0.01, num_z_flips, n * 0.5 * 0.005);
        } else {
            ASSERT_EQ(num_x_flips, 0);
            ASSERT_EQ(num_z_flips, 0);
        }
    }
})

Circuit generate_leakage_circuit_with_partial_reset(const std::string &reset_gate) {
    const std::string circuit = "LEAKAGE(0.1) 0 1 2 3 4 5 6 7 8 9 10 11\n" + reset_gate + " 4 5";
    return Circuit(circuit.c_str());
}

TEST_EACH_WORD_SIZE_W(FrameSimulatorLeakage, partial_reset_undoes_leakage_state, {
    for (const auto gate : { "MRX", "MRY", "MR", "RX", "RY", "R"}) {
        const auto circuit = generate_leakage_circuit_with_partial_reset(gate);
        const auto circuit_stats = circuit.compute_stats();
        FrameSimulator<W> frame_sim(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 0, INDEPENDENT_TEST_RNG());
        frame_sim.configure_for(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 10'000);
        frame_sim.do_circuit(circuit);
        for (size_t q = 0; q < circuit_stats.num_qubits; ++q) {
            if (q == 4 || q == 5) {
                ASSERT_FALSE(frame_sim.leakage_table[q].not_zero());
            } else {
                ASSERT_TRUE(frame_sim.leakage_table[q].not_zero());
            }
        }

    }
})

Circuit generate_leakage_circuit_with_complete_reset(const std::string &reset_gate) {
    const std::string circuit = "LEAKAGE(0.1) 0 1 2 3 4 5\n" + reset_gate + " 0 1 2 3 4 5";
    return Circuit(circuit.c_str());
}

TEST_EACH_WORD_SIZE_W(FrameSimulatorLeakage, complete_reset_undoes_leakage_state, {
    for (const auto gate : { "MRX", "MRY", "MR", "RX", "RY", "R"}) {
        const auto circuit = generate_leakage_circuit_with_complete_reset(gate);
        auto circuit_stats = circuit.compute_stats();
        FrameSimulator<W> frame_sim(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 0, INDEPENDENT_TEST_RNG());
        const size_t n = 10'000;
        frame_sim.configure_for(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, n);
        frame_sim.do_circuit(circuit);
        for (size_t q = 0; q < circuit_stats.num_qubits; ++q) {
            // Qubits that have been reset should have their leakage state zero'd out
            ASSERT_FALSE(frame_sim.leakage_table[q].not_zero());
        }
    }
})

Circuit generate_leakage_circuit_with_two_qubit_gate(const std::string &two_qubit_gate) {
    const std::string circuit = "LEAKAGE(0.1) 0 1 2 3 4 5 6 7 8 9 10 11\n" + two_qubit_gate + " 0 1 2 3 4 5 6 7 8 9 10 11";
    return Circuit(circuit.c_str());
}

TEST_EACH_WORD_SIZE_W(FrameSimulatorLeakage, leaked_qubits_depolarise_qubits_when_they_interact, {
    for (const auto gate : {"CX", "CZ", "CY"}) {
        const auto circuit = generate_leakage_circuit_with_two_qubit_gate(gate);
        const auto circuit_stats = circuit.compute_stats();
        FrameSimulator<W> frame_sim(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 0, INDEPENDENT_TEST_RNG());
        const size_t n = 10'000;
        frame_sim.configure_for(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, n);
        frame_sim.do_LEAKAGE(circuit.operations[0]);
        auto x_table = frame_sim.x_table;
        auto z_table = frame_sim.z_table;
        frame_sim.do_ZCX(circuit.operations[1]);

        for (size_t q = 0; q < circuit_stats.num_qubits; ++q) {
            size_t x_flips_given_gate = 0;
            size_t z_flips_given_gate = 0;
            for (size_t shot = 0; shot < n; ++shot) {
                x_flips_given_gate += x_table[q][shot] != frame_sim.x_table[q][shot];
                z_flips_given_gate += z_table[q][shot] != frame_sim.z_table[q][shot];
            }
            EXPECT_NEAR(n * 0.5 * 0.1, x_flips_given_gate, n * 0.5 * 0.05);
            EXPECT_NEAR(n * 0.5 * 0.1, z_flips_given_gate, n * 0.5 * 0.05);
        }
    }
})

TEST_EACH_WORD_SIZE_W(FrameSimulatorLeakage, control_will_leak_target_if_leakage_spreading_is_certain_and_control_is_already_leaked, {
    auto circuit = Circuit(R"CIRCUIT(
        LEAKAGE(1.0) 0
        CX(1.0, 0.0, 0.0, 0.0) 0 1
    )CIRCUIT");
    auto circuit_stats = circuit.compute_stats();
    FrameSimulator<W> frame_sim(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 0, INDEPENDENT_TEST_RNG());
    frame_sim.configure_for(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 1);
    frame_sim.do_circuit(circuit);
    ASSERT_TRUE(frame_sim.leakage_table[1][0]);
})

TEST_EACH_WORD_SIZE_W(FrameSimulatorLeakage, target_will_leak_control_if_leakage_spreading_is_certain_and_target_is_already_leaked, {
    auto circuit = Circuit(R"CIRCUIT(
        LEAKAGE(1.0) 1
        CX(0.0, 1.0, 0.0, 0.0) 0 1
    )CIRCUIT");
    auto circuit_stats = circuit.compute_stats();
    FrameSimulator<W> frame_sim(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 0, INDEPENDENT_TEST_RNG());
    frame_sim.configure_for(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 1);
    frame_sim.do_circuit(circuit);
    ASSERT_TRUE(frame_sim.leakage_table[0][0]);
})

TEST_EACH_WORD_SIZE_W(FrameSimulatorLeakage, leakage_spreading_statistical_test, {
    const auto circuit = Circuit(R"CIRCUIT(
        LEAKAGE(0.03) 0 1 2 3 4 5 6 7 8 9 10 11
        CX(0.4, 0.4, 0.0, 0.0) 0 1 2 3 4 5 6 7 8 9 10 11
    )CIRCUIT");
    const auto circuit_stats = circuit.compute_stats();
    std::mt19937_64 rng(0);
    FrameSimulator<W> frame_sim(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 0, std::move(rng));
    const size_t n = 10'000;
    frame_sim.configure_for(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, n);
    frame_sim.do_circuit(circuit);

    for (size_t q = 0; q < circuit_stats.num_qubits; ++q) {
        size_t num_leaked = 0;
        for (size_t shot = 0; shot < n; ++shot) {
            num_leaked += frame_sim.leakage_table[q][shot];
        }
        size_t expected_num_leaked = n * 0.03 + n * 0.03 * 0.4;
        EXPECT_NEAR(expected_num_leaked, num_leaked, expected_num_leaked * 0.2);
    }
})

TEST_EACH_WORD_SIZE_W(FrameSimulatorLeakage, control_will_be_relaxed_and_target_leaked_if_leakage_mobility_is_certain_and_control_is_already_leaked, {
    auto circuit = Circuit(R"CIRCUIT(
        LEAKAGE(1.0) 0
        CX(0.0, 0.0, 1.0, 0.0) 0 1
    )CIRCUIT");
    auto circuit_stats = circuit.compute_stats();
    FrameSimulator<W> frame_sim(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 0, INDEPENDENT_TEST_RNG());
    frame_sim.configure_for(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 1);
    frame_sim.do_circuit(circuit);
    ASSERT_TRUE(frame_sim.leakage_table[1][0]);
    ASSERT_FALSE(frame_sim.leakage_table[0][0]);
})

TEST_EACH_WORD_SIZE_W(FrameSimulatorLeakage, target_will_be_relaxed_and_control_leaked_if_leakage_mobility_is_certain_and_target_is_already_leaked, {
    auto circuit = Circuit(R"CIRCUIT(
        LEAKAGE(1.0) 1
        CX(0.0, 0.0, 0.0, 1.0) 0 1
    )CIRCUIT");
    auto circuit_stats = circuit.compute_stats();
    FrameSimulator<W> frame_sim(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 0, INDEPENDENT_TEST_RNG());
    frame_sim.configure_for(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 1);
    frame_sim.do_circuit(circuit);
    ASSERT_TRUE(frame_sim.leakage_table[0][0]);
    ASSERT_FALSE(frame_sim.leakage_table[1][0]);
})

TEST_EACH_WORD_SIZE_W(FrameSimulatorLeakage, test_relaxation_channel, {
    const auto circuit = Circuit(R"CIRCUIT(
        LEAKAGE(0.6) 0 1 2 3 4 5 6 7 8 9 10 11
        RELAX(0.03) 0 1 2 3 4 5 6 7 8 9 10 11
    )CIRCUIT");
    const auto circuit_stats = circuit.compute_stats();
    FrameSimulator<W> frame_sim(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 0, INDEPENDENT_TEST_RNG());
    const size_t n = 2560;
    frame_sim.configure_for(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, n);

    frame_sim.do_LEAKAGE(circuit.operations[0]);
    size_t num_leaked_before_relaxation = 0;
    for (size_t q = 0; q < circuit_stats.num_qubits; ++q) {
        for (size_t shot = 0; shot < n; ++shot) {
            num_leaked_before_relaxation += frame_sim.leakage_table[q][shot];
        }
    }

    frame_sim.do_RELAX(circuit.operations[1]);
    size_t num_leaked_after_relaxation = 0;
    for (size_t q = 0; q < circuit_stats.num_qubits; ++q) {
        for (size_t shot = 0; shot < n; ++shot) {
            num_leaked_after_relaxation += frame_sim.leakage_table[q][shot];
        }
    }

    EXPECT_NEAR(num_leaked_before_relaxation * 0.97,
                num_leaked_after_relaxation,
                num_leaked_before_relaxation * 1.001);
})

TEST_EACH_WORD_SIZE_W(FrameSimulatorLeakage, leakage_heralding, {
    auto circuit = Circuit(R"CIRCUIT(
        HERALD_LEAKAGE_EVENT 1 3
        DETECTOR rec[-2]
        DETECTOR rec[-1]
        HERALD_LEAKAGE_EVENT(0.3) 1 3
        DETECTOR rec[-2]
        DETECTOR rec[-1]

        LEAKAGE(0.2) 1 3

        HERALD_LEAKAGE_EVENT 1 3
        DETECTOR rec[-2]
        DETECTOR rec[-1]
        HERALD_LEAKAGE_EVENT(0.3) 1 3
        DETECTOR rec[-2]
        DETECTOR rec[-1]
    )CIRCUIT");
    auto circuit_stats = circuit.compute_stats();
    FrameSimulator<W> frame_sim(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, 0, INDEPENDENT_TEST_RNG());
    const size_t batch_size = 50'000;
    frame_sim.configure_for(circuit_stats, FrameSimulatorMode::STORE_DETECTIONS_TO_MEMORY, batch_size);
    frame_sim.do_circuit(circuit);

    for (size_t i = 0; i < 4; ++i) {
        ASSERT_EQ(frame_sim.det_record.storage[i].popcnt(), 0);
    }
    const size_t num_leaked = batch_size * 0.2;
    for (size_t i = 4; i < 6; ++i) {
        ASSERT_NEAR(frame_sim.det_record.storage[i].popcnt(), num_leaked, batch_size * 0.01);
    }
    const size_t noisy_num_leaked = num_leaked * 0.7;
    for (size_t i = 6; i < 8; ++i) {
        ASSERT_NEAR(frame_sim.det_record.storage[i].popcnt(), noisy_num_leaked, noisy_num_leaked * 0.05);
    }
})
