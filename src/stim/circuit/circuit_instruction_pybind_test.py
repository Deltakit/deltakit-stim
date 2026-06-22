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

import deltakit_stim
import pytest


def test_init_and_equality():
    i = deltakit_stim.CircuitInstruction("X_ERROR", [deltakit_stim.GateTarget(5)], [0.5])
    assert i.name == "X_ERROR"
    assert i.targets_copy() == [deltakit_stim.GateTarget(5)]
    assert i.gate_args_copy() == [0.5]
    i2 = deltakit_stim.CircuitInstruction(name="X_ERROR", targets=[deltakit_stim.GateTarget(5)], gate_args=[0.5])
    assert i == i2

    assert i == deltakit_stim.CircuitInstruction("X_ERROR", [deltakit_stim.GateTarget(5)], [0.5])
    assert not (i == deltakit_stim.CircuitInstruction("Z_ERROR", [deltakit_stim.GateTarget(5)], [0.5]))
    assert i != deltakit_stim.CircuitInstruction("Z_ERROR", [deltakit_stim.GateTarget(5)], [0.5])
    assert i != deltakit_stim.CircuitInstruction("X_ERROR", [deltakit_stim.GateTarget(5), deltakit_stim.GateTarget(6)], [0.5])
    assert i != deltakit_stim.CircuitInstruction("X_ERROR", [deltakit_stim.GateTarget(5)], [0.25])


@pytest.mark.parametrize("value", [
    deltakit_stim.CircuitInstruction("X_ERROR", [deltakit_stim.GateTarget(5)], [0.5]),
    deltakit_stim.CircuitInstruction("M", [deltakit_stim.GateTarget(deltakit_stim.target_inv(3))]),
])
def test_repr(value):
    assert eval(repr(value), {'stim': deltakit_stim}) == value
    assert repr(eval(repr(value), {'stim': deltakit_stim})) == repr(value)


def test_str():
    assert str(deltakit_stim.CircuitInstruction("X_ERROR", [deltakit_stim.GateTarget(5)], [0.5])) == "X_ERROR(0.5) 5"


def test_hashable():
    a = deltakit_stim.CircuitInstruction("X_ERROR", [deltakit_stim.GateTarget(5)], [0.5])
    b = deltakit_stim.CircuitInstruction("DEPOLARIZE1", [deltakit_stim.GateTarget(5)], [0.5])
    c = deltakit_stim.CircuitInstruction("X_ERROR", [deltakit_stim.GateTarget(5)], [0.5])
    assert hash(a) == hash(c)
    assert len({a, b, c}) == 2


def test_num_measurements():
    assert deltakit_stim.CircuitInstruction("X", [1, 2, 3]).num_measurements == 0
    assert deltakit_stim.CircuitInstruction("MXX", [1, 2]).num_measurements == 1
    assert deltakit_stim.CircuitInstruction("M", [1, 2]).num_measurements == 2
    assert deltakit_stim.CircuitInstruction("MPAD", [0, 1, 0]).num_measurements == 3


def test_target_groups():
    assert deltakit_stim.CircuitInstruction("MPAD", [0, 1, 0]).target_groups() == [
        [deltakit_stim.GateTarget(0)],
        [deltakit_stim.GateTarget(1)],
        [deltakit_stim.GateTarget(0)],
    ]
    assert deltakit_stim.CircuitInstruction("H", []).target_groups() == []
    assert deltakit_stim.CircuitInstruction("H", [1]).target_groups() == [[deltakit_stim.GateTarget(1)]]
    assert deltakit_stim.CircuitInstruction("H", [2, 3]).target_groups() == [[deltakit_stim.GateTarget(2)], [deltakit_stim.GateTarget(3)]]
    assert deltakit_stim.CircuitInstruction("CX", []).target_groups() == []
    assert deltakit_stim.CircuitInstruction("CX", [0, 1]).target_groups() == [[deltakit_stim.GateTarget(0), deltakit_stim.GateTarget(1)]]
    assert deltakit_stim.CircuitInstruction("CX", [2, 3, 5, 7]).target_groups() == [[deltakit_stim.GateTarget(2), deltakit_stim.GateTarget(3)], [deltakit_stim.GateTarget(5), deltakit_stim.GateTarget(7)]]
    assert deltakit_stim.CircuitInstruction("DETECTOR", []).target_groups() == []
    assert deltakit_stim.CircuitInstruction("CORRELATED_ERROR", [], [0.001]).target_groups() == []
    assert deltakit_stim.CircuitInstruction("MPP", []).target_groups() == []
    assert deltakit_stim.CircuitInstruction("MPAD", []).target_groups() == []
    assert deltakit_stim.CircuitInstruction("QUBIT_COORDS", [1, 2]).target_groups() == [[deltakit_stim.GateTarget(1)], [deltakit_stim.GateTarget(2)]]


def test_eager_validate():
    with pytest.raises(ValueError, match="0, 1, 2"):
        deltakit_stim.CircuitInstruction("CX", [0, 1, 2])


def test_init_from_str():
    assert deltakit_stim.CircuitInstruction("CX", [0, 1]) == deltakit_stim.CircuitInstruction("CX 0 1")

    with pytest.raises(ValueError, match="single CircuitInstruction"):
        deltakit_stim.CircuitInstruction("")

    with pytest.raises(ValueError, match="single CircuitInstruction"):
        deltakit_stim.CircuitInstruction("""
            REPEAT 5 {
                H 0
                X 1
            }
        """)

    with pytest.raises(ValueError, match="single CircuitInstruction"):
        deltakit_stim.CircuitInstruction("""
            H 0 
            X 1
        """)
