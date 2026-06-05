#include "stim/simulators/error_analyzer_pl_data.h"

#include "gtest/gtest.h"

#include "stim/circuit/circuit.h"

using namespace stim;

TEST(ErrorAnalyzerPLTest, basic) {
    auto circ = Circuit(R"CIRCUIT(
        repeat 3 {
            R 1
            LEAKAGE(0.1) 1
            HERALD_LEAKAGE_EVENT 1
            repeat 3 {
                R 1
                LEAKAGE(0.1) 1
                M 1
                HERALD_LEAKAGE_EVENT 1
            }
        }
    )CIRCUIT");

    auto mapping = get_num_meas_before_her_to_pl(circ, circ.compute_stats().num_qubits);
    std::map<uint32_t, float> expected_data {
        {0, 0.1},
        {2, 0.1},
        {4, 0.1},
        {6, 0.1},
        {7, 0.1},
        {9, 0.1},
        {11, 0.1},
        {13, 0.1},
        {14, 0.1},
        {16, 0.1},
        {18, 0.1},
        {20, 0.1},
    };
    ASSERT_EQ(mapping, expected_data);

    circ = Circuit(R"CIRCUIT(
        repeat 2 {
            R 1
            LEAKAGE(0.2) 1
            HERALD_LEAKAGE_EVENT 1
            MZ 1
            repeat 2 {
                LEAKAGE(0.1) 1
                HERALD_LEAKAGE_EVENT 1
            }
        }
    )CIRCUIT");

    mapping = get_num_meas_before_her_to_pl(circ, circ.compute_stats().num_qubits);

    expected_data = {
        {0, 0.2},
        {2, 0.3},
        {3, 0.4},
        {4, 0.2},
        {6, 0.3},
        {7, 0.4},
    };
    ASSERT_EQ(mapping, expected_data);
}
