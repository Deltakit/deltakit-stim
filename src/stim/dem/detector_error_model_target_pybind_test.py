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


def test_equality():
    assert lestim.target_relative_detector_id(5) == lestim.target_relative_detector_id(5)
    assert not (lestim.target_relative_detector_id(5) != lestim.target_relative_detector_id(5))
    assert lestim.target_relative_detector_id(4) != lestim.target_relative_detector_id(5)
    assert not (lestim.target_relative_detector_id(4) == lestim.target_relative_detector_id(5))

    assert lestim.target_relative_detector_id(5) != lestim.target_logical_observable_id(5)
    assert lestim.target_logical_observable_id(5) == lestim.target_logical_observable_id(5)
    assert lestim.target_relative_detector_id(5) != lestim.target_separator()
    assert lestim.target_separator() == lestim.target_separator()


def test_str():
    assert str(lestim.target_relative_detector_id(5)) == "D5"
    assert str(lestim.target_logical_observable_id(6)) == "L6"
    assert str(lestim.target_separator()) == "^"


def test_properties():
    assert lestim.target_relative_detector_id(6).val == 6
    assert lestim.target_relative_detector_id(5).val == 5
    assert lestim.target_relative_detector_id(5).is_relative_detector_id()
    assert not lestim.target_relative_detector_id(5).is_logical_observable_id()
    assert not lestim.target_relative_detector_id(5).is_separator()

    assert lestim.target_logical_observable_id(6).val == 6
    assert lestim.target_logical_observable_id(5).val == 5
    assert not lestim.target_logical_observable_id(5).is_relative_detector_id()
    assert lestim.target_logical_observable_id(5).is_logical_observable_id()
    assert not lestim.target_logical_observable_id(5).is_separator()

    assert not lestim.target_separator().is_relative_detector_id()
    assert not lestim.target_separator().is_logical_observable_id()
    assert lestim.target_separator().is_separator()
    with pytest.raises(ValueError, match="Separator"):
        _ = lestim.target_separator().val


def test_repr():
    v = lestim.target_relative_detector_id(5)
    assert eval(repr(v), {"stim": lestim}) == v
    v = lestim.target_logical_observable_id(6)
    assert eval(repr(v), {"stim": lestim}) == v
    v = lestim.target_separator()
    assert eval(repr(v), {"stim": lestim}) == v


def test_static_constructors():
    assert lestim.DemTarget.relative_detector_id(5) == lestim.target_relative_detector_id(5)
    assert lestim.DemTarget.logical_observable_id(5) == lestim.target_logical_observable_id(5)
    assert lestim.DemTarget.separator() == lestim.target_separator()


def test_hashable():
    a = lestim.DemTarget.relative_detector_id(3)
    b = lestim.DemTarget.logical_observable_id(5)
    c = lestim.DemTarget.relative_detector_id(3)
    assert hash(a) == hash(c)
    assert len({a, b, c}) == 2


def test_init():
    assert lestim.DemTarget("D0") == lestim.target_relative_detector_id(0)
    assert lestim.DemTarget("D5") == lestim.target_relative_detector_id(5)
    assert lestim.DemTarget("L0") == lestim.target_logical_observable_id(0)
    assert lestim.DemTarget("L5") == lestim.target_logical_observable_id(5)
    assert lestim.DemTarget("^") == lestim.target_separator()
    assert lestim.DemTarget(f"D{2**62 - 1}") == lestim.target_relative_detector_id(2**62 - 1)
    assert lestim.DemTarget(f"L{0xFFFFFFFF}") == lestim.target_logical_observable_id(0xFFFFFFFF)
    with pytest.raises(ValueError, match="Failed to parse"):
        _ = lestim.DemTarget(f"D{2**62}")
    with pytest.raises(ValueError, match="Failed to parse"):
        _ = lestim.DemTarget(f"L{0x100000000}")
    with pytest.raises(ValueError, match="Failed to parse"):
        _ = lestim.DemTarget(f"L-1")
    with pytest.raises(ValueError, match="Failed to parse"):
        _ = lestim.DemTarget(f"X5")
    with pytest.raises(ValueError, match="Failed to parse"):
        _ = lestim.DemTarget(f"5")
