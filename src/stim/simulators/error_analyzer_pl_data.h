#ifndef _STIM_SIMULATORS_ERROR_ANALYZER_PL_DATA_H
#define _STIM_SIMULATORS_ERROR_ANALYZER_PL_DATA_H

#include <cstdint>
#include <cstdio>
#include <map>

namespace stim {

struct Circuit;

std::map<uint32_t, float> get_num_meas_before_her_to_pl(const Circuit &circuit, const size_t num_qubits);

}  // namespace stim

#endif
