# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pytest
import lestim
import numpy as np


def test_basic():
    s = lestim.TableauSimulator()
    assert s.measure(0) is False
    assert s.measure(0) is False
    s.x(0)
    assert s.measure(0) is True
    assert s.measure(0) is True
    s.reset(0)
    assert s.measure(0) is False
    s.h(0)
    s.h(0)
    s.sqrt_x(1)
    s.sqrt_x(1)
    assert s.measure_many(0, 1) == [False, True]


def test_access_tableau():
    s = lestim.TableauSimulator()
    assert s.current_inverse_tableau() == lestim.Tableau(0)

    s.h(0)
    assert s.current_inverse_tableau() == lestim.Tableau.from_named_gate("H")

    s.h(0)
    assert s.current_inverse_tableau() == lestim.Tableau(1)

    s.h(1)
    s.h(1)
    assert s.current_inverse_tableau() == lestim.Tableau(2)

    s.h(2)
    assert s.current_inverse_tableau() == lestim.Tableau.from_conjugated_generators(
        xs=[
            lestim.PauliString("X__"),
            lestim.PauliString("_X_"),
            lestim.PauliString("__Z"),
        ],
        zs=[
            lestim.PauliString("Z__"),
            lestim.PauliString("_Z_"),
            lestim.PauliString("__X"),
        ],
    )


@pytest.mark.parametrize("name", [
    "x",
    "y",
    "z",
    "h",
    "h_xy",
    "h_yz",
    "sqrt_x",
    "sqrt_x_dag",
    "sqrt_y",
    "sqrt_y_dag",
    "s",
    "s_dag",
    "swap",
    "iswap",
    "iswap_dag",
    "xcx",
    "xcy",
    "xcz",
    "ycx",
    "ycy",
    "ycz",
    "cnot",
    "cy",
    "cz",
])
def test_gates_present(name: str):
    t = lestim.Tableau.from_named_gate(name)
    n = len(t)
    s1 = lestim.TableauSimulator()
    s2 = lestim.TableauSimulator()
    for k in range(n):
        s1.h(k)
        s2.h(k)
        s1.cnot(k, k + n)
        s2.cnot(k, k + n)
    getattr(s1, name)(*range(n))
    s2.do(lestim.Circuit(f"{name} " + " ".join(str(e) for e in range(n))))
    assert s1.current_inverse_tableau() == s2.current_inverse_tableau()


def test_do():
    s = lestim.TableauSimulator()
    s.do(lestim.Circuit("""
        S 0
    """))
    assert s.current_inverse_tableau() == lestim.Tableau.from_named_gate("S_DAG")


def test_peek_bloch():
    s = lestim.TableauSimulator()
    assert s.peek_bloch(0) == lestim.PauliString("+Z")
    s.x(0)
    assert s.peek_bloch(0) == lestim.PauliString("-Z")
    s.h(0)
    assert s.peek_bloch(0) == lestim.PauliString("-X")
    s.sqrt_x(1)
    assert s.peek_bloch(1) == lestim.PauliString("-Y")
    s.cz(0, 1)
    assert s.peek_bloch(0) == lestim.PauliString("+I")
    assert s.peek_bloch(1) == lestim.PauliString("+I")


def test_copy():
    s = lestim.TableauSimulator()
    s.h(0)
    s2 = s.copy()
    assert s.current_inverse_tableau() == s2.current_inverse_tableau()
    assert s is not s2


def test_paulis():
    s = lestim.TableauSimulator()
    s.h(*range(0, 22, 2))
    s.cnot(*range(22))

    s.do(lestim.PauliString("ZZZ_YYY_XXX"))
    s.z(0, 1, 2)
    s.y(4, 5, 6)
    s.x(8, 9, 10)

    s.cnot(*range(22))
    s.h(*range(0, 22, 2))
    assert s.measure_many(*range(22)) == [False] * 22

    s = lestim.TableauSimulator()
    s.do(lestim.PauliString("Z" * 500))
    assert s.measure_many(*range(500)) == [False] * 500
    s.do(lestim.PauliString("X" * 500))
    assert s.measure_many(*range(500)) == [True] * 500


def test_measure_kickback():
    s = lestim.TableauSimulator()
    assert s.measure_kickback(0) == (False, None)
    assert s.measure_kickback(0) == (False, None)
    assert s.current_measurement_record() == [False, False]

    s.h(0)
    v = s.measure_kickback(0)
    assert isinstance(v[0], bool)
    assert v[1] == lestim.PauliString("X")
    assert s.measure_kickback(0) == (v[0], None)
    assert s.current_measurement_record() == [False, False, v[0], v[0]]

    s = lestim.TableauSimulator()
    s.h(0)
    s.cnot(0, 1)
    v = s.measure_kickback(0)
    assert isinstance(v[0], bool)
    assert v[1] == lestim.PauliString("XX")
    assert s.measure_kickback(0) == (v[0], None)

    s = lestim.TableauSimulator()
    s.h(0)
    s.cnot(0, 1)
    v = s.measure_kickback(1)
    assert isinstance(v[0], bool)
    assert v[1] == lestim.PauliString("XX")
    assert s.measure_kickback(0) == (v[0], None)


def test_post_select_using_measure_kickback():
    s = lestim.TableauSimulator()

    def pseudo_post_select(qubit, desired_result):
        m, kick = s.measure_kickback(qubit)
        if m != desired_result:
            if kick is None:
                raise ValueError("Deterministic measurement differed from desired result.")
            s.do(kick)

    s.h(0)
    s.cnot(0, 1)
    s.cnot(0, 2)
    pseudo_post_select(qubit=2, desired_result=True)
    assert s.measure_many(0, 1, 2) == [True, True, True]


def test_measure_kickback_random_branches():
    s = lestim.TableauSimulator()
    s.set_inverse_tableau(lestim.Tableau.random(8))

    r = s.peek_bloch(4)
    if r[0] == 3:  # +-Z?
        assert s.measure_kickback(4) == (r.sign == -1, None)
        return

    post_false = None
    post_true = None
    for _ in range(100):
        if post_false is not None and post_true is not None:
            break
        s2 = s.copy()
        if s2.measure(4):
            post_true = s2
        else:
            post_false = s2
    assert post_false is not None and post_true is not None

    result, kick = s.measure_kickback(4)
    assert isinstance(kick, lestim.PauliString) and len(kick) == 8
    if result:
        s.do(kick)
    assert s.canonical_stabilizers() == post_false.canonical_stabilizers()
    s.do(kick)
    assert s.canonical_stabilizers() == post_true.canonical_stabilizers()


def test_set_num_qubits():
    s = lestim.TableauSimulator()
    s.h(0)
    s.cnot(0, 1)
    s.cnot(0, 2)
    s.cnot(0, 3)
    t = s.current_inverse_tableau()
    s.set_num_qubits(8)
    s.set_num_qubits(4)
    assert s.current_inverse_tableau() == t
    assert s.peek_bloch(0) == lestim.PauliString("_")
    s.set_num_qubits(8)
    s.set_num_qubits(4)
    s.cnot(0, 4)
    s.set_num_qubits(4)
    assert s.peek_bloch(0) in [lestim.PauliString("+Z"), lestim.PauliString("-Z")]


def test_canonical_stabilizers():
    s = lestim.TableauSimulator()
    s.h(0)
    s.h(1)
    s.h(2)
    s.cz(0, 1)
    s.cz(1, 2)
    assert s.canonical_stabilizers() == [
        lestim.PauliString("+X_X"),
        lestim.PauliString("+ZXZ"),
        lestim.PauliString("+_ZX"),
    ]
    s.s(1)
    assert s.canonical_stabilizers() == [
        lestim.PauliString("+X_X"),
        lestim.PauliString("-ZXY"),
        lestim.PauliString("+_ZX"),
    ]


def test_classical_control_cnot():
    s = lestim.TableauSimulator()

    with pytest.raises(IndexError, match="beginning of time"):
        s.cnot(lestim.target_rec(-1), 0)

    assert not s.measure(1)
    s.cnot(lestim.target_rec(-1), 0)
    assert not s.measure(0)

    s.x(1)
    assert s.measure(1)
    s.cnot(lestim.target_rec(-1), 0)
    assert s.measure(0)


def test_collision():
<<<<<<< HEAD
    s = lestim.TableauSimulator()
=======
    s = stim.TableauSimulator()
>>>>>>> 1a67d3a9 (feat: Sync with Stim (#32))
    with pytest.raises(ValueError, match="same target"):
        s.cnot(0, 0)
    with pytest.raises(ValueError, match="same target"):
        s.swap(0, 1, 2, 2)
    s.swap(0, 2, 2, 1)


def is_parallel_state_vector(actual, expected) -> bool:
    actual = np.array(actual, dtype=np.complex64)
    expected = np.array(expected, dtype=np.complex64)
    assert len(expected.shape) == 1
    if actual.shape != expected.shape:
        return False
    assert abs(np.linalg.norm(actual) - 1) < 1e-4
    assert abs(np.linalg.norm(expected) - 1) < 1e-4
    return abs(abs(np.dot(actual, np.conj(expected))) - 1) < 1e-4


def test_is_parallel_state_vector():
    assert is_parallel_state_vector([1], [1])
    assert is_parallel_state_vector([1], [1j])
    assert is_parallel_state_vector([1j], [1])
    assert not is_parallel_state_vector([1], [1, 2])
    assert is_parallel_state_vector([0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5])
    assert is_parallel_state_vector([0.5, 0.5, 0.5, 0.5], [0.5j, 0.5j, 0.5j, 0.5j])
    assert is_parallel_state_vector([0.5, 0.5, 0.5, 0.5], [-0.5j, -0.5j, -0.5j, -0.5j])
    assert not is_parallel_state_vector([0.5, 0.5, 0.5, 0.5], [-0.5j, -0.5j, -0.5j, 0.5j])
    assert not is_parallel_state_vector([0.5, 0.5, 0.5, 0.5], [1, 0, 0, 0])


def test_to_state_vector():
    s = lestim.TableauSimulator()
    assert is_parallel_state_vector(s.state_vector(), [1])
    s.set_num_qubits(1)
    assert is_parallel_state_vector(s.state_vector(), [1, 0])
    s.set_num_qubits(2)
    s.x(0)
    assert is_parallel_state_vector(s.state_vector(), [0, 1, 0, 0])
    s.h(1)
    assert is_parallel_state_vector(s.state_vector(), [0, 0.5**0.5, 0, 0.5**0.5])
    s.h(0)
    assert is_parallel_state_vector(s.state_vector(), [0.5, -0.5, 0.5, -0.5])
    s.cnot(1, 0)
    assert is_parallel_state_vector(s.state_vector(), [0.5, -0.5, -0.5, 0.5])
    s.x(2)
    assert is_parallel_state_vector(s.state_vector(), [0, 0, 0, 0, 0.5, -0.5, -0.5, 0.5])
    v = s.state_vector().reshape((2,) * 3)
    assert v[0, 0, 0] == 0
    assert v[1, 0, 0] != 0
    assert v[0, 1, 0] == 0
    assert v[0, 0, 1] == 0

    s = lestim.TableauSimulator()
    s.set_num_qubits(3)
    s.sqrt_x(2)
    np.testing.assert_allclose(
        s.state_vector(endian='little'),
        [np.sqrt(0.5), 0, 0, 0, -1j*np.sqrt(0.5), 0, 0, 0],
        atol=1e-4,
    )
    np.testing.assert_allclose(
        s.state_vector(endian='big'),
        [np.sqrt(0.5), -1j*np.sqrt(0.5), 0, 0, 0, 0, 0, 0],
        atol=1e-4,
    )
    with pytest.raises(ValueError, match="endian"):
        s.state_vector(endian='unknown')

    # Exact precision.
    s.h(1)
    np.testing.assert_array_equal(
        s.state_vector(),
        [0.5, 0, 0.5, 0, -0.5j, 0, -0.5j, 0],
    )


def test_peek_observable_expectation():
    s = lestim.TableauSimulator()
    s.do(lestim.Circuit('''
        H 0
        CNOT 0 1 0 2
        X 0
    '''))

    assert s.peek_observable_expectation(lestim.PauliString("ZZ_")) == -1
    assert s.peek_observable_expectation(lestim.PauliString("_ZZ")) == 1
    assert s.peek_observable_expectation(lestim.PauliString("Z_Z")) == -1
    assert s.peek_observable_expectation(lestim.PauliString("XXX")) == 1
    assert s.peek_observable_expectation(lestim.PauliString("-XXX")) == -1
    assert s.peek_observable_expectation(lestim.PauliString("YYX")) == +1
    assert s.peek_observable_expectation(lestim.PauliString("XYY")) == -1

    assert s.peek_observable_expectation(lestim.PauliString("")) == 1
    assert s.peek_observable_expectation(lestim.PauliString("-I")) == -1
    assert s.peek_observable_expectation(lestim.PauliString("_____")) == 1
    assert s.peek_observable_expectation(lestim.PauliString("XXXZZZZZ")) == 1
    assert s.peek_observable_expectation(lestim.PauliString("XXXZZZZX")) == 0

    with pytest.raises(ValueError, match="imaginary sign"):
        s.peek_observable_expectation(lestim.PauliString("iZZ"))
    with pytest.raises(ValueError, match="imaginary sign"):
        s.peek_observable_expectation(lestim.PauliString("-iZZ"))


def test_postselect():
    s = lestim.TableauSimulator()
    s.h(0)
    s.cnot(0, 1)
    s.postselect_x(0, desired_value=False)
    assert s.peek_bloch(0) == lestim.PauliString("+X")
    assert s.peek_bloch(1) == lestim.PauliString("+X")

    s.postselect_y([2, 3, 4], desired_value=False)
    assert s.peek_bloch(4) == lestim.PauliString("+Y")
    s.postselect_x(8, desired_value=True)
    assert s.peek_bloch(8) == lestim.PauliString("-X")

    s.postselect_z(9, desired_value=False)
    assert s.peek_bloch(9) == lestim.PauliString("+Z")
    with pytest.raises(ValueError, match="impossible"):
        s.postselect_z(10, desired_value=True)

    s.postselect_y(1000, desired_value=True)
    assert s.peek_bloch(1000) == lestim.PauliString("-Y")


def test_peek_pauli():
    s = lestim.TableauSimulator()
    assert s.peek_x(0) == 0
    assert s.peek_y(0) == 0
    assert s.peek_z(0) == +1

    assert s.peek_x(1000) == 0
    assert s.peek_y(1000) == 0
    assert s.peek_z(1000) == +1

    s.h(100)
    s.z(100)
    assert s.peek_x(100) == -1
    assert s.peek_y(100) == 0
    assert s.peek_z(100) == 0

    s.h_xy(100)
    assert s.peek_x(100) == 0
    assert s.peek_y(100) == -1
    assert s.peek_z(100) == 0


def test_do_circuit():
    s = lestim.TableauSimulator()
    s.do_circuit(lestim.Circuit("""
        H 0
    """))
    assert s.peek_bloch(0) == lestim.PauliString('+X')


def test_do_pauli_string():
    s = lestim.TableauSimulator()
    s.do_pauli_string(lestim.PauliString("IXYZ"))
    assert s.peek_bloch(0) == lestim.PauliString('+Z')
    assert s.peek_bloch(1) == lestim.PauliString('-Z')
    assert s.peek_bloch(2) == lestim.PauliString('-Z')
    assert s.peek_bloch(3) == lestim.PauliString('+Z')


def test_do_tableau():
    s = lestim.TableauSimulator()
    s.do_tableau(lestim.Tableau.from_named_gate("H"), [0])
    assert s.peek_bloch(0) == lestim.PauliString('+X')
    s.do_tableau(lestim.Tableau.from_named_gate("CNOT"), [0, 1])
    assert s.peek_bloch(0) == lestim.PauliString('+I')
    assert s.peek_observable_expectation(lestim.PauliString('XX')) == +1
    assert s.peek_observable_expectation(lestim.PauliString('ZZ')) == +1

    with pytest.raises(ValueError, match='len'):
        s.do_tableau(lestim.Tableau(1), [1, 2])
    with pytest.raises(ValueError, match='duplicates'):
        s.do_tableau(lestim.Tableau(3), [2, 3, 2])

    s.do_tableau(lestim.Tableau(0), [])


def test_c_xyz_zyx():
    s = lestim.TableauSimulator()
    s.c_xyz(0, 2)
    s.c_zyx(1, 2)
    assert s.peek_bloch(0) == lestim.PauliString("X")
    assert s.peek_bloch(1) == lestim.PauliString("Y")
    assert s.peek_bloch(2) == lestim.PauliString("Z")


def test_gate_aliases():
    s = lestim.TableauSimulator()
    s.h_xz(0)
    assert s.peek_bloch(0) == lestim.PauliString("X")

    s.zcx(0, 1)
    assert s.canonical_stabilizers() == [
        lestim.PauliString("+XX"),
        lestim.PauliString("+ZZ")
    ]
    s.cx(0, 1)
    assert s.canonical_stabilizers() == [
        lestim.PauliString("+X_"),
        lestim.PauliString("+_Z")
    ]

    s.zcy(0, 1)
    assert s.canonical_stabilizers() == [
        lestim.PauliString("+XY"),
        lestim.PauliString("+ZZ")
    ]

    s.zcz(0, 1)
    assert s.canonical_stabilizers() == [
        lestim.PauliString("-XY"),
        lestim.PauliString("+ZZ")
    ]


def test_num_qubits():
    s = lestim.TableauSimulator()
    assert s.num_qubits == 0
    s.cx(3, 1)
    assert s.num_qubits == 4


def test_set_state_from_state_vector():
    s = lestim.TableauSimulator()
    expected = [0.5, 0.5, 0, 0, -0.5, 0.5, 0, 0]
    s.set_state_from_state_vector(expected, endian='little')
    np.testing.assert_allclose(s.state_vector(), expected, atol=1e-6)


def test_set_state_from_stabilizers():
    s = lestim.TableauSimulator()
    s.set_state_from_stabilizers([])
    assert s.current_inverse_tableau() == lestim.Tableau(0)
    s.set_state_from_stabilizers([lestim.PauliString("XXX"), lestim.PauliString("_ZZ"), lestim.PauliString("ZZ_")])
    np.testing.assert_allclose(s.state_vector(), [0.5**0.5, 0, 0, 0, 0, 0, 0, 0.5**0.5], atol=1e-6)


def test_seed():
    ss1 = [lestim.TableauSimulator(seed=0) for _ in range(5)]
    ss2 = [lestim.TableauSimulator(seed=1) for _ in range(5)]

    def hadamard_and_measure(sim, reps=5):
        """Repeats Hadamard+measurement reps times and returns result as reps-bit integer."""
        r, v = 0, 1
        for _ in range(reps):
            sim.h(0)
            r += v * sim.measure(0)
            v *= 2
        return r

    ms1 = {hadamard_and_measure(sim) for sim in ss1}
    ms2 = {hadamard_and_measure(sim) for sim in ss2}

    assert len(ms1) == 1
    assert len(ms2) == 1
    assert ms1 != ms2


def test_copy_without_fresh_entropy():
    s1 = lestim.TableauSimulator(seed=0)
    s2 = s1.copy(copy_rng=True)

    for _ in range(100):
        s1.h(0)
        s2.h(0)
        assert s1.measure(0) == s2.measure(0)


def test_copy_with_fresh_entropy():
    s1 = lestim.TableauSimulator(seed=0)
    s2 = s1.copy()

    eq = set()
    for _ in range(100):
        s1.h(0)
        s2.h(0)
        eq.add(s1.measure(0) == s2.measure(0))
    assert eq == {False, True}


def test_copy_with_explicit_seed():
    s1 = lestim.TableauSimulator(seed=0)
    s2 = lestim.TableauSimulator(seed=1)
    s3 = s1.copy(seed=1)

    eq = set()
    for _ in range(100):
        s1.h(0)
        s2.h(0)
        s3.h(0)
        m1 = s1.measure(0)
        m2 = s2.measure(0)
        m3 = s3.measure(0)
        assert m2 == m3
        eq.add(m1 == m3)

    assert eq == {False, True}


def test_copy_with_explicit_copy_rng_and_seed():
    s = lestim.TableauSimulator()
    with pytest.raises(ValueError, match='seed and copy_rng are incompatible'):
        _ = s.copy(copy_rng=True, seed=0)


def test_do_circuit_instruction():
    s = lestim.TableauSimulator()
    assert s.peek_z(0) == +1
    s.do(lestim.Circuit("X 0")[0])
    assert s.peek_z(0) == -1

    s.do(lestim.Circuit("""
        REPEAT 100 {
            CNOT 0 1 1 2 2 3 3 4 4 5 5 6 6 7 7 0
        }
    """)[0])
    assert s.peek_z(0) == +1
    assert s.peek_z(1) == +1
    assert s.peek_z(2) == +1
    assert s.peek_z(3) == -1
    assert s.peek_z(4) == +1
    assert s.peek_z(5) == -1
    assert s.peek_z(6) == +1
    assert s.peek_z(7) == +1

    s.do(lestim.Circuit("X 500")[0])
    assert s.peek_z(499) == +1
    assert s.peek_z(500) == -1
    assert s.peek_z(501) == +1


def test_measure_observable():
    s = lestim.TableauSimulator()

    with pytest.raises(ValueError, match="0 <= flip"):
        s.measure_observable(lestim.PauliString("XX"), flip_probability=-0.1)
    with pytest.raises(ValueError, match="Hermitian"):
        s.measure_observable(lestim.PauliString("iXX"))

    s.h(0)
    s.cnot(0, 1)
    assert not s.measure_observable(lestim.PauliString("ZZ"))
    assert s.measure_observable(lestim.PauliString("YY"))
    assert s.measure_observable(lestim.PauliString("-"))
    assert not s.measure_observable(lestim.PauliString(0))
    assert not s.measure_observable(lestim.PauliString(2))
    assert not s.measure_observable(lestim.PauliString(5))
    n = sum(s.measure_observable(lestim.PauliString(0), flip_probability=0.1) for _ in range(1000))
    assert 25 <= n <= 300


def test_x_error():
    s = lestim.TableauSimulator()
    assert s.peek_bloch(0) == lestim.PauliString("+Z")
    s.x_error(0, 1, 2, p=0)
    assert s.peek_bloch(0) == lestim.PauliString("+Z")
    s.x_error(0, p=1)
    assert s.peek_bloch(0) == lestim.PauliString("-Z")


def test_z_error():
    s = lestim.TableauSimulator()
    s.reset_x(0)
    assert s.peek_bloch(0) == lestim.PauliString("+X")
    s.z_error(0, p=0)
    assert s.peek_bloch(0) == lestim.PauliString("+X")
    s.z_error(0, p=1)
    assert s.peek_bloch(0) == lestim.PauliString("-X")


def test_y_error():
    s = lestim.TableauSimulator()
    s.reset_y(0)
    assert s.peek_bloch(0) == lestim.PauliString("+Y")
    s.x_error(0, p=0)
    assert s.peek_bloch(0) == lestim.PauliString("+Y")
    s.x_error(0, p=1)
    assert s.peek_bloch(0) == lestim.PauliString("-Y")


def test_depolarize1_error():
    s = lestim.TableauSimulator()
    s.h(0)
    s.cnot(0, 1)
    t = s.current_inverse_tableau()
    s.depolarize1(0, p=0)
    assert s.current_inverse_tableau() == t
    s.depolarize1(0, p=1)
    assert s.current_inverse_tableau() != t


def test_depolarize2_error():
    s = lestim.TableauSimulator()
    s.h(0, 1)
    s.cnot(0, 2, 1, 3)
    t = s.current_inverse_tableau()
    s.depolarize2(0, 1, p=0)
    assert s.current_inverse_tableau() == t
    with pytest.raises(ValueError, match='Two qubit'):
        s.depolarize2(1, p=1)
    assert s.current_inverse_tableau() == t
    s.depolarize2(0, 1, p=1)
    assert s.current_inverse_tableau() != t

    with pytest.raises(ValueError, match='Unexpected argument'):
        s.depolarize2(1, p=1, q=2)


def test_bad_inverse_padding_issue_is_fixed():
    circuit = lestim.Circuit()
    circuit.append("H", range(467))
    sim = lestim.TableauSimulator()
    sim.do(circuit)
    stabs = sim.canonical_stabilizers()
    assert stabs[-1] == lestim.PauliString(466 * '_' + 'X')


def test_postselect_observable():
    sim = lestim.TableauSimulator()
    assert sim.peek_bloch(0) == lestim.PauliString("+Z")

    sim.postselect_observable(lestim.PauliString("+X"))
    assert sim.peek_bloch(0) == lestim.PauliString("+X")

    sim.postselect_observable(lestim.PauliString("+Z"))
    assert sim.peek_bloch(0) == lestim.PauliString("+Z")

    sim.postselect_observable(lestim.PauliString("-X"))
    assert sim.peek_bloch(0) == lestim.PauliString("-X")

    sim.postselect_observable(lestim.PauliString("+Z"))
    assert sim.peek_bloch(0) == lestim.PauliString("+Z")

    sim.postselect_observable(lestim.PauliString("-X"), desired_value=True)
    assert sim.peek_bloch(0) == lestim.PauliString("+X")

    with pytest.raises(ValueError, match="impossible"):
        sim.postselect_observable(lestim.PauliString("-X"))
    assert sim.peek_bloch(0) == lestim.PauliString("+X")

    with pytest.raises(ValueError, match="imaginary sign"):
        sim.postselect_observable(lestim.PauliString("iZ"))
    assert sim.peek_bloch(0) == lestim.PauliString("+X")

    sim.postselect_observable(lestim.PauliString("+XX"))
    sim.postselect_observable(lestim.PauliString("+ZZ"))
    assert sim.peek_observable_expectation(lestim.PauliString("+YY")) == -1
