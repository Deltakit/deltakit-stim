import deltakit_stim


def test_CircuitErrorLocationStackFrame():
    v1 = deltakit_stim.CircuitErrorLocationStackFrame(
        instruction_offset=1,
        iteration_index=2,
        instruction_repetitions_arg=3,
    )
    assert v1.instruction_offset == 1
    assert v1.iteration_index == 2
    assert v1.instruction_repetitions_arg == 3

    v2 = deltakit_stim.CircuitErrorLocationStackFrame(
        instruction_offset=2,
        iteration_index=3,
        instruction_repetitions_arg=5,
    )
    assert v1 != v2
    assert v1 == v1
    assert len({v1, v1, v2}) == 2  # Check hashable.
    assert eval(repr(v1), {"stim": deltakit_stim}) == v1
    assert eval(repr(v2), {"stim": deltakit_stim}) == v2
    assert str(v1) == repr(v1)


def test_GateTargetWithCoords():
    v1 = deltakit_stim.GateTargetWithCoords(
        gate_target=deltakit_stim.target_x(5),
        coords=[1, 2, 3],
    )
    assert v1.gate_target == deltakit_stim.GateTarget(deltakit_stim.target_x(5))
    assert v1.coords == [1, 2, 3]
    v2 = deltakit_stim.GateTargetWithCoords(
        gate_target=deltakit_stim.GateTarget(4),
        coords=[1, 2],
    )
    assert v1 != v2
    assert v1 == v1
    assert len({v1, v1, v2}) == 2  # Check hashable.
    assert eval(repr(v1), {"stim": deltakit_stim}) == v1
    assert eval(repr(v2), {"stim": deltakit_stim}) == v2
    assert str(v1) == 'X5[coords 1,2,3]'


def test_DemTargetWithCoords():
    v1 = deltakit_stim.DemTargetWithCoords(
        dem_target=deltakit_stim.DemTarget.relative_detector_id(5),
        coords=[1, 2, 3],
    )
    assert v1.dem_target == deltakit_stim.DemTarget.relative_detector_id(5)
    assert v1.coords == [1, 2, 3]
    v2 = deltakit_stim.DemTargetWithCoords(
        dem_target=deltakit_stim.DemTarget.logical_observable_id(3),
        coords=(),
    )
    assert v1 != v2
    assert v1 == v1
    assert len({v1, v1, v2}) == 2  # Check hashable.
    assert eval(repr(v1), {"stim": deltakit_stim}) == v1
    assert eval(repr(v2), {"stim": deltakit_stim}) == v2
    assert str(v1) == 'D5[coords 1,2,3]'


def test_FlippedMeasurement():
    v1 = deltakit_stim.FlippedMeasurement(
        record_index=5,
        observable=[
            deltakit_stim.GateTargetWithCoords(
                gate_target=deltakit_stim.target_x(5),
                coords=[1, 2, 3]),
        ],
    )
    assert v1.record_index == 5
    assert v1.observable == [
        deltakit_stim.GateTargetWithCoords(
            gate_target=deltakit_stim.target_x(5),
            coords=[1, 2, 3]),
    ]
    v2 = deltakit_stim.FlippedMeasurement(
        record_index=5,
        observable=[],
    )
    assert v1 != v2
    assert v1 == v1
    assert len({v1, v1, v2}) == 2  # Check hashable.
    assert eval(repr(v1), {"stim": deltakit_stim}) == v1
    assert eval(repr(v2), {"stim": deltakit_stim}) == v2
    assert str(v1) == repr(v1)


def test_CircuitTargetsInsideInstruction():
    v1 = deltakit_stim.CircuitTargetsInsideInstruction(
        gate="X_ERROR",
        args=[0.25],
        target_range_start=2,
        target_range_end=5,
        targets_in_range=[
            deltakit_stim.GateTargetWithCoords(gate_target=5, coords=[1, 2]),
            deltakit_stim.GateTargetWithCoords(gate_target=6, coords=[1, 3]),
            deltakit_stim.GateTargetWithCoords(gate_target=7, coords=[]),
        ],
    )
    assert v1.gate == "X_ERROR"
    assert v1.args == [0.25]
    assert v1.target_range_start == 2
    assert v1.target_range_end == 5
    assert v1.targets_in_range == [
        deltakit_stim.GateTargetWithCoords(gate_target=5, coords=[1, 2]),
        deltakit_stim.GateTargetWithCoords(gate_target=6, coords=[1, 3]),
        deltakit_stim.GateTargetWithCoords(gate_target=7, coords=[]),
    ]
    v2 = deltakit_stim.CircuitTargetsInsideInstruction(
        gate="Z_ERROR",
        args=[0.125],
        target_range_start=3,
        target_range_end=3,
        targets_in_range=[],
    )
    assert v1 != v2
    assert v1 == v1
    assert len({v1, v1, v2}) == 2  # Check hashable.
    assert eval(repr(v1), {"stim": deltakit_stim}) == v1
    assert eval(repr(v2), {"stim": deltakit_stim}) == v2
    assert str(v1) == "X_ERROR(0.25) 5[coords 1,2] 6[coords 1,3] 7"


def test_CircuitErrorLocation():
    m = deltakit_stim.FlippedMeasurement(
        record_index=5,
        observable=[
            deltakit_stim.GateTargetWithCoords(
                gate_target=deltakit_stim.target_x(5),
                coords=[1, 2, 3]),
        ],
    )
    p = [
        deltakit_stim.GateTargetWithCoords(
            gate_target=deltakit_stim.target_y(6),
            coords=[1, 2, 3]),
    ]
    t = deltakit_stim.CircuitTargetsInsideInstruction(
        gate="X_ERROR",
        args=[0.25],
        target_range_start=2,
        target_range_end=5,
        targets_in_range=[
            deltakit_stim.GateTargetWithCoords(gate_target=5, coords=[1, 2]),
            deltakit_stim.GateTargetWithCoords(gate_target=6, coords=[1, 3]),
            deltakit_stim.GateTargetWithCoords(gate_target=7, coords=[]),
        ],
    )
    s = [
        deltakit_stim.CircuitErrorLocationStackFrame(
            instruction_offset=1,
            iteration_index=2,
            instruction_repetitions_arg=3,
        )
    ] * 2
    v1 = deltakit_stim.CircuitErrorLocation(
        tick_offset=5,
        flipped_pauli_product=p,
        flipped_measurement=m,
        instruction_targets=t,
        stack_frames=s,
    )
    assert v1.tick_offset == 5
    assert v1.flipped_pauli_product == p
    assert v1.flipped_measurement == m
    assert v1.instruction_targets == t
    assert v1.stack_frames == s
    v2 = deltakit_stim.CircuitErrorLocation(
        tick_offset=5,
        flipped_pauli_product=[],
        flipped_measurement=None,
        instruction_targets=t,
        stack_frames=[],
    )
    assert v2.flipped_measurement is None
    assert v1 != v2
    assert v1 == v1
    assert len({v1, v1, v2}) == 2  # Check hashable.
    assert eval(repr(v1), {"stim": deltakit_stim}) == v1
    assert eval(repr(v2), {"stim": deltakit_stim}) == v2
    assert str(v1) == """CircuitErrorLocation {
    flipped_pauli_product: Y6[coords 1,2,3]
    flipped_measurement.measurement_record_index: 5
    flipped_measurement.measured_observable: X5[coords 1,2,3]
    Circuit location stack trace:
        (after 5 TICKs)
        at instruction #2 (a REPEAT 3 block) in the circuit
        after 2 completed iterations
        at instruction #2 (X_ERROR) in the REPEAT block
        at targets #3 to #5 of the instruction
        resolving to X_ERROR(0.25) 5[coords 1,2] 6[coords 1,3] 7
}"""


def test_MatchedError():
    m = deltakit_stim.FlippedMeasurement(
        record_index=5,
        observable=[
            deltakit_stim.GateTargetWithCoords(
                gate_target=deltakit_stim.target_x(5),
                coords=[1, 2, 3]),
        ],
    )
    p = [
        deltakit_stim.GateTargetWithCoords(
            gate_target=deltakit_stim.target_y(6),
            coords=[1, 2, 3]),
    ]
    t = deltakit_stim.CircuitTargetsInsideInstruction(
        gate="X_ERROR",
        args=[0.25],
        target_range_start=2,
        target_range_end=5,
        targets_in_range=[
            deltakit_stim.GateTargetWithCoords(gate_target=5, coords=[1, 2]),
            deltakit_stim.GateTargetWithCoords(gate_target=6, coords=[1, 3]),
            deltakit_stim.GateTargetWithCoords(gate_target=7, coords=[]),
        ],
    )
    s = [
        deltakit_stim.CircuitErrorLocationStackFrame(
            instruction_offset=1,
            iteration_index=2,
            instruction_repetitions_arg=3,
        )
    ] * 2
    e = deltakit_stim.CircuitErrorLocation(
        tick_offset=5,
        flipped_pauli_product=p,
        flipped_measurement=m,
        instruction_targets=t,
        stack_frames=s,
    )
    v1 = deltakit_stim.ExplainedError(
        dem_error_terms=[deltakit_stim.DemTargetWithCoords(
            dem_target=deltakit_stim.DemTarget.relative_detector_id(5),
            coords=[1, 2, 3],
        )],
        circuit_error_locations=[e],
    )
    assert v1.dem_error_terms == [deltakit_stim.DemTargetWithCoords(
        dem_target=deltakit_stim.DemTarget.relative_detector_id(5),
        coords=[1, 2, 3],
    )]
    assert v1.circuit_error_locations == [e]
    v2 = deltakit_stim.ExplainedError(
        dem_error_terms=[],
        circuit_error_locations=[],
    )
    assert v1 != v2
    assert v1 == v1
    assert len({v1, v1, v2}) == 2  # Check hashable.
    assert eval(repr(v1), {"stim": deltakit_stim}) == v1
    assert eval(repr(v2), {"stim": deltakit_stim}) == v2
    assert str(v1) == """ExplainedError {
    dem_error_terms: D5[coords 1,2,3]
    CircuitErrorLocation {
        flipped_pauli_product: Y6[coords 1,2,3]
        flipped_measurement.measurement_record_index: 5
        flipped_measurement.measured_observable: X5[coords 1,2,3]
        Circuit location stack trace:
            (after 5 TICKs)
            at instruction #2 (a REPEAT 3 block) in the circuit
            after 2 completed iterations
            at instruction #2 (X_ERROR) in the REPEAT block
            at targets #3 to #5 of the instruction
            resolving to X_ERROR(0.25) 5[coords 1,2] 6[coords 1,3] 7
    }
}"""
