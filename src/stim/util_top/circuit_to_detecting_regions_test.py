import pytest
import lestim


def test_detecting_regions_fails_on_anticommutations_at_start_of_circuit():
    c = lestim.Circuit("""
        TICK
        R 0
        TICK
        MX 0
        DETECTOR rec[-1]
    """)
    assert 'magenta' in str(c.diagram('detslice-with-ops-svg'))
    with pytest.raises(ValueError, match="anticommutation"):
        c.detecting_regions()

    c = lestim.Circuit("""
        R 0
        TICK
        MX 0
        DETECTOR rec[-1]
    """)
    assert 'magenta' in str(c.diagram('detslice-with-ops-svg'))
    with pytest.raises(ValueError, match="anticommutation"):
        c.detecting_regions()

    c = lestim.Circuit("""
        MX 0
        DETECTOR rec[-1]
    """)
    assert 'magenta' in str(c.diagram('detslice-with-ops-svg'))
    with pytest.raises(ValueError, match="anticommutation"):
        c.detecting_regions()
