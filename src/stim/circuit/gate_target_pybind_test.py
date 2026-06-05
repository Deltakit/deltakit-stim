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
    assert deltakit_stim.GateTarget(5) == deltakit_stim.GateTarget(5)
    assert deltakit_stim.GateTarget(5) == deltakit_stim.GateTarget(value=5)
    assert not (deltakit_stim.GateTarget(4) == deltakit_stim.GateTarget(5))
    assert deltakit_stim.GateTarget(4) != deltakit_stim.GateTarget(5)
    assert not (deltakit_stim.GateTarget(5) != deltakit_stim.GateTarget(5))
    assert deltakit_stim.GateTarget(deltakit_stim.target_x(5)) != deltakit_stim.GateTarget(5)
    assert deltakit_stim.GateTarget(5) == deltakit_stim.GateTarget(deltakit_stim.GateTarget(5))


def test_properties():
    g = deltakit_stim.GateTarget(5)
    assert g.value == 5
    assert not g.is_x_target
    assert not g.is_y_target
    assert not g.is_z_target
    assert not g.is_inverted_result_target
    assert not g.is_measurement_record_target
    assert not g.is_combiner
    assert g.is_qubit_target

    g = deltakit_stim.GateTarget(deltakit_stim.target_rec(-4))
    assert g.value == -4
    assert not g.is_x_target
    assert not g.is_y_target
    assert not g.is_z_target
    assert not g.is_inverted_result_target
    assert g.is_measurement_record_target
    assert not g.is_combiner
    assert not g.is_qubit_target

    g = deltakit_stim.GateTarget(deltakit_stim.target_x(3))
    assert g.value == 3
    assert g.is_x_target
    assert not g.is_y_target
    assert not g.is_z_target
    assert not g.is_inverted_result_target
    assert not g.is_measurement_record_target
    assert not g.is_combiner
    assert not g.is_qubit_target

    g = deltakit_stim.GateTarget(deltakit_stim.target_y(3))
    assert g.value == 3
    assert not g.is_x_target
    assert g.is_y_target
    assert not g.is_z_target
    assert not g.is_inverted_result_target
    assert not g.is_measurement_record_target
    assert not g.is_combiner
    assert not g.is_qubit_target

    g = deltakit_stim.GateTarget(deltakit_stim.target_z(3))
    assert g.value == 3
    assert not g.is_x_target
    assert not g.is_y_target
    assert g.is_z_target
    assert not g.is_inverted_result_target
    assert not g.is_measurement_record_target
    assert not g.is_combiner
    assert not g.is_qubit_target

    g = deltakit_stim.GateTarget(deltakit_stim.target_z(3, invert=True))
    assert g.value == 3
    assert not g.is_x_target
    assert not g.is_y_target
    assert g.is_z_target
    assert g.is_inverted_result_target
    assert not g.is_measurement_record_target
    assert not g.is_combiner
    assert not g.is_qubit_target

    g = deltakit_stim.GateTarget(deltakit_stim.target_inv(3))
    assert g.value == 3
    assert not g.is_x_target
    assert not g.is_y_target
    assert not g.is_z_target
    assert g.is_inverted_result_target
    assert not g.is_measurement_record_target
    assert not g.is_combiner
    assert g.is_qubit_target

    g = deltakit_stim.target_combiner()
    assert not g.is_x_target
    assert not g.is_y_target
    assert not g.is_z_target
    assert not g.is_inverted_result_target
    assert not g.is_measurement_record_target
    assert not g.is_qubit_target
    assert g.is_combiner


@pytest.mark.parametrize("value", [
    deltakit_stim.GateTarget(5),
    deltakit_stim.GateTarget(deltakit_stim.target_rec(-5)),
    deltakit_stim.GateTarget(deltakit_stim.target_x(5)),
    deltakit_stim.GateTarget(deltakit_stim.target_y(5)),
    deltakit_stim.GateTarget(deltakit_stim.target_z(5)),
    deltakit_stim.GateTarget(deltakit_stim.target_inv(5)),
])
def test_repr(value):
    assert eval(repr(value), {'deltakit_stim': deltakit_stim}) == value
    assert repr(eval(repr(value), {'deltakit_stim': deltakit_stim})) == repr(value)


def test_hashable():
    a = deltakit_stim.GateTarget(5)
    b = deltakit_stim.GateTarget(6)
    c = deltakit_stim.GateTarget(5)
    assert hash(a) == hash(c)
    assert len({a, b, c}) == 2


def test_pauli_type():
    assert deltakit_stim.GateTarget(5).pauli_type == 'I'
    assert deltakit_stim.target_inv(5).pauli_type == 'I'
    assert deltakit_stim.target_rec(-5).pauli_type == 'I'
    assert deltakit_stim.target_sweep_bit(6).pauli_type == 'I'

    assert deltakit_stim.target_x(7).pauli_type == 'X'
    assert deltakit_stim.target_y(8).pauli_type == 'Y'
    assert deltakit_stim.target_y(8, invert=True).pauli_type == 'Y'
    assert deltakit_stim.target_z(9).pauli_type == 'Z'
