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
    r = lestim.CircuitRepeatBlock(500, lestim.Circuit("X 0"))
    assert r.repeat_count == 500
    assert r.body_copy() == lestim.Circuit("X 0")
    assert lestim.CircuitRepeatBlock(500, lestim.Circuit("X 0")) == lestim.CircuitRepeatBlock(500, lestim.Circuit("X 0"))
    assert lestim.CircuitRepeatBlock(500, lestim.Circuit("X 0")) != lestim.CircuitRepeatBlock(500, lestim.Circuit())
    assert lestim.CircuitRepeatBlock(500, lestim.Circuit("X 0")) != lestim.CircuitRepeatBlock(101, lestim.Circuit("X 0"))
    assert not (lestim.CircuitRepeatBlock(500, lestim.Circuit("X 0")) == lestim.CircuitRepeatBlock(500, lestim.Circuit()))
    assert not (lestim.CircuitRepeatBlock(500, lestim.Circuit("X 0")) != lestim.CircuitRepeatBlock(500, lestim.Circuit("X 0")))
    r2 = lestim.CircuitRepeatBlock(repeat_count=500, body=lestim.Circuit("X 0"))
    assert r == r2

    with pytest.raises(ValueError, match="repeat 0"):
        lestim.CircuitRepeatBlock(0, lestim.Circuit())


@pytest.mark.parametrize("value", [
    lestim.CircuitRepeatBlock(500, lestim.Circuit("X 0")),
    lestim.CircuitRepeatBlock(1, lestim.Circuit("X 0\nREPEAT 100 {\nH 1\n}\n")),
])
def test_repr(value):
    assert eval(repr(value), {'stim': lestim}) == value
    assert repr(eval(repr(value), {'stim': lestim})) == repr(value)


def test_name():
    assert [e.name for e in lestim.Circuit('''
        H 0
        REPEAT 5 {
            CX 1 2
        }
        S 1
    ''')] == ['H', 'REPEAT', 'S']
