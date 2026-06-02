import lestim
import pytest


def test_args_copy():
    assert lestim.DemInstruction("error", [0.25], [lestim.target_relative_detector_id(3)]).args_copy() == [0.25]
    assert lestim.DemInstruction("error", [0.125], [lestim.target_relative_detector_id(3)]).args_copy() == [0.125]
    assert lestim.DemInstruction("shift_detectors", [], [1]).args_copy() == []
    assert lestim.DemInstruction("shift_detectors", [0.125, 0.25], [1]).args_copy() == [0.125, 0.25]


def test_targets_copy():
    t1 = [lestim.target_relative_detector_id(3), lestim.target_separator(), lestim.target_logical_observable_id(2)]
    assert lestim.DemInstruction("error", [0.25], t1).targets_copy() == t1
    assert lestim.DemInstruction("shift_detectors", [], [1]).targets_copy() == [1]
    t2 = [lestim.target_logical_observable_id(3)]
    assert lestim.DemInstruction("logical_observable", [], t2).targets_copy() == t2


def test_type():
    assert lestim.DemInstruction("error", [0.25], [lestim.target_relative_detector_id(3)]).type == "error"
    assert lestim.DemInstruction("ERROR", [0.25], [lestim.target_relative_detector_id(3)]).type == "error"
    assert lestim.DemInstruction("shift_detectors", [], [1]).type == "shift_detectors"
    assert lestim.DemInstruction("detector", [], [lestim.target_relative_detector_id(3)]).type == "detector"
    assert lestim.DemInstruction("logical_observable", [], [lestim.target_logical_observable_id(3)]).type == "logical_observable"


def test_equality():
    e1 = lestim.DemInstruction("error", [0.25], [lestim.target_relative_detector_id(3)])
    assert e1 == lestim.DemInstruction("error", [0.25], [lestim.target_relative_detector_id(3)])
    assert not (e1 != lestim.DemInstruction("error", [0.25], [lestim.target_relative_detector_id(3)]))
    assert e1 != lestim.DemInstruction("error", [0.35], [lestim.target_relative_detector_id(3)])
    assert not (e1 == lestim.DemInstruction("error", [0.35], [lestim.target_relative_detector_id(3)]))
    assert e1 != lestim.DemInstruction("error", [0.35], [lestim.target_relative_detector_id(4)])
    assert e1 != lestim.DemInstruction("shift_detectors", [0.35], [3])


def test_validation():
    with pytest.raises(ValueError, match="takes 1 arg"):
        lestim.DemInstruction("error", [], [lestim.target_relative_detector_id(3)])
    with pytest.raises(ValueError, match="takes 1 arg"):
        lestim.DemInstruction("error", [0.5, 0.5], [lestim.target_relative_detector_id(3)])
    with pytest.raises(ValueError, match="last target.+separator"):
        lestim.DemInstruction("error", [0.25], [lestim.target_separator()])
    with pytest.raises(ValueError, match="0 to 1"):
        lestim.DemInstruction("error", [-0.1], [lestim.target_relative_detector_id(3)])
    with pytest.raises(ValueError, match="0 to 1"):
        lestim.DemInstruction("error", [1.1], [lestim.target_relative_detector_id(3)])
    with pytest.raises(ValueError, match="detector.+targets"):
        lestim.DemInstruction("error", [0.25], [3])

    with pytest.raises(ValueError, match="integer targets"):
        lestim.DemInstruction("shift_detectors", [1.1], [lestim.target_relative_detector_id(3)])


def test_str():
    v = lestim.DemInstruction("ERROR", [0.125], [lestim.target_relative_detector_id(3), lestim.target_logical_observable_id(6)])
    assert str(v) == "error(0.125) D3 L6"
    v = lestim.DemInstruction("Shift_detectors", [1.5, 2.5, 5.5], [6])
    assert str(v) == "shift_detectors(1.5, 2.5, 5.5) 6"


def test_repr():
    v = lestim.DemInstruction("error", [0.25], [lestim.target_relative_detector_id(3), lestim.target_logical_observable_id(6)])
    assert eval(repr(v), {"stim": lestim}) == v
    v = lestim.DemInstruction("shift_detectors", [1.5, 2.5, 5.5], [6])
    assert eval(repr(v), {"stim": lestim}) == v


def test_hashable():
    a = lestim.DemInstruction("error", [0.25], [lestim.target_relative_detector_id(3)])
    b = lestim.DemInstruction("error", [0.125], [lestim.target_relative_detector_id(3)])
    c = lestim.DemInstruction("error", [0.25], [lestim.target_relative_detector_id(3)])
    assert hash(a) == hash(c)
    assert len({a, b, c}) == 2


def test_target_groups():
    dem = lestim.DetectorErrorModel("detector D0")
    assert dem[0].target_groups() == [[lestim.DemTarget("D0")]]


def test_init_from_str():
    assert lestim.DemInstruction("detector D0") == lestim.DemInstruction("detector", [], [lestim.target_relative_detector_id(0)])

    with pytest.raises(ValueError, match="single DemInstruction"):
        lestim.DemInstruction("")

    with pytest.raises(ValueError, match="single DemInstruction"):
        lestim.DemInstruction("""
            repeat 5 {
                error(0.25) D0
                shift_detectors 1
            }
        """)

    with pytest.raises(ValueError, match="single DemInstruction"):
        lestim.DemInstruction("""
            detector D0
            detector D1
        """)


def test_tag():
    assert lestim.DemInstruction("error[test](0.25) D1").tag == 'test'
    assert lestim.DemInstruction("error", [0.25], [lestim.DemTarget("D1")], tag="test").tag == 'test'
    dem = lestim.DetectorErrorModel('''
        error[test-tag](0.125) D0
        error(0.125) D0
    ''')
    assert dem[0].tag == 'test-tag'
    assert dem[1].tag == ''
