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
import deltakit_stim


def test_equality():
    assert deltakit_stim.target_relative_detector_id(5) == deltakit_stim.target_relative_detector_id(5)
    assert not (deltakit_stim.target_relative_detector_id(5) != deltakit_stim.target_relative_detector_id(5))
    assert deltakit_stim.target_relative_detector_id(4) != deltakit_stim.target_relative_detector_id(5)
    assert not (deltakit_stim.target_relative_detector_id(4) == deltakit_stim.target_relative_detector_id(5))

    assert deltakit_stim.target_relative_detector_id(5) != deltakit_stim.target_logical_observable_id(5)
    assert deltakit_stim.target_logical_observable_id(5) == deltakit_stim.target_logical_observable_id(5)
    assert deltakit_stim.target_relative_detector_id(5) != deltakit_stim.target_separator()
    assert deltakit_stim.target_separator() == deltakit_stim.target_separator()


def test_str():
    assert str(deltakit_stim.target_relative_detector_id(5)) == "D5"
    assert str(deltakit_stim.target_logical_observable_id(6)) == "L6"
    assert str(deltakit_stim.target_separator()) == "^"


def test_properties():
    assert deltakit_stim.target_relative_detector_id(6).val == 6
    assert deltakit_stim.target_relative_detector_id(5).val == 5
    assert deltakit_stim.target_relative_detector_id(5).is_relative_detector_id()
    assert not deltakit_stim.target_relative_detector_id(5).is_logical_observable_id()
    assert not deltakit_stim.target_relative_detector_id(5).is_separator()

    assert deltakit_stim.target_logical_observable_id(6).val == 6
    assert deltakit_stim.target_logical_observable_id(5).val == 5
    assert not deltakit_stim.target_logical_observable_id(5).is_relative_detector_id()
    assert deltakit_stim.target_logical_observable_id(5).is_logical_observable_id()
    assert not deltakit_stim.target_logical_observable_id(5).is_separator()

    assert not deltakit_stim.target_separator().is_relative_detector_id()
    assert not deltakit_stim.target_separator().is_logical_observable_id()
    assert deltakit_stim.target_separator().is_separator()
    with pytest.raises(ValueError, match="Separator"):
        _ = deltakit_stim.target_separator().val


def test_repr():
    v = deltakit_stim.target_relative_detector_id(5)
    assert eval(repr(v), {"stim": deltakit_stim}) == v
    v = deltakit_stim.target_logical_observable_id(6)
    assert eval(repr(v), {"stim": deltakit_stim}) == v
    v = deltakit_stim.target_separator()
    assert eval(repr(v), {"stim": deltakit_stim}) == v


def test_static_constructors():
    assert deltakit_stim.DemTarget.relative_detector_id(5) == deltakit_stim.target_relative_detector_id(5)
    assert deltakit_stim.DemTarget.logical_observable_id(5) == deltakit_stim.target_logical_observable_id(5)
    assert deltakit_stim.DemTarget.separator() == deltakit_stim.target_separator()


def test_hashable():
    a = deltakit_stim.DemTarget.relative_detector_id(3)
    b = deltakit_stim.DemTarget.logical_observable_id(5)
    c = deltakit_stim.DemTarget.relative_detector_id(3)
    assert hash(a) == hash(c)
    assert len({a, b, c}) == 2


def test_init():
    assert deltakit_stim.DemTarget("D0") == deltakit_stim.target_relative_detector_id(0)
    assert deltakit_stim.DemTarget("D5") == deltakit_stim.target_relative_detector_id(5)
    assert deltakit_stim.DemTarget("L0") == deltakit_stim.target_logical_observable_id(0)
    assert deltakit_stim.DemTarget("L5") == deltakit_stim.target_logical_observable_id(5)
    assert deltakit_stim.DemTarget("^") == deltakit_stim.target_separator()
    assert deltakit_stim.DemTarget(f"D{2**62 - 1}") == deltakit_stim.target_relative_detector_id(2**62 - 1)
    assert deltakit_stim.DemTarget(f"L{0xFFFFFFFF}") == deltakit_stim.target_logical_observable_id(0xFFFFFFFF)
    with pytest.raises(ValueError, match="Failed to parse"):
        _ = deltakit_stim.DemTarget(f"D{2**62}")
    with pytest.raises(ValueError, match="Failed to parse"):
        _ = deltakit_stim.DemTarget(f"L{0x100000000}")
    with pytest.raises(ValueError, match="Failed to parse"):
        _ = deltakit_stim.DemTarget(f"L-1")
    with pytest.raises(ValueError, match="Failed to parse"):
        _ = deltakit_stim.DemTarget(f"X5")
    with pytest.raises(ValueError, match="Failed to parse"):
        _ = deltakit_stim.DemTarget(f"5")
