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

import lestim
import pytest


def test_init_and_equality():
    i = lestim.CircuitInstruction("X_ERROR", [lestim.GateTarget(5)], [0.5])
    assert i.name == "X_ERROR"
    assert i.targets_copy() == [lestim.GateTarget(5)]
    assert i.gate_args_copy() == [0.5]
    i2 = lestim.CircuitInstruction(name="X_ERROR", targets=[lestim.GateTarget(5)], gate_args=[0.5])
    assert i == i2

    assert i == lestim.CircuitInstruction("X_ERROR", [lestim.GateTarget(5)], [0.5])
    assert not (i == lestim.CircuitInstruction("Z_ERROR", [lestim.GateTarget(5)], [0.5]))
    assert i != lestim.CircuitInstruction("Z_ERROR", [lestim.GateTarget(5)], [0.5])
    assert i != lestim.CircuitInstruction("X_ERROR", [lestim.GateTarget(5), lestim.GateTarget(6)], [0.5])
    assert i != lestim.CircuitInstruction("X_ERROR", [lestim.GateTarget(5)], [0.25])


@pytest.mark.parametrize("value", [
    lestim.CircuitInstruction("X_ERROR", [lestim.GateTarget(5)], [0.5]),
    lestim.CircuitInstruction("M", [lestim.GateTarget(lestim.target_inv(3))]),
])
def test_repr(value):
    assert eval(repr(value), {'stim': lestim}) == value
    assert repr(eval(repr(value), {'stim': lestim})) == repr(value)


def test_str():
    assert str(lestim.CircuitInstruction("X_ERROR", [lestim.GateTarget(5)], [0.5])) == "X_ERROR(0.5) 5"


def test_hashable():
    a = lestim.CircuitInstruction("X_ERROR", [lestim.GateTarget(5)], [0.5])
    b = lestim.CircuitInstruction("DEPOLARIZE1", [lestim.GateTarget(5)], [0.5])
    c = lestim.CircuitInstruction("X_ERROR", [lestim.GateTarget(5)], [0.5])
    assert hash(a) == hash(c)
    assert len({a, b, c}) == 2


def test_num_measurements():
    assert lestim.CircuitInstruction("X", [1, 2, 3]).num_measurements == 0
    assert lestim.CircuitInstruction("MXX", [1, 2]).num_measurements == 1
    assert lestim.CircuitInstruction("M", [1, 2]).num_measurements == 2
    assert lestim.CircuitInstruction("MPAD", [0, 1, 0]).num_measurements == 3


def test_target_groups():
    assert lestim.CircuitInstruction("MPAD", [0, 1, 0]).target_groups() == [
        [lestim.GateTarget(0)],
        [lestim.GateTarget(1)],
        [lestim.GateTarget(0)],
    ]
    assert lestim.CircuitInstruction("H", []).target_groups() == []
    assert lestim.CircuitInstruction("H", [1]).target_groups() == [[lestim.GateTarget(1)]]
    assert lestim.CircuitInstruction("H", [2, 3]).target_groups() == [[lestim.GateTarget(2)], [lestim.GateTarget(3)]]
    assert lestim.CircuitInstruction("CX", []).target_groups() == []
    assert lestim.CircuitInstruction("CX", [0, 1]).target_groups() == [[lestim.GateTarget(0), lestim.GateTarget(1)]]
    assert lestim.CircuitInstruction("CX", [2, 3, 5, 7]).target_groups() == [[lestim.GateTarget(2), lestim.GateTarget(3)], [lestim.GateTarget(5), lestim.GateTarget(7)]]
    assert lestim.CircuitInstruction("DETECTOR", []).target_groups() == []
    assert lestim.CircuitInstruction("CORRELATED_ERROR", [], [0.001]).target_groups() == []
    assert lestim.CircuitInstruction("MPP", []).target_groups() == []
    assert lestim.CircuitInstruction("MPAD", []).target_groups() == []
    assert lestim.CircuitInstruction("QUBIT_COORDS", [1, 2]).target_groups() == [[lestim.GateTarget(1)], [lestim.GateTarget(2)]]


def test_eager_validate():
    with pytest.raises(ValueError, match="0, 1, 2"):
        lestim.CircuitInstruction("CX", [0, 1, 2])


def test_init_from_str():
    assert lestim.CircuitInstruction("CX", [0, 1]) == lestim.CircuitInstruction("CX 0 1")

    with pytest.raises(ValueError, match="single CircuitInstruction"):
        lestim.CircuitInstruction("")

    with pytest.raises(ValueError, match="single CircuitInstruction"):
        lestim.CircuitInstruction("""
            REPEAT 5 {
                H 0
                X 1
            }
        """)

    with pytest.raises(ValueError, match="single CircuitInstruction"):
        lestim.CircuitInstruction("""
            H 0 
            X 1
        """)
