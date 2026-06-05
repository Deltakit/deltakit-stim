#include "error_analyzer_pl_data.h"
#include "stim/circuit/circuit.h"

using namespace stim;

bool has_herald_gates(const Circuit &circuit) {
    for (const auto &op : circuit.operations) {
        if (op.gate_type == GateType::REPEAT) {
            if (has_herald_gates(op.repeat_block_body(circuit))) {
                return true;
            }
        }
        if (op.gate_type == GateType::HERALD_LEAKAGE_EVENT) {
            return true;
        }
    }
    return false;
}

std::map<uint32_t, float> stim::get_num_meas_before_her_to_pl(const Circuit &circuit, const size_t num_qubits) {
    // avoids performing a linear forward pass if there is no leakage heralding
    // (and in any case some tests would expect this to be periodic)
    if (!has_herald_gates(circuit)) {
        return {};
    }

    uint32_t measurement_idx = 0;
    std::map<uint32_t, float> qubits_to_current_leakage_sensitivity;
    std::map<uint32_t, float> mapping;
    circuit.for_each_operation([&mapping,
                                &measurement_idx,
                                &qubits_to_current_leakage_sensitivity](const CircuitInstruction &op) {
        if (op.gate_type == GateType::HERALD_LEAKAGE_EVENT) {
            for (const auto &t : op.targets) {
                mapping.emplace(measurement_idx, qubits_to_current_leakage_sensitivity[t.data]);
                ++measurement_idx;
            }
        } else if (GATE_DATA[op.gate_type].flags & GateFlags::GATE_PRODUCES_RESULTS) {
            measurement_idx += op.count_measurement_results();
        } else if (op.gate_type == GateType::LEAKAGE) {
            for (const auto &t : op.targets) {
                qubits_to_current_leakage_sensitivity[t.data] += op.args[0];
            }
        } else if (GATE_DATA[op.gate_type].flags & GateFlags::GATE_IS_RESET) {
            for (const auto &t : op.targets) {
                qubits_to_current_leakage_sensitivity[t.data] = 0;
            }
        }
    });
    return mapping;
}
