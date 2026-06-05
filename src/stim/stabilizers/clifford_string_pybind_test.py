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
import deltakit_stim


def test_trivial():
    p = deltakit_stim.CliffordString(3)
    assert repr(p) == 'deltakit_stim.CliffordString("I,I,I")'
    assert len(p) == 3
    assert p[1:] == deltakit_stim.CliffordString(2)
    assert p[0] == deltakit_stim.gate_data('I')


def test_simple():
    assert deltakit_stim.CliffordString("X,Y,Z,H,SQRT_X,C_XYZ,H_NXZ") == deltakit_stim.CliffordString("  X  ,   Y  ,  Z  , H_XZ , SQRT_X,C_XYZ,H_NXZ,   ")
    p = deltakit_stim.CliffordString("X,Y,Z,H,SQRT_X,C_XYZ,H_NXZ")
    assert repr(p) == 'deltakit_stim.CliffordString("X,Y,Z,H,SQRT_X,C_XYZ,H_NXZ")'
    assert str(p) == 'X,Y,Z,H,SQRT_X,C_XYZ,H_NXZ'
    assert len(p) == 7
    assert p != deltakit_stim.CliffordString("Y,Y,Z,H,SQRT_X,C_XYZ,H_NXZ")
    assert not (p != deltakit_stim.CliffordString("X,Y,Z,H,SQRT_X,C_XYZ,H_NXZ"))
    assert not (p == deltakit_stim.CliffordString("Y,Y,Z,H,SQRT_X,C_XYZ,H_NXZ"))
    assert p[1::2] == deltakit_stim.CliffordString("Y,H,C_XYZ")

    assert deltakit_stim.CliffordString(6) == deltakit_stim.CliffordString("I,I,I,I,I,I")

    assert deltakit_stim.CliffordString(deltakit_stim.PauliString("XYZ_XYZ")) == deltakit_stim.CliffordString("X,Y,Z,I,X,Y,Z")

    v = deltakit_stim.CliffordString("X,Y,H")
    v2 = deltakit_stim.CliffordString(v)
    assert v == v2
    assert v is not v2

    assert deltakit_stim.CliffordString(['X', 'Y', 'Z', deltakit_stim.gate_data('H'), 'S']) == deltakit_stim.CliffordString('X,Y,Z,H,S')


def test_multiplication():
    a = deltakit_stim.CliffordString("Z,H,S,C_XYZ")
    b = deltakit_stim.CliffordString("S,Z,S,C_XYZ,I")
    assert a * b == deltakit_stim.CliffordString("S_DAG,SQRT_Y,Z,C_ZYX,I")
    a *= b
    assert a == deltakit_stim.CliffordString("S_DAG,SQRT_Y,Z,C_ZYX,I")

    assert deltakit_stim.CliffordString("X") * deltakit_stim.CliffordString("H") == deltakit_stim.CliffordString("H") * deltakit_stim.CliffordString("Z")
    assert deltakit_stim.CliffordString("X") * deltakit_stim.CliffordString("H") != deltakit_stim.CliffordString("Z") * deltakit_stim.CliffordString("H")
    assert deltakit_stim.CliffordString("X") * deltakit_stim.CliffordString("H") == deltakit_stim.CliffordString("SQRT_Y")


def test_random():
    c1 = deltakit_stim.CliffordString.random(128)
    c2 = deltakit_stim.CliffordString.random(128)
    assert len(c1) == len(c2) == 128
    assert c1 != c2


def test_set_item():
    c = deltakit_stim.CliffordString(5)
    c[1] = "H"
    assert c == deltakit_stim.CliffordString("I,H,I,I,I")
    with pytest.raises(ValueError, match="index"):
        c[2:3] = None
    with pytest.raises(ValueError, match="index"):
        c[2] = None
    c[2:4] = deltakit_stim.CliffordString("X,Y")
    assert c == deltakit_stim.CliffordString("I,H,X,Y,I")
    c[::2] = deltakit_stim.CliffordString("S,Z,S_DAG")
    assert c == deltakit_stim.CliffordString("S,H,Z,Y,S_DAG")
    c[:] = 'H'
    assert c == deltakit_stim.CliffordString("H,H,H,H,H")
    c[:-2] = deltakit_stim.gate_data('S')
    assert c == deltakit_stim.CliffordString("S,S,S,H,H")
    c[0] = deltakit_stim.gate_data('X')
    assert c == deltakit_stim.CliffordString("X,S,S,H,H")

    with pytest.raises(ValueError, match="object of type"):
        c[0] = deltakit_stim.CliffordString("Y")
    with pytest.raises(ValueError, match="Length mismatch"):
        c[:2] = deltakit_stim.CliffordString("Y")
    assert c == deltakit_stim.CliffordString("X,S,S,H,H")
    c[:2] = deltakit_stim.CliffordString("Y,Y")
    assert c == deltakit_stim.CliffordString("Y,Y,S,H,H")


def all_cliffords_string_from_gate_data():
    c = deltakit_stim.CliffordString(24)
    r = 0
    for g in deltakit_stim.gate_data().values():
        if g.is_unitary and g.is_single_qubit_gate:
            c[r] = g
            r += 1
    return c


def test_x_outputs():
    paulis, signs = deltakit_stim.CliffordString("I,X,Y,Z,H,S,S_DAG,C_XYZ,C_ZYX,SQRT_X,SQRT_X_DAG").x_outputs()
    assert paulis == deltakit_stim.PauliString("XXXXZYYYZXX")
    np.testing.assert_array_equal(signs, [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0])

    c = all_cliffords_string_from_gate_data()
    paulis, signs = c.x_outputs()
    for k in range(len(c)):
        expected = c[k].tableau.x_output(0)
        assert (-1 if signs[k] else 1) == expected.sign
        assert paulis[k] == expected[0]


def test_y_outputs():
    paulis, signs = deltakit_stim.CliffordString("I,X,Y,Z,H,S,S_DAG,C_XYZ,C_ZYX,SQRT_X,SQRT_X_DAG").y_outputs()
    assert paulis == deltakit_stim.PauliString("YYYYYXXZXZZ")
    np.testing.assert_array_equal(signs, [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1])

    c = all_cliffords_string_from_gate_data()
    paulis, signs = c.y_outputs()
    for k in range(len(c)):
        expected = c[k].tableau.y_output(0)
        assert (-1 if signs[k] else 1) == expected.sign
        assert paulis[k] == expected[0]


def test_z_outputs():
    paulis, signs = deltakit_stim.CliffordString("I,X,Y,Z,H,S,S_DAG,C_XYZ,C_ZYX,SQRT_X,SQRT_X_DAG").z_outputs()
    assert paulis == deltakit_stim.PauliString("ZZZZXZZXYYY")
    np.testing.assert_array_equal(signs, [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0])

    c = all_cliffords_string_from_gate_data()
    paulis, signs = c.z_outputs()
    for k in range(len(c)):
        expected = c[k].tableau.z_output(0)
        assert (-1 if signs[k] else 1) == expected.sign
        assert paulis[k] == expected[0]


def test_all_cliffords_string():
    c = deltakit_stim.CliffordString.all_cliffords_string()
    assert len(c) == 24
    assert set(e.name for e in all_cliffords_string_from_gate_data()) == set(e.name for e in c)
