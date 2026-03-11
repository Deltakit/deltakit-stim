import pytest
<<<<<<< HEAD
import lestim


def test_detecting_regions_fails_on_anticommutations_at_start_of_circuit():
    c = lestim.Circuit("""
=======
import stim


def test_detecting_regions_fails_on_anticommutations_at_start_of_circuit():
    c = stim.Circuit("""
>>>>>>> 1a67d3a9 (feat: Sync with Stim (#32))
        TICK
        R 0
        TICK
        MX 0
        DETECTOR rec[-1]
    """)
    assert 'magenta' in str(c.diagram('detslice-with-ops-svg'))
    with pytest.raises(ValueError, match="anticommutation"):
        c.detecting_regions()

<<<<<<< HEAD
    c = lestim.Circuit("""
=======
    c = stim.Circuit("""
>>>>>>> 1a67d3a9 (feat: Sync with Stim (#32))
        R 0
        TICK
        MX 0
        DETECTOR rec[-1]
    """)
    assert 'magenta' in str(c.diagram('detslice-with-ops-svg'))
    with pytest.raises(ValueError, match="anticommutation"):
        c.detecting_regions()

<<<<<<< HEAD
    c = lestim.Circuit("""
=======
    c = stim.Circuit("""
>>>>>>> 1a67d3a9 (feat: Sync with Stim (#32))
        MX 0
        DETECTOR rec[-1]
    """)
    assert 'magenta' in str(c.diagram('detslice-with-ops-svg'))
    with pytest.raises(ValueError, match="anticommutation"):
        c.detecting_regions()
