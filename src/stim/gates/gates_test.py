import numpy as np
import deltakit_stim


def test_gate_data_eq():
    assert deltakit_stim.gate_data('H') == deltakit_stim.GateData('H')
    assert deltakit_stim.gate_data('H') == deltakit_stim.gate_data('H_XZ')
    assert not (deltakit_stim.gate_data('H') == deltakit_stim.GateData('X_ERROR'))
    assert deltakit_stim.gate_data('X') != deltakit_stim.GateData('H')


def test_gate_data_str():
    assert str(deltakit_stim.GateData('MXX')) == '''
deltakit_stim.GateData {
    .name = 'MXX'
    .aliases = ['MXX']
    .is_noisy_gate = True
    .is_reset = False
    .is_single_qubit_gate = False
    .is_two_qubit_gate = True
    .is_unitary = False
    .num_parens_arguments_range = range(0, 2)
    .produces_measurements = True
    .takes_measurement_record_targets = False
    .takes_pauli_targets = False
}
    '''.strip()
    assert str(deltakit_stim.GateData('H')) == '''
deltakit_stim.GateData {
    .name = 'H'
    .aliases = ['H', 'H_XZ']
    .is_noisy_gate = False
    .is_reset = False
    .is_single_qubit_gate = True
    .is_two_qubit_gate = False
    .is_unitary = True
    .num_parens_arguments_range = range(0, 1)
    .produces_measurements = False
    .takes_measurement_record_targets = False
    .takes_pauli_targets = False
    .tableau = deltakit_stim.Tableau.from_conjugated_generators(
        xs=[
            deltakit_stim.PauliString("+Z"),
        ],
        zs=[
            deltakit_stim.PauliString("+X"),
        ],
    )
    .unitary_matrix = np.array([[(0.7071067690849304+0j), (0.7071067690849304+0j)], [(0.7071067690849304+0j), (-0.7071067690849304-0j)]], dtype=np.complex64)
}
    '''.strip()


def test_num_parens_arguments_range():
    assert deltakit_stim.gate_data('H').num_parens_arguments_range == range(0, 1)
    assert deltakit_stim.gate_data('M').num_parens_arguments_range == range(0, 2)


def test_is_reset():
    assert not deltakit_stim.gate_data('H').is_reset
    assert deltakit_stim.gate_data('R').is_reset
    assert deltakit_stim.gate_data('MR').is_reset


def test_is_two_qubit_gate():
    assert not deltakit_stim.gate_data('H').is_two_qubit_gate
    assert deltakit_stim.gate_data('CX').is_two_qubit_gate


def test_is_single_qubit_gate():
    assert deltakit_stim.gate_data('H').is_single_qubit_gate
    assert not deltakit_stim.gate_data('CX').is_single_qubit_gate


def test_is_noisy_gate():
    assert deltakit_stim.gate_data('X_ERROR').is_noisy_gate
    assert not deltakit_stim.gate_data('X').is_noisy_gate


def test_produces_measurements():
    assert deltakit_stim.gate_data('MR').produces_measurements
    assert not deltakit_stim.gate_data('R').produces_measurements


def test_takes_pauli_targets():
    assert deltakit_stim.gate_data('MPP').takes_pauli_targets
    assert not deltakit_stim.gate_data('MXX').takes_pauli_targets


def test_aliases():
    assert deltakit_stim.gate_data('H').aliases == ['H', 'H_XZ']
    assert deltakit_stim.gate_data('CX').aliases == ['CNOT', 'CX', 'ZCX']


def test_tableau():
    assert deltakit_stim.gate_data('H').tableau == deltakit_stim.Tableau.from_named_gate('H')


def test_name():
    assert deltakit_stim.gate_data('H').name == 'H'


def test_gate_data_repr():
    val = deltakit_stim.GateData('MPP')
    assert eval(repr(val), {"deltakit_stim": deltakit_stim}) == val


def test_takes_measurement_record_targets():
    assert not deltakit_stim.gate_data('H').takes_measurement_record_targets
    assert deltakit_stim.gate_data('DETECTOR').takes_measurement_record_targets


def test_gate_data_inverse():
    for v in deltakit_stim.gate_data().values():
        assert v.is_unitary == (v.inverse is not None)
        matrix = v.unitary_matrix
        if matrix is not None:
            assert v.is_unitary
            assert np.allclose(matrix.conj().T, v.inverse.unitary_matrix, atol=1e-6), (v.name, v.inverse.name)
            assert v.inverse == v.generalized_inverse

    assert deltakit_stim.gate_data('H').inverse == deltakit_stim.gate_data('H')
    assert deltakit_stim.gate_data('S').inverse == deltakit_stim.gate_data('S_DAG')
    assert deltakit_stim.gate_data('M').inverse is None
    assert deltakit_stim.gate_data('CXSWAP').inverse == deltakit_stim.gate_data('SWAPCX')
    assert deltakit_stim.gate_data('SPP').inverse == deltakit_stim.gate_data('SPP_DAG')

    assert deltakit_stim.gate_data('S').generalized_inverse == deltakit_stim.gate_data('S_DAG')
    assert deltakit_stim.gate_data('M').generalized_inverse == deltakit_stim.gate_data('M')
    assert deltakit_stim.gate_data('R').generalized_inverse == deltakit_stim.gate_data('M')
    assert deltakit_stim.gate_data('MR').generalized_inverse == deltakit_stim.gate_data('MR')
    assert deltakit_stim.gate_data('MPP').generalized_inverse == deltakit_stim.gate_data('MPP')
    assert deltakit_stim.gate_data('ELSE_CORRELATED_ERROR').generalized_inverse == deltakit_stim.gate_data('ELSE_CORRELATED_ERROR')


def test_gate_data_flows():
    assert deltakit_stim.GateData('H').flows == [
        deltakit_stim.Flow("X -> Z"),
        deltakit_stim.Flow("Z -> X"),
    ]


def test_gate_is_symmetric():
    assert deltakit_stim.GateData('SWAP').is_symmetric_gate
    assert deltakit_stim.GateData('H').is_symmetric_gate
    assert deltakit_stim.GateData('MYY').is_symmetric_gate
    assert deltakit_stim.GateData('DEPOLARIZE2').is_symmetric_gate
    assert not deltakit_stim.GateData('PAULI_CHANNEL_2').is_symmetric_gate
    assert not deltakit_stim.GateData('DETECTOR').is_symmetric_gate
    assert not deltakit_stim.GateData('TICK').is_symmetric_gate


def test_gate_hadamard_conjugated():
    assert deltakit_stim.GateData('CZSWAP').hadamard_conjugated(unsigned=True) is None
    assert deltakit_stim.GateData('TICK').hadamard_conjugated() == deltakit_stim.GateData('TICK')
    assert deltakit_stim.GateData('MYY').hadamard_conjugated() == deltakit_stim.GateData('MYY')
    assert deltakit_stim.GateData('XCZ').hadamard_conjugated() == deltakit_stim.GateData('CX')
    assert deltakit_stim.GateData('X_ERROR').hadamard_conjugated() == deltakit_stim.GateData('Z_ERROR')
    assert deltakit_stim.GateData('Y_ERROR').hadamard_conjugated() == deltakit_stim.GateData('Y_ERROR')
    assert deltakit_stim.GateData('Z_ERROR').hadamard_conjugated() == deltakit_stim.GateData('X_ERROR')
    assert deltakit_stim.GateData('I_ERROR').hadamard_conjugated() == deltakit_stim.GateData('I_ERROR')
    assert deltakit_stim.GateData('II_ERROR').hadamard_conjugated() == deltakit_stim.GateData('II_ERROR')
