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

import pytest

import deltakit_stim


def test_init_get():
    model = deltakit_stim.DetectorErrorModel("""
        error(0.125) D0 L0
        ERROR(0.25) D0 ^ D1
        repeat 100 {
            shift_detectors 1
            error(0.125) D0 D1
        }
        shift_detectors(1, 1.5, 2, 2.5) 1
        shift_detectors 5
    """)
    assert len(model) == 5
    assert model[0] == deltakit_stim.DemInstruction(
        "error",
        [0.125],
        [deltakit_stim.target_relative_detector_id(0), deltakit_stim.target_logical_observable_id(0)])
    assert model[1] == deltakit_stim.DemInstruction(
        "error",
        [0.25],
        [deltakit_stim.target_relative_detector_id(0), deltakit_stim.target_separator(), deltakit_stim.target_relative_detector_id(1)])
    assert model[2] == deltakit_stim.DemRepeatBlock(
        100,
        deltakit_stim.DetectorErrorModel("""
            shift_detectors 1
            error(0.125) D0 D1
        """))
    assert model[3] == deltakit_stim.DemInstruction(
        "shift_detectors",
        [1, 1.5, 2, 2.5],
        [1])
    assert model[4] == deltakit_stim.DemInstruction(
        "shift_detectors",
        [],
        [5])


def test_equality():
    assert deltakit_stim.DetectorErrorModel() == deltakit_stim.DetectorErrorModel()
    assert not (deltakit_stim.DetectorErrorModel() != deltakit_stim.DetectorErrorModel())
    assert not (deltakit_stim.DetectorErrorModel() == deltakit_stim.DetectorErrorModel("error(0.125) D0"))
    assert deltakit_stim.DetectorErrorModel() != deltakit_stim.DetectorErrorModel("error(0.125) D0")

    assert deltakit_stim.DetectorErrorModel("error(0.125) D0") == deltakit_stim.DetectorErrorModel("error(0.125) D0")
    assert deltakit_stim.DetectorErrorModel("error(0.125) D0") != deltakit_stim.DetectorErrorModel("error(0.126) D0")
    assert deltakit_stim.DetectorErrorModel("error(0.125) D0") != deltakit_stim.DetectorErrorModel("detector(0.125) D0")
    assert deltakit_stim.DetectorErrorModel("error(0.125) D0") != deltakit_stim.DetectorErrorModel("error(0.125) D1")
    assert deltakit_stim.DetectorErrorModel("error(0.125) D0") != deltakit_stim.DetectorErrorModel("error(0.125) L0")
    assert deltakit_stim.DetectorErrorModel("error(0.125) D0") != deltakit_stim.DetectorErrorModel("error(0.125) D0 D1")
    assert deltakit_stim.DetectorErrorModel("""
        REPEAT 3 {
            shift_detectors 4
        }
    """) == deltakit_stim.DetectorErrorModel("""
        REPEAT 3 {
            shift_detectors 4
        }
    """)
    assert deltakit_stim.DetectorErrorModel("""
        REPEAT 3 {
            shift_detectors 4
        }
    """) != deltakit_stim.DetectorErrorModel("""
        REPEAT 4 {
            shift_detectors 4
        }
    """)
    assert deltakit_stim.DetectorErrorModel("""
        REPEAT 3 {
            shift_detectors 4
        }
    """) != deltakit_stim.DetectorErrorModel("""
        REPEAT 3 {
            shift_detectors 5
        }
    """)


def test_repr():
    v = deltakit_stim.DetectorErrorModel()
    assert eval(repr(v), {"deltakit_stim": deltakit_stim}) == v
    v = deltakit_stim.DetectorErrorModel("error(0.125) D0 D1")
    assert eval(repr(v), {"deltakit_stim": deltakit_stim}) == v


def test_approx_equals():
    base = deltakit_stim.DetectorErrorModel("error(0.099) D0")
    assert not base.approx_equals(deltakit_stim.DetectorErrorModel("error(0.101) D0"), atol=0)
    assert not base.approx_equals(deltakit_stim.DetectorErrorModel("error(0.101) D0"), atol=0.00001)
    assert base.approx_equals(deltakit_stim.DetectorErrorModel("error(0.101) D0"), atol=0.01)
    assert base.approx_equals(deltakit_stim.DetectorErrorModel("error(0.101) D0"), atol=999)
    assert not base.approx_equals(deltakit_stim.DetectorErrorModel("error(0.101) D0 D1"), atol=999)

    assert not base.approx_equals(object(), atol=999)
    assert not base.approx_equals(deltakit_stim.PauliString("XYZ"), atol=999)


def test_append():
    m = deltakit_stim.DetectorErrorModel()
    m.append("error", 0.125, [
        deltakit_stim.DemTarget.relative_detector_id(1),
    ])
    m.append("error", 0.25, [
        deltakit_stim.DemTarget.relative_detector_id(1),
        deltakit_stim.DemTarget.separator(),
        deltakit_stim.DemTarget.relative_detector_id(2),
        deltakit_stim.DemTarget.logical_observable_id(3),
    ])
    m.append("shift_detectors", (1, 2, 3), [5])
    m += m * 3
    m.append(m[0])
    m.append(m[-2])
    assert m == deltakit_stim.DetectorErrorModel("""
        error(0.125) D1
        error(0.25) D1 ^ D2 L3
        shift_detectors(1, 2, 3) 5
        repeat 3 {
            error(0.125) D1
            error(0.25) D1 ^ D2 L3
            shift_detectors(1, 2, 3) 5
        }
        error(0.125) D1
        repeat 3 {
            error(0.125) D1
            error(0.25) D1 ^ D2 L3
            shift_detectors(1, 2, 3) 5
        }
    """)


def test_append_bad():
    m = deltakit_stim.DetectorErrorModel()
    m.append("error", 0.125, [deltakit_stim.target_relative_detector_id(0)])
    m.append("error", [0.125], [deltakit_stim.target_relative_detector_id(0)])
    m.append("shift_detectors", [], [5])
    m += m * 3

    with pytest.raises(ValueError, match=r"Bad target 'deltakit_stim.DemTarget\('D0'\)' for instruction 'shift_detectors'"):
        m.append("shift_detectors", [0.125, 0.25], [deltakit_stim.target_relative_detector_id(0)])
    with pytest.raises(ValueError, match="takes 1 argument"):
        m.append("error", [0.125, 0.25], [deltakit_stim.target_relative_detector_id(0)])

    with pytest.raises(ValueError, match="Bad target '0' for instruction 'error'"):
        m.append("error", [0.125], [0])

    with pytest.raises(ValueError, match="First argument"):
        m.append(None)
    with pytest.raises(ValueError, match="First argument"):
        m.append(object())
    with pytest.raises(ValueError, match="Must specify.*instruction name"):
        m.append("error")
    with pytest.raises(ValueError, match="Can't specify.*instruction is a"):
        m.append(m[0], 0.125, [])
    with pytest.raises(ValueError, match="Can't specify.*instruction is a"):
        m.append(m[-1], 0.125, [])


def test_pickle():
    import pickle

    t = deltakit_stim.DetectorErrorModel("""
        repeat 100 {
            error(0.25) D0 L1
            shift_detectors(1, 2) 3
        }
    """)
    a = pickle.dumps(t)
    assert pickle.loads(a) == t


def test_count_errors():
    assert deltakit_stim.DetectorErrorModel().num_errors == 0

    assert deltakit_stim.DetectorErrorModel("""
        logical_observable L100
        detector D100
        shift_detectors(100, 100, 100) 100
        error(0.125) D100
    """).num_errors == 1

    assert deltakit_stim.DetectorErrorModel("""
        error(0.125) D0
        REPEAT 100 {
            REPEAT 5 {
                error(0.25) D1
            }
        }
    """).num_errors == 501


def test_shortest_graphlike_error_trivial():
    with pytest.raises(ValueError, match="any graphlike logical errors"):
        _ = deltakit_stim.DetectorErrorModel().shortest_graphlike_error()
    with pytest.raises(ValueError, match="any graphlike logical errors"):
        _ = deltakit_stim.DetectorErrorModel("""
            error(0.1) D0
        """).shortest_graphlike_error()
    with pytest.raises(ValueError, match="any graphlike logical errors"):
        _ = deltakit_stim.DetectorErrorModel("""
            error(0.1) D0 L0
        """).shortest_graphlike_error()
    assert deltakit_stim.DetectorErrorModel("""
        error(0.1) L0
    """).shortest_graphlike_error() == deltakit_stim.DetectorErrorModel("""
        error(1) L0
    """)
    assert deltakit_stim.DetectorErrorModel("""
        error(0.1) D0 D1 L0
        error(0.1) D0 D1
    """).shortest_graphlike_error() == deltakit_stim.DetectorErrorModel("""
        error(1) D0 D1
        error(1) D0 D1 L0
    """)


def test_shortest_graphlike_error_line():
    assert deltakit_stim.DetectorErrorModel("""
        error(0.125) D0
        error(0.125) D0 D1
        error(0.125) D1 L55
        error(0.125) D1
    """).shortest_graphlike_error() == deltakit_stim.DetectorErrorModel("""
        error(1) D1
        error(1) D1 L55
    """)

    assert len(deltakit_stim.DetectorErrorModel("""
        error(0.1) D0 D1 L5
        REPEAT 1000 {
            error(0.1) D0 D2
            error(0.1) D1 D3
            shift_detectors 2
        }
        error(0.1) D0
        error(0.1) D1
    """).shortest_graphlike_error()) == 2003


def test_shortest_graphlike_error_ignore():
    assert deltakit_stim.DetectorErrorModel("""
        error(0.125) D0 D1 D2
        error(0.125) L0
    """).shortest_graphlike_error(ignore_ungraphlike_errors=True) == deltakit_stim.DetectorErrorModel("""
        error(1) L0
    """)


def test_shortest_graphlike_error_rep_code():
    circuit = deltakit_stim.Circuit.generated("repetition_code:memory",
                                     rounds=10,
                                     distance=7,
                                     before_round_data_depolarization=0.01)
    model = circuit.detector_error_model(decompose_errors=True)
    assert len(model.shortest_graphlike_error()) == 7


def test_shortest_graphlike_error_msgs():
    with pytest.raises(ValueError, match=r"NO OBSERVABLES(.|\n)*NO DETECTORS(.|\n)*NO ERRORS"):
        deltakit_stim.Circuit().detector_error_model(decompose_errors=True).shortest_graphlike_error()

    c = deltakit_stim.Circuit("""
        M 0
        OBSERVABLE_INCLUDE(0) rec[-1]
    """)
    with pytest.raises(ValueError, match=r"NO DETECTORS(.|\n)*NO ERRORS"):
        c.detector_error_model(decompose_errors=True).shortest_graphlike_error()

    c = deltakit_stim.Circuit("""
        X_ERROR(0.1) 0
        M 0
    """)
    with pytest.raises(ValueError, match=r"NO OBSERVABLES(.|\n)*NO DETECTORS(.|\n)*NO ERRORS"):
        c.detector_error_model(decompose_errors=True).shortest_graphlike_error()

    c = deltakit_stim.Circuit("""
        M 0
        DETECTOR rec[-1]
        OBSERVABLE_INCLUDE(0) rec[-1]
    """)
    with pytest.raises(ValueError, match=r"NO ERRORS"):
        c.detector_error_model(decompose_errors=True).shortest_graphlike_error()

    c = deltakit_stim.Circuit("""
        X_ERROR(0.1) 0
        M 0
        DETECTOR rec[-1]
    """)
    with pytest.raises(ValueError, match=r"NO OBSERVABLES"):
        c.detector_error_model(decompose_errors=True).shortest_graphlike_error()


def test_coords():
    circuit = deltakit_stim.Circuit("""
        M 0
        DETECTOR(1, 2, 3) rec[-1]
        REPEAT 3 {
            DETECTOR(2) rec[-1]
            SHIFT_COORDS(5)
        }
    """)
    dem = circuit.detector_error_model()

    assert dem.get_detector_coordinates() == {
        0: [1, 2, 3],
        1: [2],
        2: [7],
        3: [12],
    }
    assert circuit.get_detector_coordinates() == {
        0: [1, 2, 3],
        1: [2],
        2: [7],
        3: [12],
    }

    assert dem.get_detector_coordinates([1]) == {
        1: [2],
    }
    assert circuit.get_detector_coordinates([1]) == {
        1: [2],
    }
    assert dem.get_detector_coordinates(1) == {
        1: [2],
    }
    assert circuit.get_detector_coordinates(1) == {
        1: [2],
    }
    assert dem.get_detector_coordinates({1}) == {
        1: [2],
    }
    assert circuit.get_detector_coordinates({1}) == {
        1: [2],
    }
    assert dem.get_detector_coordinates(deltakit_stim.DemTarget.relative_detector_id(1)) == {
        1: [2],
    }
    assert circuit.get_detector_coordinates(deltakit_stim.DemTarget.relative_detector_id(1)) == {
        1: [2],
    }
    assert dem.get_detector_coordinates((deltakit_stim.DemTarget.relative_detector_id(1),)) == {
        1: [2],
    }
    assert circuit.get_detector_coordinates((deltakit_stim.DemTarget.relative_detector_id(1),)) == {
        1: [2],
    }

    assert dem.get_detector_coordinates(only=[2, 3]) == {
        2: [7],
        3: [12],
    }
    assert circuit.get_detector_coordinates(only=[2, 3]) == {
        2: [7],
        3: [12],
    }

    with pytest.raises(ValueError, match="Expected a detector id"):
        dem.get_detector_coordinates([-1])
    with pytest.raises(ValueError, match="too big"):
        dem.get_detector_coordinates([500])
    with pytest.raises(ValueError, match="Expected a detector id"):
        circuit.get_detector_coordinates([-1])
    with pytest.raises(ValueError, match="too big"):
        circuit.get_detector_coordinates([500])


def test_dem_from_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        path = tmpdir + '/tmp.deltakit_stim'
        with open(path, 'w') as f:
            print('error(0.125) D0 L5', file=f)
        assert deltakit_stim.DetectorErrorModel.from_file(path) == deltakit_stim.DetectorErrorModel('error(0.125) D0 L5')

    with tempfile.TemporaryDirectory() as tmpdir:
        path = pathlib.Path(tmpdir) / 'tmp.deltakit_stim'
        with open(path, 'w') as f:
            print('error(0.125) D0 L5', file=f)
        assert deltakit_stim.DetectorErrorModel.from_file(path) == deltakit_stim.DetectorErrorModel('error(0.125) D0 L5')

    with tempfile.TemporaryDirectory() as tmpdir:
        path = tmpdir + '/tmp.deltakit_stim'
        with open(path, 'w') as f:
            print('error(0.125) D0 L5', file=f)
        with open(path) as f:
            assert deltakit_stim.DetectorErrorModel.from_file(f) == deltakit_stim.DetectorErrorModel('error(0.125) D0 L5')

    with pytest.raises(ValueError, match="how to read"):
        deltakit_stim.DetectorErrorModel.from_file(object())
    with pytest.raises(ValueError, match="how to read"):
        deltakit_stim.DetectorErrorModel.from_file(123)


def test_dem_to_file():
    c = deltakit_stim.DetectorErrorModel('error(0.125) D0 L5\n')
    with tempfile.TemporaryDirectory() as tmpdir:
        path = tmpdir + '/tmp.deltakit_stim'
        c.to_file(path)
        with open(path) as f:
            assert f.read() == 'error(0.125) D0 L5\n'

    with tempfile.TemporaryDirectory() as tmpdir:
        path = pathlib.Path(tmpdir) / 'tmp.deltakit_stim'
        c.to_file(path)
        with open(path) as f:
            assert f.read() == 'error(0.125) D0 L5\n'

    with tempfile.TemporaryDirectory() as tmpdir:
        path = tmpdir + '/tmp.deltakit_stim'
        with open(path, 'w') as f:
            c.to_file(f)
        with open(path) as f:
            assert f.read() == 'error(0.125) D0 L5\n'

    with pytest.raises(ValueError, match="how to write"):
        c.to_file(object())
    with pytest.raises(ValueError, match="how to write"):
        c.to_file(123)


def test_flattened():
    dem = deltakit_stim.DetectorErrorModel("""
        shift_detectors 5
        repeat 2 {
            error(0.125) D0 D1
        }
    """)
    assert dem.flattened() == deltakit_stim.DetectorErrorModel("""
        error(0.125) D5 D6
        error(0.125) D5 D6
    """)


def test_rounded():
    dem = deltakit_stim.DetectorErrorModel("""
        error(0.1248) D0 D1
    """)
    assert dem.rounded(1) == deltakit_stim.DetectorErrorModel("""
        error(0.1) D0 D1
    """)
    assert dem.rounded(2) == deltakit_stim.DetectorErrorModel("""
        error(0.12) D0 D1
    """)
    assert dem.rounded(3) == deltakit_stim.DetectorErrorModel("""
        error(0.125) D0 D1
    """)
    assert dem.rounded(4) == deltakit_stim.DetectorErrorModel("""
        error(0.1248) D0 D1
    """)
    assert dem.rounded(5) == deltakit_stim.DetectorErrorModel("""
        error(0.1248) D0 D1
    """)

    dem = deltakit_stim.DetectorErrorModel("""
        error(0.01248) D0 D1
    """)
    assert dem.rounded(1) == deltakit_stim.DetectorErrorModel("""
        error(0) D0 D1
    """)
    assert dem.rounded(2) == deltakit_stim.DetectorErrorModel("""
        error(0.01) D0 D1
    """)
    assert dem.rounded(3) == deltakit_stim.DetectorErrorModel("""
        error(0.012) D0 D1
    """)
    assert dem.rounded(4) == deltakit_stim.DetectorErrorModel("""
        error(0.0125) D0 D1
    """)


def test_diagram():
    circuit = deltakit_stim.Circuit.generated("repetition_code:memory",
                                     rounds=10,
                                     distance=7,
                                     before_round_data_depolarization=0.01)
    dem = circuit.detector_error_model(decompose_errors=True)
    assert dem.diagram("matchgraph-svg") is not None
    assert dem.diagram("matchgraph-3d") is not None
    assert dem.diagram("matchgraph-3d-html") is not None
    assert dem.diagram("match-graph-svg") is not None
    assert dem.diagram(type="match-graph-svg") is not None
    assert dem.diagram(type="match-graph-3d") is not None
    assert dem.diagram(type="match-graph-3d-html") is not None
    assert "iframe" in str(dem.diagram(type="match-graph-svg-html"))


def test_shortest_graphlike_error_remnant():
    c = deltakit_stim.Circuit("""
        X_ERROR(0.125) 0 1 2 3 4 5 6 7 10
        E(0.125) X2 X3 X10
        M 0 1 2 3 4 5 6 7 10
        OBSERVABLE_INCLUDE(0) rec[-2]
        DETECTOR rec[-1]
        DETECTOR rec[-2] rec[-3]
        DETECTOR rec[-3] rec[-4]
        DETECTOR rec[-4] rec[-5]
        DETECTOR rec[-5] rec[-6]
        DETECTOR rec[-6] rec[-7]
        DETECTOR rec[-7] rec[-8]
        DETECTOR rec[-8] rec[-9]
    """)
    d = deltakit_stim.DetectorErrorModel("""
        error(0.125) D0
        error(0.125) D0 ^ D4 D6
        error(0.125) D1 D2
        error(0.125) D1 L0
        error(0.125) D2 D3
        error(0.125) D3 D4
        error(0.125) D4 D5
        error(0.125) D5 D6
        error(0.125) D6 D7
        error(0.125) D7
    """)
    assert c.detector_error_model(decompose_errors=True) == d
    assert len(c.shortest_graphlike_error(ignore_ungraphlike_errors=False)) == 7
    assert len(d.shortest_graphlike_error(ignore_ungraphlike_errors=False)) == 7
    assert len(c.shortest_graphlike_error(ignore_ungraphlike_errors=True)) == 8
    assert len(d.shortest_graphlike_error(ignore_ungraphlike_errors=True)) == 8
    assert len(c.shortest_graphlike_error()) == 8
    assert len(d.shortest_graphlike_error()) == 8


def test_init_parse():
    assert deltakit_stim.DemInstruction("error(0.125) D0 D1") == deltakit_stim.DemInstruction("error", [0.125], [deltakit_stim.DemTarget("D0"), deltakit_stim.DemTarget("D1")])


def test_without_tags():
    dem = deltakit_stim.DetectorErrorModel("""
        error[tag](0.25) D5
    """)
    assert dem.without_tags() == deltakit_stim.DetectorErrorModel("""
        error(0.25) D5
    """)


def test_append_dem_to_dem():
    dem = deltakit_stim.DetectorErrorModel("""
        error(0.25) D0
    """)
    dem.append(deltakit_stim.DetectorErrorModel("""
        error(0.125) D1
        error(0.25) D2
    """))
    assert dem == deltakit_stim.DetectorErrorModel("""
        error(0.25) D0
        error(0.125) D1
        error(0.25) D2
    """)