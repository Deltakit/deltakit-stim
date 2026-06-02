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
import lestim
import pytest


def test_basics():
    p = lestim.Flow()
    assert p.input_copy() == lestim.PauliString(0)
    assert p.output_copy() == lestim.PauliString(0)
    assert p.measurements_copy() == []
    assert str(p) == "1 -> 1"
    assert repr(p) == 'stim.Flow("1 -> 1")'

    p = lestim.Flow(
        input=lestim.PauliString("XX"),
        output=lestim.PauliString("-YYZ"),
        measurements=[-1, 2, 3],
    )
    assert p.input_copy() == lestim.PauliString("XX")
    assert p.output_copy() == lestim.PauliString("-YYZ")
    assert p.measurements_copy() == [-1, 2, 3]
    assert str(p) == "XX -> -YYZ xor rec[-1] xor rec[2] xor rec[3]"
    assert repr(p) == 'stim.Flow("XX -> -YYZ xor rec[-1] xor rec[2] xor rec[3]")'

    p = lestim.Flow("-X1*Z2 -> Y3 xor rec[-1]")
    assert p.input_copy() == lestim.PauliString("-_XZ")
    assert p.output_copy() == lestim.PauliString("___Y")
    assert p.measurements_copy() == [-1]
    assert str(p) == "-_XZ -> ___Y xor rec[-1]"
    assert repr(p) == 'stim.Flow("-_XZ -> ___Y xor rec[-1]")'

    p = lestim.Flow("X20 -> Y xor rec[-1]")
    assert p.input_copy() == lestim.PauliString("X20")
    assert p.output_copy() == lestim.PauliString("Y")
    assert p.measurements_copy() == [-1]
    assert str(p) == "X20 -> Y0 xor rec[-1]"
    assert repr(p) == 'stim.Flow("X20 -> Y0 xor rec[-1]")'

    p = lestim.Flow("X20*I21 -> Y xor rec[-1]")
    assert p.input_copy() == lestim.PauliString("____________________X_")
    assert p.output_copy() == lestim.PauliString("Y")
    assert p.measurements_copy() == [-1]
    assert str(p) == "____________________X_ -> Y xor rec[-1]"
    assert repr(p) == 'stim.Flow("____________________X_ -> Y xor rec[-1]")'

    p = lestim.Flow("iX -> iY")
    assert p.input_copy() == lestim.PauliString("X")
    assert p.output_copy() == lestim.PauliString("Y")
    assert p.measurements_copy() == []

    p = lestim.Flow(input=lestim.PauliString("iX"), output=lestim.PauliString("iY"))
    assert p.input_copy() == lestim.PauliString("X")
    assert p.output_copy() == lestim.PauliString("Y")
    assert p.measurements_copy() == []

    with pytest.raises(ValueError, match="Anti-Hermitian"):
        lestim.Flow("iX -> Y")
    with pytest.raises(ValueError, match="Anti-Hermitian"):
        lestim.Flow(input=lestim.PauliString("iX"), output=lestim.PauliString("Y"))


def test_equality():
    assert not (lestim.Flow() == None)
    assert not (lestim.Flow() == "other object")
    assert not (lestim.Flow() == object())
    assert lestim.Flow() != None
    assert lestim.Flow() != "other object"
    assert lestim.Flow() != object()

    assert lestim.Flow('X -> Y') == lestim.Flow('X -> Y')
    assert lestim.Flow('X -> X') != lestim.Flow('X -> Y')
    assert not (lestim.Flow('X -> Y') != lestim.Flow('X -> Y'))
    assert not (lestim.Flow('X -> Y') == lestim.Flow('X -> X'))

    assert lestim.Flow("X -> X xor rec[-1]") == lestim.Flow("X -> X xor rec[-1]")
    assert lestim.Flow("X -> X xor rec[-1]") != lestim.Flow("Y -> X xor rec[-1]")
    assert lestim.Flow("X -> X xor rec[-1]") != lestim.Flow("X -> Y xor rec[-1]")
    assert lestim.Flow("X -> X xor rec[-1]") != lestim.Flow("X -> X xor rec[-2]")


@pytest.mark.parametrize("value", [
    lestim.Flow(),
    lestim.Flow("X -> Y xor rec[-1]"),
    lestim.Flow("X -> 1"),
    lestim.Flow("-X -> Y"),
    lestim.Flow("X -> -Y"),
    lestim.Flow("-X -> -Y"),
    lestim.Flow("1 -> X"),
    lestim.Flow("X__________________ -> ________Y"),
])
def test_repr(value):
    assert eval(repr(value), {'stim': lestim}) == value
    assert repr(eval(repr(value), {'stim': lestim})) == repr(value)


def test_obs_flows():
    assert lestim.Circuit("""
        OBSERVABLE_INCLUDE(1) X2
    """).has_flow(lestim.Flow("X2 -> obs[1]"))
    assert not lestim.Circuit("""
        OBSERVABLE_INCLUDE(1) !X2
    """).has_flow(lestim.Flow("X2 -> obs[1]"))
    assert lestim.Circuit("""
        OBSERVABLE_INCLUDE(1) !X2
    """).has_flow(lestim.Flow("X2 -> obs[1]"), unsigned=True)
    assert lestim.Circuit("""
        OBSERVABLE_INCLUDE(1) !X2
    """).has_flow(lestim.Flow("-X2 -> obs[1]"))
    assert not lestim.Circuit("""
        OBSERVABLE_INCLUDE(1) X2
    """).has_flow(lestim.Flow("Y2 -> obs[1]"))
    assert not lestim.Circuit("""
        OBSERVABLE_INCLUDE(1) X2
    """).has_flow(lestim.Flow("Y2 -> obs[1]"), unsigned=True)


def test_obs_include_pauli_terms_sensitivity():
    _, obs = lestim.Circuit("""
        OBSERVABLE_INCLUDE(0) X0
        X_ERROR(0.5) 0
        OBSERVABLE_INCLUDE(0) X0
    """).compile_detector_sampler().sample(shots=1024, separate_observables=True)
    assert np.count_nonzero(obs) == 0

    _, obs = lestim.Circuit("""
        OBSERVABLE_INCLUDE(0) X0
        OBSERVABLE_INCLUDE(1) Y0
        OBSERVABLE_INCLUDE(2) Z0
        X_ERROR(0.5) 0
        OBSERVABLE_INCLUDE(0) X0
        OBSERVABLE_INCLUDE(1) Y0
        OBSERVABLE_INCLUDE(2) Z0
    """).compile_detector_sampler().sample(shots=1024, separate_observables=True)
    xs, ys, zs = np.count_nonzero(obs, axis=0)
    assert xs == 0
    assert 256 <= ys <= 768
    assert zs == ys

    _, obs = lestim.Circuit("""
        OBSERVABLE_INCLUDE(0) X0
        OBSERVABLE_INCLUDE(1) Y0
        OBSERVABLE_INCLUDE(2) Z0
        Y_ERROR(0.5) 0
        OBSERVABLE_INCLUDE(0) X0
        OBSERVABLE_INCLUDE(1) Y0
        OBSERVABLE_INCLUDE(2) Z0
    """).compile_detector_sampler().sample(shots=1024, separate_observables=True)
    xs, ys, zs = np.count_nonzero(obs, axis=0)
    assert ys == 0
    assert 256 <= xs <= 768
    assert zs == xs

    _, obs = lestim.Circuit("""
        OBSERVABLE_INCLUDE(0) X0
        OBSERVABLE_INCLUDE(1) Y0
        OBSERVABLE_INCLUDE(2) Z0
        Z_ERROR(0.5) 0
        OBSERVABLE_INCLUDE(0) X0
        OBSERVABLE_INCLUDE(1) Y0
        OBSERVABLE_INCLUDE(2) Z0
    """).compile_detector_sampler().sample(shots=1024, separate_observables=True)
    xs, ys, zs = np.count_nonzero(obs, axis=0)
    assert zs == 0
    assert 256 <= ys <= 768
    assert xs == ys


def test_flow_canonicalization():
    assert lestim.Flow(measurements=[4, 0, 4]) == lestim.Flow(measurements=[0])
    assert lestim.Flow(included_observables=[4, 0, 4]) == lestim.Flow(included_observables=[0])


def test_flow_multiplication():
    assert lestim.Flow("XYZ -> 1") * lestim.Flow("1 -> XYZ") == lestim.Flow("XYZ -> XYZ")
    assert lestim.Flow("XX_ -> 1") * lestim.Flow("_XX -> 1") == lestim.Flow("X_X -> 1")
    assert lestim.Flow("1 -> XX_") * lestim.Flow("1 -> _XX") == lestim.Flow("1 -> X_X")
    assert lestim.Flow("1 -> rec[-1] xor rec[-3]") * lestim.Flow("1 -> rec[-1] xor rec[-2]") == lestim.Flow("1 -> rec[-2] xor rec[-3]")
    assert lestim.Flow("1 -> obs[1] xor obs[3]") * lestim.Flow("1 -> obs[1] xor obs[2]") == lestim.Flow("1 -> obs[2] xor obs[3]")
    assert lestim.Flow("X -> X") * lestim.Flow("Z -> Z") == lestim.Flow("Y -> Y")
    assert lestim.Flow("1 -> XX") * lestim.Flow("1 -> ZZ") == lestim.Flow("1 -> -YY")
    assert lestim.Flow("1 -> obs[1]") * lestim.Flow("1 -> obs[1]") == lestim.Flow("1 -> 1")
    assert lestim.Flow("1 -> rec[1]") * lestim.Flow("1 -> rec[1]") == lestim.Flow("1 -> 1")
    with pytest.raises(ValueError, match="anticommute"):
        _ = lestim.Flow("1 -> X") * lestim.Flow("1 -> Y")
    with pytest.raises(ValueError, match="anticommute"):
        _ = lestim.Flow("1 -> Y") * lestim.Flow("1 -> X")
