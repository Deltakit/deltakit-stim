import lestim


def test_solve_flow_measurements():
    assert lestim.Circuit("""
        M 2
    """).solve_flow_measurements([
        lestim.Flow("X2 -> X2"),
    ]) == [None]

    assert lestim.Circuit("""
        M 2
    """).solve_flow_measurements([
        lestim.Flow("X2 -> X2"),
        lestim.Flow("Y2 -> Y2"),
        lestim.Flow("Z2 -> Z2"),
        lestim.Flow("Z2 -> 1"),
    ]) == [None, None, [], [0]]

    assert lestim.Circuit("""
        MXX 0 1
    """).solve_flow_measurements([
        lestim.Flow("YY -> ZZ"),
        lestim.Flow("YY -> YY"),
        lestim.Flow("YZ -> ZY"),
    ]) == [[0], [], [0]]


def test_solve_flow_generators_measurements_multi_target():
    assert lestim.Circuit("""
        M 1 2
    """).flow_generators() == [
        lestim.Flow("1 -> __Z xor rec[1]"),
        lestim.Flow("1 -> _Z_ xor rec[0]"),
        lestim.Flow("__Z -> rec[1]"),
        lestim.Flow("_Z_ -> rec[0]"),
        lestim.Flow("X__ -> X__"),
        lestim.Flow("Z__ -> Z__"),
    ]

    assert lestim.Circuit("""
        MX 1 2
    """).flow_generators() == [
        lestim.Flow("1 -> __X xor rec[1]"),
        lestim.Flow("1 -> _X_ xor rec[0]"),
        lestim.Flow("__X -> rec[1]"),
        lestim.Flow("_X_ -> rec[0]"),
        lestim.Flow("X__ -> X__"),
        lestim.Flow("Z__ -> Z__"),
    ]

    assert lestim.Circuit("""
        MYY 1 2 3 4
    """).flow_generators() == [
        lestim.Flow("1 -> ___YY xor rec[1]"),
        lestim.Flow("1 -> _YY__ xor rec[0]"),
        lestim.Flow("____Y -> ____Y"),
        lestim.Flow("___XZ -> ___ZX xor rec[1]"),
        lestim.Flow("___ZZ -> ___ZZ"),
        lestim.Flow("__Y__ -> __Y__"),
        lestim.Flow("_XZ__ -> _ZX__ xor rec[0]"),
        lestim.Flow("_ZZ__ -> _ZZ__"),
        lestim.Flow("X____ -> X____"),
        lestim.Flow("Z____ -> Z____"),
    ]
    assert lestim.Circuit("""
        MPP Y1*Y2 Y3*Y4
    """).flow_generators() == [
        lestim.Flow("1 -> ___YY xor rec[1]"),
        lestim.Flow("1 -> _YY__ xor rec[0]"),
        lestim.Flow("____Y -> ____Y"),
        lestim.Flow("___XZ -> ___ZX xor rec[1]"),
        lestim.Flow("___ZZ -> ___ZZ"),
        lestim.Flow("__Y__ -> __Y__"),
        lestim.Flow("_XZ__ -> _ZX__ xor rec[0]"),
        lestim.Flow("_ZZ__ -> _ZZ__"),
        lestim.Flow("X____ -> X____"),
        lestim.Flow("Z____ -> Z____"),
    ]


def test_solve_flow_measurements_multi_target():
    assert lestim.Circuit("""
        M 1 2
    """).solve_flow_measurements([
        lestim.Flow("Z1 -> 1"),
    ]) == [[0]]

    assert lestim.Circuit("""
        MX 1 2
    """).solve_flow_measurements([
        lestim.Flow("X1 -> 1"),
    ]) == [[0]]

    assert lestim.Circuit("""
        MYY 1 2 3 4
    """).solve_flow_measurements([
        lestim.Flow("Y1*Y2 -> 1"),
    ]) == [[0]]

    assert lestim.Circuit("""
        MPP Y1*Y2 Y3*Y4
    """).solve_flow_measurements([
        lestim.Flow("Y1*Y2 -> 1"),
    ]) == [[0]]


def test_solve_flow_measurements_fewer_measurements_heuristic():
    assert lestim.Circuit("""
        MPP Z0*Z1*Z2*Z3*Z4*Z5*Z6*Z7*Z8
        M 0 1 2 3 4 5 6 7 8
    """).solve_flow_measurements([
        lestim.Flow("1 -> Z0*Z1*Z2*Z3*Z4*Z5*Z6*Z7*Z8"),
    ]) == [[0]]

    assert lestim.Circuit("""
        MPP Z0*Z1*Z2*Z3*Z4*Z5*Z6*Z7*Z8
        M 0 1 2 3 4 5 6 7 8
    """).solve_flow_measurements([
        lestim.Flow("Z0*Z1*Z2*Z3*Z4*Z5*Z6*Z7*Z8 -> 1"),
    ]) == [[0]]

    assert lestim.Circuit("""
        M 0 1 2 3 4 5 6 7 8
        MPP Z0*Z1*Z2*Z3*Z4*Z5*Z6*Z7*Z8
    """).solve_flow_measurements([
        lestim.Flow("1 -> Z0*Z1*Z2*Z3*Z4*Z5*Z6*Z7*Z8"),
    ]) == [[9]]

    assert lestim.Circuit("""
        M 0 1 2 3 4 5 6 7 8
        MPP Z0*Z1*Z2*Z3*Z4*Z5*Z6*Z7*Z8
    """).solve_flow_measurements([
        lestim.Flow("Z0*Z1*Z2*Z3*Z4*Z5*Z6*Z7*Z8 -> 1"),
    ]) == [[9]]
