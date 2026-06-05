import pytest
import deltakit_stim


def test_detecting_regions_fails_on_anticommutations_at_start_of_circuit():
    c = deltakit_stim.Circuit("""
        TICK
        R 0
        TICK
        MX 0
        DETECTOR rec[-1]
    """)
    assert 'magenta' in str(c.diagram('detslice-with-ops-svg'))
    with pytest.raises(ValueError, match="anticommutation"):
        c.detecting_regions()

    c = deltakit_stim.Circuit("""
        R 0
        TICK
        MX 0
        DETECTOR rec[-1]
    """)
    assert 'magenta' in str(c.diagram('detslice-with-ops-svg'))
    with pytest.raises(ValueError, match="anticommutation"):
        c.detecting_regions()

    c = deltakit_stim.Circuit("""
        MX 0
        DETECTOR rec[-1]
    """)
    assert 'magenta' in str(c.diagram('detslice-with-ops-svg'))
    with pytest.raises(ValueError, match="anticommutation"):
        c.detecting_regions()
