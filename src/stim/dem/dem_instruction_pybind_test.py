import deltakit_stim
import pytest


def test_args_copy():
    assert deltakit_stim.DemInstruction("error", [0.25], [deltakit_stim.target_relative_detector_id(3)]).args_copy() == [0.25]
    assert deltakit_stim.DemInstruction("error", [0.125], [deltakit_stim.target_relative_detector_id(3)]).args_copy() == [0.125]
    assert deltakit_stim.DemInstruction("shift_detectors", [], [1]).args_copy() == []
    assert deltakit_stim.DemInstruction("shift_detectors", [0.125, 0.25], [1]).args_copy() == [0.125, 0.25]


def test_targets_copy():
    t1 = [deltakit_stim.target_relative_detector_id(3), deltakit_stim.target_separator(), deltakit_stim.target_logical_observable_id(2)]
    assert deltakit_stim.DemInstruction("error", [0.25], t1).targets_copy() == t1
    assert deltakit_stim.DemInstruction("shift_detectors", [], [1]).targets_copy() == [1]
    t2 = [deltakit_stim.target_logical_observable_id(3)]
    assert deltakit_stim.DemInstruction("logical_observable", [], t2).targets_copy() == t2


def test_type():
    assert deltakit_stim.DemInstruction("error", [0.25], [deltakit_stim.target_relative_detector_id(3)]).type == "error"
    assert deltakit_stim.DemInstruction("ERROR", [0.25], [deltakit_stim.target_relative_detector_id(3)]).type == "error"
    assert deltakit_stim.DemInstruction("shift_detectors", [], [1]).type == "shift_detectors"
    assert deltakit_stim.DemInstruction("detector", [], [deltakit_stim.target_relative_detector_id(3)]).type == "detector"
    assert deltakit_stim.DemInstruction("logical_observable", [], [deltakit_stim.target_logical_observable_id(3)]).type == "logical_observable"


def test_equality():
    e1 = deltakit_stim.DemInstruction("error", [0.25], [deltakit_stim.target_relative_detector_id(3)])
    assert e1 == deltakit_stim.DemInstruction("error", [0.25], [deltakit_stim.target_relative_detector_id(3)])
    assert not (e1 != deltakit_stim.DemInstruction("error", [0.25], [deltakit_stim.target_relative_detector_id(3)]))
    assert e1 != deltakit_stim.DemInstruction("error", [0.35], [deltakit_stim.target_relative_detector_id(3)])
    assert not (e1 == deltakit_stim.DemInstruction("error", [0.35], [deltakit_stim.target_relative_detector_id(3)]))
    assert e1 != deltakit_stim.DemInstruction("error", [0.35], [deltakit_stim.target_relative_detector_id(4)])
    assert e1 != deltakit_stim.DemInstruction("shift_detectors", [0.35], [3])


def test_validation():
    with pytest.raises(ValueError, match="takes 1 arg"):
        deltakit_stim.DemInstruction("error", [], [deltakit_stim.target_relative_detector_id(3)])
    with pytest.raises(ValueError, match="takes 1 arg"):
        deltakit_stim.DemInstruction("error", [0.5, 0.5], [deltakit_stim.target_relative_detector_id(3)])
    with pytest.raises(ValueError, match="last target.+separator"):
        deltakit_stim.DemInstruction("error", [0.25], [deltakit_stim.target_separator()])
    with pytest.raises(ValueError, match="0 to 1"):
        deltakit_stim.DemInstruction("error", [-0.1], [deltakit_stim.target_relative_detector_id(3)])
    with pytest.raises(ValueError, match="0 to 1"):
        deltakit_stim.DemInstruction("error", [1.1], [deltakit_stim.target_relative_detector_id(3)])
    with pytest.raises(ValueError, match="detector.+targets"):
        deltakit_stim.DemInstruction("error", [0.25], [3])

    with pytest.raises(ValueError, match="integer targets"):
        deltakit_stim.DemInstruction("shift_detectors", [1.1], [deltakit_stim.target_relative_detector_id(3)])


def test_str():
    v = deltakit_stim.DemInstruction("ERROR", [0.125], [deltakit_stim.target_relative_detector_id(3), deltakit_stim.target_logical_observable_id(6)])
    assert str(v) == "error(0.125) D3 L6"
    v = deltakit_stim.DemInstruction("Shift_detectors", [1.5, 2.5, 5.5], [6])
    assert str(v) == "shift_detectors(1.5, 2.5, 5.5) 6"


def test_repr():
    v = deltakit_stim.DemInstruction("error", [0.25], [deltakit_stim.target_relative_detector_id(3), deltakit_stim.target_logical_observable_id(6)])
    assert eval(repr(v), {"stim": deltakit_stim}) == v
    v = deltakit_stim.DemInstruction("shift_detectors", [1.5, 2.5, 5.5], [6])
    assert eval(repr(v), {"stim": deltakit_stim}) == v


def test_hashable():
    a = deltakit_stim.DemInstruction("error", [0.25], [deltakit_stim.target_relative_detector_id(3)])
    b = deltakit_stim.DemInstruction("error", [0.125], [deltakit_stim.target_relative_detector_id(3)])
    c = deltakit_stim.DemInstruction("error", [0.25], [deltakit_stim.target_relative_detector_id(3)])
    assert hash(a) == hash(c)
    assert len({a, b, c}) == 2


def test_target_groups():
    dem = deltakit_stim.DetectorErrorModel("detector D0")
    assert dem[0].target_groups() == [[deltakit_stim.DemTarget("D0")]]


def test_init_from_str():
    assert deltakit_stim.DemInstruction("detector D0") == deltakit_stim.DemInstruction("detector", [], [deltakit_stim.target_relative_detector_id(0)])

    with pytest.raises(ValueError, match="single DemInstruction"):
        deltakit_stim.DemInstruction("")

    with pytest.raises(ValueError, match="single DemInstruction"):
        deltakit_stim.DemInstruction("""
            repeat 5 {
                error(0.25) D0
                shift_detectors 1
            }
        """)

    with pytest.raises(ValueError, match="single DemInstruction"):
        deltakit_stim.DemInstruction("""
            detector D0
            detector D1
        """)


def test_tag():
    assert deltakit_stim.DemInstruction("error[test](0.25) D1").tag == 'test'
    assert deltakit_stim.DemInstruction("error", [0.25], [deltakit_stim.DemTarget("D1")], tag="test").tag == 'test'
    dem = deltakit_stim.DetectorErrorModel('''
        error[test-tag](0.125) D0
        error(0.125) D0
    ''')
    assert dem[0].tag == 'test-tag'
    assert dem[1].tag == ''
