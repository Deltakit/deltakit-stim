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
import pathlib

import tempfile

import doctest

import numpy as np
import pytest
import types

import deltakit_stim
import re

def test_version():
    assert re.match(r"^\d\.\d+", deltakit_stim.__version__)


def test_targets():
    t = deltakit_stim.target_x(5)
    assert isinstance(t, deltakit_stim.GateTarget)
    assert t.is_x_target and t.value == 5
    assert not t.is_y_target

    t = deltakit_stim.target_y(6)
    assert isinstance(t, deltakit_stim.GateTarget)
    assert t.is_y_target and t.value == 6

    t = deltakit_stim.target_z(5)
    assert isinstance(t, deltakit_stim.GateTarget)
    assert t.is_z_target and t.value == 5

    t = deltakit_stim.target_inv(5)
    assert isinstance(t, deltakit_stim.GateTarget)
    assert t.is_inverted_result_target and t.value == 5

    t = deltakit_stim.target_rec(-5)
    assert isinstance(t, deltakit_stim.GateTarget)
    assert t.is_measurement_record_target and not t.is_inverted_result_target and t.value == -5

    t = deltakit_stim.target_sweep_bit(4)
    assert isinstance(t, deltakit_stim.GateTarget)
    assert t.is_sweep_bit_target and not t.is_inverted_result_target and t.value == 4

    t = deltakit_stim.target_combiner()
    assert isinstance(t, deltakit_stim.GateTarget)


def test_gate_data():
    data = deltakit_stim.gate_data()
    assert len(data) == 85
    assert data["CX"].name == "CX"
    assert data["CX"].aliases == ["CNOT", "CX", "ZCX"]
    assert data["X"].is_unitary
    assert "CNOT" not in data


def test_format_data():
    format_data = deltakit_stim._UNSTABLE_raw_format_data()
    assert len(format_data) >= 6

    # Check that example code has needed imports.
    for k, v in format_data.items():
        exec(v["parse_example"], {}, {})
        exec(v["save_example"], {}, {})

    # Collect sample methods.
    ctx = {}
    for k, v in format_data.items():
        exec(v["parse_example"], {}, ctx)
        exec(v["save_example"], {}, ctx)

    # Manually test example save/parse methods.
    data = [[0, 1, 1, 0], [0, 0, 0, 0]]
    saved = "0110\n0000\n"
    assert ctx["save_01"](data) == saved
    assert ctx["parse_01"](saved) == data

    saved = b"\x01\x00\x01\x04"
    assert ctx["save_r8"](data) == saved
    assert ctx["parse_r8"](saved, bits_per_shot=4) == data

    saved = b"\x06\x00"
    assert ctx["save_b8"](data) == saved
    assert ctx["parse_b8"](saved, bits_per_shot=4) == data

    saved = "1,2\n\n"
    assert ctx["save_hits"](data) == saved
    assert ctx["parse_hits"](saved, bits_per_shot=4) == data

    saved = "shot D1 L0\nshot\n"
    assert ctx["save_dets"](data, num_detectors=2, num_observables=2) == saved
    assert ctx["parse_dets"](saved, num_detectors=2, num_observables=2) == data

    big_data = [data[0]] + [data[1]] * 36 + [[1, 0, 1, 0]] * 4 + [data[1]] * (64 - 41)
    saved = (b"\x00\x00\x00\x00\xe0\x01\x00\x00"
             b"\x01\x00\x00\x00\x00\x00\x00\x00"
             b"\x01\x00\x00\x00\xe0\x01\x00\x00"
             b"\x00\x00\x00\x00\x00\x00\x00\x00")
    assert ctx["save_ptb64"](big_data) == saved
    assert ctx["parse_ptb64"](saved, bits_per_shot=4) == big_data

    # Check that python examples in help strings are correct.
    for k, v in format_data.items():
        mod = types.ModuleType('deltakit_stim_test_fake')
        mod.f = lambda: 5
        mod.__test__ = {"f": mod.f}
        mod.f.__doc__ = v["help"]
        assert doctest.testmod(mod).failed == 0, k


def test_main_write_to_file():
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / 'tmp'
        assert deltakit_stim.main(command_line_args=[
            "gen",
            "--code=repetition_code",
            "--task=memory",
            "--rounds=1000",
            "--distance=2",
            f"--out={p}"
        ]) == 0
        with open(p) as f:
            assert "Generated repetition_code" in f.read()


def test_main_help(capsys):
    assert deltakit_stim.main(command_line_args=["help"]) == 0
    captured = capsys.readouterr()
    assert captured.err == ""
    assert 'Available deltakit_stim commands' in captured.out


def test_main_redirects_stdout(capsys):
    assert deltakit_stim.main(command_line_args=[
        "gen",
        "--code=repetition_code",
        "--task=memory",
        "--rounds=1000",
        "--distance=2",
    ]) == 0
    captured = capsys.readouterr()
    assert "Generated repetition_code" in captured.out
    assert captured.err == ""


def test_main_redirects_stderr(capsys):
    assert deltakit_stim.main(command_line_args=[
        "gen",
        "--code=XXXXX",
        "--task=memory",
        "--rounds=1000",
        "--distance=2",
    ]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "Unrecognized value 'XXXXX'" in captured.err


def test_target_methods_accept_gate_targets():
    assert deltakit_stim.target_inv(deltakit_stim.GateTarget(5)) == deltakit_stim.target_inv(5)
    assert deltakit_stim.target_inv(deltakit_stim.target_inv(5)) == deltakit_stim.GateTarget(5)
    assert deltakit_stim.target_inv(deltakit_stim.target_x(5)) == deltakit_stim.target_x(5, invert=True)
    assert deltakit_stim.target_inv(deltakit_stim.target_y(5)) == deltakit_stim.target_y(5, invert=True)
    assert deltakit_stim.target_inv(deltakit_stim.target_z(5)) == deltakit_stim.target_z(5, invert=True)

    assert deltakit_stim.target_x(deltakit_stim.GateTarget(5)) == deltakit_stim.target_x(5)
    assert deltakit_stim.target_x(deltakit_stim.target_inv(deltakit_stim.GateTarget(5))) == deltakit_stim.target_x(5, invert=True)
    assert deltakit_stim.target_x(deltakit_stim.GateTarget(5), invert=True) == deltakit_stim.target_x(5, invert=True)
    assert deltakit_stim.target_x(deltakit_stim.target_inv(deltakit_stim.GateTarget(5)), invert=True) == deltakit_stim.target_x(5)

    assert deltakit_stim.target_y(deltakit_stim.GateTarget(5)) == deltakit_stim.target_y(5)
    assert deltakit_stim.target_y(deltakit_stim.target_inv(deltakit_stim.GateTarget(5))) == deltakit_stim.target_y(5, invert=True)
    assert deltakit_stim.target_y(deltakit_stim.GateTarget(5), invert=True) == deltakit_stim.target_y(5, invert=True)
    assert deltakit_stim.target_y(deltakit_stim.target_inv(deltakit_stim.GateTarget(5)), invert=True) == deltakit_stim.target_y(5)

    assert deltakit_stim.target_z(deltakit_stim.GateTarget(5)) == deltakit_stim.target_z(5)
    assert deltakit_stim.target_z(deltakit_stim.target_inv(deltakit_stim.GateTarget(5))) == deltakit_stim.target_z(5, invert=True)
    assert deltakit_stim.target_z(deltakit_stim.GateTarget(5), invert=True) == deltakit_stim.target_z(5, invert=True)
    assert deltakit_stim.target_z(deltakit_stim.target_inv(deltakit_stim.GateTarget(5)), invert=True) == deltakit_stim.target_z(5)

    with pytest.raises(ValueError):
        deltakit_stim.target_inv(deltakit_stim.target_sweep_bit(4))

    with pytest.raises(ValueError):
        deltakit_stim.target_inv(deltakit_stim.target_rec(-4))

    with pytest.raises(ValueError):
        deltakit_stim.target_x(deltakit_stim.target_sweep_bit(4))

    with pytest.raises(ValueError):
        deltakit_stim.target_y(deltakit_stim.target_sweep_bit(4))

    with pytest.raises(ValueError):
        deltakit_stim.target_z(deltakit_stim.target_sweep_bit(4))


def test_target_pauli():
    assert deltakit_stim.target_pauli(2, "I") == deltakit_stim.GateTarget(2)
    assert deltakit_stim.target_pauli(2, "X") == deltakit_stim.target_x(2)
    assert deltakit_stim.target_pauli(2, "Y") == deltakit_stim.target_y(2)
    assert deltakit_stim.target_pauli(2, "Z") == deltakit_stim.target_z(2)
    assert deltakit_stim.target_pauli(5, "x") == deltakit_stim.target_x(5)
    assert deltakit_stim.target_pauli(2, "y") == deltakit_stim.target_y(2)
    assert deltakit_stim.target_pauli(2, "z") == deltakit_stim.target_z(2)
    assert deltakit_stim.target_pauli(2, 0) == deltakit_stim.GateTarget(2)
    assert deltakit_stim.target_pauli(2, 1) == deltakit_stim.target_x(2)
    assert deltakit_stim.target_pauli(2, 2) == deltakit_stim.target_y(2)
    assert deltakit_stim.target_pauli(2, 3) == deltakit_stim.target_z(2)
    assert deltakit_stim.target_pauli(2, 3, True) == deltakit_stim.target_z(2, True)
    assert deltakit_stim.target_pauli(qubit_index=2, pauli=3, invert=True) == deltakit_stim.target_z(2, True)
    assert deltakit_stim.target_pauli(5, np.array([2], dtype=np.uint8)[0]) == deltakit_stim.target_y(5)
    assert deltakit_stim.target_pauli(5, np.array([2], dtype=np.uint32)[0]) == deltakit_stim.target_y(5)
    assert deltakit_stim.target_pauli(5, np.array([2], dtype=np.int16)[0]) == deltakit_stim.target_y(5)

    with pytest.raises(ValueError, match="too large"):
        deltakit_stim.target_pauli(2**31, 'X')
    with pytest.raises(ValueError, match="Expected pauli"):
        deltakit_stim.target_pauli(5, 'F')
    with pytest.raises(ValueError, match="Expected pauli"):
        deltakit_stim.target_pauli(5, np.array([257], dtype=np.uint32)[0])


def test_target_combined_paulis():
    assert deltakit_stim.target_combined_paulis(deltakit_stim.PauliString("XYZ")) == [
        deltakit_stim.target_x(0),
        deltakit_stim.target_combiner(),
        deltakit_stim.target_y(1),
        deltakit_stim.target_combiner(),
        deltakit_stim.target_z(2),
    ]

    assert deltakit_stim.target_combined_paulis(deltakit_stim.PauliString("X"), True) == [
        deltakit_stim.target_x(0, True),
    ]

    assert deltakit_stim.target_combined_paulis(deltakit_stim.PauliString("-XYIZ")) == [
        deltakit_stim.target_x(0, invert=True),
        deltakit_stim.target_combiner(),
        deltakit_stim.target_y(1),
        deltakit_stim.target_combiner(),
        deltakit_stim.target_z(3),
    ]

    assert deltakit_stim.target_combined_paulis(deltakit_stim.PauliString("-XYIZ"), True) == [
        deltakit_stim.target_x(0),
        deltakit_stim.target_combiner(),
        deltakit_stim.target_y(1),
        deltakit_stim.target_combiner(),
        deltakit_stim.target_z(3),
    ]

    assert deltakit_stim.target_combined_paulis([deltakit_stim.target_x(5), deltakit_stim.target_z(9)]) == [
        deltakit_stim.target_x(5),
        deltakit_stim.target_combiner(),
        deltakit_stim.target_z(9),
    ]

    assert deltakit_stim.target_combined_paulis([deltakit_stim.target_x(5, True), deltakit_stim.target_z(9)]) == [
        deltakit_stim.target_x(5, True),
        deltakit_stim.target_combiner(),
        deltakit_stim.target_z(9),
    ]
    assert deltakit_stim.target_combined_paulis([deltakit_stim.target_x(5), deltakit_stim.target_z(9, True)]) == [
        deltakit_stim.target_x(5, True),
        deltakit_stim.target_combiner(),
        deltakit_stim.target_z(9),
    ]
    assert deltakit_stim.target_combined_paulis([deltakit_stim.target_x(5), deltakit_stim.target_z(9)], True) == [
        deltakit_stim.target_x(5, True),
        deltakit_stim.target_combiner(),
        deltakit_stim.target_z(9),
    ]
    assert deltakit_stim.target_combined_paulis([deltakit_stim.target_y(4)]) == [
        deltakit_stim.target_y(4),
    ]

    with pytest.raises(ValueError, match="Expected a pauli string"):
        deltakit_stim.target_combined_paulis([deltakit_stim.target_rec(-2)])
    with pytest.raises(ValueError, match="Expected a pauli string"):
        deltakit_stim.target_combined_paulis([object()])
    with pytest.raises(ValueError, match="Identity pauli product"):
        deltakit_stim.target_combined_paulis([])
    with pytest.raises(ValueError, match="Identity pauli product"):
        deltakit_stim.target_combined_paulis(deltakit_stim.PauliString(0))
    with pytest.raises(ValueError, match="Identity pauli product"):
        deltakit_stim.target_combined_paulis(deltakit_stim.PauliString(10))
    with pytest.raises(ValueError, match="Imaginary"):
        deltakit_stim.target_combined_paulis(deltakit_stim.PauliString("iX"))
