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

import numpy as np
import pytest
import lestim


def test_trivial():
    p = lestim.CliffordString(3)
    assert repr(p) == 'stim.CliffordString("I,I,I")'
    assert len(p) == 3
    assert p[1:] == lestim.CliffordString(2)
    assert p[0] == lestim.gate_data('I')


def test_simple():
    assert lestim.CliffordString("X,Y,Z,H,SQRT_X,C_XYZ,H_NXZ") == lestim.CliffordString("  X  ,   Y  ,  Z  , H_XZ , SQRT_X,C_XYZ,H_NXZ,   ")
    p = lestim.CliffordString("X,Y,Z,H,SQRT_X,C_XYZ,H_NXZ")
    assert repr(p) == 'stim.CliffordString("X,Y,Z,H,SQRT_X,C_XYZ,H_NXZ")'
    assert str(p) == 'X,Y,Z,H,SQRT_X,C_XYZ,H_NXZ'
    assert len(p) == 7
    assert p != lestim.CliffordString("Y,Y,Z,H,SQRT_X,C_XYZ,H_NXZ")
    assert not (p != lestim.CliffordString("X,Y,Z,H,SQRT_X,C_XYZ,H_NXZ"))
    assert not (p == lestim.CliffordString("Y,Y,Z,H,SQRT_X,C_XYZ,H_NXZ"))
    assert p[1::2] == lestim.CliffordString("Y,H,C_XYZ")

    assert lestim.CliffordString(6) == lestim.CliffordString("I,I,I,I,I,I")

    assert lestim.CliffordString(lestim.PauliString("XYZ_XYZ")) == lestim.CliffordString("X,Y,Z,I,X,Y,Z")

    v = lestim.CliffordString("X,Y,H")
    v2 = lestim.CliffordString(v)
    assert v == v2
    assert v is not v2

    assert lestim.CliffordString(['X', 'Y', 'Z', lestim.gate_data('H'), 'S']) == lestim.CliffordString('X,Y,Z,H,S')


def test_multiplication():
    a = lestim.CliffordString("Z,H,S,C_XYZ")
    b = lestim.CliffordString("S,Z,S,C_XYZ,I")
    assert a * b == lestim.CliffordString("S_DAG,SQRT_Y,Z,C_ZYX,I")
    a *= b
    assert a == lestim.CliffordString("S_DAG,SQRT_Y,Z,C_ZYX,I")

    assert lestim.CliffordString("X") * lestim.CliffordString("H") == lestim.CliffordString("H") * lestim.CliffordString("Z")
    assert lestim.CliffordString("X") * lestim.CliffordString("H") != lestim.CliffordString("Z") * lestim.CliffordString("H")
    assert lestim.CliffordString("X") * lestim.CliffordString("H") == lestim.CliffordString("SQRT_Y")


def test_random():
    c1 = lestim.CliffordString.random(128)
    c2 = lestim.CliffordString.random(128)
    assert len(c1) == len(c2) == 128
    assert c1 != c2


def test_set_item():
    c = lestim.CliffordString(5)
    c[1] = "H"
    assert c == lestim.CliffordString("I,H,I,I,I")
    with pytest.raises(ValueError, match="index"):
        c[2:3] = None
    with pytest.raises(ValueError, match="index"):
        c[2] = None
    c[2:4] = lestim.CliffordString("X,Y")
    assert c == lestim.CliffordString("I,H,X,Y,I")
    c[::2] = lestim.CliffordString("S,Z,S_DAG")
    assert c == lestim.CliffordString("S,H,Z,Y,S_DAG")
    c[:] = 'H'
    assert c == lestim.CliffordString("H,H,H,H,H")
    c[:-2] = lestim.gate_data('S')
    assert c == lestim.CliffordString("S,S,S,H,H")
    c[0] = lestim.gate_data('X')
    assert c == lestim.CliffordString("X,S,S,H,H")

    with pytest.raises(ValueError, match="object of type"):
        c[0] = lestim.CliffordString("Y")
    with pytest.raises(ValueError, match="Length mismatch"):
        c[:2] = lestim.CliffordString("Y")
    assert c == lestim.CliffordString("X,S,S,H,H")
    c[:2] = lestim.CliffordString("Y,Y")
    assert c == lestim.CliffordString("Y,Y,S,H,H")


def all_cliffords_string_from_gate_data():
    c = lestim.CliffordString(24)
    r = 0
    for g in lestim.gate_data().values():
        if g.is_unitary and g.is_single_qubit_gate:
            c[r] = g
            r += 1
    return c


def test_x_outputs():
    paulis, signs = lestim.CliffordString("I,X,Y,Z,H,S,S_DAG,C_XYZ,C_ZYX,SQRT_X,SQRT_X_DAG").x_outputs()
    assert paulis == lestim.PauliString("XXXXZYYYZXX")
    np.testing.assert_array_equal(signs, [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0])

    c = all_cliffords_string_from_gate_data()
    paulis, signs = c.x_outputs()
    for k in range(len(c)):
        expected = c[k].tableau.x_output(0)
        assert (-1 if signs[k] else 1) == expected.sign
        assert paulis[k] == expected[0]


def test_y_outputs():
    paulis, signs = lestim.CliffordString("I,X,Y,Z,H,S,S_DAG,C_XYZ,C_ZYX,SQRT_X,SQRT_X_DAG").y_outputs()
    assert paulis == lestim.PauliString("YYYYYXXZXZZ")
    np.testing.assert_array_equal(signs, [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1])

    c = all_cliffords_string_from_gate_data()
    paulis, signs = c.y_outputs()
    for k in range(len(c)):
        expected = c[k].tableau.y_output(0)
        assert (-1 if signs[k] else 1) == expected.sign
        assert paulis[k] == expected[0]


def test_z_outputs():
    paulis, signs = lestim.CliffordString("I,X,Y,Z,H,S,S_DAG,C_XYZ,C_ZYX,SQRT_X,SQRT_X_DAG").z_outputs()
    assert paulis == lestim.PauliString("ZZZZXZZXYYY")
    np.testing.assert_array_equal(signs, [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0])

    c = all_cliffords_string_from_gate_data()
    paulis, signs = c.z_outputs()
    for k in range(len(c)):
        expected = c[k].tableau.z_output(0)
        assert (-1 if signs[k] else 1) == expected.sign
        assert paulis[k] == expected[0]


def test_all_cliffords_string():
    c = lestim.CliffordString.all_cliffords_string()
    assert len(c) == 24
    assert set(e.name for e in all_cliffords_string_from_gate_data()) == set(e.name for e in c)
