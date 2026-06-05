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
import deltakit_stim
import pytest


def test_basics():
    p = deltakit_stim.Flow()
    assert p.input_copy() == deltakit_stim.PauliString(0)
    assert p.output_copy() == deltakit_stim.PauliString(0)
    assert p.measurements_copy() == []
    assert str(p) == "1 -> 1"
    assert repr(p) == 'deltakit_stim.Flow("1 -> 1")'

    p = deltakit_stim.Flow(
        input=deltakit_stim.PauliString("XX"),
        output=deltakit_stim.PauliString("-YYZ"),
        measurements=[-1, 2, 3],
    )
    assert p.input_copy() == deltakit_stim.PauliString("XX")
    assert p.output_copy() == deltakit_stim.PauliString("-YYZ")
    assert p.measurements_copy() == [-1, 2, 3]
    assert str(p) == "XX -> -YYZ xor rec[-1] xor rec[2] xor rec[3]"
    assert repr(p) == 'deltakit_stim.Flow("XX -> -YYZ xor rec[-1] xor rec[2] xor rec[3]")'

    p = deltakit_stim.Flow("-X1*Z2 -> Y3 xor rec[-1]")
    assert p.input_copy() == deltakit_stim.PauliString("-_XZ")
    assert p.output_copy() == deltakit_stim.PauliString("___Y")
    assert p.measurements_copy() == [-1]
    assert str(p) == "-_XZ -> ___Y xor rec[-1]"
    assert repr(p) == 'deltakit_stim.Flow("-_XZ -> ___Y xor rec[-1]")'

    p = deltakit_stim.Flow("X20 -> Y xor rec[-1]")
    assert p.input_copy() == deltakit_stim.PauliString("X20")
    assert p.output_copy() == deltakit_stim.PauliString("Y")
    assert p.measurements_copy() == [-1]
    assert str(p) == "X20 -> Y0 xor rec[-1]"
    assert repr(p) == 'deltakit_stim.Flow("X20 -> Y0 xor rec[-1]")'

    p = deltakit_stim.Flow("X20*I21 -> Y xor rec[-1]")
    assert p.input_copy() == deltakit_stim.PauliString("____________________X_")
    assert p.output_copy() == deltakit_stim.PauliString("Y")
    assert p.measurements_copy() == [-1]
    assert str(p) == "____________________X_ -> Y xor rec[-1]"
    assert repr(p) == 'deltakit_stim.Flow("____________________X_ -> Y xor rec[-1]")'

    p = deltakit_stim.Flow("iX -> iY")
    assert p.input_copy() == deltakit_stim.PauliString("X")
    assert p.output_copy() == deltakit_stim.PauliString("Y")
    assert p.measurements_copy() == []

    p = deltakit_stim.Flow(input=deltakit_stim.PauliString("iX"), output=deltakit_stim.PauliString("iY"))
    assert p.input_copy() == deltakit_stim.PauliString("X")
    assert p.output_copy() == deltakit_stim.PauliString("Y")
    assert p.measurements_copy() == []

    with pytest.raises(ValueError, match="Anti-Hermitian"):
        deltakit_stim.Flow("iX -> Y")
    with pytest.raises(ValueError, match="Anti-Hermitian"):
        deltakit_stim.Flow(input=deltakit_stim.PauliString("iX"), output=deltakit_stim.PauliString("Y"))


def test_equality():
    assert not (deltakit_stim.Flow() == None)
    assert not (deltakit_stim.Flow() == "other object")
    assert not (deltakit_stim.Flow() == object())
    assert deltakit_stim.Flow() != None
    assert deltakit_stim.Flow() != "other object"
    assert deltakit_stim.Flow() != object()

    assert deltakit_stim.Flow('X -> Y') == deltakit_stim.Flow('X -> Y')
    assert deltakit_stim.Flow('X -> X') != deltakit_stim.Flow('X -> Y')
    assert not (deltakit_stim.Flow('X -> Y') != deltakit_stim.Flow('X -> Y'))
    assert not (deltakit_stim.Flow('X -> Y') == deltakit_stim.Flow('X -> X'))

    assert deltakit_stim.Flow("X -> X xor rec[-1]") == deltakit_stim.Flow("X -> X xor rec[-1]")
    assert deltakit_stim.Flow("X -> X xor rec[-1]") != deltakit_stim.Flow("Y -> X xor rec[-1]")
    assert deltakit_stim.Flow("X -> X xor rec[-1]") != deltakit_stim.Flow("X -> Y xor rec[-1]")
    assert deltakit_stim.Flow("X -> X xor rec[-1]") != deltakit_stim.Flow("X -> X xor rec[-2]")


@pytest.mark.parametrize("value", [
    deltakit_stim.Flow(),
    deltakit_stim.Flow("X -> Y xor rec[-1]"),
    deltakit_stim.Flow("X -> 1"),
    deltakit_stim.Flow("-X -> Y"),
    deltakit_stim.Flow("X -> -Y"),
    deltakit_stim.Flow("-X -> -Y"),
    deltakit_stim.Flow("1 -> X"),
    deltakit_stim.Flow("X__________________ -> ________Y"),
])
def test_repr(value):
    assert eval(repr(value), {'deltakit_stim': deltakit_stim}) == value
    assert repr(eval(repr(value), {'deltakit_stim': deltakit_stim})) == repr(value)


def test_obs_flows():
    assert deltakit_stim.Circuit("""
        OBSERVABLE_INCLUDE(1) X2
    """).has_flow(deltakit_stim.Flow("X2 -> obs[1]"))
    assert not deltakit_stim.Circuit("""
        OBSERVABLE_INCLUDE(1) !X2
    """).has_flow(deltakit_stim.Flow("X2 -> obs[1]"))
    assert deltakit_stim.Circuit("""
        OBSERVABLE_INCLUDE(1) !X2
    """).has_flow(deltakit_stim.Flow("X2 -> obs[1]"), unsigned=True)
    assert deltakit_stim.Circuit("""
        OBSERVABLE_INCLUDE(1) !X2
    """).has_flow(deltakit_stim.Flow("-X2 -> obs[1]"))
    assert not deltakit_stim.Circuit("""
        OBSERVABLE_INCLUDE(1) X2
    """).has_flow(deltakit_stim.Flow("Y2 -> obs[1]"))
    assert not deltakit_stim.Circuit("""
        OBSERVABLE_INCLUDE(1) X2
    """).has_flow(deltakit_stim.Flow("Y2 -> obs[1]"), unsigned=True)


def test_obs_include_pauli_terms_sensitivity():
    _, obs = deltakit_stim.Circuit("""
        OBSERVABLE_INCLUDE(0) X0
        X_ERROR(0.5) 0
        OBSERVABLE_INCLUDE(0) X0
    """).compile_detector_sampler().sample(shots=1024, separate_observables=True)
    assert np.count_nonzero(obs) == 0

    _, obs = deltakit_stim.Circuit("""
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

    _, obs = deltakit_stim.Circuit("""
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

    _, obs = deltakit_stim.Circuit("""
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
    assert deltakit_stim.Flow(measurements=[4, 0, 4]) == deltakit_stim.Flow(measurements=[0])
    assert deltakit_stim.Flow(included_observables=[4, 0, 4]) == deltakit_stim.Flow(included_observables=[0])


def test_flow_multiplication():
    assert deltakit_stim.Flow("XYZ -> 1") * deltakit_stim.Flow("1 -> XYZ") == deltakit_stim.Flow("XYZ -> XYZ")
    assert deltakit_stim.Flow("XX_ -> 1") * deltakit_stim.Flow("_XX -> 1") == deltakit_stim.Flow("X_X -> 1")
    assert deltakit_stim.Flow("1 -> XX_") * deltakit_stim.Flow("1 -> _XX") == deltakit_stim.Flow("1 -> X_X")
    assert deltakit_stim.Flow("1 -> rec[-1] xor rec[-3]") * deltakit_stim.Flow("1 -> rec[-1] xor rec[-2]") == deltakit_stim.Flow("1 -> rec[-2] xor rec[-3]")
    assert deltakit_stim.Flow("1 -> obs[1] xor obs[3]") * deltakit_stim.Flow("1 -> obs[1] xor obs[2]") == deltakit_stim.Flow("1 -> obs[2] xor obs[3]")
    assert deltakit_stim.Flow("X -> X") * deltakit_stim.Flow("Z -> Z") == deltakit_stim.Flow("Y -> Y")
    assert deltakit_stim.Flow("1 -> XX") * deltakit_stim.Flow("1 -> ZZ") == deltakit_stim.Flow("1 -> -YY")
    assert deltakit_stim.Flow("1 -> obs[1]") * deltakit_stim.Flow("1 -> obs[1]") == deltakit_stim.Flow("1 -> 1")
    assert deltakit_stim.Flow("1 -> rec[1]") * deltakit_stim.Flow("1 -> rec[1]") == deltakit_stim.Flow("1 -> 1")
    with pytest.raises(ValueError, match="anticommute"):
        _ = deltakit_stim.Flow("1 -> X") * deltakit_stim.Flow("1 -> Y")
    with pytest.raises(ValueError, match="anticommute"):
        _ = deltakit_stim.Flow("1 -> Y") * deltakit_stim.Flow("1 -> X")
