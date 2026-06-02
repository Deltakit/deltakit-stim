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


def test_init_vs_properties():
    v = lestim.DemRepeatBlock(5, lestim.DetectorErrorModel('error(0.125) D1 L2'))
    assert v.repeat_count == 5
    assert v.body_copy() == lestim.DetectorErrorModel('error(0.125) D1 L2')
    assert v.body_copy() is not v.body_copy()


def test_equality():
    m0 = lestim.DetectorErrorModel()
    m1 = lestim.DetectorErrorModel('error(0.125) D1 L2')
    assert lestim.DemRepeatBlock(5, m0) == lestim.DemRepeatBlock(5, m0)
    assert not (lestim.DemRepeatBlock(5, m0) != lestim.DemRepeatBlock(5, m0))
    assert lestim.DemRepeatBlock(5, m0) != lestim.DemRepeatBlock(5, m1)
    assert not (lestim.DemRepeatBlock(5, m0) == lestim.DemRepeatBlock(5, m1))
    assert lestim.DemRepeatBlock(5, m0) != lestim.DemRepeatBlock(6, m0)


def test_repr():
    v = lestim.DemRepeatBlock(5, lestim.DetectorErrorModel('error(0.125) D1 L2'))
    assert eval(repr(v), {"stim": lestim}) == v


def test_type():
    assert [e.type for e in lestim.DetectorErrorModel('''
        detector D0
        REPEAT 5 {
            error(0.1) D0
        }
        logical_observable L0
    ''')] == ['detector', 'repeat', 'logical_observable']
