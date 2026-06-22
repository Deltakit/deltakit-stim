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
    r = deltakit_stim.CircuitRepeatBlock(500, deltakit_stim.Circuit("X 0"))
    assert r.repeat_count == 500
    assert r.body_copy() == deltakit_stim.Circuit("X 0")
    assert deltakit_stim.CircuitRepeatBlock(500, deltakit_stim.Circuit("X 0")) == deltakit_stim.CircuitRepeatBlock(500, deltakit_stim.Circuit("X 0"))
    assert deltakit_stim.CircuitRepeatBlock(500, deltakit_stim.Circuit("X 0")) != deltakit_stim.CircuitRepeatBlock(500, deltakit_stim.Circuit())
    assert deltakit_stim.CircuitRepeatBlock(500, deltakit_stim.Circuit("X 0")) != deltakit_stim.CircuitRepeatBlock(101, deltakit_stim.Circuit("X 0"))
    assert not (deltakit_stim.CircuitRepeatBlock(500, deltakit_stim.Circuit("X 0")) == deltakit_stim.CircuitRepeatBlock(500, deltakit_stim.Circuit()))
    assert not (deltakit_stim.CircuitRepeatBlock(500, deltakit_stim.Circuit("X 0")) != deltakit_stim.CircuitRepeatBlock(500, deltakit_stim.Circuit("X 0")))
    r2 = deltakit_stim.CircuitRepeatBlock(repeat_count=500, body=deltakit_stim.Circuit("X 0"))
    assert r == r2

    with pytest.raises(ValueError, match="repeat 0"):
        deltakit_stim.CircuitRepeatBlock(0, deltakit_stim.Circuit())


@pytest.mark.parametrize("value", [
    deltakit_stim.CircuitRepeatBlock(500, deltakit_stim.Circuit("X 0")),
    deltakit_stim.CircuitRepeatBlock(1, deltakit_stim.Circuit("X 0\nREPEAT 100 {\nH 1\n}\n")),
])
def test_repr(value):
    assert eval(repr(value), {'stim': deltakit_stim}) == value
    assert repr(eval(repr(value), {'stim': deltakit_stim})) == repr(value)


def test_name():
    assert [e.name for e in deltakit_stim.Circuit('''
        H 0
        REPEAT 5 {
            CX 1 2
        }
        S 1
    ''')] == ['H', 'REPEAT', 'S']
