import numpy as np
import lestim


def test_gate_data_eq():
    assert lestim.gate_data('H') == lestim.GateData('H')
    assert lestim.gate_data('H') == lestim.gate_data('H_XZ')
    assert not (lestim.gate_data('H') == lestim.GateData('X_ERROR'))
    assert lestim.gate_data('X') != lestim.GateData('H')


def test_gate_data_str():
    assert str(lestim.GateData('MXX')) == '''
stim.GateData {
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
    assert str(lestim.GateData('H')) == '''
stim.GateData {
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
    .tableau = stim.Tableau.from_conjugated_generators(
        xs=[
            stim.PauliString("+Z"),
        ],
        zs=[
            stim.PauliString("+X"),
        ],
    )
    .unitary_matrix = np.array([[(0.7071067690849304+0j), (0.7071067690849304+0j)], [(0.7071067690849304+0j), (-0.7071067690849304-0j)]], dtype=np.complex64)
}
    '''.strip()


def test_num_parens_arguments_range():
<<<<<<< HEAD
    assert lestim.gate_data('H').num_parens_arguments_range == range(0, 1)
    assert lestim.gate_data('M').num_parens_arguments_range == range(0, 2)


def test_is_reset():
    assert not lestim.gate_data('H').is_reset
    assert lestim.gate_data('R').is_reset
    assert lestim.gate_data('MR').is_reset


def test_is_two_qubit_gate():
    assert not lestim.gate_data('H').is_two_qubit_gate
    assert lestim.gate_data('CX').is_two_qubit_gate


def test_is_single_qubit_gate():
    assert lestim.gate_data('H').is_single_qubit_gate
    assert not lestim.gate_data('CX').is_single_qubit_gate


def test_is_noisy_gate():
    assert lestim.gate_data('X_ERROR').is_noisy_gate
    assert not lestim.gate_data('X').is_noisy_gate


def test_produces_measurements():
    assert lestim.gate_data('MR').produces_measurements
    assert not lestim.gate_data('R').produces_measurements


def test_takes_pauli_targets():
    assert lestim.gate_data('MPP').takes_pauli_targets
    assert not lestim.gate_data('MXX').takes_pauli_targets


def test_aliases():
    assert lestim.gate_data('H').aliases == ['H', 'H_XZ']
    assert lestim.gate_data('CX').aliases == ['CNOT', 'CX', 'ZCX']


def test_tableau():
    assert lestim.gate_data('H').tableau == lestim.Tableau.from_named_gate('H')


def test_name():
    assert lestim.gate_data('H').name == 'H'
=======
    assert stim.gate_data('H').num_parens_arguments_range == range(0, 1)
    assert stim.gate_data('M').num_parens_arguments_range == range(0, 2)


def test_is_reset():
    assert not stim.gate_data('H').is_reset
    assert stim.gate_data('R').is_reset
    assert stim.gate_data('MR').is_reset


def test_is_two_qubit_gate():
    assert not stim.gate_data('H').is_two_qubit_gate
    assert stim.gate_data('CX').is_two_qubit_gate


def test_is_single_qubit_gate():
    assert stim.gate_data('H').is_single_qubit_gate
    assert not stim.gate_data('CX').is_single_qubit_gate


def test_is_noisy_gate():
    assert stim.gate_data('X_ERROR').is_noisy_gate
    assert not stim.gate_data('X').is_noisy_gate


def test_produces_measurements():
    assert stim.gate_data('MR').produces_measurements
    assert not stim.gate_data('R').produces_measurements


def test_takes_pauli_targets():
    assert stim.gate_data('MPP').takes_pauli_targets
    assert not stim.gate_data('MXX').takes_pauli_targets


def test_aliases():
    assert stim.gate_data('H').aliases == ['H', 'H_XZ']
    assert stim.gate_data('CX').aliases == ['CNOT', 'CX', 'ZCX']


def test_tableau():
    assert stim.gate_data('H').tableau == stim.Tableau.from_named_gate('H')


def test_name():
    assert stim.gate_data('H').name == 'H'
>>>>>>> 1a67d3a9 (feat: Sync with Stim (#32))


def test_gate_data_repr():
    val = lestim.GateData('MPP')
    assert eval(repr(val), {"stim": lestim}) == val


def test_takes_measurement_record_targets():
    assert not lestim.gate_data('H').takes_measurement_record_targets
    assert lestim.gate_data('DETECTOR').takes_measurement_record_targets


def test_takes_measurement_record_targets():
    assert not stim.gate_data('H').takes_measurement_record_targets
    assert stim.gate_data('DETECTOR').takes_measurement_record_targets


def test_gate_data_inverse():
    for v in lestim.gate_data().values():
        assert v.is_unitary == (v.inverse is not None)
        matrix = v.unitary_matrix
        if matrix is not None:
            assert v.is_unitary
            assert np.allclose(matrix.conj().T, v.inverse.unitary_matrix, atol=1e-6), (v.name, v.inverse.name)
            assert v.inverse == v.generalized_inverse

<<<<<<< HEAD
    assert lestim.gate_data('H').inverse == lestim.gate_data('H')
    assert lestim.gate_data('S').inverse == lestim.gate_data('S_DAG')
    assert lestim.gate_data('M').inverse is None
    assert lestim.gate_data('CXSWAP').inverse == lestim.gate_data('SWAPCX')
    assert lestim.gate_data('SPP').inverse == lestim.gate_data('SPP_DAG')
=======
    assert stim.gate_data('H').inverse == stim.gate_data('H')
    assert stim.gate_data('S').inverse == stim.gate_data('S_DAG')
    assert stim.gate_data('M').inverse is None
    assert stim.gate_data('CXSWAP').inverse == stim.gate_data('SWAPCX')
    assert stim.gate_data('SPP').inverse == stim.gate_data('SPP_DAG')
>>>>>>> 1a67d3a9 (feat: Sync with Stim (#32))

    assert lestim.gate_data('S').generalized_inverse == lestim.gate_data('S_DAG')
    assert lestim.gate_data('M').generalized_inverse == lestim.gate_data('M')
    assert lestim.gate_data('R').generalized_inverse == lestim.gate_data('M')
    assert lestim.gate_data('MR').generalized_inverse == lestim.gate_data('MR')
    assert lestim.gate_data('MPP').generalized_inverse == lestim.gate_data('MPP')
    assert lestim.gate_data('ELSE_CORRELATED_ERROR').generalized_inverse == lestim.gate_data('ELSE_CORRELATED_ERROR')


def test_gate_data_flows():
    assert lestim.GateData('H').flows == [
        lestim.Flow("X -> Z"),
        lestim.Flow("Z -> X"),
    ]


def test_gate_is_symmetric():
<<<<<<< HEAD
    assert lestim.GateData('SWAP').is_symmetric_gate
    assert lestim.GateData('H').is_symmetric_gate
    assert lestim.GateData('MYY').is_symmetric_gate
    assert lestim.GateData('DEPOLARIZE2').is_symmetric_gate
    assert not lestim.GateData('PAULI_CHANNEL_2').is_symmetric_gate
    assert not lestim.GateData('DETECTOR').is_symmetric_gate
    assert not lestim.GateData('TICK').is_symmetric_gate


def test_gate_hadamard_conjugated():
    assert lestim.GateData('CZSWAP').hadamard_conjugated(unsigned=True) is None
    assert lestim.GateData('TICK').hadamard_conjugated() == lestim.GateData('TICK')
    assert lestim.GateData('MYY').hadamard_conjugated() == lestim.GateData('MYY')
    assert lestim.GateData('XCZ').hadamard_conjugated() == lestim.GateData('CX')
    assert lestim.GateData('X_ERROR').hadamard_conjugated() == lestim.GateData('Z_ERROR')
    assert lestim.GateData('Y_ERROR').hadamard_conjugated() == lestim.GateData('Y_ERROR')
    assert lestim.GateData('Z_ERROR').hadamard_conjugated() == lestim.GateData('X_ERROR')
    assert lestim.GateData('I_ERROR').hadamard_conjugated() == lestim.GateData('I_ERROR')
    assert lestim.GateData('II_ERROR').hadamard_conjugated() == lestim.GateData('II_ERROR')
=======
    assert stim.GateData('SWAP').is_symmetric_gate
    assert stim.GateData('H').is_symmetric_gate
    assert stim.GateData('MYY').is_symmetric_gate
    assert stim.GateData('DEPOLARIZE2').is_symmetric_gate
    assert not stim.GateData('PAULI_CHANNEL_2').is_symmetric_gate
    assert not stim.GateData('DETECTOR').is_symmetric_gate
    assert not stim.GateData('TICK').is_symmetric_gate


def test_gate_hadamard_conjugated():
    assert stim.GateData('CZSWAP').hadamard_conjugated(unsigned=True) is None
    assert stim.GateData('TICK').hadamard_conjugated() == stim.GateData('TICK')
    assert stim.GateData('MYY').hadamard_conjugated() == stim.GateData('MYY')
    assert stim.GateData('XCZ').hadamard_conjugated() == stim.GateData('CX')
    assert stim.GateData('X_ERROR').hadamard_conjugated() == stim.GateData('Z_ERROR')
    assert stim.GateData('Y_ERROR').hadamard_conjugated() == stim.GateData('Y_ERROR')
    assert stim.GateData('Z_ERROR').hadamard_conjugated() == stim.GateData('X_ERROR')
    assert stim.GateData('I_ERROR').hadamard_conjugated() == stim.GateData('I_ERROR')
    assert stim.GateData('II_ERROR').hadamard_conjugated() == stim.GateData('II_ERROR')
>>>>>>> 1a67d3a9 (feat: Sync with Stim (#32))
