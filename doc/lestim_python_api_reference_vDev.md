# Lestim (Development Version) API Reference

*CAUTION*: this API reference is for the in-development version of lestim.
Methods and arguments mentioned here may not be accessible in stable versions, yet.

## Index
- [`lestim.Circuit`](#lestim.Circuit)
    - [`lestim.Circuit.__add__`](#lestim.Circuit.__add__)
    - [`lestim.Circuit.__eq__`](#lestim.Circuit.__eq__)
    - [`lestim.Circuit.__getitem__`](#lestim.Circuit.__getitem__)
    - [`lestim.Circuit.__iadd__`](#lestim.Circuit.__iadd__)
    - [`lestim.Circuit.__imul__`](#lestim.Circuit.__imul__)
    - [`lestim.Circuit.__init__`](#lestim.Circuit.__init__)
    - [`lestim.Circuit.__len__`](#lestim.Circuit.__len__)
    - [`lestim.Circuit.__mul__`](#lestim.Circuit.__mul__)
    - [`lestim.Circuit.__ne__`](#lestim.Circuit.__ne__)
    - [`lestim.Circuit.__repr__`](#lestim.Circuit.__repr__)
    - [`lestim.Circuit.__rmul__`](#lestim.Circuit.__rmul__)
    - [`lestim.Circuit.__str__`](#lestim.Circuit.__str__)
    - [`lestim.Circuit.append`](#lestim.Circuit.append)
    - [`lestim.Circuit.append_from_stim_program_text`](#lestim.Circuit.append_from_stim_program_text)
    - [`lestim.Circuit.approx_equals`](#lestim.Circuit.approx_equals)
    - [`lestim.Circuit.clear`](#lestim.Circuit.clear)
    - [`lestim.Circuit.compile_detector_sampler`](#lestim.Circuit.compile_detector_sampler)
    - [`lestim.Circuit.compile_m2d_converter`](#lestim.Circuit.compile_m2d_converter)
    - [`lestim.Circuit.compile_sampler`](#lestim.Circuit.compile_sampler)
    - [`lestim.Circuit.copy`](#lestim.Circuit.copy)
    - [`lestim.Circuit.count_determined_measurements`](#lestim.Circuit.count_determined_measurements)
    - [`lestim.Circuit.decomposed`](#lestim.Circuit.decomposed)
    - [`lestim.Circuit.detecting_regions`](#lestim.Circuit.detecting_regions)
    - [`lestim.Circuit.detector_error_model`](#lestim.Circuit.detector_error_model)
    - [`lestim.Circuit.diagram`](#lestim.Circuit.diagram)
    - [`lestim.Circuit.explain_detector_error_model_errors`](#lestim.Circuit.explain_detector_error_model_errors)
    - [`lestim.Circuit.flattened`](#lestim.Circuit.flattened)
    - [`lestim.Circuit.from_file`](#lestim.Circuit.from_file)
    - [`lestim.Circuit.generated`](#lestim.Circuit.generated)
    - [`lestim.Circuit.get_detector_coordinates`](#lestim.Circuit.get_detector_coordinates)
    - [`lestim.Circuit.get_final_qubit_coordinates`](#lestim.Circuit.get_final_qubit_coordinates)
    - [`lestim.Circuit.has_all_flows`](#lestim.Circuit.has_all_flows)
    - [`lestim.Circuit.has_flow`](#lestim.Circuit.has_flow)
    - [`lestim.Circuit.inverse`](#lestim.Circuit.inverse)
    - [`lestim.Circuit.likeliest_error_sat_problem`](#lestim.Circuit.likeliest_error_sat_problem)
    - [`lestim.Circuit.num_detectors`](#lestim.Circuit.num_detectors)
    - [`lestim.Circuit.num_measurements`](#lestim.Circuit.num_measurements)
    - [`lestim.Circuit.num_observables`](#lestim.Circuit.num_observables)
    - [`lestim.Circuit.num_qubits`](#lestim.Circuit.num_qubits)
    - [`lestim.Circuit.num_sweep_bits`](#lestim.Circuit.num_sweep_bits)
    - [`lestim.Circuit.num_ticks`](#lestim.Circuit.num_ticks)
    - [`lestim.Circuit.reference_sample`](#lestim.Circuit.reference_sample)
    - [`lestim.Circuit.search_for_undetectable_logical_errors`](#lestim.Circuit.search_for_undetectable_logical_errors)
    - [`lestim.Circuit.shortest_error_sat_problem`](#lestim.Circuit.shortest_error_sat_problem)
    - [`lestim.Circuit.shortest_graphlike_error`](#lestim.Circuit.shortest_graphlike_error)
    - [`lestim.Circuit.time_reversed_for_flows`](#lestim.Circuit.time_reversed_for_flows)
    - [`lestim.Circuit.to_crumble_url`](#lestim.Circuit.to_crumble_url)
    - [`lestim.Circuit.to_file`](#lestim.Circuit.to_file)
    - [`lestim.Circuit.to_qasm`](#lestim.Circuit.to_qasm)
    - [`lestim.Circuit.to_quirk_url`](#lestim.Circuit.to_quirk_url)
    - [`lestim.Circuit.to_tableau`](#lestim.Circuit.to_tableau)
    - [`lestim.Circuit.with_inlined_feedback`](#lestim.Circuit.with_inlined_feedback)
    - [`lestim.Circuit.without_noise`](#lestim.Circuit.without_noise)
- [`lestim.CircuitErrorLocation`](#lestim.CircuitErrorLocation)
    - [`lestim.CircuitErrorLocation.__init__`](#lestim.CircuitErrorLocation.__init__)
    - [`lestim.CircuitErrorLocation.flipped_measurement`](#lestim.CircuitErrorLocation.flipped_measurement)
    - [`lestim.CircuitErrorLocation.flipped_pauli_product`](#lestim.CircuitErrorLocation.flipped_pauli_product)
    - [`lestim.CircuitErrorLocation.instruction_targets`](#lestim.CircuitErrorLocation.instruction_targets)
    - [`lestim.CircuitErrorLocation.stack_frames`](#lestim.CircuitErrorLocation.stack_frames)
    - [`lestim.CircuitErrorLocation.tick_offset`](#lestim.CircuitErrorLocation.tick_offset)
- [`lestim.CircuitErrorLocationStackFrame`](#lestim.CircuitErrorLocationStackFrame)
    - [`lestim.CircuitErrorLocationStackFrame.__init__`](#lestim.CircuitErrorLocationStackFrame.__init__)
    - [`lestim.CircuitErrorLocationStackFrame.instruction_offset`](#lestim.CircuitErrorLocationStackFrame.instruction_offset)
    - [`lestim.CircuitErrorLocationStackFrame.instruction_repetitions_arg`](#lestim.CircuitErrorLocationStackFrame.instruction_repetitions_arg)
    - [`lestim.CircuitErrorLocationStackFrame.iteration_index`](#lestim.CircuitErrorLocationStackFrame.iteration_index)
- [`lestim.CircuitInstruction`](#lestim.CircuitInstruction)
    - [`lestim.CircuitInstruction.__eq__`](#lestim.CircuitInstruction.__eq__)
    - [`lestim.CircuitInstruction.__init__`](#lestim.CircuitInstruction.__init__)
    - [`lestim.CircuitInstruction.__ne__`](#lestim.CircuitInstruction.__ne__)
    - [`lestim.CircuitInstruction.__repr__`](#lestim.CircuitInstruction.__repr__)
    - [`lestim.CircuitInstruction.__str__`](#lestim.CircuitInstruction.__str__)
    - [`lestim.CircuitInstruction.gate_args_copy`](#lestim.CircuitInstruction.gate_args_copy)
    - [`lestim.CircuitInstruction.name`](#lestim.CircuitInstruction.name)
    - [`lestim.CircuitInstruction.targets_copy`](#lestim.CircuitInstruction.targets_copy)
- [`lestim.CircuitRepeatBlock`](#lestim.CircuitRepeatBlock)
    - [`lestim.CircuitRepeatBlock.__eq__`](#lestim.CircuitRepeatBlock.__eq__)
    - [`lestim.CircuitRepeatBlock.__init__`](#lestim.CircuitRepeatBlock.__init__)
    - [`lestim.CircuitRepeatBlock.__ne__`](#lestim.CircuitRepeatBlock.__ne__)
    - [`lestim.CircuitRepeatBlock.__repr__`](#lestim.CircuitRepeatBlock.__repr__)
    - [`lestim.CircuitRepeatBlock.body_copy`](#lestim.CircuitRepeatBlock.body_copy)
    - [`lestim.CircuitRepeatBlock.name`](#lestim.CircuitRepeatBlock.name)
    - [`lestim.CircuitRepeatBlock.repeat_count`](#lestim.CircuitRepeatBlock.repeat_count)
- [`lestim.CircuitTargetsInsideInstruction`](#lestim.CircuitTargetsInsideInstruction)
    - [`lestim.CircuitTargetsInsideInstruction.__init__`](#lestim.CircuitTargetsInsideInstruction.__init__)
    - [`lestim.CircuitTargetsInsideInstruction.args`](#lestim.CircuitTargetsInsideInstruction.args)
    - [`lestim.CircuitTargetsInsideInstruction.gate`](#lestim.CircuitTargetsInsideInstruction.gate)
    - [`lestim.CircuitTargetsInsideInstruction.target_range_end`](#lestim.CircuitTargetsInsideInstruction.target_range_end)
    - [`lestim.CircuitTargetsInsideInstruction.target_range_start`](#lestim.CircuitTargetsInsideInstruction.target_range_start)
    - [`lestim.CircuitTargetsInsideInstruction.targets_in_range`](#lestim.CircuitTargetsInsideInstruction.targets_in_range)
- [`lestim.CompiledDemSampler`](#lestim.CompiledDemSampler)
    - [`lestim.CompiledDemSampler.sample`](#lestim.CompiledDemSampler.sample)
    - [`lestim.CompiledDemSampler.sample_write`](#lestim.CompiledDemSampler.sample_write)
- [`lestim.CompiledDetectorSampler`](#lestim.CompiledDetectorSampler)
    - [`lestim.CompiledDetectorSampler.__init__`](#lestim.CompiledDetectorSampler.__init__)
    - [`lestim.CompiledDetectorSampler.__repr__`](#lestim.CompiledDetectorSampler.__repr__)
    - [`lestim.CompiledDetectorSampler.sample`](#lestim.CompiledDetectorSampler.sample)
    - [`lestim.CompiledDetectorSampler.sample_write`](#lestim.CompiledDetectorSampler.sample_write)
- [`lestim.CompiledMeasurementSampler`](#lestim.CompiledMeasurementSampler)
    - [`lestim.CompiledMeasurementSampler.__init__`](#lestim.CompiledMeasurementSampler.__init__)
    - [`lestim.CompiledMeasurementSampler.__repr__`](#lestim.CompiledMeasurementSampler.__repr__)
    - [`lestim.CompiledMeasurementSampler.sample`](#lestim.CompiledMeasurementSampler.sample)
    - [`lestim.CompiledMeasurementSampler.sample_write`](#lestim.CompiledMeasurementSampler.sample_write)
- [`lestim.CompiledMeasurementsToDetectionEventsConverter`](#lestim.CompiledMeasurementsToDetectionEventsConverter)
    - [`lestim.CompiledMeasurementsToDetectionEventsConverter.__init__`](#lestim.CompiledMeasurementsToDetectionEventsConverter.__init__)
    - [`lestim.CompiledMeasurementsToDetectionEventsConverter.__repr__`](#lestim.CompiledMeasurementsToDetectionEventsConverter.__repr__)
    - [`lestim.CompiledMeasurementsToDetectionEventsConverter.convert`](#lestim.CompiledMeasurementsToDetectionEventsConverter.convert)
    - [`lestim.CompiledMeasurementsToDetectionEventsConverter.convert_file`](#lestim.CompiledMeasurementsToDetectionEventsConverter.convert_file)
- [`lestim.DemInstruction`](#lestim.DemInstruction)
    - [`lestim.DemInstruction.__eq__`](#lestim.DemInstruction.__eq__)
    - [`lestim.DemInstruction.__init__`](#lestim.DemInstruction.__init__)
    - [`lestim.DemInstruction.__ne__`](#lestim.DemInstruction.__ne__)
    - [`lestim.DemInstruction.__repr__`](#lestim.DemInstruction.__repr__)
    - [`lestim.DemInstruction.__str__`](#lestim.DemInstruction.__str__)
    - [`lestim.DemInstruction.args_copy`](#lestim.DemInstruction.args_copy)
    - [`lestim.DemInstruction.targets_copy`](#lestim.DemInstruction.targets_copy)
    - [`lestim.DemInstruction.type`](#lestim.DemInstruction.type)
- [`lestim.DemRepeatBlock`](#lestim.DemRepeatBlock)
    - [`lestim.DemRepeatBlock.__eq__`](#lestim.DemRepeatBlock.__eq__)
    - [`lestim.DemRepeatBlock.__init__`](#lestim.DemRepeatBlock.__init__)
    - [`lestim.DemRepeatBlock.__ne__`](#lestim.DemRepeatBlock.__ne__)
    - [`lestim.DemRepeatBlock.__repr__`](#lestim.DemRepeatBlock.__repr__)
    - [`lestim.DemRepeatBlock.body_copy`](#lestim.DemRepeatBlock.body_copy)
    - [`lestim.DemRepeatBlock.repeat_count`](#lestim.DemRepeatBlock.repeat_count)
    - [`lestim.DemRepeatBlock.type`](#lestim.DemRepeatBlock.type)
- [`lestim.DemTarget`](#lestim.DemTarget)
    - [`lestim.DemTarget.__eq__`](#lestim.DemTarget.__eq__)
    - [`lestim.DemTarget.__ne__`](#lestim.DemTarget.__ne__)
    - [`lestim.DemTarget.__repr__`](#lestim.DemTarget.__repr__)
    - [`lestim.DemTarget.__str__`](#lestim.DemTarget.__str__)
    - [`lestim.DemTarget.is_logical_observable_id`](#lestim.DemTarget.is_logical_observable_id)
    - [`lestim.DemTarget.is_relative_detector_id`](#lestim.DemTarget.is_relative_detector_id)
    - [`lestim.DemTarget.is_separator`](#lestim.DemTarget.is_separator)
    - [`lestim.DemTarget.logical_observable_id`](#lestim.DemTarget.logical_observable_id)
    - [`lestim.DemTarget.relative_detector_id`](#lestim.DemTarget.relative_detector_id)
    - [`lestim.DemTarget.separator`](#lestim.DemTarget.separator)
    - [`lestim.DemTarget.val`](#lestim.DemTarget.val)
- [`lestim.DemTargetWithCoords`](#lestim.DemTargetWithCoords)
    - [`lestim.DemTargetWithCoords.__init__`](#lestim.DemTargetWithCoords.__init__)
    - [`lestim.DemTargetWithCoords.coords`](#lestim.DemTargetWithCoords.coords)
    - [`lestim.DemTargetWithCoords.dem_target`](#lestim.DemTargetWithCoords.dem_target)
- [`lestim.DetectorErrorModel`](#lestim.DetectorErrorModel)
    - [`lestim.DetectorErrorModel.__add__`](#lestim.DetectorErrorModel.__add__)
    - [`lestim.DetectorErrorModel.__eq__`](#lestim.DetectorErrorModel.__eq__)
    - [`lestim.DetectorErrorModel.__getitem__`](#lestim.DetectorErrorModel.__getitem__)
    - [`lestim.DetectorErrorModel.__iadd__`](#lestim.DetectorErrorModel.__iadd__)
    - [`lestim.DetectorErrorModel.__imul__`](#lestim.DetectorErrorModel.__imul__)
    - [`lestim.DetectorErrorModel.__init__`](#lestim.DetectorErrorModel.__init__)
    - [`lestim.DetectorErrorModel.__len__`](#lestim.DetectorErrorModel.__len__)
    - [`lestim.DetectorErrorModel.__mul__`](#lestim.DetectorErrorModel.__mul__)
    - [`lestim.DetectorErrorModel.__ne__`](#lestim.DetectorErrorModel.__ne__)
    - [`lestim.DetectorErrorModel.__repr__`](#lestim.DetectorErrorModel.__repr__)
    - [`lestim.DetectorErrorModel.__rmul__`](#lestim.DetectorErrorModel.__rmul__)
    - [`lestim.DetectorErrorModel.__str__`](#lestim.DetectorErrorModel.__str__)
    - [`lestim.DetectorErrorModel.append`](#lestim.DetectorErrorModel.append)
    - [`lestim.DetectorErrorModel.approx_equals`](#lestim.DetectorErrorModel.approx_equals)
    - [`lestim.DetectorErrorModel.clear`](#lestim.DetectorErrorModel.clear)
    - [`lestim.DetectorErrorModel.compile_sampler`](#lestim.DetectorErrorModel.compile_sampler)
    - [`lestim.DetectorErrorModel.copy`](#lestim.DetectorErrorModel.copy)
    - [`lestim.DetectorErrorModel.diagram`](#lestim.DetectorErrorModel.diagram)
    - [`lestim.DetectorErrorModel.flattened`](#lestim.DetectorErrorModel.flattened)
    - [`lestim.DetectorErrorModel.from_file`](#lestim.DetectorErrorModel.from_file)
    - [`lestim.DetectorErrorModel.get_detector_coordinates`](#lestim.DetectorErrorModel.get_detector_coordinates)
    - [`lestim.DetectorErrorModel.num_detectors`](#lestim.DetectorErrorModel.num_detectors)
    - [`lestim.DetectorErrorModel.num_errors`](#lestim.DetectorErrorModel.num_errors)
    - [`lestim.DetectorErrorModel.num_observables`](#lestim.DetectorErrorModel.num_observables)
    - [`lestim.DetectorErrorModel.rounded`](#lestim.DetectorErrorModel.rounded)
    - [`lestim.DetectorErrorModel.shortest_graphlike_error`](#lestim.DetectorErrorModel.shortest_graphlike_error)
    - [`lestim.DetectorErrorModel.to_file`](#lestim.DetectorErrorModel.to_file)
- [`lestim.ExplainedError`](#lestim.ExplainedError)
    - [`lestim.ExplainedError.__init__`](#lestim.ExplainedError.__init__)
    - [`lestim.ExplainedError.circuit_error_locations`](#lestim.ExplainedError.circuit_error_locations)
    - [`lestim.ExplainedError.dem_error_terms`](#lestim.ExplainedError.dem_error_terms)
- [`lestim.FlipSimulator`](#lestim.FlipSimulator)
    - [`lestim.FlipSimulator.__init__`](#lestim.FlipSimulator.__init__)
    - [`lestim.FlipSimulator.batch_size`](#lestim.FlipSimulator.batch_size)
    - [`lestim.FlipSimulator.broadcast_pauli_errors`](#lestim.FlipSimulator.broadcast_pauli_errors)
    - [`lestim.FlipSimulator.do`](#lestim.FlipSimulator.do)
    - [`lestim.FlipSimulator.get_detector_flips`](#lestim.FlipSimulator.get_detector_flips)
    - [`lestim.FlipSimulator.get_measurement_flips`](#lestim.FlipSimulator.get_measurement_flips)
    - [`lestim.FlipSimulator.get_observable_flips`](#lestim.FlipSimulator.get_observable_flips)
    - [`lestim.FlipSimulator.num_detectors`](#lestim.FlipSimulator.num_detectors)
    - [`lestim.FlipSimulator.num_measurements`](#lestim.FlipSimulator.num_measurements)
    - [`lestim.FlipSimulator.num_observables`](#lestim.FlipSimulator.num_observables)
    - [`lestim.FlipSimulator.num_qubits`](#lestim.FlipSimulator.num_qubits)
    - [`lestim.FlipSimulator.peek_pauli_flips`](#lestim.FlipSimulator.peek_pauli_flips)
    - [`lestim.FlipSimulator.set_pauli_flip`](#lestim.FlipSimulator.set_pauli_flip)
- [`lestim.FlippedMeasurement`](#lestim.FlippedMeasurement)
    - [`lestim.FlippedMeasurement.__init__`](#lestim.FlippedMeasurement.__init__)
    - [`lestim.FlippedMeasurement.observable`](#lestim.FlippedMeasurement.observable)
    - [`lestim.FlippedMeasurement.record_index`](#lestim.FlippedMeasurement.record_index)
- [`lestim.Flow`](#lestim.Flow)
    - [`lestim.Flow.__eq__`](#lestim.Flow.__eq__)
    - [`lestim.Flow.__init__`](#lestim.Flow.__init__)
    - [`lestim.Flow.__ne__`](#lestim.Flow.__ne__)
    - [`lestim.Flow.__repr__`](#lestim.Flow.__repr__)
    - [`lestim.Flow.__str__`](#lestim.Flow.__str__)
    - [`lestim.Flow.input_copy`](#lestim.Flow.input_copy)
    - [`lestim.Flow.measurements_copy`](#lestim.Flow.measurements_copy)
    - [`lestim.Flow.output_copy`](#lestim.Flow.output_copy)
- [`lestim.GateData`](#lestim.GateData)
    - [`lestim.GateData.__eq__`](#lestim.GateData.__eq__)
    - [`lestim.GateData.__init__`](#lestim.GateData.__init__)
    - [`lestim.GateData.__ne__`](#lestim.GateData.__ne__)
    - [`lestim.GateData.__repr__`](#lestim.GateData.__repr__)
    - [`lestim.GateData.__str__`](#lestim.GateData.__str__)
    - [`lestim.GateData.aliases`](#lestim.GateData.aliases)
    - [`lestim.GateData.flows`](#lestim.GateData.flows)
    - [`lestim.GateData.generalized_inverse`](#lestim.GateData.generalized_inverse)
    - [`lestim.GateData.inverse`](#lestim.GateData.inverse)
    - [`lestim.GateData.is_noisy_gate`](#lestim.GateData.is_noisy_gate)
    - [`lestim.GateData.is_reset`](#lestim.GateData.is_reset)
    - [`lestim.GateData.is_single_qubit_gate`](#lestim.GateData.is_single_qubit_gate)
    - [`lestim.GateData.is_two_qubit_gate`](#lestim.GateData.is_two_qubit_gate)
    - [`lestim.GateData.is_unitary`](#lestim.GateData.is_unitary)
    - [`lestim.GateData.name`](#lestim.GateData.name)
    - [`lestim.GateData.num_parens_arguments_range`](#lestim.GateData.num_parens_arguments_range)
    - [`lestim.GateData.produces_measurements`](#lestim.GateData.produces_measurements)
    - [`lestim.GateData.tableau`](#lestim.GateData.tableau)
    - [`lestim.GateData.takes_measurement_record_targets`](#lestim.GateData.takes_measurement_record_targets)
    - [`lestim.GateData.takes_pauli_targets`](#lestim.GateData.takes_pauli_targets)
    - [`lestim.GateData.unitary_matrix`](#lestim.GateData.unitary_matrix)
- [`lestim.GateTarget`](#lestim.GateTarget)
    - [`lestim.GateTarget.__eq__`](#lestim.GateTarget.__eq__)
    - [`lestim.GateTarget.__init__`](#lestim.GateTarget.__init__)
    - [`lestim.GateTarget.__ne__`](#lestim.GateTarget.__ne__)
    - [`lestim.GateTarget.__repr__`](#lestim.GateTarget.__repr__)
    - [`lestim.GateTarget.is_combiner`](#lestim.GateTarget.is_combiner)
    - [`lestim.GateTarget.is_inverted_result_target`](#lestim.GateTarget.is_inverted_result_target)
    - [`lestim.GateTarget.is_measurement_record_target`](#lestim.GateTarget.is_measurement_record_target)
    - [`lestim.GateTarget.is_qubit_target`](#lestim.GateTarget.is_qubit_target)
    - [`lestim.GateTarget.is_sweep_bit_target`](#lestim.GateTarget.is_sweep_bit_target)
    - [`lestim.GateTarget.is_x_target`](#lestim.GateTarget.is_x_target)
    - [`lestim.GateTarget.is_y_target`](#lestim.GateTarget.is_y_target)
    - [`lestim.GateTarget.is_z_target`](#lestim.GateTarget.is_z_target)
    - [`lestim.GateTarget.pauli_type`](#lestim.GateTarget.pauli_type)
    - [`lestim.GateTarget.qubit_value`](#lestim.GateTarget.qubit_value)
    - [`lestim.GateTarget.value`](#lestim.GateTarget.value)
- [`lestim.GateTargetWithCoords`](#lestim.GateTargetWithCoords)
    - [`lestim.GateTargetWithCoords.__init__`](#lestim.GateTargetWithCoords.__init__)
    - [`lestim.GateTargetWithCoords.coords`](#lestim.GateTargetWithCoords.coords)
    - [`lestim.GateTargetWithCoords.gate_target`](#lestim.GateTargetWithCoords.gate_target)
- [`lestim.PauliString`](#lestim.PauliString)
    - [`lestim.PauliString.__add__`](#lestim.PauliString.__add__)
    - [`lestim.PauliString.__eq__`](#lestim.PauliString.__eq__)
    - [`lestim.PauliString.__getitem__`](#lestim.PauliString.__getitem__)
    - [`lestim.PauliString.__iadd__`](#lestim.PauliString.__iadd__)
    - [`lestim.PauliString.__imul__`](#lestim.PauliString.__imul__)
    - [`lestim.PauliString.__init__`](#lestim.PauliString.__init__)
    - [`lestim.PauliString.__itruediv__`](#lestim.PauliString.__itruediv__)
    - [`lestim.PauliString.__len__`](#lestim.PauliString.__len__)
    - [`lestim.PauliString.__mul__`](#lestim.PauliString.__mul__)
    - [`lestim.PauliString.__ne__`](#lestim.PauliString.__ne__)
    - [`lestim.PauliString.__neg__`](#lestim.PauliString.__neg__)
    - [`lestim.PauliString.__pos__`](#lestim.PauliString.__pos__)
    - [`lestim.PauliString.__repr__`](#lestim.PauliString.__repr__)
    - [`lestim.PauliString.__rmul__`](#lestim.PauliString.__rmul__)
    - [`lestim.PauliString.__setitem__`](#lestim.PauliString.__setitem__)
    - [`lestim.PauliString.__str__`](#lestim.PauliString.__str__)
    - [`lestim.PauliString.__truediv__`](#lestim.PauliString.__truediv__)
    - [`lestim.PauliString.after`](#lestim.PauliString.after)
    - [`lestim.PauliString.before`](#lestim.PauliString.before)
    - [`lestim.PauliString.commutes`](#lestim.PauliString.commutes)
    - [`lestim.PauliString.copy`](#lestim.PauliString.copy)
    - [`lestim.PauliString.from_numpy`](#lestim.PauliString.from_numpy)
    - [`lestim.PauliString.from_unitary_matrix`](#lestim.PauliString.from_unitary_matrix)
    - [`lestim.PauliString.iter_all`](#lestim.PauliString.iter_all)
    - [`lestim.PauliString.pauli_indices`](#lestim.PauliString.pauli_indices)
    - [`lestim.PauliString.random`](#lestim.PauliString.random)
    - [`lestim.PauliString.sign`](#lestim.PauliString.sign)
    - [`lestim.PauliString.to_numpy`](#lestim.PauliString.to_numpy)
    - [`lestim.PauliString.to_tableau`](#lestim.PauliString.to_tableau)
    - [`lestim.PauliString.to_unitary_matrix`](#lestim.PauliString.to_unitary_matrix)
    - [`lestim.PauliString.weight`](#lestim.PauliString.weight)
- [`lestim.PauliStringIterator`](#lestim.PauliStringIterator)
    - [`lestim.PauliStringIterator.__iter__`](#lestim.PauliStringIterator.__iter__)
    - [`lestim.PauliStringIterator.__next__`](#lestim.PauliStringIterator.__next__)
- [`lestim.Tableau`](#lestim.Tableau)
    - [`lestim.Tableau.__add__`](#lestim.Tableau.__add__)
    - [`lestim.Tableau.__call__`](#lestim.Tableau.__call__)
    - [`lestim.Tableau.__eq__`](#lestim.Tableau.__eq__)
    - [`lestim.Tableau.__iadd__`](#lestim.Tableau.__iadd__)
    - [`lestim.Tableau.__init__`](#lestim.Tableau.__init__)
    - [`lestim.Tableau.__len__`](#lestim.Tableau.__len__)
    - [`lestim.Tableau.__mul__`](#lestim.Tableau.__mul__)
    - [`lestim.Tableau.__ne__`](#lestim.Tableau.__ne__)
    - [`lestim.Tableau.__pow__`](#lestim.Tableau.__pow__)
    - [`lestim.Tableau.__repr__`](#lestim.Tableau.__repr__)
    - [`lestim.Tableau.__str__`](#lestim.Tableau.__str__)
    - [`lestim.Tableau.append`](#lestim.Tableau.append)
    - [`lestim.Tableau.copy`](#lestim.Tableau.copy)
    - [`lestim.Tableau.from_circuit`](#lestim.Tableau.from_circuit)
    - [`lestim.Tableau.from_conjugated_generators`](#lestim.Tableau.from_conjugated_generators)
    - [`lestim.Tableau.from_named_gate`](#lestim.Tableau.from_named_gate)
    - [`lestim.Tableau.from_numpy`](#lestim.Tableau.from_numpy)
    - [`lestim.Tableau.from_stabilizers`](#lestim.Tableau.from_stabilizers)
    - [`lestim.Tableau.from_state_vector`](#lestim.Tableau.from_state_vector)
    - [`lestim.Tableau.from_unitary_matrix`](#lestim.Tableau.from_unitary_matrix)
    - [`lestim.Tableau.inverse`](#lestim.Tableau.inverse)
    - [`lestim.Tableau.inverse_x_output`](#lestim.Tableau.inverse_x_output)
    - [`lestim.Tableau.inverse_x_output_pauli`](#lestim.Tableau.inverse_x_output_pauli)
    - [`lestim.Tableau.inverse_y_output`](#lestim.Tableau.inverse_y_output)
    - [`lestim.Tableau.inverse_y_output_pauli`](#lestim.Tableau.inverse_y_output_pauli)
    - [`lestim.Tableau.inverse_z_output`](#lestim.Tableau.inverse_z_output)
    - [`lestim.Tableau.inverse_z_output_pauli`](#lestim.Tableau.inverse_z_output_pauli)
    - [`lestim.Tableau.iter_all`](#lestim.Tableau.iter_all)
    - [`lestim.Tableau.prepend`](#lestim.Tableau.prepend)
    - [`lestim.Tableau.random`](#lestim.Tableau.random)
    - [`lestim.Tableau.then`](#lestim.Tableau.then)
    - [`lestim.Tableau.to_circuit`](#lestim.Tableau.to_circuit)
    - [`lestim.Tableau.to_numpy`](#lestim.Tableau.to_numpy)
    - [`lestim.Tableau.to_pauli_string`](#lestim.Tableau.to_pauli_string)
    - [`lestim.Tableau.to_stabilizers`](#lestim.Tableau.to_stabilizers)
    - [`lestim.Tableau.to_state_vector`](#lestim.Tableau.to_state_vector)
    - [`lestim.Tableau.to_unitary_matrix`](#lestim.Tableau.to_unitary_matrix)
    - [`lestim.Tableau.x_output`](#lestim.Tableau.x_output)
    - [`lestim.Tableau.x_output_pauli`](#lestim.Tableau.x_output_pauli)
    - [`lestim.Tableau.x_sign`](#lestim.Tableau.x_sign)
    - [`lestim.Tableau.y_output`](#lestim.Tableau.y_output)
    - [`lestim.Tableau.y_output_pauli`](#lestim.Tableau.y_output_pauli)
    - [`lestim.Tableau.y_sign`](#lestim.Tableau.y_sign)
    - [`lestim.Tableau.z_output`](#lestim.Tableau.z_output)
    - [`lestim.Tableau.z_output_pauli`](#lestim.Tableau.z_output_pauli)
    - [`lestim.Tableau.z_sign`](#lestim.Tableau.z_sign)
- [`lestim.TableauIterator`](#lestim.TableauIterator)
    - [`lestim.TableauIterator.__iter__`](#lestim.TableauIterator.__iter__)
    - [`lestim.TableauIterator.__next__`](#lestim.TableauIterator.__next__)
- [`lestim.TableauSimulator`](#lestim.TableauSimulator)
    - [`lestim.TableauSimulator.__init__`](#lestim.TableauSimulator.__init__)
    - [`lestim.TableauSimulator.c_xyz`](#lestim.TableauSimulator.c_xyz)
    - [`lestim.TableauSimulator.c_zyx`](#lestim.TableauSimulator.c_zyx)
    - [`lestim.TableauSimulator.canonical_stabilizers`](#lestim.TableauSimulator.canonical_stabilizers)
    - [`lestim.TableauSimulator.cnot`](#lestim.TableauSimulator.cnot)
    - [`lestim.TableauSimulator.copy`](#lestim.TableauSimulator.copy)
    - [`lestim.TableauSimulator.current_inverse_tableau`](#lestim.TableauSimulator.current_inverse_tableau)
    - [`lestim.TableauSimulator.current_measurement_record`](#lestim.TableauSimulator.current_measurement_record)
    - [`lestim.TableauSimulator.cx`](#lestim.TableauSimulator.cx)
    - [`lestim.TableauSimulator.cy`](#lestim.TableauSimulator.cy)
    - [`lestim.TableauSimulator.cz`](#lestim.TableauSimulator.cz)
    - [`lestim.TableauSimulator.depolarize1`](#lestim.TableauSimulator.depolarize1)
    - [`lestim.TableauSimulator.depolarize2`](#lestim.TableauSimulator.depolarize2)
    - [`lestim.TableauSimulator.do`](#lestim.TableauSimulator.do)
    - [`lestim.TableauSimulator.do_circuit`](#lestim.TableauSimulator.do_circuit)
    - [`lestim.TableauSimulator.do_pauli_string`](#lestim.TableauSimulator.do_pauli_string)
    - [`lestim.TableauSimulator.do_tableau`](#lestim.TableauSimulator.do_tableau)
    - [`lestim.TableauSimulator.h`](#lestim.TableauSimulator.h)
    - [`lestim.TableauSimulator.h_xy`](#lestim.TableauSimulator.h_xy)
    - [`lestim.TableauSimulator.h_xz`](#lestim.TableauSimulator.h_xz)
    - [`lestim.TableauSimulator.h_yz`](#lestim.TableauSimulator.h_yz)
    - [`lestim.TableauSimulator.iswap`](#lestim.TableauSimulator.iswap)
    - [`lestim.TableauSimulator.iswap_dag`](#lestim.TableauSimulator.iswap_dag)
    - [`lestim.TableauSimulator.measure`](#lestim.TableauSimulator.measure)
    - [`lestim.TableauSimulator.measure_kickback`](#lestim.TableauSimulator.measure_kickback)
    - [`lestim.TableauSimulator.measure_many`](#lestim.TableauSimulator.measure_many)
    - [`lestim.TableauSimulator.measure_observable`](#lestim.TableauSimulator.measure_observable)
    - [`lestim.TableauSimulator.num_qubits`](#lestim.TableauSimulator.num_qubits)
    - [`lestim.TableauSimulator.peek_bloch`](#lestim.TableauSimulator.peek_bloch)
    - [`lestim.TableauSimulator.peek_observable_expectation`](#lestim.TableauSimulator.peek_observable_expectation)
    - [`lestim.TableauSimulator.peek_x`](#lestim.TableauSimulator.peek_x)
    - [`lestim.TableauSimulator.peek_y`](#lestim.TableauSimulator.peek_y)
    - [`lestim.TableauSimulator.peek_z`](#lestim.TableauSimulator.peek_z)
    - [`lestim.TableauSimulator.postselect_observable`](#lestim.TableauSimulator.postselect_observable)
    - [`lestim.TableauSimulator.postselect_x`](#lestim.TableauSimulator.postselect_x)
    - [`lestim.TableauSimulator.postselect_y`](#lestim.TableauSimulator.postselect_y)
    - [`lestim.TableauSimulator.postselect_z`](#lestim.TableauSimulator.postselect_z)
    - [`lestim.TableauSimulator.reset`](#lestim.TableauSimulator.reset)
    - [`lestim.TableauSimulator.reset_x`](#lestim.TableauSimulator.reset_x)
    - [`lestim.TableauSimulator.reset_y`](#lestim.TableauSimulator.reset_y)
    - [`lestim.TableauSimulator.reset_z`](#lestim.TableauSimulator.reset_z)
    - [`lestim.TableauSimulator.s`](#lestim.TableauSimulator.s)
    - [`lestim.TableauSimulator.s_dag`](#lestim.TableauSimulator.s_dag)
    - [`lestim.TableauSimulator.set_inverse_tableau`](#lestim.TableauSimulator.set_inverse_tableau)
    - [`lestim.TableauSimulator.set_num_qubits`](#lestim.TableauSimulator.set_num_qubits)
    - [`lestim.TableauSimulator.set_state_from_stabilizers`](#lestim.TableauSimulator.set_state_from_stabilizers)
    - [`lestim.TableauSimulator.set_state_from_state_vector`](#lestim.TableauSimulator.set_state_from_state_vector)
    - [`lestim.TableauSimulator.sqrt_x`](#lestim.TableauSimulator.sqrt_x)
    - [`lestim.TableauSimulator.sqrt_x_dag`](#lestim.TableauSimulator.sqrt_x_dag)
    - [`lestim.TableauSimulator.sqrt_y`](#lestim.TableauSimulator.sqrt_y)
    - [`lestim.TableauSimulator.sqrt_y_dag`](#lestim.TableauSimulator.sqrt_y_dag)
    - [`lestim.TableauSimulator.state_vector`](#lestim.TableauSimulator.state_vector)
    - [`lestim.TableauSimulator.swap`](#lestim.TableauSimulator.swap)
    - [`lestim.TableauSimulator.x`](#lestim.TableauSimulator.x)
    - [`lestim.TableauSimulator.x_error`](#lestim.TableauSimulator.x_error)
    - [`lestim.TableauSimulator.xcx`](#lestim.TableauSimulator.xcx)
    - [`lestim.TableauSimulator.xcy`](#lestim.TableauSimulator.xcy)
    - [`lestim.TableauSimulator.xcz`](#lestim.TableauSimulator.xcz)
    - [`lestim.TableauSimulator.y`](#lestim.TableauSimulator.y)
    - [`lestim.TableauSimulator.y_error`](#lestim.TableauSimulator.y_error)
    - [`lestim.TableauSimulator.ycx`](#lestim.TableauSimulator.ycx)
    - [`lestim.TableauSimulator.ycy`](#lestim.TableauSimulator.ycy)
    - [`lestim.TableauSimulator.ycz`](#lestim.TableauSimulator.ycz)
    - [`lestim.TableauSimulator.z`](#lestim.TableauSimulator.z)
    - [`lestim.TableauSimulator.z_error`](#lestim.TableauSimulator.z_error)
    - [`lestim.TableauSimulator.zcx`](#lestim.TableauSimulator.zcx)
    - [`lestim.TableauSimulator.zcy`](#lestim.TableauSimulator.zcy)
    - [`lestim.TableauSimulator.zcz`](#lestim.TableauSimulator.zcz)
- [`lestim.gate_data`](#lestim.gate_data)
- [`lestim.main`](#lestim.main)
- [`lestim.read_shot_data_file`](#lestim.read_shot_data_file)
- [`lestim.target_combined_paulis`](#lestim.target_combined_paulis)
- [`lestim.target_combiner`](#lestim.target_combiner)
- [`lestim.target_inv`](#lestim.target_inv)
- [`lestim.target_logical_observable_id`](#lestim.target_logical_observable_id)
- [`lestim.target_pauli`](#lestim.target_pauli)
- [`lestim.target_rec`](#lestim.target_rec)
- [`lestim.target_relative_detector_id`](#lestim.target_relative_detector_id)
- [`lestim.target_separator`](#lestim.target_separator)
- [`lestim.target_sweep_bit`](#lestim.target_sweep_bit)
- [`lestim.target_x`](#lestim.target_x)
- [`lestim.target_y`](#lestim.target_y)
- [`lestim.target_z`](#lestim.target_z)
- [`lestim.write_shot_data_file`](#lestim.write_shot_data_file)
```python
# Types used by the method definitions.
from typing import overload, TYPE_CHECKING, Any, Dict, Iterable, List, Optional, Tuple, Union
import io
import pathlib
import numpy as np
```

<a name="lestim.Circuit"></a>
```python
# lestim.Circuit

# (at top-level in the lestim module)
class Circuit:
    """A mutable stabilizer circuit.

    The lestim.Circuit class is arguably the most important object in the
    entire library. It is the interface through which you explain a
    noisy quantum computation to Stim, in order to do fast bulk sampling
    or fast error analysis.

    For example, suppose you want to use a matching-based decoder on a
    new quantum error correction construction. Stim can help you do this
    but the very first step is to create a circuit implementing the
    construction. Once you have the circuit you can then use methods like
    lestim.Circuit.detector_error_model() to create an object that can be
    used to configure the decoder, or like
    lestim.Circuit.compile_detector_sampler() to produce problems for the
    decoder to solve, or like lestim.Circuit.shortest_graphlike_error() to
    check for mistakes in the implementation of the code.

    Examples:
        >>> import lestim
        >>> c = lestim.Circuit()
        >>> c.append("X", 0)
        >>> c.append("M", 0)
        >>> c.compile_sampler().sample(shots=1)
        array([[ True]])

        >>> lestim.Circuit('''
        ...    H 0
        ...    CNOT 0 1
        ...    M 0 1
        ...    DETECTOR rec[-1] rec[-2]
        ... ''').compile_detector_sampler().sample(shots=1)
        array([[False]])
    """
```

<a name="lestim.Circuit.__add__"></a>
```python
# lestim.Circuit.__add__

# (in class lestim.Circuit)
def __add__(
    self,
    second: lestim._stim_polyfill.Circuit,
) -> lestim._stim_polyfill.Circuit:
    """Creates a circuit by appending two circuits.

    Examples:
        >>> import lestim
        >>> c1 = lestim.Circuit('''
        ...    X 0
        ...    Y 1 2
        ... ''')
        >>> c2 = lestim.Circuit('''
        ...    M 0 1 2
        ... ''')
        >>> c1 + c2
        lestim.Circuit('''
            X 0
            Y 1 2
            M 0 1 2
        ''')
    """
```

<a name="lestim.Circuit.__eq__"></a>
```python
# lestim.Circuit.__eq__

# (in class lestim.Circuit)
def __eq__(
    self,
    arg0: lestim._stim_polyfill.Circuit,
) -> bool:
    """Determines if two circuits have identical contents.
    """
```

<a name="lestim.Circuit.__getitem__"></a>
```python
# lestim.Circuit.__getitem__

# (in class lestim.Circuit)
@overload
def __getitem__(
    self,
    index_or_slice: int,
) -> Union[stim.CircuitInstruction, stim.CircuitRepeatBlock]:
    pass
@overload
def __getitem__(
    self,
    index_or_slice: slice,
) -> stim.Circuit:
    pass
def __getitem__(
    self,
    index_or_slice: object,
) -> object:
    """Returns copies of instructions from the circuit.

    Args:
        index_or_slice: An integer index picking out an instruction to return, or a
            slice picking out a range of instructions to return as a circuit.

    Returns:
        If the index was an integer, then an instruction from the circuit.
        If the index was a slice, then a circuit made up of the instructions in that
        slice.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit('''
        ...    X 0
        ...    X_ERROR(0.5) 2
        ...    REPEAT 100 {
        ...        X 0
        ...        Y 1 2
        ...    }
        ...    TICK
        ...    M 0
        ...    DETECTOR rec[-1]
        ... ''')
        >>> circuit[1]
        lestim.CircuitInstruction('X_ERROR', [lestim.GateTarget(2)], [0.5])
        >>> circuit[2]
        lestim.CircuitRepeatBlock(100, lestim.Circuit('''
            X 0
            Y 1 2
        '''))
        >>> circuit[1::2]
        lestim.Circuit('''
            X_ERROR(0.5) 2
            TICK
            DETECTOR rec[-1]
        ''')
    """
```

<a name="lestim.Circuit.__iadd__"></a>
```python
# lestim.Circuit.__iadd__

# (in class lestim.Circuit)
def __iadd__(
    self,
    second: lestim._stim_polyfill.Circuit,
) -> lestim._stim_polyfill.Circuit:
    """Appends a circuit into the receiving circuit (mutating it).

    Examples:
        >>> import lestim
        >>> c1 = lestim.Circuit('''
        ...    X 0
        ...    Y 1 2
        ... ''')
        >>> c2 = lestim.Circuit('''
        ...    M 0 1 2
        ... ''')
        >>> c1 += c2
        >>> print(repr(c1))
        lestim.Circuit('''
            X 0
            Y 1 2
            M 0 1 2
        ''')
    """
```

<a name="lestim.Circuit.__imul__"></a>
```python
# lestim.Circuit.__imul__

# (in class lestim.Circuit)
def __imul__(
    self,
    repetitions: int,
) -> lestim._stim_polyfill.Circuit:
    """Mutates the circuit by putting its contents into a REPEAT block.

    Special case: if the repetition count is 0, the circuit is cleared.
    Special case: if the repetition count is 1, nothing happens.

    Args:
        repetitions: The number of times the REPEAT block should repeat.

    Examples:
        >>> import lestim
        >>> c = lestim.Circuit('''
        ...    X 0
        ...    Y 1 2
        ... ''')
        >>> c *= 3
        >>> print(repr(c))
        lestim.Circuit('''
            REPEAT 3 {
                X 0
                Y 1 2
            }
        ''')
    """
```

<a name="lestim.Circuit.__init__"></a>
```python
# lestim.Circuit.__init__

# (in class lestim.Circuit)
def __init__(
    self,
    stim_program_text: str = '',
) -> None:
    """Creates a lestim.Circuit.

    Args:
        lestim_program_text: Defaults to empty. Describes operations to append into
            the circuit.

    Examples:
        >>> import lestim
        >>> empty = lestim.Circuit()
        >>> not_empty = lestim.Circuit('''
        ...    X 0
        ...    CNOT 0 1
        ...    M 1
        ... ''')
    """
```

<a name="lestim.Circuit.__len__"></a>
```python
# lestim.Circuit.__len__

# (in class lestim.Circuit)
def __len__(
    self,
) -> int:
    """Returns the number of top-level instructions and blocks in the circuit.

    Instructions inside of blocks are not included in this count.

    Examples:
        >>> import lestim
        >>> len(lestim.Circuit())
        0
        >>> len(lestim.Circuit('''
        ...    X 0
        ...    X_ERROR(0.5) 1 2
        ...    TICK
        ...    M 0
        ...    DETECTOR rec[-1]
        ... '''))
        5
        >>> len(lestim.Circuit('''
        ...    REPEAT 100 {
        ...        X 0
        ...        Y 1 2
        ...    }
        ... '''))
        1
    """
```

<a name="lestim.Circuit.__mul__"></a>
```python
# lestim.Circuit.__mul__

# (in class lestim.Circuit)
def __mul__(
    self,
    repetitions: int,
) -> lestim._stim_polyfill.Circuit:
    """Repeats the circuit using a REPEAT block.

    Has special cases for 0 repetitions and 1 repetitions.

    Args:
        repetitions: The number of times the REPEAT block should repeat.

    Returns:
        repetitions=0: An empty circuit.
        repetitions=1: A copy of this circuit.
        repetitions>=2: A circuit with a single REPEAT block, where the contents of
            that repeat block are this circuit.

    Examples:
        >>> import lestim
        >>> c = lestim.Circuit('''
        ...    X 0
        ...    Y 1 2
        ... ''')
        >>> c * 3
        lestim.Circuit('''
            REPEAT 3 {
                X 0
                Y 1 2
            }
        ''')
    """
```

<a name="lestim.Circuit.__ne__"></a>
```python
# lestim.Circuit.__ne__

# (in class lestim.Circuit)
def __ne__(
    self,
    arg0: lestim._stim_polyfill.Circuit,
) -> bool:
    """Determines if two circuits have non-identical contents.
    """
```

<a name="lestim.Circuit.__repr__"></a>
```python
# lestim.Circuit.__repr__

# (in class lestim.Circuit)
def __repr__(
    self,
) -> str:
    """Returns text that is a valid python expression evaluating to an equivalent `lestim.Circuit`.
    """
```

<a name="lestim.Circuit.__rmul__"></a>
```python
# lestim.Circuit.__rmul__

# (in class lestim.Circuit)
def __rmul__(
    self,
    repetitions: int,
) -> lestim._stim_polyfill.Circuit:
    """Repeats the circuit using a REPEAT block.

    Has special cases for 0 repetitions and 1 repetitions.

    Args:
        repetitions: The number of times the REPEAT block should repeat.

    Returns:
        repetitions=0: An empty circuit.
        repetitions=1: A copy of this circuit.
        repetitions>=2: A circuit with a single REPEAT block, where the contents of
            that repeat block are this circuit.

    Examples:
        >>> import lestim
        >>> c = lestim.Circuit('''
        ...    X 0
        ...    Y 1 2
        ... ''')
        >>> 3 * c
        lestim.Circuit('''
            REPEAT 3 {
                X 0
                Y 1 2
            }
        ''')
    """
```

<a name="lestim.Circuit.__str__"></a>
```python
# lestim.Circuit.__str__

# (in class lestim.Circuit)
def __str__(
    self,
) -> str:
    """Returns lestim instructions (that can be saved to a file and parsed by lestim) for the current circuit.
    """
```

<a name="lestim.Circuit.append"></a>
```python
# lestim.Circuit.append

# (in class lestim.Circuit)
@overload
def append(
    self,
    name: str,
    targets: Union[int, stim.GateTarget, Iterable[Union[int, stim.GateTarget]]],
    arg: Union[float, Iterable[float]],
) -> None:
    pass
@overload
def append(
    self,
    name: Union[stim.CircuitOperation, stim.CircuitRepeatBlock],
) -> None:
    pass
def append(
    self,
    name: object,
    targets: object = (),
    arg: object = None,
) -> None:
    """Appends an operation into the circuit.

    Note: `lestim.Circuit.append_operation` is an alias of `lestim.Circuit.append`.

    Examples:
        >>> import lestim
        >>> c = lestim.Circuit()
        >>> c.append("X", 0)
        >>> c.append("H", [0, 1])
        >>> c.append("M", [0, lestim.target_inv(1)])
        >>> c.append("CNOT", [lestim.target_rec(-1), 0])
        >>> c.append("X_ERROR", [0], 0.125)
        >>> c.append("CORRELATED_ERROR", [lestim.target_x(0), lestim.target_y(2)], 0.25)
        >>> print(repr(c))
        lestim.Circuit('''
            X 0
            H 0 1
            M 0 !1
            CX rec[-1] 0
            X_ERROR(0.125) 0
            E(0.25) X0 Y2
        ''')

    Args:
        name: The name of the operation's gate (e.g. "H" or "M" or "CNOT").

            This argument can also be set to a `lestim.CircuitInstruction` or
            `lestim.CircuitInstructionBlock`, which results in the instruction or
            block being appended to the circuit. The other arguments (targets
            and arg) can't be specified when doing so.

            (The argument being called `name` is no longer quite right, but
            is being kept for backwards compatibility.)
        targets: The objects operated on by the gate. This can be either a
            single target or an iterable of multiple targets to broadcast the
            gate over. Each target can be an integer (a qubit), a
            lestim.GateTarget, or a special target from one of the `lestim.target_*`
            methods (such as a measurement record target like `rec[-1]` from
            `lestim.target_rec(-1)`).
        arg: The "parens arguments" for the gate, such as the probability for a
            noise operation. A double or list of doubles parameterizing the
            gate. Different gates take different parens arguments. For example,
            X_ERROR takes a probability, OBSERVABLE_INCLUDE takes an observable
            index, and PAULI_CHANNEL_1 takes three disjoint probabilities.

            Note: Defaults to no parens arguments. Except, for backwards
            compatibility reasons, `cirq.append_operation` (but not
            `cirq.append`) will default to a single 0.0 argument for gates that
            take exactly one argument.
    """
```

<a name="lestim.Circuit.append_from_stim_program_text"></a>
```python
# lestim.Circuit.append_from_stim_program_text

# (in class lestim.Circuit)
def append_from_stim_program_text(
    self,
    stim_program_text: str,
) -> None:
    """Appends operations described by a STIM format program into the circuit.

    Examples:
        >>> import lestim
        >>> c = lestim.Circuit()
        >>> c.append_from_lestim_program_text('''
        ...    H 0  # comment
        ...    CNOT 0 2
        ...
        ...    M 2
        ...    CNOT rec[-1] 1
        ... ''')
        >>> print(c)
        H 0
        CX 0 2
        M 2
        CX rec[-1] 1

    Args:
        lestim_program_text: The STIM program text containing the circuit operations
            to append.
    """
```

<a name="lestim.Circuit.approx_equals"></a>
```python
# lestim.Circuit.approx_equals

# (in class lestim.Circuit)
def approx_equals(
    self,
    other: object,
    *,
    atol: float,
) -> bool:
    """Checks if a circuit is approximately equal to another circuit.

    Two circuits are approximately equal if they are equal up to slight
    perturbations of instruction arguments such as probabilities. For example,
    `X_ERROR(0.100) 0` is approximately equal to `X_ERROR(0.099)` within an absolute
    tolerance of 0.002. All other details of the circuits (such as the ordering of
    instructions and targets) must be exactly the same.

    Args:
        other: The circuit, or other object, to compare to this one.
        atol: The absolute error tolerance. The maximum amount each probability may
            have been perturbed by.

    Returns:
        True if the given object is a circuit approximately equal up to the
        receiving circuit up to the given tolerance, otherwise False.

    Examples:
        >>> import lestim
        >>> base = lestim.Circuit('''
        ...    X_ERROR(0.099) 0 1 2
        ...    M 0 1 2
        ... ''')

        >>> base.approx_equals(base, atol=0)
        True

        >>> base.approx_equals(lestim.Circuit('''
        ...    X_ERROR(0.101) 0 1 2
        ...    M 0 1 2
        ... '''), atol=0)
        False

        >>> base.approx_equals(lestim.Circuit('''
        ...    X_ERROR(0.101) 0 1 2
        ...    M 0 1 2
        ... '''), atol=0.0001)
        False

        >>> base.approx_equals(lestim.Circuit('''
        ...    X_ERROR(0.101) 0 1 2
        ...    M 0 1 2
        ... '''), atol=0.01)
        True

        >>> base.approx_equals(lestim.Circuit('''
        ...    DEPOLARIZE1(0.099) 0 1 2
        ...    MRX 0 1 2
        ... '''), atol=9999)
        False
    """
```

<a name="lestim.Circuit.clear"></a>
```python
# lestim.Circuit.clear

# (in class lestim.Circuit)
def clear(
    self,
) -> None:
    """Clears the contents of the circuit.

    Examples:
        >>> import lestim
        >>> c = lestim.Circuit('''
        ...    X 0
        ...    Y 1 2
        ... ''')
        >>> c.clear()
        >>> c
        lestim.Circuit()
    """
```

<a name="lestim.Circuit.compile_detector_sampler"></a>
```python
# lestim.Circuit.compile_detector_sampler

# (in class lestim.Circuit)
def compile_detector_sampler(
    self,
    *,
    seed: object = None,
) -> lestim._stim_polyfill.CompiledDetectorSampler:
    """Returns an object that can batch sample detection events from the circuit.

    Args:
        seed: PARTIALLY determines simulation results by deterministically seeding
            the random number generator.

            Must be None or an integer in range(2**64).

            Defaults to None. When None, the prng is seeded from system entropy.

            When set to an integer, making the exact same series calls on the exact
            same machine with the exact same version of Stim will produce the exact
            same simulation results.

            CAUTION: simulation results *WILL NOT* be consistent between versions of
            Stim. This restriction is present to make it possible to have future
            optimizations to the random sampling, and is enforced by introducing
            intentional differences in the seeding strategy from version to version.

            CAUTION: simulation results *MAY NOT* be consistent across machines that
            differ in the width of supported SIMD instructions. For example, using
            the same seed on a machine that supports AVX instructions and one that
            only supports SSE instructions may produce different simulation results.

            CAUTION: simulation results *MAY NOT* be consistent if you vary how many
            shots are taken. For example, taking 10 shots and then 90 shots will
            give different results from taking 100 shots in one call.

    Examples:
        >>> import lestim
        >>> c = lestim.Circuit('''
        ...    H 0
        ...    CNOT 0 1
        ...    M 0 1
        ...    DETECTOR rec[-1] rec[-2]
        ... ''')
        >>> s = c.compile_detector_sampler()
        >>> s.sample(shots=1)
        array([[False]])
    """
```

<a name="lestim.Circuit.compile_m2d_converter"></a>
```python
# lestim.Circuit.compile_m2d_converter

# (in class lestim.Circuit)
def compile_m2d_converter(
    self,
    *,
    skip_reference_sample: bool = False,
) -> lestim._stim_polyfill.CompiledMeasurementsToDetectionEventsConverter:
    """Creates a measurement-to-detection-event converter for the given circuit.

    The converter uses a noiseless reference sample, collected from the circuit
    using lestim's Tableau simulator during initialization of the converter, as a
    baseline for determining what the expected value of a detector is.

    Note that the expected behavior of gauge detectors (detectors that are not
    actually deterministic under noiseless execution) can vary depending on the
    reference sample. Stim mitigates this by always generating the same reference
    sample for a given circuit.

    Args:
        skip_reference_sample: Defaults to False. When set to True, the reference
            sample used by the converter is initialized to all-zeroes instead of
            being collected from the circuit. This should only be used if it's known
            that the all-zeroes sample is actually a possible result from the
            circuit (under noiseless execution).

    Returns:
        An initialized lestim.CompiledMeasurementsToDetectionEventsConverter.

    Examples:
        >>> import lestim
        >>> import numpy as np
        >>> converter = lestim.Circuit('''
        ...    X 0
        ...    M 0
        ...    DETECTOR rec[-1]
        ... ''').compile_m2d_converter()
        >>> converter.convert(
        ...     measurements=np.array([[0], [1]], dtype=np.bool_),
        ...     append_observables=False,
        ... )
        array([[ True],
               [False]])
    """
```

<a name="lestim.Circuit.compile_sampler"></a>
```python
# lestim.Circuit.compile_sampler

# (in class lestim.Circuit)
def compile_sampler(
    self,
    *,
    skip_reference_sample: bool = False,
    seed: Optional[int] = None,
    reference_sample: Optional[np.ndarray] = None,
) -> stim.CompiledMeasurementSampler:
    """Returns an object that can quickly batch sample measurements from the circuit.

    Args:
        skip_reference_sample: Defaults to False. When set to True, the reference
            sample used by the sampler is initialized to all-zeroes instead of being
            collected from the circuit. This means that the results returned by the
            sampler are actually whether or not each measurement was *flipped*,
            instead of true measurement results.

            Forcing an all-zero reference sample is useful when you are only
            interested in error propagation and don't want to have to deal with the
            fact that some measurements want to be On when no errors occur. It is
            also useful when you know for sure that the all-zero result is actually
            a possible result from the circuit (under noiseless execution), meaning
            it is a valid reference sample as good as any other. Computing the
            reference sample is the most time consuming and memory intensive part of
            simulating the circuit, so promising that the simulator can safely skip
            that step is an effective optimization.
        seed: PARTIALLY determines simulation results by deterministically seeding
            the random number generator.

            Must be None or an integer in range(2**64).

            Defaults to None. When None, the prng is seeded from system entropy.

            When set to an integer, making the exact same series calls on the exact
            same machine with the exact same version of Stim will produce the exact
            same simulation results.

            CAUTION: simulation results *WILL NOT* be consistent between versions of
            Stim. This restriction is present to make it possible to have future
            optimizations to the random sampling, and is enforced by introducing
            intentional differences in the seeding strategy from version to version.

            CAUTION: simulation results *MAY NOT* be consistent across machines that
            differ in the width of supported SIMD instructions. For example, using
            the same seed on a machine that supports AVX instructions and one that
            only supports SSE instructions may produce different simulation results.

            CAUTION: simulation results *MAY NOT* be consistent if you vary how many
            shots are taken. For example, taking 10 shots and then 90 shots will
            give different results from taking 100 shots in one call.
        reference_sample: The data to xor into the measurement flips produced by the
            frame simulator, in order to produce proper measurement results.
            This can either be specified as an `np.bool_` array or a bit packed
            `np.uint8` array (little endian). Under normal conditions, the reference
            sample should be a valid noiseless sample of the circuit, such as the
            one returned by `circuit.reference_sample()`. If this argument is not
            provided, the reference sample will be set to
            `circuit.reference_sample()`, unless `skip_reference_sample=True`
            is used, in which case it will be set to all-zeros.

    Raises:
        ValueError: skip_reference_sample is True and reference_sample is not None.

    Examples:
        >>> import lestim
        >>> c = lestim.Circuit('''
        ...    X 2
        ...    M 0 1 2
        ... ''')
        >>> s = c.compile_sampler()
        >>> s.sample(shots=1)
        array([[False, False,  True]])
    """
```

<a name="lestim.Circuit.copy"></a>
```python
# lestim.Circuit.copy

# (in class lestim.Circuit)
def copy(
    self,
) -> lestim._stim_polyfill.Circuit:
    """Returns a copy of the circuit. An independent circuit with the same contents.

    Examples:
        >>> import lestim

        >>> c1 = lestim.Circuit("H 0")
        >>> c2 = c1.copy()
        >>> c2 is c1
        False
        >>> c2 == c1
        True
    """
```

<a name="lestim.Circuit.count_determined_measurements"></a>
```python
# lestim.Circuit.count_determined_measurements

# (in class lestim.Circuit)
def count_determined_measurements(
    self,
) -> int:
    """Counts the number of predictable measurements in the circuit.

    This method ignores any noise in the circuit.

    This method works by performing a tableau stabilizer simulation of the circuit
    and, before each measurement is simulated, checking if its expectation is
    non-zero.

    A measurement is predictable if its result can be predicted by using other
    measurements that have already been performed, assuming the circuit is executed
    without any noise.

    Note that, when multiple measurements occur at the same time, re-ordering the
    order they are resolved can change which specific measurements are predictable
    but won't change how many of them were predictable in total.

    The number of predictable measurements is a useful quantity because it's
    related to the number of detectors and observables that a circuit should
    declare. If circuit.num_detectors + circuit.num_observables is less than
    circuit.count_determined_measurements(), this is a warning sign that you've
    missed some detector declarations.

    The exact relationship between the number of determined measurements and the
    number of detectors and observables can differ from code to code. For example,
    the toric code has an extra redundant measurement compared to the surface code
    because in the toric code the last X stabilizer to be measured is equal to the
    product of all other X stabilizers even in the first round when initializing in
    the Z basis. Typically this relationship is not declared as a detector, because
    it's not local, or as an observable, because it doesn't store a qubit.

    Returns:
        The number of measurements that were predictable.

    Examples:
        >>> import lestim

        >>> lestim.Circuit('''
        ...     R 0
        ...     M 0
        ... ''').count_determined_measurements()
        1

        >>> lestim.Circuit('''
        ...     R 0
        ...     H 0
        ...     M 0
        ... ''').count_determined_measurements()
        0

        >>> lestim.Circuit('''
        ...     R 0 1
        ...     MZZ 0 1
        ...     MYY 0 1
        ...     MXX 0 1
        ... ''').count_determined_measurements()
        2

        >>> circuit = lestim.Circuit.generated(
        ...     "surface_code:rotated_memory_x",
        ...     distance=5,
        ...     rounds=9,
        ... )
        >>> circuit.count_determined_measurements()
        217
        >>> circuit.num_detectors + circuit.num_observables
        217
    """
```

<a name="lestim.Circuit.decomposed"></a>
```python
# lestim.Circuit.decomposed

# (in class lestim.Circuit)
def decomposed(
    self,
) -> lestim._stim_polyfill.Circuit:
    """Recreates the circuit using (mostly) the {H,S,CX,M,R} gate set.

    The intent of this method is to simplify the circuit to use fewer gate types,
    so it's easier for other tools to consume. Currently, this method performs the
    following simplifications:

    - Single qubit cliffords are decomposed into {H,S}.
    - Multi-qubit cliffords are decomposed into {H,S,CX}.
    - Single qubit dissipative gates are decomposed into {H,S,M,R}.
    - Multi-qubit dissipative gates are decomposed into {H,S,CX,M,R}.

    Currently, the following types of gate *aren't* simplified, but they may be
    in the future:

    - Noise instructions (like X_ERROR, DEPOLARIZE2, and E).
    - Annotations (like TICK, DETECTOR, and SHIFT_COORDS).
    - The MPAD instruction.
    - Repeat blocks are not flattened.

    Returns:
        A `lestim.Circuit` whose function is equivalent to the original circuit,
        but with most gates decomposed into the {H,S,CX,M,R} gate set.

    Examples:
        >>> import lestim

        >>> lestim.Circuit('''
        ...     SWAP 0 1
        ... ''').decomposed()
        lestim.Circuit('''
            CX 0 1 1 0 0 1
        ''')

        >>> lestim.Circuit('''
        ...     ISWAP 0 1 2 1
        ...     TICK
        ...     MPP !X1*Y2*Z3
        ... ''').decomposed()
        lestim.Circuit('''
            H 0
            CX 0 1 1 0
            H 1
            S 1 0
            H 2
            CX 2 1 1 2
            H 1
            S 1 2
            TICK
            H 1 2
            S 2
            H 2
            S 2 2
            CX 2 1 3 1
            M !1
            CX 2 1 3 1
            H 2
            S 2
            H 2
            S 2 2
            H 1
        ''')
    """
```

<a name="lestim.Circuit.detecting_regions"></a>
```python
# lestim.Circuit.detecting_regions

# (in class lestim.Circuit)
def detecting_regions(
    self,
    *,
    targets: Optional[Iterable[stim.DemTarget | str | Iterable[float]]] = None,
    ticks: Optional[Iterable[int]] = None,
) -> Dict[stim.DemTarget, Dict[int, stim.PauliString]]:
    """Records where detectors and observables are sensitive to errors over time.

    The result of this method is a nested dictionary, mapping detectors/observables
    and ticks to Pauli sensitivities for that detector/observable at that time.

    For example, if observable 2 has Z-type sensitivity on qubits 5 and 6 during
    tick 3, then `result[lestim.target_logical_observable_id(2)][3]` will be equal to
    `lestim.PauliString("Z5*Z6")`.

    If you want sensitivities from more places in the circuit, besides just at the
    TICK instructions, you can work around this by making a version of the circuit
    with more TICKs.

    Args:
        targets: Defaults to everything (None).

            When specified, this should be an iterable of filters where items
            matching any one filter are included.

            A variety of filters are supported:
                lestim.DemTarget: Includes the targeted detector or observable.
                Iterable[float]: Coordinate prefix match. Includes detectors whose
                    coordinate data begins with the same floats.
                "D": Includes all detectors.
                "L": Includes all observables.
                "D#" (e.g. "D5"): Includes the detector with the specified index.
                "L#" (e.g. "L5"): Includes the observable with the specified index.

        ticks: Defaults to everything (None).
            When specified, this should be a list of integers corresponding to
            the tick indices to report sensitivities for.

        ignore_anticommutation_errors: Defaults to False.
            When set to False, invalid detecting regions that anticommute with a
            reset will cause the method to raise an exception. When set to True,
            the offending component will simply be silently dropped. This can
            result in broken detectors having apparently enormous detecting
            regions.

    Returns:
        Nested dictionaries keyed first by a `lestim.DemTarget` identifying the
        detector or observable, then by the index of the tick, leading to a
        PauliString with that target's error sensitivity at that tick.

        Note you can use `lestim.PauliString.pauli_indices` to quickly get to the
        non-identity terms in the sensitivity.

    Examples:
        >>> import lestim

        >>> detecting_regions = lestim.Circuit('''
        ...     R 0
        ...     TICK
        ...     H 0
        ...     TICK
        ...     CX 0 1
        ...     TICK
        ...     MX 0 1
        ...     DETECTOR rec[-1] rec[-2]
        ... ''').detecting_regions()
        >>> for target, tick_regions in detecting_regions.items():
        ...     print("target", target)
        ...     for tick, sensitivity in tick_regions.items():
        ...         print("    tick", tick, "=", sensitivity)
        target D0
            tick 0 = +Z_
            tick 1 = +X_
            tick 2 = +XX

        >>> circuit = lestim.Circuit.generated(
        ...     "surface_code:rotated_memory_x",
        ...     rounds=5,
        ...     distance=4,
        ... )

        >>> detecting_regions = circuit.detecting_regions(
        ...     targets=["L0", (2, 4), lestim.DemTarget.relative_detector_id(5)],
        ...     ticks=range(5, 15),
        ... )
        >>> for target, tick_regions in detecting_regions.items():
        ...     print("target", target)
        ...     for tick, sensitivity in tick_regions.items():
        ...         print("    tick", tick, "=", sensitivity)
        target D1
            tick 5 = +____________________X______________________
            tick 6 = +____________________Z______________________
        target D5
            tick 5 = +______X____________________________________
            tick 6 = +______Z____________________________________
        target D14
            tick 5 = +__________X_X______XXX_____________________
            tick 6 = +__________X_X______XZX_____________________
            tick 7 = +__________X_X______XZX_____________________
            tick 8 = +__________X_X______XXX_____________________
            tick 9 = +__________XXX_____XXX______________________
            tick 10 = +__________XXX_______X______________________
            tick 11 = +__________X_________X______________________
            tick 12 = +____________________X______________________
            tick 13 = +____________________Z______________________
        target D29
            tick 7 = +____________________Z______________________
            tick 8 = +____________________X______________________
            tick 9 = +____________________XX_____________________
            tick 10 = +___________________XXX_______X_____________
            tick 11 = +____________X______XXXX______X_____________
            tick 12 = +__________X_X______XXX_____________________
            tick 13 = +__________X_X______XZX_____________________
            tick 14 = +__________X_X______XZX_____________________
        target D44
            tick 14 = +____________________Z______________________
        target L0
            tick 5 = +_X________X________X________X______________
            tick 6 = +_X________X________X________X______________
            tick 7 = +_X________X________X________X______________
            tick 8 = +_X________X________X________X______________
            tick 9 = +_X________X_______XX________X______________
            tick 10 = +_X________X________X________X______________
            tick 11 = +_X________XX_______X________XX_____________
            tick 12 = +_X________X________X________X______________
            tick 13 = +_X________X________X________X______________
            tick 14 = +_X________X________X________X______________
    """
```

<a name="lestim.Circuit.detector_error_model"></a>
```python
# lestim.Circuit.detector_error_model

# (in class lestim.Circuit)
def detector_error_model(
    self,
    *,
    decompose_errors: bool = False,
    flatten_loops: bool = False,
    allow_gauge_detectors: bool = False,
    approximate_disjoint_errors: float = False,
    ignore_decomposition_failures: bool = False,
    block_decomposition_from_introducing_remnant_edges: bool = False,
) -> lestim._stim_polyfill.DetectorErrorModel:
    """Returns a lestim.DetectorErrorModel describing the error processes in the circuit.

    Args:
        decompose_errors: Defaults to false. When set to true, the error analysis
            attempts to decompose the components of composite error mechanisms (such
            as depolarization errors) into simpler errors, and suggest this
            decomposition via `lestim.target_separator()` between the components. For
            example, in an XZ surface code, single qubit depolarization has a Y
            error term which can be decomposed into simpler X and Z error terms.
            Decomposition fails (causing this method to throw) if it's not possible
            to decompose large errors into simple errors that affect at most two
            detectors.
        flatten_loops: Defaults to false. When set to True, the output will not
            contain any `repeat` blocks. When set to False, the error analysis
            watches for loops in the circuit reaching a periodic steady state with
            respect to the detectors being introduced, the error mechanisms that
            affect them, and the locations of the logical observables. When it
            identifies such a steady state, it outputs a repeat block. This is
            massively more efficient than flattening for circuits that contain
            loops, but creates a more complex output.
        allow_gauge_detectors: Defaults to false. When set to false, the error
            analysis verifies that detectors in the circuit are actually
            deterministic under noiseless execution of the circuit. When set to
            True, these detectors are instead considered to be part of degrees
            freedom that can be removed from the error model. For example, if
            detectors D1 and D3 both anti-commute with a reset, then the error model
            has a gauge `error(0.5) D1 D3`. When gauges are identified, one of the
            involved detectors is removed from the system using Gaussian
            elimination.

            Note that logical observables are still verified to be deterministic,
            even if this option is set.
        approximate_disjoint_errors: Defaults to false. When set to false, composite
            error mechanisms with disjoint components (such as
            `PAULI_CHANNEL_1(0.1, 0.2, 0.0)`) can cause the error analysis to throw
            exceptions (because detector error models can only contain independent
            error mechanisms). When set to true, the probabilities of the disjoint
            cases are instead assumed to be independent probabilities. For example,
            a `PAULI_CHANNEL_1(0.1, 0.2, 0.0)` becomes equivalent to an
            `X_ERROR(0.1)` followed by a `Y_ERROR(0.2)`. This assumption is an
            approximation, but it is a good approximation for small probabilities.

            This argument can also be set to a probability between 0 and 1, setting
            a threshold below which the approximation is acceptable. Any error
            mechanisms that have a component probability above the threshold will
            cause an exception to be thrown.
        ignore_decomposition_failures: Defaults to False.
            When this is set to True, circuit errors that fail to decompose into
            graphlike detector error model errors no longer cause the conversion
            process to abort. Instead, the undecomposed error is inserted into the
            output. Whatever tool the detector error model is then given to is
            responsible for dealing with the undecomposed errors (e.g. a tool may
            choose to simply ignore them).

            Irrelevant unless decompose_errors=True.
        block_decomposition_from_introducing_remnant_edges: Defaults to False.
            Requires that both A B and C D be present elsewhere in the detector
            error model in order to decompose A B C D into A B ^ C D. Normally, only
            one of A B or C D needs to appear to allow this decomposition.

            Remnant edges can be a useful feature for ensuring decomposition
            succeeds, but they can also reduce the effective code distance by giving
            the decoder single edges that actually represent multiple errors in the
            circuit (resulting in the decoder making misinformed choices when
            decoding).

            Irrelevant unless decompose_errors=True.

    Examples:
        >>> import lestim

        >>> lestim.Circuit('''
        ...     X_ERROR(0.125) 0
        ...     X_ERROR(0.25) 1
        ...     CORRELATED_ERROR(0.375) X0 X1
        ...     M 0 1
        ...     DETECTOR rec[-2]
        ...     DETECTOR rec[-1]
        ... ''').detector_error_model()
        lestim.DetectorErrorModel('''
            error(0.125) D0
            error(0.375) D0 D1
            error(0.25) D1
        ''')
    """
```

<a name="lestim.Circuit.diagram"></a>
```python
# lestim.Circuit.diagram

# (in class lestim.Circuit)
def diagram(
    self,
    type: str = 'timeline-text',
    *,
    tick: Union[None, int, range] = None,
    filter_coords: Iterable[Union[Iterable[float], stim.DemTarget]] = ((),),
) -> 'stim._DiagramHelper':
    """Returns a diagram of the circuit, from a variety of options.

    Args:
        type: The type of diagram. Available types are:
            "timeline-text" (default): An ASCII diagram of the
                operations applied by the circuit over time. Includes
                annotations showing the measurement record index that
                each measurement writes to, and the measurements used
                by detectors.
            "timeline-svg": An SVG image of the operations applied by
                the circuit over time. Includes annotations showing the
                measurement record index that each measurement writes
                to, and the measurements used by detectors.
            "timeline-svg-html": A resizable SVG image viewer of the
                operations applied by the circuit over time. Includes
                annotations showing the measurement record index that
                each measurement writes to, and the measurements used
                by detectors.
            "timeline-3d": A 3d model, in GLTF format, of the operations
                applied by the circuit over time.
            "timeline-3d-html": Same 3d model as 'timeline-3d' but
                embedded into an HTML web page containing an interactive
                THREE.js viewer for the 3d model.
            "detslice-text": An ASCII diagram of the stabilizers
                that detectors declared by the circuit correspond to
                during the TICK instruction identified by the `tick`
                argument.
            "detslice-svg": An SVG image of the stabilizers
                that detectors declared by the circuit correspond to
                during the TICK instruction identified by the `tick`
                argument. For example, a detector slice diagram of a
                CSS surface code circuit during the TICK between a
                measurement layer and a reset layer will produce the
                usual diagram of a surface code.

                Uses the Pauli color convention XYZ=RGB.
            "detslice-svg-html": Same as detslice-svg but the SVG image
                is inside a resizable HTML iframe.
            "matchgraph-svg": An SVG image of the match graph extracted
                from the circuit by lestim.Circuit.detector_error_model.
            "matchgraph-svg-html": Same as matchgraph-svg but the SVG image
                is inside a resizable HTML iframe.
            "matchgraph-3d": An 3D model of the match graph extracted
                from the circuit by lestim.Circuit.detector_error_model.
            "matchgraph-3d-html": Same 3d model as 'match-graph-3d' but
                embedded into an HTML web page containing an interactive
                THREE.js viewer for the 3d model.
            "timeslice-svg": An SVG image of the operations applied
                between two TICK instructions in the circuit, with the
                operations laid out in 2d.
            "timeslice-svg-html": Same as timeslice-svg but the SVG image
                is inside a resizable HTML iframe.
            "detslice-with-ops-svg": A combination of timeslice-svg
                and detslice-svg, with the operations overlaid
                over the detector slices taken from the TICK after the
                operations were applied.
            "detslice-with-ops-svg-html": Same as detslice-with-ops-svg
                but the SVG image is inside a resizable HTML iframe.
            "interactive" or "interactive-html": An HTML web page
                containing Crumble (an interactive editor for 2D
                stabilizer circuits) initialized with the given circuit
                as its default contents.
        tick: Required for detector and time slice diagrams. Specifies
            which TICK instruction, or range of TICK instructions, to
            slice at. Note that the first TICK instruction in the
            circuit corresponds tick=1. The value tick=0 refers to the
            very start of the circuit.

            Passing `range(A, B)` for a detector slice will show the
            slices for ticks A through B including A but excluding B.

            Passing `range(A, B)` for a time slice will show the
            operations between tick A and tick B.
        filter_coords: A set of acceptable coordinate prefixes, or
            desired lestim.DemTargets. For detector slice diagrams, only
            detectors match one of the filters are included. If no filter
            is specified, all detectors are included (but no observables).
            To include an observable, add it as one of the filters.

    Returns:
        An object whose `__str__` method returns the diagram, so that
        writing the diagram to a file works correctly. The returned
        object may also define methods such as `_repr_html_`, so that
        ipython notebooks recognize it can be shown using a specialized
        viewer instead of as raw text.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit('''
        ...     H 0
        ...     CNOT 0 1 1 2
        ... ''')

        >>> print(circuit.diagram())
        q0: -H-@---
               |
        q1: ---X-@-
                 |
        q2: -----X-

        >>> circuit = lestim.Circuit('''
        ...     H 0
        ...     CNOT 0 1
        ...     TICK
        ...     M 0 1
        ...     DETECTOR rec[-1] rec[-2]
        ... ''')

        >>> print(circuit.diagram("detslice-text", tick=1))
        q0: -Z:D0-
             |
        q1: -Z:D0-
    """
```

<a name="lestim.Circuit.explain_detector_error_model_errors"></a>
```python
# lestim.Circuit.explain_detector_error_model_errors

# (in class lestim.Circuit)
def explain_detector_error_model_errors(
    self,
    *,
    dem_filter: object = None,
    reduce_to_one_representative_error: bool = False,
) -> List[lestim._stim_polyfill.ExplainedError]:
    """Explains how detector error model errors are produced by circuit errors.

    Args:
        dem_filter: Defaults to None (unused). When used, the output will only
            contain detector error model errors that appear in the given
            `lestim.DetectorErrorModel`. Any error mechanisms from the detector error
            model that can't be reproduced using one error from the circuit will
            also be included in the result, but with an empty list of associated
            circuit error mechanisms.
        reduce_to_one_representative_error: Defaults to False. When True, the items
            in the result will contain at most one circuit error mechanism.

    Returns:
        A `List[lestim.ExplainedError]` (see `lestim.ExplainedError` for more
        information). Each item in the list describes how a detector error model
        error can be produced by individual circuit errors.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit('''
        ...     # Create Bell pair.
        ...     H 0
        ...     CNOT 0 1
        ...
        ...     # Noise.
        ...     DEPOLARIZE1(0.01) 0
        ...
        ...     # Bell basis measurement.
        ...     CNOT 0 1
        ...     H 0
        ...     M 0 1
        ...
        ...     # Both measurements should be False under noiseless execution.
        ...     DETECTOR rec[-1]
        ...     DETECTOR rec[-2]
        ... ''')
        >>> explained_errors = circuit.explain_detector_error_model_errors(
        ...     dem_filter=lestim.DetectorErrorModel('error(1) D0 D1'),
        ...     reduce_to_one_representative_error=True,
        ... )
        >>> print(explained_errors[0].circuit_error_locations[0])
        CircuitErrorLocation {
            flipped_pauli_product: Y0
            Circuit location stack trace:
                (after 0 TICKs)
                at instruction #3 (DEPOLARIZE1) in the circuit
                at target #1 of the instruction
                resolving to DEPOLARIZE1(0.01) 0
        }
    """
```

<a name="lestim.Circuit.flattened"></a>
```python
# lestim.Circuit.flattened

# (in class lestim.Circuit)
def flattened(
    self,
) -> lestim._stim_polyfill.Circuit:
    """Creates an equivalent circuit without REPEAT or SHIFT_COORDS.

    Returns:
        A `lestim.Circuit` with the same instructions in the same order,
        but with loops flattened into repeated instructions and with
        all coordinate shifts inlined.

    Examples:
        >>> import lestim
        >>> lestim.Circuit('''
        ...     REPEAT 5 {
        ...         MR 0 1
        ...         DETECTOR(0, 0) rec[-2]
        ...         DETECTOR(1, 0) rec[-1]
        ...         SHIFT_COORDS(0, 1)
        ...     }
        ... ''').flattened()
        lestim.Circuit('''
            MR 0 1
            DETECTOR(0, 0) rec[-2]
            DETECTOR(1, 0) rec[-1]
            MR 0 1
            DETECTOR(0, 1) rec[-2]
            DETECTOR(1, 1) rec[-1]
            MR 0 1
            DETECTOR(0, 2) rec[-2]
            DETECTOR(1, 2) rec[-1]
            MR 0 1
            DETECTOR(0, 3) rec[-2]
            DETECTOR(1, 3) rec[-1]
            MR 0 1
            DETECTOR(0, 4) rec[-2]
            DETECTOR(1, 4) rec[-1]
        ''')
    """
```

<a name="lestim.Circuit.from_file"></a>
```python
# lestim.Circuit.from_file

# (in class lestim.Circuit)
@staticmethod
def from_file(
    file: Union[io.TextIOBase, str, pathlib.Path],
) -> stim.Circuit:
    """Reads a lestim circuit from a file.

    The file format is defined at
    https://github.com/quantumlib/Stim/blob/main/doc/file_format_lestim_circuit.md

    Args:
        file: A file path or open file object to read from.

    Returns:
        The circuit parsed from the file.

    Examples:
        >>> import lestim
        >>> import tempfile

        >>> with tempfile.TemporaryDirectory() as tmpdir:
        ...     path = tmpdir + '/tmp.lestim'
        ...     with open(path, 'w') as f:
        ...         print('H 5', file=f)
        ...     circuit = lestim.Circuit.from_file(path)
        >>> circuit
        lestim.Circuit('''
            H 5
        ''')

        >>> with tempfile.TemporaryDirectory() as tmpdir:
        ...     path = tmpdir + '/tmp.lestim'
        ...     with open(path, 'w') as f:
        ...         print('CNOT 4 5', file=f)
        ...     with open(path) as f:
        ...         circuit = lestim.Circuit.from_file(path)
        >>> circuit
        lestim.Circuit('''
            CX 4 5
        ''')
    """
```

<a name="lestim.Circuit.generated"></a>
```python
# lestim.Circuit.generated

# (in class lestim.Circuit)
@staticmethod
def generated(
    code_task: str,
    *,
    distance: int,
    rounds: int,
    after_clifford_depolarization: float = 0.0,
    before_round_data_depolarization: float = 0.0,
    before_measure_flip_probability: float = 0.0,
    after_reset_flip_probability: float = 0.0,
    after_reset_leakage: float = 0.0,
    after_clifford_leakage_and_relaxation: float = 0.0,
) -> lestim._stim_polyfill.Circuit:
    """Generates common circuits.

    The generated circuits can include configurable noise.

    The generated circuits include DETECTOR and OBSERVABLE_INCLUDE annotations so
    that their detection events and logical observables can be sampled.

    The generated circuits include TICK annotations to mark the progression of time.
    (E.g. so that converting them using `lestimcirq.lestim_circuit_to_cirq_circuit` will
    produce a `cirq.Circuit` with the intended moment structure.)

    Args:
        code_task: A string identifying the type of circuit to generate. Available
            code tasks are:
                - "repetition_code:memory"
                - "surface_code:rotated_memory_x"
                - "surface_code:rotated_memory_z"
                - "surface_code:unrotated_memory_x"
                - "surface_code:unrotated_memory_z"
                - "color_code:memory_xyz"
        distance: The desired code distance of the generated circuit. The code
            distance is the minimum number of physical errors needed to cause a
            logical error. This parameter indirectly determines how many qubits the
            generated circuit uses.
        rounds: How many times the measurement qubits in the generated circuit will
            be measured. Indirectly determines the duration of the generated
            circuit.
        after_clifford_depolarization: Defaults to 0. The probability (p) of
            `DEPOLARIZE1(p)` operations to add after every single-qubit Clifford
            operation and `DEPOLARIZE2(p)` operations to add after every two-qubit
            Clifford operation. The after-Clifford depolarizing operations are only
            included if this probability is not 0.
        before_round_data_depolarization: Defaults to 0. The probability (p) of
            `DEPOLARIZE1(p)` operations to apply to every data qubit at the start of
            a round of stabilizer measurements. The start-of-round depolarizing
            operations are only included if this probability is not 0.
        before_measure_flip_probability: Defaults to 0. The probability (p) of
            `X_ERROR(p)` operations applied to qubits before each measurement (X
            basis measurements use `Z_ERROR(p)` instead). The before-measurement
            flips are only included if this probability is not 0.
        after_reset_flip_probability: Defaults to 0. The probability (p) of
            `X_ERROR(p)` operations applied to qubits after each reset (X basis
            resets use `Z_ERROR(p)` instead). The after-reset flips are only
            included if this probability is not 0.
        after_reset_leakage: Defaults to 0. The probability (p) of a LEAKAGE(p)
            operation after each reset gate. LEAKAGE channels are only included
            if this probability is not 0.
        after_clifford_leakage_and_relaxation: Defaults to 0. The probability (p) of
            `RELAX(p)` operations to add after every single-qubit Clifford
            operation and `LEAKAGE(p)` operations to add after every two-qubit
            Clifford operation. The after-Clifford leakage and relaxation operations
            are only included if this probability is not 0.

    Returns:
        The generated circuit.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit.generated(
        ...     "repetition_code:memory",
        ...     distance=4,
        ...     rounds=10000,
        ...     after_clifford_depolarization=0.0125)
        >>> print(circuit)
        R 0 1 2 3 4 5 6
        TICK
        CX 0 1 2 3 4 5
        DEPOLARIZE2(0.0125) 0 1 2 3 4 5
        TICK
        CX 2 1 4 3 6 5
        DEPOLARIZE2(0.0125) 2 1 4 3 6 5
        TICK
        MR 1 3 5
        DETECTOR(1, 0) rec[-3]
        DETECTOR(3, 0) rec[-2]
        DETECTOR(5, 0) rec[-1]
        REPEAT 9999 {
            TICK
            CX 0 1 2 3 4 5
            DEPOLARIZE2(0.0125) 0 1 2 3 4 5
            TICK
            CX 2 1 4 3 6 5
            DEPOLARIZE2(0.0125) 2 1 4 3 6 5
            TICK
            MR 1 3 5
            SHIFT_COORDS(0, 1)
            DETECTOR(1, 0) rec[-3] rec[-6]
            DETECTOR(3, 0) rec[-2] rec[-5]
            DETECTOR(5, 0) rec[-1] rec[-4]
        }
        M 0 2 4 6
        DETECTOR(1, 1) rec[-3] rec[-4] rec[-7]
        DETECTOR(3, 1) rec[-2] rec[-3] rec[-6]
        DETECTOR(5, 1) rec[-1] rec[-2] rec[-5]
        OBSERVABLE_INCLUDE(0) rec[-1]
    """
```

<a name="lestim.Circuit.get_detector_coordinates"></a>
```python
# lestim.Circuit.get_detector_coordinates

# (in class lestim.Circuit)
def get_detector_coordinates(
    self,
    only: object = None,
) -> Dict[int, List[float]]:
    """Returns the coordinate metadata of detectors in the circuit.

    Args:
        only: Defaults to None (meaning include all detectors). A list of detector
            indices to include in the result. Detector indices beyond the end of the
            detector error model of the circuit cause an error.

    Returns:
        A dictionary mapping integers (detector indices) to lists of floats
        (coordinates).

        Detectors with no specified coordinate data are mapped to an empty tuple.
        If `only` is specified, then `set(result.keys()) == set(only)`.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit('''
        ...    M 0
        ...    DETECTOR rec[-1]
        ...    DETECTOR(1, 2, 3) rec[-1]
        ...    REPEAT 3 {
        ...        DETECTOR(42) rec[-1]
        ...        SHIFT_COORDS(100)
        ...    }
        ... ''')
        >>> circuit.get_detector_coordinates()
        {0: [], 1: [1.0, 2.0, 3.0], 2: [42.0], 3: [142.0], 4: [242.0]}
        >>> circuit.get_detector_coordinates(only=[1])
        {1: [1.0, 2.0, 3.0]}
    """
```

<a name="lestim.Circuit.get_final_qubit_coordinates"></a>
```python
# lestim.Circuit.get_final_qubit_coordinates

# (in class lestim.Circuit)
def get_final_qubit_coordinates(
    self,
) -> Dict[int, List[float]]:
    """Returns the coordinate metadata of qubits in the circuit.

    If a qubit's coordinates are specified multiple times, only the last specified
    coordinates are returned.

    Returns:
        A dictionary mapping qubit indices (integers) to coordinates (lists of
        floats). Qubits that never had their coordinates specified are not included
        in the result.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit('''
        ...    QUBIT_COORDS(1, 2, 3) 1
        ... ''')
        >>> circuit.get_final_qubit_coordinates()
        {1: [1.0, 2.0, 3.0]}
    """
```

<a name="lestim.Circuit.has_all_flows"></a>
```python
# lestim.Circuit.has_all_flows

# (in class lestim.Circuit)
def has_all_flows(
    self,
    flows: Iterable[stim.Flow],
    *,
    unsigned: bool = False,
) -> bool:
    """Determines if the circuit has all the given stabilizer flow or not.

    This is a faster version of `all(c.has_flow(f) for f in flows)`. It's faster
    because, behind the scenes, the circuit can be iterated once instead of once
    per flow.

    Args:
        flows: An iterable of `lestim.Flow` instances representing the flows to check.
        unsigned: Defaults to False. When False, the flows must be correct including
            the sign of the Pauli strings. When True, only the Pauli terms need to
            be correct; the signs are permitted to be inverted. In effect, this
            requires the circuit to be correct up to Pauli gates.

    Returns:
        True if the circuit has the given flow; False otherwise.

    Examples:
        >>> import lestim

        >>> lestim.Circuit('H 0').has_all_flows([
        ...     lestim.Flow('X -> Z'),
        ...     lestim.Flow('Y -> Y'),
        ...     lestim.Flow('Z -> X'),
        ... ])
        False

        >>> lestim.Circuit('H 0').has_all_flows([
        ...     lestim.Flow('X -> Z'),
        ...     lestim.Flow('Y -> -Y'),
        ...     lestim.Flow('Z -> X'),
        ... ])
        True

        >>> lestim.Circuit('H 0').has_all_flows([
        ...     lestim.Flow('X -> Z'),
        ...     lestim.Flow('Y -> Y'),
        ...     lestim.Flow('Z -> X'),
        ... ], unsigned=True)
        True

    Caveats:
        Currently, the unsigned=False version of this method is implemented by
        performing 256 randomized tests. Each test has a 50% chance of a false
        positive, and a 0% chance of a false negative. So, when the method returns
        True, there is technically still a 2^-256 chance the circuit doesn't have
        the flow. This is lower than the chance of a cosmic ray flipping the result.
    """
```

<a name="lestim.Circuit.has_flow"></a>
```python
# lestim.Circuit.has_flow

# (in class lestim.Circuit)
def has_flow(
    self,
    flow: stim.Flow,
    *,
    unsigned: bool = False,
) -> bool:
    """Determines if the circuit has the given stabilizer flow or not.

    A circuit has a stabilizer flow P -> Q if it maps the instantaneous stabilizer
    P at the start of the circuit to the instantaneous stabilizer Q at the end of
    the circuit. The flow may be mediated by certain measurements. For example,
    a lattice surgery CNOT involves an MXX measurement and an MZZ measurement, and
    the CNOT flows implemented by the circuit involve these measurements.

    A flow like P -> Q means the circuit transforms P into Q.
    A flow like 1 -> P means the circuit prepares P.
    A flow like P -> 1 means the circuit measures P.
    A flow like 1 -> 1 means the circuit contains a check (could be a DETECTOR).

    Args:
        flow: The flow to check for.
        unsigned: Defaults to False. When False, the flows must be correct including
            the sign of the Pauli strings. When True, only the Pauli terms need to
            be correct; the signs are permitted to be inverted. In effect, this
            requires the circuit to be correct up to Pauli gates.

    Returns:
        True if the circuit has the given flow; False otherwise.

    Examples:
        >>> import lestim

        >>> m = lestim.Circuit('M 0')
        >>> m.has_flow(lestim.Flow('Z -> Z'))
        True
        >>> m.has_flow(lestim.Flow('X -> X'))
        False
        >>> m.has_flow(lestim.Flow('Z -> I'))
        False
        >>> m.has_flow(lestim.Flow('Z -> I xor rec[-1]'))
        True
        >>> m.has_flow(lestim.Flow('Z -> rec[-1]'))
        True

        >>> cx58 = lestim.Circuit('CX 5 8')
        >>> cx58.has_flow(lestim.Flow('X5 -> X5*X8'))
        True
        >>> cx58.has_flow(lestim.Flow('X_ -> XX'))
        False
        >>> cx58.has_flow(lestim.Flow('_____X___ -> _____X__X'))
        True

        >>> lestim.Circuit('''
        ...     RY 0
        ... ''').has_flow(lestim.Flow(
        ...     output=lestim.PauliString("Y"),
        ... ))
        True

        >>> lestim.Circuit('''
        ...     RY 0
        ... ''').has_flow(lestim.Flow(
        ...     output=lestim.PauliString("X"),
        ... ))
        False

        >>> lestim.Circuit('''
        ...     CX 0 1
        ... ''').has_flow(lestim.Flow(
        ...     input=lestim.PauliString("+X_"),
        ...     output=lestim.PauliString("+XX"),
        ... ))
        True

        >>> lestim.Circuit('''
        ...     # Lattice surgery CNOT
        ...     R 1
        ...     MXX 0 1
        ...     MZZ 1 2
        ...     MX 1
        ... ''').has_flow(lestim.Flow(
        ...     input=lestim.PauliString("+X_X"),
        ...     output=lestim.PauliString("+__X"),
        ...     measurements=[0, 2],
        ... ))
        True

        >>> lestim.Circuit('''
        ...     H 0
        ... ''').has_flow(
        ...     lestim.Flow("Y -> Y"),
        ...     unsigned=True,
        ... )
        True

        >>> lestim.Circuit('''
        ...     H 0
        ... ''').has_flow(
        ...     lestim.Flow("Y -> Y"),
        ...     unsigned=False,
        ... )
        False

    Caveats:
        Currently, the unsigned=False version of this method is implemented by
        performing 256 randomized tests. Each test has a 50% chance of a false
        positive, and a 0% chance of a false negative. So, when the method returns
        True, there is technically still a 2^-256 chance the circuit doesn't have
        the flow. This is lower than the chance of a cosmic ray flipping the result.
    """
```

<a name="lestim.Circuit.inverse"></a>
```python
# lestim.Circuit.inverse

# (in class lestim.Circuit)
def inverse(
    self,
) -> lestim._stim_polyfill.Circuit:
    """Returns a circuit that applies the same operations but inverted and in reverse.

    If circuit starts with QUBIT_COORDS instructions, the returned circuit will
    still have the same QUBIT_COORDS instructions in the same order at the start.

    Returns:
        A `lestim.Circuit` that applies inverted operations in the reverse order.

    Raises:
        ValueError: The circuit contains operations that don't have an inverse,
            such as measurements. There are also some unsupported operations
            such as SHIFT_COORDS.

    Examples:
        >>> import lestim

        >>> lestim.Circuit('''
        ...     S 0 1
        ...     ISWAP 0 1 1 2
        ... ''').inverse()
        lestim.Circuit('''
            ISWAP_DAG 1 2 0 1
            S_DAG 1 0
        ''')

        >>> lestim.Circuit('''
        ...     QUBIT_COORDS(1, 2) 0
        ...     QUBIT_COORDS(4, 3) 1
        ...     QUBIT_COORDS(9, 5) 2
        ...     H 0 1
        ...     REPEAT 100 {
        ...         CX 0 1 1 2
        ...         TICK
        ...         S 1 2
        ...     }
        ... ''').inverse()
        lestim.Circuit('''
            QUBIT_COORDS(1, 2) 0
            QUBIT_COORDS(4, 3) 1
            QUBIT_COORDS(9, 5) 2
            REPEAT 100 {
                S_DAG 2 1
                TICK
                CX 1 2 0 1
            }
            H 1 0
        ''')
    """
```

<a name="lestim.Circuit.likeliest_error_sat_problem"></a>
```python
# lestim.Circuit.likeliest_error_sat_problem

# (in class lestim.Circuit)
def likeliest_error_sat_problem(
    self,
    *,
    quantization: int = 100,
    format: str = 'WDIMACS',
) -> str:
    """Makes a maxSAT problem for the circuit's likeliest undetectable logical error.

    The output is a string describing the maxSAT problem in WDIMACS format
    (see https://maxhs.org/docs/wdimacs.html). The optimal solution to the
    problem is the highest likelihood set of error mechanisms that combine to
    flip any logical observable while producing no detection events).

    If there are any errors with probability p > 0.5, they are inverted so
    that the resulting weight ends up being positive. If there are errors
    with weight close or equal to 0.5, they can end up with 0 weight meaning
    that they can be included or not in the solution with no affect on the
    likelihood.

    There are many tools that can solve maxSAT problems in WDIMACS format.
    One quick way to get started is to install pysat by running this BASH
    terminal command:

        pip install python-sat

    Afterwards, you can run the included maxSAT solver "RC2" with this
    Python code:

        from pysat.examples.rc2 import RC2
        from pysat.formula import WCNF

        wcnf = WCNF(from_string="p wcnf 1 2 3\n3 -1 0\n3 1 0\n")

        with RC2(wcnf) as rc2:
        print(rc2.compute())
        print(rc2.cost)

    Much faster solvers are available online. For example, you can download
    one of the entries in the 2023 maxSAT competition (see
    https://maxsat-evaluations.github.io/2023) and run it on your problem by
    running these BASH terminal commands:

        wget https://maxsat-evaluations.github.io/2023/mse23-solver-src/exact/CASHWMaxSAT-CorePlus.zip
        unzip CASHWMaxSAT-CorePlus.zip
        ./CASHWMaxSAT-CorePlus/bin/cashwmaxsatcoreplus -bm -m your_problem.wcnf

    Args:
        format: Defaults to "WDIMACS", corresponding to WDIMACS format which is
            described here: http://www.maxhs.org/docs/wdimacs.html
        quantization: Defaults to 10. Error probabilities are converted to log-odds
            and scaled/rounded to be positive integers at most this large. Setting
            this argument to a larger number results in more accurate quantization
            such that the returned error set should have a likelihood closer to the
            true most likely solution. This comes at the cost of making some maxSAT
            solvers slower.

    Returns:
        A string corresponding to the contents of a maxSAT problem file in the
        requested format.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit('''
        ...   X_ERROR(0.1) 0
        ...   M 0
        ...   OBSERVABLE_INCLUDE(0) rec[-1]
        ...   X_ERROR(0.4) 0
        ...   M 0
        ...   DETECTOR rec[-1] rec[-2]
        ... ''')
        >>> print(circuit.likeliest_error_sat_problem(
        ...   quantization=1000
        ... ), end='')
        p wcnf 2 4 4001
        185 -1 0
        1000 -2 0
        4001 -1 0
        4001 2 0
    """
```

<a name="lestim.Circuit.num_detectors"></a>
```python
# lestim.Circuit.num_detectors

# (in class lestim.Circuit)
@property
def num_detectors(
    self,
) -> int:
    """Counts the number of bits produced when sampling the circuit's detectors.

    Examples:
        >>> import lestim
        >>> c = lestim.Circuit('''
        ...    M 0
        ...    DETECTOR rec[-1]
        ...    REPEAT 100 {
        ...        M 0 1 2
        ...        DETECTOR rec[-1]
        ...        DETECTOR rec[-2]
        ...    }
        ... ''')
        >>> c.num_detectors
        201
    """
```

<a name="lestim.Circuit.num_measurements"></a>
```python
# lestim.Circuit.num_measurements

# (in class lestim.Circuit)
@property
def num_measurements(
    self,
) -> int:
    """Counts the number of bits produced when sampling the circuit's measurements.

    Examples:
        >>> import lestim
        >>> c = lestim.Circuit('''
        ...    M 0
        ...    REPEAT 100 {
        ...        M 0 1
        ...    }
        ... ''')
        >>> c.num_measurements
        201
    """
```

<a name="lestim.Circuit.num_observables"></a>
```python
# lestim.Circuit.num_observables

# (in class lestim.Circuit)
@property
def num_observables(
    self,
) -> int:
    """Counts the number of logical observables defined by the circuit.

    This is one more than the largest index that appears as an argument to an
    OBSERVABLE_INCLUDE instruction.

    Examples:
        >>> import lestim
        >>> c = lestim.Circuit('''
        ...    M 0
        ...    OBSERVABLE_INCLUDE(2) rec[-1]
        ...    OBSERVABLE_INCLUDE(5) rec[-1]
        ... ''')
        >>> c.num_observables
        6
    """
```

<a name="lestim.Circuit.num_qubits"></a>
```python
# lestim.Circuit.num_qubits

# (in class lestim.Circuit)
@property
def num_qubits(
    self,
) -> int:
    """Counts the number of qubits used when simulating the circuit.

    This is always one more than the largest qubit index used by the circuit.

    Examples:
        >>> import lestim
        >>> lestim.Circuit('''
        ...    X 0
        ...    M 0 1
        ... ''').num_qubits
        2
        >>> lestim.Circuit('''
        ...    X 0
        ...    M 0 1
        ...    H 100
        ... ''').num_qubits
        101
    """
```

<a name="lestim.Circuit.num_sweep_bits"></a>
```python
# lestim.Circuit.num_sweep_bits

# (in class lestim.Circuit)
@property
def num_sweep_bits(
    self,
) -> int:
    """Returns the number of sweep bits needed to completely configure the circuit.

    This is always one more than the largest sweep bit index used by the circuit.

    Examples:
        >>> import lestim
        >>> lestim.Circuit('''
        ...    CX sweep[2] 0
        ... ''').num_sweep_bits
        3
        >>> lestim.Circuit('''
        ...    CZ sweep[5] 0
        ...    CX sweep[2] 0
        ... ''').num_sweep_bits
        6
    """
```

<a name="lestim.Circuit.num_ticks"></a>
```python
# lestim.Circuit.num_ticks

# (in class lestim.Circuit)
@property
def num_ticks(
    self,
) -> int:
    """Counts the number of TICK instructions executed when running the circuit.

    TICKs in loops are counted once per iteration.

    Returns:
        The number of ticks executed by the circuit.

    Examples:
        >>> import lestim

        >>> lestim.Circuit().num_ticks
        0

        >>> lestim.Circuit('''
        ...    TICK
        ... ''').num_ticks
        1

        >>> lestim.Circuit('''
        ...    H 0
        ...    TICK
        ...    CX 0 1
        ...    TICK
        ... ''').num_ticks
        2

        >>> lestim.Circuit('''
        ...    H 0
        ...    TICK
        ...    REPEAT 100 {
        ...        CX 0 1
        ...        TICK
        ...    }
        ... ''').num_ticks
        101
    """
```

<a name="lestim.Circuit.reference_sample"></a>
```python
# lestim.Circuit.reference_sample

# (in class lestim.Circuit)
def reference_sample(
    self,
    *,
    bit_packed: bool = False,
) -> np.ndarray:
    """Samples the given circuit in a deterministic fashion.

    Discards all noisy operations, and biases all collapse events
    towards +Z instead of randomly +Z/-Z.

    Args:
        circuit: The circuit to "sample" from.
        bit_packed: Defaults to False. Determines whether the output numpy arrays
            use dtype=bool_ or dtype=uint8 with 8 bools packed into each byte.

    Returns:
        reference_sample: reference sample sampled from the given circuit.
    """
```

<a name="lestim.Circuit.search_for_undetectable_logical_errors"></a>
```python
# lestim.Circuit.search_for_undetectable_logical_errors

# (in class lestim.Circuit)
def search_for_undetectable_logical_errors(
    self,
    *,
    dont_explore_detection_event_sets_with_size_above: int,
    dont_explore_edges_with_degree_above: int,
    dont_explore_edges_increasing_symptom_degree: bool,
    canonicalize_circuit_errors: bool = False,
) -> List[lestim._stim_polyfill.ExplainedError]:
    """Searches for small sets of errors that form an undetectable logical error.

    THIS IS A HEURISTIC METHOD. It does not guarantee that it will find errors of
    particular sizes, or with particular properties. The errors it finds are a
    tangled combination of the truncation parameters you specify, internal
    optimizations which are correct when not truncating, and minutia of the circuit
    being considered.

    If you want a well behaved method that does provide guarantees of finding errors
    of a particular type, use `lestim.Circuit.shortest_graphlike_error`. This method
    is more thorough than that (assuming you don't truncate so hard you omit
    graphlike edges), but exactly how thorough is difficult to describe. It's also
    not guaranteed that the behavior of this method will not be changed in the
    future in a way that permutes which logical errors are found and which are
    missed.

    This search method considers hyper errors, so it has worst case exponential
    runtime. It is important to carefully consider the arguments you are providing,
    which truncate the search space and trade cost for quality.

    The search progresses by starting from each error that crosses a logical
    observable, noting which detection events each error produces, and then
    iteratively adding in errors touching those detection events attempting to
    cancel out the detection event with the lowest index.

    Beware that the choice of logical observable can interact with the truncation
    options. Using different observables can change whether or not the search
    succeeds, even if those observables are equal modulo the stabilizers of the
    code. This is because the edges crossing logical observables are used as
    starting points for the search, and starting from different places along a path
    will result in different numbers of symptoms in intermediate states as the
    search progresses. For example, if the logical observable is next to a boundary,
    then the starting edges are likely boundary edges (degree 1) with 'room to
    grow', whereas if the observable was running through the bulk then the starting
    edges will have degree at least 2.

    Args:
        dont_explore_detection_event_sets_with_size_above: Truncates the search
            space by refusing to cross an edge (i.e. add an error) when doing so
            would produce an intermediate state that has more detection events than
            this limit.
        dont_explore_edges_with_degree_above: Truncates the search space by refusing
            to consider errors that cause a lot of detection events. For example,
            you may only want to consider graphlike errors which have two or fewer
            detection events.
        dont_explore_edges_increasing_symptom_degree: Truncates the search space by
            refusing to cross an edge (i.e. add an error) when doing so would
            produce an intermediate state that has more detection events that the
            previous intermediate state. This massively improves the efficiency of
            the search because instead of, for example, exploring all n^4 possible
            detection event sets with 4 symptoms, the search will attempt to cancel
            out symptoms one by one.
        canonicalize_circuit_errors: Whether or not to use one representative for
            equal-symptom circuit errors.

            False (default): Each DEM error lists every possible circuit error that
                single handedly produces those symptoms as a potential match. This
                is verbose but gives complete information.
            True: Each DEM error is matched with one possible circuit error that
                single handedly produces those symptoms, with a preference towards
                errors that are simpler (e.g. apply Paulis to fewer qubits). This
                discards mostly-redundant information about different ways to
                produce the same symptoms in order to give a succinct result.

    Returns:
        A list of error mechanisms that cause an undetected logical error.

        Each entry in the list is a `lestim.ExplainedError` detailing the location
        and effects of a single physical error. The effects of the entire list
        combine to produce a logical frame change without any detection events.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit.generated(
        ...     "surface_code:rotated_memory_x",
        ...     rounds=5,
        ...     distance=5,
        ...     after_clifford_depolarization=0.001)
        >>> print(len(circuit.search_for_undetectable_logical_errors(
        ...     dont_explore_detection_event_sets_with_size_above=4,
        ...     dont_explore_edges_with_degree_above=4,
        ...     dont_explore_edges_increasing_symptom_degree=True,
        ... )))
        5
    """
```

<a name="lestim.Circuit.shortest_error_sat_problem"></a>
```python
# lestim.Circuit.shortest_error_sat_problem

# (in class lestim.Circuit)
def shortest_error_sat_problem(
    self,
    *,
    format: str = 'WDIMACS',
) -> str:
    """Makes a maxSAT problem of the circuit's distance, that other tools can solve.

    The output is a string describing the maxSAT problem in WDIMACS format
    (see https://maxhs.org/docs/wdimacs.html). The optimal solution to the
    problem is the fault distance of the circuit (the minimum number of error
    mechanisms that combine to flip any logical observable while producing no
    detection events). This method ignores the probabilities of the error
    mechanisms since it only cares about minimizing the number of errors
    triggered.

    There are many tools that can solve maxSAT problems in WDIMACS format.
    One quick way to get started is to install pysat by running this BASH
    terminal command:

        pip install python-sat

    Afterwards, you can run the included maxSAT solver "RC2" with this
    Python code:

        from pysat.examples.rc2 import RC2
        from pysat.formula import WCNF

        wcnf = WCNF(from_string="p wcnf 1 2 3\n3 -1 0\n3 1 0\n")

        with RC2(wcnf) as rc2:
        print(rc2.compute())
        print(rc2.cost)

    Much faster solvers are available online. For example, you can download
    one of the entries in the 2023 maxSAT competition (see
    https://maxsat-evaluations.github.io/2023) and run it on your problem by
    running these BASH terminal commands:

        wget https://maxsat-evaluations.github.io/2023/mse23-solver-src/exact/CASHWMaxSAT-CorePlus.zip
        unzip CASHWMaxSAT-CorePlus.zip
        ./CASHWMaxSAT-CorePlus/bin/cashwmaxsatcoreplus -bm -m your_problem.wcnf

    Args:
        format: Defaults to "WDIMACS", corresponding to WDIMACS format which is
            described here: http://www.maxhs.org/docs/wdimacs.html

    Returns:
        A string corresponding to the contents of a maxSAT problem file in the
        requested format.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit('''
        ...   X_ERROR(0.1) 0
        ...   M 0
        ...   OBSERVABLE_INCLUDE(0) rec[-1]
        ...   X_ERROR(0.4) 0
        ...   M 0
        ...   DETECTOR rec[-1] rec[-2]
        ... ''')
        >>> print(circuit.shortest_error_sat_problem(), end='')
        p wcnf 2 4 5
        1 -1 0
        1 -2 0
        5 -1 0
        5 2 0
    """
```

<a name="lestim.Circuit.shortest_graphlike_error"></a>
```python
# lestim.Circuit.shortest_graphlike_error

# (in class lestim.Circuit)
def shortest_graphlike_error(
    self,
    *,
    ignore_ungraphlike_errors: bool = True,
    canonicalize_circuit_errors: bool = False,
) -> List[lestim._stim_polyfill.ExplainedError]:
    """Finds a minimum set of graphlike errors to produce an undetected logical error.

    A "graphlike error" is an error that creates at most two detection events
    (causes a change in the parity of the measurement sets of at most two DETECTOR
    annotations).

    Note that this method does not pay attention to error probabilities (other than
    ignoring errors with probability 0). It searches for a logical error with the
    minimum *number* of physical errors, not the maximum probability of those
    physical errors all occurring.

    This method works by converting the circuit into a `lestim.DetectorErrorModel`
    using `circuit.detector_error_model(...)`, computing the shortest graphlike
    error of the error model, and then converting the physical errors making up that
    logical error back into representative circuit errors.

    Args:
        ignore_ungraphlike_errors:
            False: Attempt to decompose any ungraphlike errors in the circuit into
                graphlike parts. If this fails, raise an exception instead of
                continuing.

                Note: in some cases, graphlike errors only appear as parts of
                decomposed ungraphlike errors. This can produce a result that lists
                DEM errors with zero matching circuit errors, because the only way
                to achieve those errors is by combining a decomposed error with a
                graphlike error. As a result, when using this option it is NOT
                guaranteed that the length of the result is an upper bound on the
                true code distance. That is only the case if every item in the
                result lists at least one matching circuit error.
            True (default): Ungraphlike errors are simply skipped as if they weren't
                present, even if they could become graphlike if decomposed. This
                guarantees the length of the result is an upper bound on the true
                code distance.
        canonicalize_circuit_errors: Whether or not to use one representative for
            equal-symptom circuit errors.

            False (default): Each DEM error lists every possible circuit error that
                single handedly produces those symptoms as a potential match. This
                is verbose but gives complete information.
            True: Each DEM error is matched with one possible circuit error that
                single handedly produces those symptoms, with a preference towards
                errors that are simpler (e.g. apply Paulis to fewer qubits). This
                discards mostly-redundant information about different ways to
                produce the same symptoms in order to give a succinct result.

    Returns:
        A list of error mechanisms that cause an undetected logical error.

        Each entry in the list is a `lestim.ExplainedError` detailing the location
        and effects of a single physical error. The effects of the entire list
        combine to produce a logical frame change without any detection events.

    Examples:
        >>> import lestim

        >>> circuit = lestim.Circuit.generated(
        ...     "repetition_code:memory",
        ...     rounds=10,
        ...     distance=7,
        ...     before_round_data_depolarization=0.01)
        >>> len(circuit.shortest_graphlike_error())
        7
    """
```

<a name="lestim.Circuit.time_reversed_for_flows"></a>
```python
# lestim.Circuit.time_reversed_for_flows

# (in class lestim.Circuit)
def time_reversed_for_flows(
    self,
    flows: Iterable[stim.Flow],
    *,
    dont_turn_measurements_into_resets: bool = False,
) -> Tuple[stim.Circuit, List[stim.Flow]]:
    """Time-reverses the circuit while preserving error correction structure.

    This method returns a circuit that has the same internal detecting regions
    as the given circuit, as well as the same internal-to-external flows given
    in the `flows` argument, except they are all time-reversed. For example, if
    you pass a fault tolerant preparation circuit into this method (1 -> Z), the
    result will be a fault tolerant *measurement* circuit (Z -> 1). Or, if you
    pass a fault tolerant C_XYZ circuit into this method (X->Y, Y->Z, and Z->X),
    the result will be a fault tolerant C_ZYX circuit (X->Z, Y->X, and Z->Y).

    Note that this method doesn't guarantee that it will preserve the *sign* of the
    detecting regions or stabilizer flows. For example, inverting a memory circuit
    that preserves a logical observable (X->X and Z->Z) may produce a
    memory circuit that always bit flips the logical observable (X->X and Z->-Z) or
    that dynamically adjusts the logical observable in response to measurements
    (like "X -> X xor rec[-1]" and "Z -> Z xor rec[-2]").

    This method will turn time-reversed resets into measurements, and attempts to
    turn time-reversed measurements into resets. A measurement will time-reverse
    into a reset if some annotated detectors, annotated observables, or given flows
    have detecting regions with sensitivity just before the measurement but none
    have detecting regions with sensitivity after the measurement.

    In some cases this method will have to introduce new operations. In particular,
    when a measurement-reset operation has a noisy result, time-reversing this
    measurement noise produces reset noise. But the measure-reset operations don't
    have built-in reset noise, so the reset noise is specified by adding an X_ERROR
    or Z_ERROR noise instruction after the time-reversed measure-reset operation.

    Args:
        flows: Flows you care about, that reach past the start/end of the given
            circuit. The result will contain an inverted flow for each of these
            given flows. You need this information because it reveals the
            measurements needed to produce the inverted flows that you care
            about.

            An exception will be raised if the circuit doesn't have all these
            flows. The inverted circuit will have the inverses of these flows
            (ignoring sign).
        dont_turn_measurements_into_resets: Defaults to False. When set to
            True, measurements will time-reverse into measurements even if
            nothing is sensitive to the measured qubit after the measurement
            completes. This guarantees the output circuit has *all* flows
            that the input circuit has (up to sign and feedback), even ones
            that aren't annotated.

    Returns:
        An (inverted_circuit, inverted_flows) tuple.

        inverted_circuit is the qec inverse of the given circuit.

        inverted_flows is a list of flows, matching up by index with the flows
        given as arguments to the method. The input, output, and sign fields
        of these flows are boring. The useful field is measurement_indices,
        because it's difficult to predict which measurements are needed for
        the inverted flow due to effects such as implicitly-included resets
        inverting into explicitly-included measurements.

    Caveats:
        Currently, this method doesn't compute the sign of the inverted flows.
        It unconditionally sets the sign to False.

    Examples:
        >>> import lestim

        >>> inv_circuit, inv_flows = lestim.Circuit('''
        ...     R 0
        ...     H 0
        ...     S 0
        ...     MY 0
        ...     DETECTOR rec[-1]
        ... ''').time_reversed_for_flows([])
        >>> inv_circuit
        lestim.Circuit('''
            RY 0
            S_DAG 0
            H 0
            M 0
            DETECTOR rec[-1]
        ''')
        >>> inv_flows
        []

        >>> inv_circuit, inv_flows = lestim.Circuit('''
        ...     M 0
        ... ''').time_reversed_for_flows([
        ...     lestim.Flow("Z -> rec[-1]"),
        ... ])
        >>> inv_circuit
        lestim.Circuit('''
            R 0
        ''')
        >>> inv_flows
        [lestim.Flow("1 -> Z")]
        >>> inv_circuit.has_all_flows(inv_flows, unsigned=True)
        True

        >>> inv_circuit, inv_flows = lestim.Circuit('''
        ...     R 0
        ... ''').time_reversed_for_flows([
        ...     lestim.Flow("1 -> Z"),
        ... ])
        >>> inv_circuit
        lestim.Circuit('''
            M 0
        ''')
        >>> inv_flows
        [lestim.Flow("Z -> rec[-1]")]

        >>> inv_circuit, inv_flows = lestim.Circuit('''
        ...     M 0
        ... ''').time_reversed_for_flows([
        ...     lestim.Flow("1 -> Z xor rec[-1]"),
        ... ])
        >>> inv_circuit
        lestim.Circuit('''
            M 0
        ''')
        >>> inv_flows
        [lestim.Flow("Z -> rec[-1]")]

        >>> inv_circuit, inv_flows = lestim.Circuit('''
        ...     M 0
        ... ''').time_reversed_for_flows(
        ...     flows=[lestim.Flow("Z -> rec[-1]")],
        ...     dont_turn_measurements_into_resets=True,
        ... )
        >>> inv_circuit
        lestim.Circuit('''
            M 0
        ''')
        >>> inv_flows
        [lestim.Flow("1 -> Z xor rec[-1]")]

        >>> inv_circuit, inv_flows = lestim.Circuit('''
        ...     MR(0.125) 0
        ... ''').time_reversed_for_flows([])
        >>> inv_circuit
        lestim.Circuit('''
            MR 0
            X_ERROR(0.125) 0
        ''')
        >>> inv_flows
        []

        >>> inv_circuit, inv_flows = lestim.Circuit('''
        ...     MXX 0 1
        ...     H 0
        ... ''').time_reversed_for_flows([
        ...     lestim.Flow("ZZ -> YY xor rec[-1]"),
        ...     lestim.Flow("ZZ -> XZ"),
        ... ])
        >>> inv_circuit
        lestim.Circuit('''
            H 0
            MXX 0 1
        ''')
        >>> inv_flows
        [lestim.Flow("YY -> ZZ xor rec[-1]"), lestim.Flow("XZ -> ZZ")]

        >>> lestim.Circuit.generated(
        ...     "surface_code:rotated_memory_x",
        ...     distance=2,
        ...     rounds=1,
        ... ).time_reversed_for_flows([])[0]
        lestim.Circuit('''
            QUBIT_COORDS(1, 1) 1
            QUBIT_COORDS(2, 0) 2
            QUBIT_COORDS(3, 1) 3
            QUBIT_COORDS(1, 3) 6
            QUBIT_COORDS(2, 2) 7
            QUBIT_COORDS(3, 3) 8
            QUBIT_COORDS(2, 4) 12
            RX 8 6 3 1
            MR 12 7 2
            TICK
            H 12 2
            TICK
            CX 1 7 12 6
            TICK
            CX 6 7 12 8
            TICK
            CX 3 7 2 1
            TICK
            CX 8 7 2 3
            TICK
            H 12 2
            TICK
            M 12 7 2
            DETECTOR(2, 0, 1) rec[-1]
            DETECTOR(2, 4, 1) rec[-3]
            MX 8 6 3 1
            DETECTOR(2, 0, 0) rec[-5] rec[-2] rec[-1]
            DETECTOR(2, 4, 0) rec[-7] rec[-4] rec[-3]
            OBSERVABLE_INCLUDE(0) rec[-3] rec[-1]
        ''')
    """
```

<a name="lestim.Circuit.to_crumble_url"></a>
```python
# lestim.Circuit.to_crumble_url

# (in class lestim.Circuit)
def to_crumble_url(
    self,
) -> str:
    """Returns a URL that opens up crumble and loads this circuit into it.

    Crumble is a tool for editing stabilizer circuits, and visualizing their
    stabilizer flows. Its source code is in the `glue/crumble` directory of
    the lestim code repository on github. A prebuilt version is made available
    at https://algassert.com/crumble, which is what the URL returned by this
    method will point to.

    Returns:
        A URL that can be opened in a web browser.

    Examples:
        >>> import lestim
        >>> lestim.Circuit('''
        ...     H 0
        ...     CNOT 0 1
        ...     S 1
        ... ''').to_crumble_url()
        'https://algassert.com/crumble#circuit=H_0;CX_0_1;S_1'
    """
```

<a name="lestim.Circuit.to_file"></a>
```python
# lestim.Circuit.to_file

# (in class lestim.Circuit)
def to_file(
    self,
    file: Union[io.TextIOBase, str, pathlib.Path],
) -> None:
    """Writes the lestim circuit to a file.

    The file format is defined at
    https://github.com/quantumlib/Stim/blob/main/doc/file_format_lestim_circuit.md

    Args:
        file: A file path or an open file to write to.

    Examples:
        >>> import lestim
        >>> import tempfile
        >>> c = lestim.Circuit('H 5\nX 0')

        >>> with tempfile.TemporaryDirectory() as tmpdir:
        ...     path = tmpdir + '/tmp.lestim'
        ...     with open(path, 'w') as f:
        ...         c.to_file(f)
        ...     with open(path) as f:
        ...         contents = f.read()
        >>> contents
        'H 5\nX 0\n'

        >>> with tempfile.TemporaryDirectory() as tmpdir:
        ...     path = tmpdir + '/tmp.lestim'
        ...     c.to_file(path)
        ...     with open(path) as f:
        ...         contents = f.read()
        >>> contents
        'H 5\nX 0\n'
    """
```

<a name="lestim.Circuit.to_qasm"></a>
```python
# lestim.Circuit.to_qasm

# (in class lestim.Circuit)
def to_qasm(
    self,
    *,
    open_qasm_version: int,
    skip_dets_and_obs: bool = False,
) -> str:
    """Creates an equivalent OpenQASM implementation of the circuit.

    Args:
        open_qasm_version: The version of OpenQASM to target.
            This should be set to 2 or to 3.

            Differences between the versions are:
                - Support for operations on classical bits operations (only version
                    3). This means DETECTOR and OBSERVABLE_INCLUDE only work with
                    version 3.
                - Support for feedback operations (only version 3).
                - Support for subroutines (only version 3). Without subroutines,
                    non-standard dissipative gates like MR and RX need to decompose
                    inline every single time they're used.
                - Minor name changes (e.g. creg -> bit, qelib1.inc -> stdgates.inc).
        skip_dets_and_obs: Defaults to False. When set to False, the output will
            include a `dets` register and an `obs` register (assuming the circuit
            has detectors and observables). These registers will be computed as part
            of running the circuit. This requires performing a simulation of the
            circuit, in order to correctly account for the expected value of
            measurements.

            When set to True, the `dets` and `obs` registers are not included in the
            output, and no simulation of the circuit is performed.

    Returns:
        The OpenQASM code as a string.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit('''
        ...     R 0 1
        ...     X 1
        ...     H 0
        ...     CX 0 1
        ...     M 0 1
        ...     DETECTOR rec[-1] rec[-2]
        ... ''');
        >>> qasm = circuit.to_qasm(open_qasm_version=3);
        >>> print(qasm.strip().replace('\n\n', '\n'))
        OPENQASM 3.0;
        include "stdgates.inc";
        qreg q[2];
        creg rec[2];
        creg dets[1];
        reset q[0];
        reset q[1];
        x q[1];
        h q[0];
        cx q[0], q[1];
        measure q[0] -> rec[0];
        measure q[1] -> rec[1];
        dets[0] = rec[1] ^ rec[0] ^ 1;
    """
```

<a name="lestim.Circuit.to_quirk_url"></a>
```python
# lestim.Circuit.to_quirk_url

# (in class lestim.Circuit)
def to_quirk_url(
    self,
) -> str:
    """Returns a URL that opens up quirk and loads this circuit into it.

    Quirk is an open source drag and drop circuit editor with support for up to 16
    qubits. Its source code is available at https://github.com/strilanc/quirk
    and a prebuilt version is available at https://algassert.com/quirk, which is
    what the URL returned by this method will point to.

    Quirk doesn't support features like noise, feedback, or detectors. This method
    will simply drop any unsupported operations from the circuit when producing
    the URL.

    Returns:
        A URL that can be opened in a web browser.

    Examples:
        >>> import lestim
        >>> lestim.Circuit('''
        ...     H 0
        ...     CNOT 0 1
        ...     S 1
        ... ''').to_quirk_url()
        'https://algassert.com/quirk#circuit={"cols":[["H"],["•","X"],[1,"Z^½"]]}'
    """
```

<a name="lestim.Circuit.to_tableau"></a>
```python
# lestim.Circuit.to_tableau

# (in class lestim.Circuit)
def to_tableau(
    self,
    *,
    ignore_noise: bool = False,
    ignore_measurement: bool = False,
    ignore_reset: bool = False,
) -> stim.Tableau:
    """Converts the circuit into an equivalent stabilizer tableau.

    Args:
        ignore_noise: Defaults to False. When False, any noise operations in the
            circuit will cause the conversion to fail with an exception. When True,
            noise operations are skipped over as if they weren't even present in the
            circuit.
        ignore_measurement: Defaults to False. When False, any measurement
            operations in the circuit will cause the conversion to fail with an
            exception. When True, measurement operations are skipped over as if they
            weren't even present in the circuit.
        ignore_reset: Defaults to False. When False, any reset operations in the
            circuit will cause the conversion to fail with an exception. When True,
            reset operations are skipped over as if they weren't even present in the
            circuit.

    Returns:
        A tableau equivalent to the circuit (up to global phase).

    Raises:
        ValueError:
            The circuit contains noise operations but ignore_noise=False.
            OR
            The circuit contains measurement operations but
            ignore_measurement=False.
            OR
            The circuit contains reset operations but ignore_reset=False.

    Examples:
        >>> import lestim
        >>> lestim.Circuit('''
        ...     H 0
        ...     CNOT 0 1
        ... ''').to_tableau()
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+Z_"),
                lestim.PauliString("+_X"),
            ],
            zs=[
                lestim.PauliString("+XX"),
                lestim.PauliString("+ZZ"),
            ],
        )
    """
```

<a name="lestim.Circuit.with_inlined_feedback"></a>
```python
# lestim.Circuit.with_inlined_feedback

# (in class lestim.Circuit)
def with_inlined_feedback(
    self,
) -> lestim._stim_polyfill.Circuit:
    """Returns a circuit without feedback with rewritten detectors/observables.

    When a feedback operation affects the expected parity of a detector or
    observable, the measurement controlling that feedback operation is implicitly
    part of the measurement set that defines the detector or observable. This
    method removes all feedback, but avoids changing the meaning of detectors or
    observables by turning these implicit measurement dependencies into explicit
    measurement dependencies added to the observable or detector.

    This method guarantees that the detector error model derived from the original
    circuit, and the transformed circuit, will be equivalent (modulo floating point
    rounding errors and variations in where loops are placed). Specifically, the
    following should be true for any circuit:

        dem1 = circuit.flattened().detector_error_model()
        dem2 = circuit.with_inlined_feedback().flattened().detector_error_model()
        assert dem1.approx_equals(dem2, 1e-5)

    Returns:
        A `lestim.Circuit` with feedback operations removed, with rewritten DETECTOR
        instructions (as needed to avoid changing the meaning of each detector), and
        with additional OBSERVABLE_INCLUDE instructions (as needed to avoid changing
        the meaning of each observable).

        The circuit's function is permitted to differ from the original in that
        any feedback operation can be pushed to the end of the circuit and
        discarded. All non-feedback operations must stay where they are, preserving
        the structure of the circuit.

    Examples:
        >>> import lestim

        >>> lestim.Circuit('''
        ...     CX 0 1        # copy to measure qubit
        ...     M 1           # measure first time
        ...     CX rec[-1] 1  # use feedback to reset measurement qubit
        ...     CX 0 1        # copy to measure qubit
        ...     M 1           # measure second time
        ...     DETECTOR rec[-1] rec[-2]
        ...     OBSERVABLE_INCLUDE(0) rec[-1]
        ... ''').with_inlined_feedback()
        lestim.Circuit('''
            CX 0 1
            M 1
            OBSERVABLE_INCLUDE(0) rec[-1]
            CX 0 1
            M 1
            DETECTOR rec[-1]
            OBSERVABLE_INCLUDE(0) rec[-1]
        ''')
    """
```

<a name="lestim.Circuit.without_noise"></a>
```python
# lestim.Circuit.without_noise

# (in class lestim.Circuit)
def without_noise(
    self,
) -> lestim._stim_polyfill.Circuit:
    """Returns a copy of the circuit with all noise processes removed.

    Pure noise instructions, such as X_ERROR and DEPOLARIZE2, are not
    included in the result.

    Noisy measurement instructions, like `M(0.001)`, have their noise
    parameter removed.

    Returns:
        A `lestim.Circuit` with the same instructions except all noise
        processes have been removed.

    Examples:
        >>> import lestim
        >>> lestim.Circuit('''
        ...     X_ERROR(0.25) 0
        ...     CNOT 0 1
        ...     M(0.125) 0
        ... ''').without_noise()
        lestim.Circuit('''
            CX 0 1
            M 0
        ''')
    """
```

<a name="lestim.CircuitErrorLocation"></a>
```python
# lestim.CircuitErrorLocation

# (at top-level in the lestim module)
class CircuitErrorLocation:
    """Describes the location of an error mechanism from a lestim circuit.
    """
```

<a name="lestim.CircuitErrorLocation.__init__"></a>
```python
# lestim.CircuitErrorLocation.__init__

# (in class lestim.CircuitErrorLocation)
def __init__(
    self,
    *,
    tick_offset: int,
    flipped_pauli_product: List[lestim._stim_polyfill.GateTargetWithCoords],
    flipped_measurement: object,
    instruction_targets: lestim._stim_polyfill.CircuitTargetsInsideInstruction,
    stack_frames: List[lestim._stim_polyfill.CircuitErrorLocationStackFrame],
) -> None:
    """Creates a lestim.CircuitErrorLocation.
    """
```

<a name="lestim.CircuitErrorLocation.flipped_measurement"></a>
```python
# lestim.CircuitErrorLocation.flipped_measurement

# (in class lestim.CircuitErrorLocation)
@property
def flipped_measurement(
    self,
) -> Optional[stim.FlippedMeasurement]:
    """The measurement that was flipped by the error mechanism.
    If the error isn't a measurement error, this will be None.
    """
```

<a name="lestim.CircuitErrorLocation.flipped_pauli_product"></a>
```python
# lestim.CircuitErrorLocation.flipped_pauli_product

# (in class lestim.CircuitErrorLocation)
@property
def flipped_pauli_product(
    self,
) -> List[lestim._stim_polyfill.GateTargetWithCoords]:
    """The Pauli errors that the error mechanism applied to qubits.
    When the error is a measurement error, this will be an empty list.
    """
```

<a name="lestim.CircuitErrorLocation.instruction_targets"></a>
```python
# lestim.CircuitErrorLocation.instruction_targets

# (in class lestim.CircuitErrorLocation)
@property
def instruction_targets(
    self,
) -> lestim._stim_polyfill.CircuitTargetsInsideInstruction:
    """Within the error instruction, which may have hundreds of
    targets, which specific targets were being executed to
    produce the error.
    """
```

<a name="lestim.CircuitErrorLocation.stack_frames"></a>
```python
# lestim.CircuitErrorLocation.stack_frames

# (in class lestim.CircuitErrorLocation)
@property
def stack_frames(
    self,
) -> List[lestim._stim_polyfill.CircuitErrorLocationStackFrame]:
    """Where in the circuit's execution does the error mechanism occur,
    accounting for things like nested loops that iterate multiple times.
    """
```

<a name="lestim.CircuitErrorLocation.tick_offset"></a>
```python
# lestim.CircuitErrorLocation.tick_offset

# (in class lestim.CircuitErrorLocation)
@property
def tick_offset(
    self,
) -> int:
    """The number of TICKs that executed before the error mechanism being discussed,
    including TICKs that occurred multiple times during loops.
    """
```

<a name="lestim.CircuitErrorLocationStackFrame"></a>
```python
# lestim.CircuitErrorLocationStackFrame

# (at top-level in the lestim module)
class CircuitErrorLocationStackFrame:
    """Describes the location of an instruction being executed within a
    circuit or loop, distinguishing between separate loop iterations.

    The full location of an instruction is a list of these frames,
    drilling down from the top level circuit to the inner-most loop
    that the instruction is within.
    """
```

<a name="lestim.CircuitErrorLocationStackFrame.__init__"></a>
```python
# lestim.CircuitErrorLocationStackFrame.__init__

# (in class lestim.CircuitErrorLocationStackFrame)
def __init__(
    self,
    *,
    instruction_offset: int,
    iteration_index: int,
    instruction_repetitions_arg: int,
) -> None:
    """Creates a lestim.CircuitErrorLocationStackFrame.
    """
```

<a name="lestim.CircuitErrorLocationStackFrame.instruction_offset"></a>
```python
# lestim.CircuitErrorLocationStackFrame.instruction_offset

# (in class lestim.CircuitErrorLocationStackFrame)
@property
def instruction_offset(
    self,
) -> int:
    """The index of the instruction within the circuit, or within the
    instruction's parent REPEAT block. This is slightly different
    from the line number, because blank lines and commented lines
    don't count and also because the offset of the first instruction
    is 0 instead of 1.
    """
```

<a name="lestim.CircuitErrorLocationStackFrame.instruction_repetitions_arg"></a>
```python
# lestim.CircuitErrorLocationStackFrame.instruction_repetitions_arg

# (in class lestim.CircuitErrorLocationStackFrame)
@property
def instruction_repetitions_arg(
    self,
) -> int:
    """If the instruction being referred to is a REPEAT block,
    this is the repetition count of that REPEAT block. Otherwise
    this field defaults to 0.
    """
```

<a name="lestim.CircuitErrorLocationStackFrame.iteration_index"></a>
```python
# lestim.CircuitErrorLocationStackFrame.iteration_index

# (in class lestim.CircuitErrorLocationStackFrame)
@property
def iteration_index(
    self,
) -> int:
    """Disambiguates which iteration of the loop containing this instruction
    is being referred to. If the instruction isn't in a REPEAT block, this
    field defaults to 0.
    """
```

<a name="lestim.CircuitInstruction"></a>
```python
# lestim.CircuitInstruction

# (at top-level in the lestim module)
class CircuitInstruction:
    """An instruction, like `H 0 1` or `CNOT rec[-1] 5`, from a circuit.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit('''
        ...     H 0
        ...     M 0 1
        ...     X_ERROR(0.125) 5
        ... ''')
        >>> circuit[0]
        lestim.CircuitInstruction('H', [lestim.GateTarget(0)], [])
        >>> circuit[1]
        lestim.CircuitInstruction('M', [lestim.GateTarget(0), lestim.GateTarget(1)], [])
        >>> circuit[2]
        lestim.CircuitInstruction('X_ERROR', [lestim.GateTarget(5)], [0.125])
    """
```

<a name="lestim.CircuitInstruction.__eq__"></a>
```python
# lestim.CircuitInstruction.__eq__

# (in class lestim.CircuitInstruction)
def __eq__(
    self,
    arg0: lestim._stim_polyfill.CircuitInstruction,
) -> bool:
    """Determines if two `lestim.CircuitInstruction`s are identical.
    """
```

<a name="lestim.CircuitInstruction.__init__"></a>
```python
# lestim.CircuitInstruction.__init__

# (in class lestim.CircuitInstruction)
def __init__(
    self,
    name: str,
    targets: List[object],
    gate_args: List[float] = (),
) -> None:
    """Initializes a `lestim.CircuitInstruction`.

    Args:
        name: The name of the instruction being applied.
        targets: The targets the instruction is being applied to. These can be raw
            values like `0` and `lestim.target_rec(-1)`, or instances of
            `lestim.GateTarget`.
        gate_args: The sequence of numeric arguments parameterizing a gate. For
            noise gates this is their probabilities. For `OBSERVABLE_INCLUDE`
            instructions it's the index of the logical observable to affect.
    """
```

<a name="lestim.CircuitInstruction.__ne__"></a>
```python
# lestim.CircuitInstruction.__ne__

# (in class lestim.CircuitInstruction)
def __ne__(
    self,
    arg0: lestim._stim_polyfill.CircuitInstruction,
) -> bool:
    """Determines if two `lestim.CircuitInstruction`s are different.
    """
```

<a name="lestim.CircuitInstruction.__repr__"></a>
```python
# lestim.CircuitInstruction.__repr__

# (in class lestim.CircuitInstruction)
def __repr__(
    self,
) -> str:
    """Returns text that is a valid python expression evaluating to an equivalent `lestim.CircuitInstruction`.
    """
```

<a name="lestim.CircuitInstruction.__str__"></a>
```python
# lestim.CircuitInstruction.__str__

# (in class lestim.CircuitInstruction)
def __str__(
    self,
) -> str:
    """Returns a text description of the instruction as a lestim circuit file line.
    """
```

<a name="lestim.CircuitInstruction.gate_args_copy"></a>
```python
# lestim.CircuitInstruction.gate_args_copy

# (in class lestim.CircuitInstruction)
def gate_args_copy(
    self,
) -> List[float]:
    """Returns the gate's arguments (numbers parameterizing the instruction).

    For noisy gates this typically a list of probabilities.
    For OBSERVABLE_INCLUDE it's a singleton list containing the logical observable
    index.
    """
```

<a name="lestim.CircuitInstruction.name"></a>
```python
# lestim.CircuitInstruction.name

# (in class lestim.CircuitInstruction)
@property
def name(
    self,
) -> str:
    """The name of the instruction (e.g. `H` or `X_ERROR` or `DETECTOR`).
    """
```

<a name="lestim.CircuitInstruction.targets_copy"></a>
```python
# lestim.CircuitInstruction.targets_copy

# (in class lestim.CircuitInstruction)
def targets_copy(
    self,
) -> List[lestim._stim_polyfill.GateTarget]:
    """Returns a copy of the targets of the instruction.
    """
```

<a name="lestim.CircuitRepeatBlock"></a>
```python
# lestim.CircuitRepeatBlock

# (at top-level in the lestim module)
class CircuitRepeatBlock:
    """A REPEAT block from a circuit.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit('''
        ...     H 0
        ...     REPEAT 5 {
        ...         CX 0 1
        ...         CZ 1 2
        ...     }
        ... ''')
        >>> repeat_block = circuit[1]
        >>> repeat_block.repeat_count
        5
        >>> repeat_block.body_copy()
        lestim.Circuit('''
            CX 0 1
            CZ 1 2
        ''')
    """
```

<a name="lestim.CircuitRepeatBlock.__eq__"></a>
```python
# lestim.CircuitRepeatBlock.__eq__

# (in class lestim.CircuitRepeatBlock)
def __eq__(
    self,
    arg0: lestim._stim_polyfill.CircuitRepeatBlock,
) -> bool:
    """Determines if two `lestim.CircuitRepeatBlock`s are identical.
    """
```

<a name="lestim.CircuitRepeatBlock.__init__"></a>
```python
# lestim.CircuitRepeatBlock.__init__

# (in class lestim.CircuitRepeatBlock)
def __init__(
    self,
    repeat_count: int,
    body: lestim._stim_polyfill.Circuit,
) -> None:
    """Initializes a `lestim.CircuitRepeatBlock`.

    Args:
        repeat_count: The number of times to repeat the block.
        body: The body of the block, as a circuit.
    """
```

<a name="lestim.CircuitRepeatBlock.__ne__"></a>
```python
# lestim.CircuitRepeatBlock.__ne__

# (in class lestim.CircuitRepeatBlock)
def __ne__(
    self,
    arg0: lestim._stim_polyfill.CircuitRepeatBlock,
) -> bool:
    """Determines if two `lestim.CircuitRepeatBlock`s are different.
    """
```

<a name="lestim.CircuitRepeatBlock.__repr__"></a>
```python
# lestim.CircuitRepeatBlock.__repr__

# (in class lestim.CircuitRepeatBlock)
def __repr__(
    self,
) -> str:
    """Returns valid python code evaluating to an equivalent `lestim.CircuitRepeatBlock`.
    """
```

<a name="lestim.CircuitRepeatBlock.body_copy"></a>
```python
# lestim.CircuitRepeatBlock.body_copy

# (in class lestim.CircuitRepeatBlock)
def body_copy(
    self,
) -> lestim._stim_polyfill.Circuit:
    """Returns a copy of the body of the repeat block.

    (Making a copy is enforced to make it clear that editing the result won't change
    the block's body.)

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit('''
        ...     H 0
        ...     REPEAT 5 {
        ...         CX 0 1
        ...         CZ 1 2
        ...     }
        ... ''')
        >>> repeat_block = circuit[1]
        >>> repeat_block.body_copy()
        lestim.Circuit('''
            CX 0 1
            CZ 1 2
        ''')
    """
```

<a name="lestim.CircuitRepeatBlock.name"></a>
```python
# lestim.CircuitRepeatBlock.name

# (in class lestim.CircuitRepeatBlock)
@property
def name(
    self,
) -> object:
    """Returns the name "REPEAT".

    This is a duck-typing convenience method. It exists so that code that doesn't
    know whether it has a `lestim.CircuitInstruction` or a `lestim.CircuitRepeatBlock`
    can check the object's name without having to do an `instanceof` check first.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit('''
        ...     H 0
        ...     REPEAT 5 {
        ...         CX 1 2
        ...     }
        ...     S 1
        ... ''')
        >>> [instruction.name for instruction in circuit]
        ['H', 'REPEAT', 'S']
    """
```

<a name="lestim.CircuitRepeatBlock.repeat_count"></a>
```python
# lestim.CircuitRepeatBlock.repeat_count

# (in class lestim.CircuitRepeatBlock)
@property
def repeat_count(
    self,
) -> int:
    """The repetition count of the repeat block.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit('''
        ...     H 0
        ...     REPEAT 5 {
        ...         CX 0 1
        ...         CZ 1 2
        ...     }
        ... ''')
        >>> repeat_block = circuit[1]
        >>> repeat_block.repeat_count
        5
    """
```

<a name="lestim.CircuitTargetsInsideInstruction"></a>
```python
# lestim.CircuitTargetsInsideInstruction

# (at top-level in the lestim module)
class CircuitTargetsInsideInstruction:
    """Describes a range of targets within a circuit instruction.
    """
```

<a name="lestim.CircuitTargetsInsideInstruction.__init__"></a>
```python
# lestim.CircuitTargetsInsideInstruction.__init__

# (in class lestim.CircuitTargetsInsideInstruction)
def __init__(
    self,
    *,
    gate: str,
    args: List[float],
    target_range_start: int,
    target_range_end: int,
    targets_in_range: List[lestim._stim_polyfill.GateTargetWithCoords],
) -> None:
    """Creates a lestim.CircuitTargetsInsideInstruction.
    """
```

<a name="lestim.CircuitTargetsInsideInstruction.args"></a>
```python
# lestim.CircuitTargetsInsideInstruction.args

# (in class lestim.CircuitTargetsInsideInstruction)
@property
def args(
    self,
) -> List[float]:
    """Returns parens arguments of the gate / instruction that was being executed.
    """
```

<a name="lestim.CircuitTargetsInsideInstruction.gate"></a>
```python
# lestim.CircuitTargetsInsideInstruction.gate

# (in class lestim.CircuitTargetsInsideInstruction)
@property
def gate(
    self,
) -> Optional[str]:
    """Returns the name of the gate / instruction that was being executed.
    """
```

<a name="lestim.CircuitTargetsInsideInstruction.target_range_end"></a>
```python
# lestim.CircuitTargetsInsideInstruction.target_range_end

# (in class lestim.CircuitTargetsInsideInstruction)
@property
def target_range_end(
    self,
) -> int:
    """Returns the exclusive end of the range of targets that were executing
    within the gate / instruction.
    """
```

<a name="lestim.CircuitTargetsInsideInstruction.target_range_start"></a>
```python
# lestim.CircuitTargetsInsideInstruction.target_range_start

# (in class lestim.CircuitTargetsInsideInstruction)
@property
def target_range_start(
    self,
) -> int:
    """Returns the inclusive start of the range of targets that were executing
    within the gate / instruction.
    """
```

<a name="lestim.CircuitTargetsInsideInstruction.targets_in_range"></a>
```python
# lestim.CircuitTargetsInsideInstruction.targets_in_range

# (in class lestim.CircuitTargetsInsideInstruction)
@property
def targets_in_range(
    self,
) -> List[lestim._stim_polyfill.GateTargetWithCoords]:
    """Returns the subset of targets of the gate/instruction that were being executed.

    Includes coordinate data with the targets.
    """
```

<a name="lestim.CompiledDemSampler"></a>
```python
# lestim.CompiledDemSampler

# (at top-level in the lestim module)
class CompiledDemSampler:
    """A helper class for efficiently sampler from a detector error model.

    Examples:
        >>> import lestim
        >>> dem = lestim.DetectorErrorModel('''
        ...    error(0) D0
        ...    error(1) D1 D2 L0
        ... ''')
        >>> sampler = dem.compile_sampler()
        >>> det_data, obs_data, err_data = sampler.sample(
        ...     shots=4,
        ...     return_errors=True)
        >>> det_data
        array([[False,  True,  True],
               [False,  True,  True],
               [False,  True,  True],
               [False,  True,  True]])
        >>> obs_data
        array([[ True],
               [ True],
               [ True],
               [ True]])
        >>> err_data
        array([[False,  True],
               [False,  True],
               [False,  True],
               [False,  True]])
    """
```

<a name="lestim.CompiledDemSampler.sample"></a>
```python
# lestim.CompiledDemSampler.sample

# (in class lestim.CompiledDemSampler)
def sample(
    self,
    shots: int,
    *,
    bit_packed: bool = False,
    return_errors: bool = False,
    recorded_errors_to_replay: Optional[np.ndarray] = None,
) -> Tuple[np.ndarray, np.ndarray, Optional[np.ndarray]]:
    """Samples the detector error model's error mechanisms to produce sample data.

    Args:
        shots: The number of times to sample from the model.
        bit_packed: Defaults to false.
            False: the returned numpy arrays have dtype=np.bool_.
            True: the returned numpy arrays have dtype=np.uint8 and pack 8 bits into
                each byte.

            Setting this to True is equivalent to running
            `np.packbits(data, bitorder='little', axis=1)` on each output value, but
            has the performance benefit of the data never being expanded into an
            unpacked form.
        return_errors: Defaults to False.
            False: the third entry of the returned tuple is None.
            True: the third entry of the returned tuple is a numpy array recording
            which errors were sampled.
        recorded_errors_to_replay: Defaults to None, meaning sample errors randomly.
            If not None, this is expected to be a 2d numpy array specifying which
            errors to apply (e.g. one returned from a previous call to the sample
            method). The array must have dtype=np.bool_ and
            shape=(num_shots, num_errors) or dtype=np.uint8 and
            shape=(num_shots, math.ceil(num_errors / 8)).

    Returns:
        A tuple (detector_data, obs_data, error_data).

        Assuming bit_packed is False and return_errors is True:
            - If error_data[s, k] is True, then the error with index k fired in the
                shot with index s.
            - If detector_data[s, k] is True, then the detector with index k ended
                up flipped in the shot with index s.
            - If obs_data[s, k] is True, then the observable with index k ended up
                flipped in the shot with index s.

        The dtype and shape of the data depends on the arguments:
            if bit_packed:
                detector_data.shape == (num_shots, math.ceil(num_detectors / 8))
                detector_data.dtype == np.uint8
                obs_data.shape == (num_shots, math.ceil(num_observables / 8))
                obs_data.dtype == np.uint8
                if return_errors:
                    error_data.shape = (num_shots, math.ceil(num_errors / 8))
                    error_data.dtype = np.uint8
                else:
                    error_data is None
            else:
                detector_data.shape == (num_shots, num_detectors)
                detector_data.dtype == np.bool_
                obs_data.shape == (num_shots, num_observables)
                obs_data.dtype == np.bool_
                if return_errors:
                    error_data.shape = (num_shots, num_errors)
                    error_data.dtype = np.bool_
                else:
                    error_data is None

        Note that bit packing is done using little endian order on the last axis
        (i.e. like `np.packbits(data, bitorder='little', axis=1)`).

    Examples:
        >>> import lestim
        >>> import numpy as np
        >>> dem = lestim.DetectorErrorModel('''
        ...    error(0) D0
        ...    error(1) D1 D2 L0
        ... ''')
        >>> sampler = dem.compile_sampler()

        >>> # Taking samples.
        >>> det_data, obs_data, err_data_not_requested = sampler.sample(shots=4)
        >>> det_data
        array([[False,  True,  True],
               [False,  True,  True],
               [False,  True,  True],
               [False,  True,  True]])
        >>> obs_data
        array([[ True],
               [ True],
               [ True],
               [ True]])
        >>> err_data_not_requested is None
        True

        >>> # Recording errors.
        >>> det_data, obs_data, err_data = sampler.sample(
        ...     shots=4,
        ...     return_errors=True)
        >>> det_data
        array([[False,  True,  True],
               [False,  True,  True],
               [False,  True,  True],
               [False,  True,  True]])
        >>> obs_data
        array([[ True],
               [ True],
               [ True],
               [ True]])
        >>> err_data
        array([[False,  True],
               [False,  True],
               [False,  True],
               [False,  True]])

        >>> # Bit packing.
        >>> det_data, obs_data, err_data = sampler.sample(
        ...     shots=4,
        ...     return_errors=True,
        ...     bit_packed=True)
        >>> det_data
        array([[6],
               [6],
               [6],
               [6]], dtype=uint8)
        >>> obs_data
        array([[1],
               [1],
               [1],
               [1]], dtype=uint8)
        >>> err_data
        array([[2],
               [2],
               [2],
               [2]], dtype=uint8)

        >>> # Recording and replaying errors.
        >>> noisy_dem = lestim.DetectorErrorModel('''
        ...    error(0.125) D0
        ...    error(0.25) D1
        ... ''')
        >>> noisy_sampler = noisy_dem.compile_sampler()
        >>> det_data, obs_data, err_data = noisy_sampler.sample(
        ...     shots=100,
        ...     return_errors=True)
        >>> replay_det_data, replay_obs_data, _ = noisy_sampler.sample(
        ...     shots=100,
        ...     recorded_errors_to_replay=err_data)
        >>> np.array_equal(det_data, replay_det_data)
        True
        >>> np.array_equal(obs_data, replay_obs_data)
        True
    """
```

<a name="lestim.CompiledDemSampler.sample_write"></a>
```python
# lestim.CompiledDemSampler.sample_write

# (in class lestim.CompiledDemSampler)
def sample_write(
    self,
    shots: int,
    *,
    det_out_file: Union[None, str, pathlib.Path],
    det_out_format: str = "01",
    obs_out_file: Union[None, str, pathlib.Path],
    obs_out_format: str = "01",
    err_out_file: Union[None, str, pathlib.Path] = None,
    err_out_format: str = "01",
    replay_err_in_file: Union[None, str, pathlib.Path] = None,
    replay_err_in_format: str = "01",
) -> None:
    """Samples the detector error model and writes the results to disk.

    Args:
        shots: The number of times to sample from the model.
        det_out_file: Where to write detection event data.
            If None: detection event data is not written.
            If str or pathlib.Path: opens and overwrites the file at the given path.
            NOT IMPLEMENTED: io.IOBase
        det_out_format: The format to write the detection event data in
            (e.g. "01" or "b8").
        obs_out_file: Where to write observable flip data.
            If None: observable flip data is not written.
            If str or pathlib.Path: opens and overwrites the file at the given path.
            NOT IMPLEMENTED: io.IOBase
        obs_out_format: The format to write the observable flip data in
            (e.g. "01" or "b8").
        err_out_file: Where to write errors-that-occurred data.
            If None: errors-that-occurred data is not written.
            If str or pathlib.Path: opens and overwrites the file at the given path.
            NOT IMPLEMENTED: io.IOBase
        err_out_format: The format to write the errors-that-occurred data in
            (e.g. "01" or "b8").
        replay_err_in_file: If this is specified, errors are replayed from data
            instead of generated randomly. The following types are supported:
            - None: errors are generated randomly according to the probabilities
                in the detector error model.
            - str or pathlib.Path: the file at the given path is opened and
                errors-to-apply data is read from there.
            - io.IOBase: NOT IMPLEMENTED
        replay_err_in_format: The format to write the errors-that-occurred data in
            (e.g. "01" or "b8").

    Returns:
        Nothing. Results are written to disk.

    Examples:
        >>> import lestim
        >>> import tempfile
        >>> import pathlib
        >>> dem = lestim.DetectorErrorModel('''
        ...    error(0) D0
        ...    error(0) D1
        ...    error(0) D0
        ...    error(1) D1 D2 L0
        ...    error(0) D0
        ... ''')
        >>> sampler = dem.compile_sampler()
        >>> with tempfile.TemporaryDirectory() as d:
        ...     d = pathlib.Path(d)
        ...     sampler.sample_write(
        ...         shots=1,
        ...         det_out_file=d / 'dets.01',
        ...         det_out_format='01',
        ...         obs_out_file=d / 'obs.01',
        ...         obs_out_format='01',
        ...         err_out_file=d / 'err.hits',
        ...         err_out_format='hits',
        ...     )
        ...     with open(d / 'dets.01') as f:
        ...         assert f.read() == "011\n"
        ...     with open(d / 'obs.01') as f:
        ...         assert f.read() == "1\n"
        ...     with open(d / 'err.hits') as f:
        ...         assert f.read() == "3\n"
    """
```

<a name="lestim.CompiledDetectorSampler"></a>
```python
# lestim.CompiledDetectorSampler

# (at top-level in the lestim module)
class CompiledDetectorSampler:
    """An analyzed stabilizer circuit whose detection events can be sampled quickly.
    """
```

<a name="lestim.CompiledDetectorSampler.__init__"></a>
```python
# lestim.CompiledDetectorSampler.__init__

# (in class lestim.CompiledDetectorSampler)
def __init__(
    self,
    circuit: lestim._stim_polyfill.Circuit,
    *,
    seed: object = None,
) -> None:
    """Creates an object that can sample the detection events from a circuit.

    Args:
        circuit: The circuit to sample from.
        seed: PARTIALLY determines simulation results by deterministically seeding
            the random number generator.

            Must be None or an integer in range(2**64).

            Defaults to None. When None, the prng is seeded from system entropy.

            When set to an integer, making the exact same series calls on the exact
            same machine with the exact same version of Stim will produce the exact
            same simulation results.

            CAUTION: simulation results *WILL NOT* be consistent between versions of
            Stim. This restriction is present to make it possible to have future
            optimizations to the random sampling, and is enforced by introducing
            intentional differences in the seeding strategy from version to version.

            CAUTION: simulation results *MAY NOT* be consistent across machines that
            differ in the width of supported SIMD instructions. For example, using
            the same seed on a machine that supports AVX instructions and one that
            only supports SSE instructions may produce different simulation results.

            CAUTION: simulation results *MAY NOT* be consistent if you vary how many
            shots are taken. For example, taking 10 shots and then 90 shots will
            give different results from taking 100 shots in one call.

    Returns:
        An initialized lestim.CompiledDetectorSampler.

    Examples:
        >>> import lestim
        >>> c = lestim.Circuit('''
        ...    H 0
        ...    CNOT 0 1
        ...    X_ERROR(1.0) 0
        ...    M 0 1
        ...    DETECTOR rec[-1] rec[-2]
        ... ''')
        >>> s = c.compile_detector_sampler()
        >>> s.sample(shots=1)
        array([[ True]])
    """
```

<a name="lestim.CompiledDetectorSampler.__repr__"></a>
```python
# lestim.CompiledDetectorSampler.__repr__

# (in class lestim.CompiledDetectorSampler)
def __repr__(
    self,
) -> str:
    """Returns valid python code evaluating to an equivalent `lestim.CompiledDetectorSampler`.
    """
```

<a name="lestim.CompiledDetectorSampler.sample"></a>
```python
# lestim.CompiledDetectorSampler.sample

# (in class lestim.CompiledDetectorSampler)
@overload
def sample(
    self,
    shots: int,
    *,
    prepend_observables: bool = False,
    append_observables: bool = False,
    bit_packed: bool = False,
) -> np.ndarray:
    pass
@overload
def sample(
    self,
    shots: int,
    *,
    separate_observables: Literal[True],
    bit_packed: bool = False,
) -> Tuple[np.ndarray, np.ndarray]:
    pass
def sample(
    self,
    shots: int,
    *,
    prepend_observables: bool = False,
    append_observables: bool = False,
    separate_observables: bool = False,
    bit_packed: bool = False,
) -> Union[np.ndarray, Tuple[np.ndarray, np.ndarray]]:
    """Returns a numpy array containing a batch of detector samples from the circuit.

    The circuit must define the detectors using DETECTOR instructions. Observables
    defined by OBSERVABLE_INCLUDE instructions can also be included in the results
    as honorary detectors.

    Args:
        shots: The number of times to sample every detector in the circuit.
        separate_observables: Defaults to False. When set to True, the return value
            is a (detection_events, observable_flips) tuple instead of a flat
            detection_events array.
        prepend_observables: Defaults to false. When set, observables are included
            with the detectors and are placed at the start of the results.
        append_observables: Defaults to false. When set, observables are included
            with the detectors and are placed at the end of the results.
        bit_packed: Returns a uint8 numpy array with 8 bits per byte, instead of
            a bool_ numpy array with 1 bit per byte. Uses little endian packing.

    Returns:
        A numpy array or tuple of numpy arrays containing the samples.

        if separate_observables=False and bit_packed=False:
            A single numpy array.
            dtype=bool_
            shape=(
                shots,
                num_detectors + num_observables * (
                    append_observables + prepend_observables),
            )
            The bit for detection event `m` in shot `s` is at
                result[s, m]

        if separate_observables=False and bit_packed=True:
            A single numpy array.
            dtype=uint8
            shape=(
                shots,
                math.ceil((num_detectors + num_observables * (
                    append_observables + prepend_observables)) / 8),
            )
            The bit for detection event `m` in shot `s` is at
                (result[s, m // 8] >> (m % 8)) & 1

        if separate_observables=True and bit_packed=False:
            A (dets, obs) tuple.
            dets.dtype=bool_
            dets.shape=(shots, num_detectors)
            obs.dtype=bool_
            obs.shape=(shots, num_observables)
            The bit for detection event `m` in shot `s` is at
                dets[s, m]
            The bit for observable `m` in shot `s` is at
                obs[s, m]

        if separate_observables=True and bit_packed=True:
            A (dets, obs) tuple.
            dets.dtype=uint8
            dets.shape=(shots, math.ceil(num_detectors / 8))
            obs.dtype=uint8
            obs.shape=(shots, math.ceil(num_observables / 8))
            The bit for detection event `m` in shot `s` is at
                (dets[s, m // 8] >> (m % 8)) & 1
            The bit for observable `m` in shot `s` is at
                (obs[s, m // 8] >> (m % 8)) & 1
    """
```

<a name="lestim.CompiledDetectorSampler.sample_write"></a>
```python
# lestim.CompiledDetectorSampler.sample_write

# (in class lestim.CompiledDetectorSampler)
def sample_write(
    self,
    shots: int,
    *,
    filepath: Union[str, pathlib.Path],
    format: 'Literal["01", "b8", "r8", "ptb64", "hits", "dets"]' = '01',
    obs_out_filepath: Optional[Union[str, pathlib.Path]] = None,
    obs_out_format: 'Literal["01", "b8", "r8", "ptb64", "hits", "dets"]' = '01',
    prepend_observables: bool = False,
    append_observables: bool = False,
) -> None:
    """Samples detection events from the circuit and writes them to a file.

    Args:
        shots: The number of times to sample every measurement in the circuit.
        filepath: The file to write the results to.
        format: The output format to write the results with.
            Valid values are "01", "b8", "r8", "hits", "dets", and "ptb64".
            Defaults to "01".
        obs_out_filepath: Sample observables as part of each shot, and write them to
            this file. This keeps the observable data separate from the detector
            data.
        obs_out_format: If writing the observables to a file, this is the format to
            write them in.

            Valid values are "01", "b8", "r8", "hits", "dets", and "ptb64".
            Defaults to "01".
        prepend_observables: Sample observables as part of each shot, and put them
            at the start of the detector data.
        append_observables: Sample observables as part of each shot, and put them at
            the end of the detector data.

    Returns:
        None.

    Examples:
        >>> import lestim
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     path = f"{d}/tmp.dat"
        ...     c = lestim.Circuit('''
        ...         X_ERROR(1) 0
        ...         M 0 1
        ...         DETECTOR rec[-2]
        ...         DETECTOR rec[-1]
        ...     ''')
        ...     c.compile_detector_sampler().sample_write(
        ...         shots=3,
        ...         filepath=path,
        ...         format="dets")
        ...     with open(path) as f:
        ...         print(f.read(), end='')
        shot D0
        shot D0
        shot D0
    """
```

<a name="lestim.CompiledMeasurementSampler"></a>
```python
# lestim.CompiledMeasurementSampler

# (at top-level in the lestim module)
class CompiledMeasurementSampler:
    """An analyzed stabilizer circuit whose measurements can be sampled quickly.
    """
```

<a name="lestim.CompiledMeasurementSampler.__init__"></a>
```python
# lestim.CompiledMeasurementSampler.__init__

# (in class lestim.CompiledMeasurementSampler)
def __init__(
    self,
    circuit: lestim._stim_polyfill.Circuit,
    *,
    skip_reference_sample: bool = False,
    seed: object = None,
    reference_sample: object = None,
) -> None:
    """Creates a measurement sampler for the given circuit.

    The sampler uses a noiseless reference sample, collected from the circuit using
    lestim's Tableau simulator during initialization of the sampler, as a baseline for
    deriving more samples using an error propagation simulator.

    Args:
        circuit: The lestim circuit to sample from.
        skip_reference_sample: Defaults to False. When set to True, the reference
            sample used by the sampler is initialized to all-zeroes instead of being
            collected from the circuit. This means that the results returned by the
            sampler are actually whether or not each measurement was *flipped*,
            instead of true measurement results.

            Forcing an all-zero reference sample is useful when you are only
            interested in error propagation and don't want to have to deal with the
            fact that some measurements want to be On when no errors occur. It is
            also useful when you know for sure that the all-zero result is actually
            a possible result from the circuit (under noiseless execution), meaning
            it is a valid reference sample as good as any other. Computing the
            reference sample is the most time consuming and memory intensive part of
            simulating the circuit, so promising that the simulator can safely skip
            that step is an effective optimization.
        seed: PARTIALLY determines simulation results by deterministically seeding
            the random number generator.

            Must be None or an integer in range(2**64).

            Defaults to None. When None, the prng is seeded from system entropy.

            When set to an integer, making the exact same series calls on the exact
            same machine with the exact same version of Stim will produce the exact
            same simulation results.

            CAUTION: simulation results *WILL NOT* be consistent between versions of
            Stim. This restriction is present to make it possible to have future
            optimizations to the random sampling, and is enforced by introducing
            intentional differences in the seeding strategy from version to version.

            CAUTION: simulation results *MAY NOT* be consistent across machines that
            differ in the width of supported SIMD instructions. For example, using
            the same seed on a machine that supports AVX instructions and one that
            only supports SSE instructions may produce different simulation results.

            CAUTION: simulation results *MAY NOT* be consistent if you vary how many
            shots are taken. For example, taking 10 shots and then 90 shots will
            give different results from taking 100 shots in one call.
        reference_sample: The data to xor into the measurement flips produced by the
            frame simulator, in order to produce proper measurement results.
            This can either be specified as an `np.bool_` array or a bit packed
            `np.uint8` array (little endian). Under normal conditions, the reference
            sample should be a valid noiseless sample of the circuit, such as the
            one returned by `circuit.reference_sample()`. If this argument is not
            provided, the reference sample will be set to
            `circuit.reference_sample()`, unless `skip_reference_sample=True`
            is used, in which case it will be set to all-zeros.

    Returns:
        An initialized lestim.CompiledMeasurementSampler.

    Examples:
        >>> import lestim
        >>> c = lestim.Circuit('''
        ...    X 0   2 3
        ...    M 0 1 2 3
        ... ''')
        >>> s = c.compile_sampler()
        >>> s.sample(shots=1)
        array([[ True, False,  True,  True]])
    """
```

<a name="lestim.CompiledMeasurementSampler.__repr__"></a>
```python
# lestim.CompiledMeasurementSampler.__repr__

# (in class lestim.CompiledMeasurementSampler)
def __repr__(
    self,
) -> str:
    """Returns text that is a valid python expression evaluating to an equivalent `lestim.CompiledMeasurementSampler`.
    """
```

<a name="lestim.CompiledMeasurementSampler.sample"></a>
```python
# lestim.CompiledMeasurementSampler.sample

# (in class lestim.CompiledMeasurementSampler)
def sample(
    self,
    shots: int,
    *,
    bit_packed: bool = False,
) -> np.ndarray:
    """Samples a batch of measurement samples from the circuit.

    Args:
        shots: The number of times to sample every measurement in the circuit.
        bit_packed: Returns a uint8 numpy array with 8 bits per byte, instead of
            a bool_ numpy array with 1 bit per byte. Uses little endian packing.

    Returns:
        A numpy array containing the samples.

        If bit_packed=False:
            dtype=bool_
            shape=(shots, circuit.num_measurements)
            The bit for measurement `m` in shot `s` is at
                result[s, m]
        If bit_packed=True:
            dtype=uint8
            shape=(shots, math.ceil(circuit.num_measurements / 8))
            The bit for measurement `m` in shot `s` is at
                (result[s, m // 8] >> (m % 8)) & 1

    Examples:
        >>> import lestim
        >>> c = lestim.Circuit('''
        ...    X 0   2 3
        ...    M 0 1 2 3
        ... ''')
        >>> s = c.compile_sampler()
        >>> s.sample(shots=1)
        array([[ True, False,  True,  True]])
    """
```

<a name="lestim.CompiledMeasurementSampler.sample_write"></a>
```python
# lestim.CompiledMeasurementSampler.sample_write

# (in class lestim.CompiledMeasurementSampler)
def sample_write(
    self,
    shots: int,
    *,
    filepath: str,
    format: str = '01',
) -> None:
    """Samples measurements from the circuit and writes them to a file.

    Examples:
        >>> import lestim
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     path = f"{d}/tmp.dat"
        ...     c = lestim.Circuit('''
        ...         X 0   2 3
        ...         M 0 1 2 3
        ...     ''')
        ...     c.compile_sampler().sample_write(5, filepath=path, format="01")
        ...     with open(path) as f:
        ...         print(f.read(), end='')
        1011
        1011
        1011
        1011
        1011

    Args:
        shots: The number of times to sample every measurement in the circuit.
        filepath: The file to write the results to.
        format: The output format to write the results with.
            Valid values are "01", "b8", "r8", "hits", "dets", and "ptb64".
            Defaults to "01".

    Returns:
        None.
    """
```

<a name="lestim.CompiledMeasurementsToDetectionEventsConverter"></a>
```python
# lestim.CompiledMeasurementsToDetectionEventsConverter

# (at top-level in the lestim module)
class CompiledMeasurementsToDetectionEventsConverter:
    """A tool for quickly converting measurements from an analyzed stabilizer circuit into detection events.
    """
```

<a name="lestim.CompiledMeasurementsToDetectionEventsConverter.__init__"></a>
```python
# lestim.CompiledMeasurementsToDetectionEventsConverter.__init__

# (in class lestim.CompiledMeasurementsToDetectionEventsConverter)
def __init__(
    self,
    circuit: lestim._stim_polyfill.Circuit,
    *,
    skip_reference_sample: bool = False,
) -> None:
    """Creates a measurement-to-detection-events converter for the given circuit.

    The converter uses a noiseless reference sample, collected from the circuit
    using lestim's Tableau simulator during initialization of the converter, as a
    baseline for determining what the expected value of a detector is.

    Note that the expected behavior of gauge detectors (detectors that are not
    actually deterministic under noiseless execution) can vary depending on the
    reference sample. Stim mitigates this by always generating the same reference
    sample for a given circuit.

    Args:
        circuit: The lestim circuit to use for conversions.
        skip_reference_sample: Defaults to False. When set to True, the reference
            sample used by the converter is initialized to all-zeroes instead of
            being collected from the circuit. This should only be used if it's known
            that the all-zeroes sample is actually a possible result from the
            circuit (under noiseless execution).

    Returns:
        An initialized lestim.CompiledMeasurementsToDetectionEventsConverter.

    Examples:
        >>> import lestim
        >>> import numpy as np
        >>> converter = lestim.Circuit('''
        ...    X 0
        ...    M 0
        ...    DETECTOR rec[-1]
        ... ''').compile_m2d_converter()
        >>> converter.convert(
        ...     measurements=np.array([[0], [1]], dtype=np.bool_),
        ...     append_observables=False,
        ... )
        array([[ True],
               [False]])
    """
```

<a name="lestim.CompiledMeasurementsToDetectionEventsConverter.__repr__"></a>
```python
# lestim.CompiledMeasurementsToDetectionEventsConverter.__repr__

# (in class lestim.CompiledMeasurementsToDetectionEventsConverter)
def __repr__(
    self,
) -> str:
    """Returns text that is a valid python expression evaluating to an equivalent `lestim.CompiledMeasurementsToDetectionEventsConverter`.
    """
```

<a name="lestim.CompiledMeasurementsToDetectionEventsConverter.convert"></a>
```python
# lestim.CompiledMeasurementsToDetectionEventsConverter.convert

# (in class lestim.CompiledMeasurementsToDetectionEventsConverter)
@overload
def convert(
    self,
    *,
    measurements: np.ndarray,
    sweep_bits: Optional[np.ndarray] = None,
    append_observables: bool = False,
    bit_packed: bool = False,
) -> np.ndarray:
    pass
@overload
def convert(
    self,
    *,
    measurements: np.ndarray,
    sweep_bits: Optional[np.ndarray] = None,
    separate_observables: 'Literal[True]',
    append_observables: bool = False,
    bit_packed: bool = False,
) -> Tuple[np.ndarray, np.ndarray]:
    pass
def convert(
    self,
    *,
    measurements: np.ndarray,
    sweep_bits: Optional[np.ndarray] = None,
    separate_observables: bool = False,
    append_observables: bool = False,
    bit_packed: bool = False,
) -> Union[np.ndarray, Tuple[np.ndarray, np.ndarray]]:
    """Converts measurement data into detection event data.

    Args:
        measurements: A numpy array containing measurement data.

            The dtype of the array is used to determine if it is bit packed or not.
            dtype=np.bool_ (unpacked data):
                shape=(num_shots, circuit.num_measurements)
            dtype=np.uint8 (bit packed data):
                shape=(num_shots, math.ceil(circuit.num_measurements / 8))
        sweep_bits: Optional. A numpy array containing sweep data for the `sweep[k]`
            controls in the circuit.

            The dtype of the array is used to determine if it is bit packed or not.
            dtype=np.bool_ (unpacked data):
                shape=(num_shots, circuit.num_sweep_bits)
            dtype=np.uint8 (bit packed data):
                shape=(num_shots, math.ceil(circuit.num_sweep_bits / 8))
        separate_observables: Defaults to False. When set to True, two numpy arrays
            are returned instead of one, with the second array containing the
            observable flip data.
        append_observables: Defaults to False. When set to True, the observables in
            the circuit are treated as if they were additional detectors. Their
            results are appended to the end of the detection event data.
        bit_packed: Defaults to False. When set to True, the returned numpy
            array contains bit packed data (dtype=np.uint8 with 8 bits per item)
            instead of unpacked data (dtype=np.bool_).

    Returns:
        The detection event data and (optionally) observable data. The result is a
        single numpy array if separate_observables is false, otherwise it's a tuple
        of two numpy arrays.

        When returning two numpy arrays, the first array is the detection event data
        and the second is the observable flip data.

        The dtype of the returned arrays is np.bool_ if bit_packed is false,
        otherwise they're np.uint8 arrays.

        shape[0] of the array(s) is the number of shots.
        shape[1] of the array(s) is the number of bits per shot (divided by 8 if bit
        packed) (e.g. for just detection event data it would be
        circuit.num_detectors).

    Examples:
        >>> import lestim
        >>> import numpy as np
        >>> converter = lestim.Circuit('''
        ...    X 0
        ...    M 0 1
        ...    DETECTOR rec[-1]
        ...    DETECTOR rec[-2]
        ...    OBSERVABLE_INCLUDE(0) rec[-2]
        ... ''').compile_m2d_converter()
        >>> dets, obs = converter.convert(
        ...     measurements=np.array([[1, 0],
        ...                            [1, 0],
        ...                            [1, 0],
        ...                            [0, 0],
        ...                            [1, 0]], dtype=np.bool_),
        ...     separate_observables=True,
        ... )
        >>> dets
        array([[False, False],
               [False, False],
               [False, False],
               [False,  True],
               [False, False]])
        >>> obs
        array([[False],
               [False],
               [False],
               [ True],
               [False]])
    """
```

<a name="lestim.CompiledMeasurementsToDetectionEventsConverter.convert_file"></a>
```python
# lestim.CompiledMeasurementsToDetectionEventsConverter.convert_file

# (in class lestim.CompiledMeasurementsToDetectionEventsConverter)
def convert_file(
    self,
    *,
    measurements_filepath: str,
    measurements_format: str = '01',
    sweep_bits_filepath: str = None,
    sweep_bits_format: str = '01',
    detection_events_filepath: str,
    detection_events_format: str = '01',
    append_observables: bool = False,
    obs_out_filepath: str = None,
    obs_out_format: str = '01',
) -> None:
    """Reads measurement data from a file and writes detection events to another file.

    Args:
        measurements_filepath: A file containing measurement data to be converted.
        measurements_format: The format the measurement data is stored in.
            Valid values are "01", "b8", "r8", "hits", "dets", and "ptb64".
            Defaults to "01".
        detection_events_filepath: Where to save detection event data to.
        detection_events_format: The format to save the detection event data in.
            Valid values are "01", "b8", "r8", "hits", "dets", and "ptb64".
            Defaults to "01".
        sweep_bits_filepath: Defaults to None. A file containing sweep data, or
            None. When specified, sweep data (used for `sweep[k]` controls in the
            circuit, which can vary from shot to shot) will be read from the given
            file. When not specified, all sweep bits default to False and no
            sweep-controlled operations occur.
        sweep_bits_format: The format the sweep data is stored in.
            Valid values are "01", "b8", "r8", "hits", "dets", and "ptb64".
            Defaults to "01".
        obs_out_filepath: Sample observables as part of each shot, and write them to
            this file. This keeps the observable data separate from the detector
            data.
        obs_out_format: If writing the observables to a file, this is the format to
            write them in.
            Valid values are "01", "b8", "r8", "hits", "dets", and "ptb64".
            Defaults to "01".
        append_observables: When True, the observables in the circuit are included
            as part of the detection event data. Specifically, they are treated as
            if they were additional detectors at the end of the circuit. When False,
            observable data is not output.

    Examples:
        >>> import lestim
        >>> import tempfile
        >>> converter = lestim.Circuit('''
        ...    X 0
        ...    M 0
        ...    DETECTOR rec[-1]
        ... ''').compile_m2d_converter()
        >>> with tempfile.TemporaryDirectory() as d:
        ...    with open(f"{d}/measurements.01", "w") as f:
        ...        print("0", file=f)
        ...        print("1", file=f)
        ...    converter.convert_file(
        ...        measurements_filepath=f"{d}/measurements.01",
        ...        detection_events_filepath=f"{d}/detections.01",
        ...        append_observables=False,
        ...    )
        ...    with open(f"{d}/detections.01") as f:
        ...        print(f.read(), end="")
        1
        0
    """
```

<a name="lestim.DemInstruction"></a>
```python
# lestim.DemInstruction

# (at top-level in the lestim module)
class DemInstruction:
    """An instruction from a detector error model.

    Examples:
        >>> import lestim
        >>> model = lestim.DetectorErrorModel('''
        ...     error(0.125) D0
        ...     error(0.125) D0 D1 L0
        ...     error(0.125) D1 D2
        ...     error(0.125) D2 D3
        ...     error(0.125) D3
        ... ''')
        >>> instruction = model[0]
        >>> instruction
        lestim.DemInstruction('error', [0.125], [lestim.target_relative_detector_id(0)])
    """
```

<a name="lestim.DemInstruction.__eq__"></a>
```python
# lestim.DemInstruction.__eq__

# (in class lestim.DemInstruction)
def __eq__(
    self,
    arg0: lestim._stim_polyfill.DemInstruction,
) -> bool:
    """Determines if two instructions have identical contents.
    """
```

<a name="lestim.DemInstruction.__init__"></a>
```python
# lestim.DemInstruction.__init__

# (in class lestim.DemInstruction)
def __init__(
    self,
    type: str,
    args: List[float],
    targets: List[object],
) -> None:
    """Creates a lestim.DemInstruction.

    Args:
        type: The name of the instruction type (e.g. "error" or "shift_detectors").
        args: Numeric values parameterizing the instruction (e.g. the 0.1 in
            "error(0.1)").
        targets: The objects the instruction involves (e.g. the "D0" and "L1" in
            "error(0.1) D0 L1").

    Examples:
        >>> import lestim
        >>> instruction = lestim.DemInstruction(
        ...     'error',
        ...     [0.125],
        ...     [lestim.target_relative_detector_id(5)])
        >>> print(instruction)
        error(0.125) D5
    """
```

<a name="lestim.DemInstruction.__ne__"></a>
```python
# lestim.DemInstruction.__ne__

# (in class lestim.DemInstruction)
def __ne__(
    self,
    arg0: lestim._stim_polyfill.DemInstruction,
) -> bool:
    """Determines if two instructions have non-identical contents.
    """
```

<a name="lestim.DemInstruction.__repr__"></a>
```python
# lestim.DemInstruction.__repr__

# (in class lestim.DemInstruction)
def __repr__(
    self,
) -> str:
    """Returns text that is a valid python expression evaluating to an equivalent `lestim.DetectorErrorModel`.
    """
```

<a name="lestim.DemInstruction.__str__"></a>
```python
# lestim.DemInstruction.__str__

# (in class lestim.DemInstruction)
def __str__(
    self,
) -> str:
    """Returns detector error model (.dem) instructions (that can be parsed by lestim) for the model.
    """
```

<a name="lestim.DemInstruction.args_copy"></a>
```python
# lestim.DemInstruction.args_copy

# (in class lestim.DemInstruction)
def args_copy(
    self,
) -> List[float]:
    """Returns a copy of the list of numbers parameterizing the instruction (e.g. the probability of an error).
    """
```

<a name="lestim.DemInstruction.targets_copy"></a>
```python
# lestim.DemInstruction.targets_copy

# (in class lestim.DemInstruction)
def targets_copy(
    self,
) -> List[Union[int, stim.DemTarget]]:
    """Returns a copy of the instruction's targets.

    (Making a copy is enforced to make it clear that editing the result won't change
    the instruction's targets.)
    """
```

<a name="lestim.DemInstruction.type"></a>
```python
# lestim.DemInstruction.type

# (in class lestim.DemInstruction)
@property
def type(
    self,
) -> str:
    """The name of the instruction type (e.g. "error" or "shift_detectors").
    """
```

<a name="lestim.DemRepeatBlock"></a>
```python
# lestim.DemRepeatBlock

# (at top-level in the lestim module)
class DemRepeatBlock:
    """A repeat block from a detector error model.

    Examples:
        >>> import lestim
        >>> model = lestim.DetectorErrorModel('''
        ...     repeat 100 {
        ...         error(0.125) D0 D1
        ...         shift_detectors 1
        ...     }
        ... ''')
        >>> model[0]
        lestim.DemRepeatBlock(100, lestim.DetectorErrorModel('''
            error(0.125) D0 D1
            shift_detectors 1
        '''))
    """
```

<a name="lestim.DemRepeatBlock.__eq__"></a>
```python
# lestim.DemRepeatBlock.__eq__

# (in class lestim.DemRepeatBlock)
def __eq__(
    self,
    arg0: lestim._stim_polyfill.DemRepeatBlock,
) -> bool:
    """Determines if two repeat blocks are identical.
    """
```

<a name="lestim.DemRepeatBlock.__init__"></a>
```python
# lestim.DemRepeatBlock.__init__

# (in class lestim.DemRepeatBlock)
def __init__(
    self,
    repeat_count: int,
    block: lestim._stim_polyfill.DetectorErrorModel,
) -> None:
    """Creates a lestim.DemRepeatBlock.

    Args:
        repeat_count: The number of times the repeat block's body is supposed to
            execute.
        block: The body of the repeat block as a DetectorErrorModel containing the
            instructions to repeat.

    Examples:
        >>> import lestim
        >>> repeat_block = lestim.DemRepeatBlock(100, lestim.DetectorErrorModel('''
        ...     error(0.125) D0 D1
        ...     shift_detectors 1
        ... '''))
    """
```

<a name="lestim.DemRepeatBlock.__ne__"></a>
```python
# lestim.DemRepeatBlock.__ne__

# (in class lestim.DemRepeatBlock)
def __ne__(
    self,
    arg0: lestim._stim_polyfill.DemRepeatBlock,
) -> bool:
    """Determines if two repeat blocks are different.
    """
```

<a name="lestim.DemRepeatBlock.__repr__"></a>
```python
# lestim.DemRepeatBlock.__repr__

# (in class lestim.DemRepeatBlock)
def __repr__(
    self,
) -> str:
    """Returns text that is a valid python expression evaluating to an equivalent `lestim.DemRepeatBlock`.
    """
```

<a name="lestim.DemRepeatBlock.body_copy"></a>
```python
# lestim.DemRepeatBlock.body_copy

# (in class lestim.DemRepeatBlock)
def body_copy(
    self,
) -> lestim._stim_polyfill.DetectorErrorModel:
    """Returns a copy of the block's body, as a lestim.DetectorErrorModel.
    """
```

<a name="lestim.DemRepeatBlock.repeat_count"></a>
```python
# lestim.DemRepeatBlock.repeat_count

# (in class lestim.DemRepeatBlock)
@property
def repeat_count(
    self,
) -> int:
    """The number of times the repeat block's body is supposed to execute.
    """
```

<a name="lestim.DemRepeatBlock.type"></a>
```python
# lestim.DemRepeatBlock.type

# (in class lestim.DemRepeatBlock)
@property
def type(
    self,
) -> object:
    """Returns the type name "repeat".

    This is a duck-typing convenience method. It exists so that code that doesn't
    know whether it has a `lestim.DemInstruction` or a `lestim.DemRepeatBlock`
    can check the type field without having to do an `instanceof` check first.

    Examples:
        >>> import lestim
        >>> dem = lestim.DetectorErrorModel('''
        ...     error(0.1) D0 L0
        ...     repeat 5 {
        ...         error(0.1) D0 D1
        ...         shift_detectors 1
        ...     }
        ...     logical_observable L0
        ... ''')
        >>> [instruction.type for instruction in dem]
        ['error', 'repeat', 'logical_observable']
    """
```

<a name="lestim.DemTarget"></a>
```python
# lestim.DemTarget

# (at top-level in the lestim module)
class DemTarget:
    """An instruction target from a detector error model (.dem) file.
    """
```

<a name="lestim.DemTarget.__eq__"></a>
```python
# lestim.DemTarget.__eq__

# (in class lestim.DemTarget)
def __eq__(
    self,
    arg0: lestim._stim_polyfill.DemTarget,
) -> bool:
    """Determines if two `lestim.DemTarget`s are identical.
    """
```

<a name="lestim.DemTarget.__ne__"></a>
```python
# lestim.DemTarget.__ne__

# (in class lestim.DemTarget)
def __ne__(
    self,
    arg0: lestim._stim_polyfill.DemTarget,
) -> bool:
    """Determines if two `lestim.DemTarget`s are different.
    """
```

<a name="lestim.DemTarget.__repr__"></a>
```python
# lestim.DemTarget.__repr__

# (in class lestim.DemTarget)
def __repr__(
    self,
) -> str:
    """Returns valid python code evaluating to an equivalent `lestim.DemTarget`.
    """
```

<a name="lestim.DemTarget.__str__"></a>
```python
# lestim.DemTarget.__str__

# (in class lestim.DemTarget)
def __str__(
    self,
) -> str:
    """Returns a text description of the detector error model target.
    """
```

<a name="lestim.DemTarget.is_logical_observable_id"></a>
```python
# lestim.DemTarget.is_logical_observable_id

# (in class lestim.DemTarget)
def is_logical_observable_id(
    self,
) -> bool:
    """Determines if the detector error model target is a logical observable id target.

    In a detector error model file, observable targets are prefixed by `L`. For
    example, in `error(0.25) D0 L1` the `L1` is an observable target.
    """
```

<a name="lestim.DemTarget.is_relative_detector_id"></a>
```python
# lestim.DemTarget.is_relative_detector_id

# (in class lestim.DemTarget)
def is_relative_detector_id(
    self,
) -> bool:
    """Determines if the detector error model target is a relative detector id target.

    In a detector error model file, detectors are prefixed by `D`. For
    example, in `error(0.25) D0 L1` the `D0` is a relative detector target.
    """
```

<a name="lestim.DemTarget.is_separator"></a>
```python
# lestim.DemTarget.is_separator

# (in class lestim.DemTarget)
def is_separator(
    self,
) -> bool:
    """Determines if the detector error model target is a separator.

    Separates separate the components of a suggested decompositions within an error.
    For example, the `^` in `error(0.25) D1 D2 ^ D3 D4` is the separator.
    """
```

<a name="lestim.DemTarget.logical_observable_id"></a>
```python
# lestim.DemTarget.logical_observable_id

# (in class lestim.DemTarget)
@staticmethod
def logical_observable_id(
    index: int,
) -> lestim._stim_polyfill.DemTarget:
    """Returns a logical observable id identifying a frame change.

    Args:
        index: The index of the observable.

    Returns:
        The logical observable target.

    Examples:
        >>> import lestim
        >>> m = lestim.DetectorErrorModel()
        >>> m.append("error", 0.25, [
        ...     lestim.DemTarget.logical_observable_id(13)
        ... ])
        >>> print(repr(m))
        lestim.DetectorErrorModel('''
            error(0.25) L13
        ''')
    """
```

<a name="lestim.DemTarget.relative_detector_id"></a>
```python
# lestim.DemTarget.relative_detector_id

# (in class lestim.DemTarget)
@staticmethod
def relative_detector_id(
    index: int,
) -> lestim._stim_polyfill.DemTarget:
    """Returns a relative detector id (e.g. "D5" in a .dem file).

    Args:
        index: The index of the detector, relative to the current detector offset.

    Returns:
        The relative detector target.

    Examples:
        >>> import lestim
        >>> m = lestim.DetectorErrorModel()
        >>> m.append("error", 0.25, [
        ...     lestim.DemTarget.relative_detector_id(13)
        ... ])
        >>> print(repr(m))
        lestim.DetectorErrorModel('''
            error(0.25) D13
        ''')
    """
```

<a name="lestim.DemTarget.separator"></a>
```python
# lestim.DemTarget.separator

# (in class lestim.DemTarget)
@staticmethod
def separator(
) -> lestim._stim_polyfill.DemTarget:
    """Returns a target separator (e.g. "^" in a .dem file).

    Examples:
        >>> import lestim
        >>> m = lestim.DetectorErrorModel()
        >>> m.append("error", 0.25, [
        ...     lestim.DemTarget.relative_detector_id(1),
        ...     lestim.DemTarget.separator(),
        ...     lestim.DemTarget.relative_detector_id(2),
        ... ])
        >>> print(repr(m))
        lestim.DetectorErrorModel('''
            error(0.25) D1 ^ D2
        ''')
    """
```

<a name="lestim.DemTarget.val"></a>
```python
# lestim.DemTarget.val

# (in class lestim.DemTarget)
@property
def val(
    self,
) -> int:
    """Returns the target's integer value.

    Example:

        >>> import lestim
        >>> lestim.target_relative_detector_id(5).val
        5
        >>> lestim.target_logical_observable_id(6).val
        6
    """
```

<a name="lestim.DemTargetWithCoords"></a>
```python
# lestim.DemTargetWithCoords

# (at top-level in the lestim module)
class DemTargetWithCoords:
    """A detector error model instruction target with associated coords.

    It is also guaranteed that, if the type of the DEM target is a
    relative detector id, it is actually absolute (i.e. relative to
    0).

    For example, if the DEM target is a detector from a circuit with
    coordinate arguments given to detectors, the coords field will
    contain the coordinate data for the detector.

    This is helpful information to have available when debugging a
    problem in a circuit, instead of having to constantly manually
    look up the coordinates of a detector index in order to understand
    what is happening.
    """
```

<a name="lestim.DemTargetWithCoords.__init__"></a>
```python
# lestim.DemTargetWithCoords.__init__

# (in class lestim.DemTargetWithCoords)
def __init__(
    self,
    *,
    dem_target: lestim._stim_polyfill.DemTarget,
    coords: List[float],
) -> None:
    """Creates a lestim.DemTargetWithCoords.
    """
```

<a name="lestim.DemTargetWithCoords.coords"></a>
```python
# lestim.DemTargetWithCoords.coords

# (in class lestim.DemTargetWithCoords)
@property
def coords(
    self,
) -> List[float]:
    """Returns the associated coordinate information as a list of floats.

    If there is no coordinate information, returns an empty list.
    """
```

<a name="lestim.DemTargetWithCoords.dem_target"></a>
```python
# lestim.DemTargetWithCoords.dem_target

# (in class lestim.DemTargetWithCoords)
@property
def dem_target(
    self,
) -> lestim._stim_polyfill.DemTarget:
    """Returns the actual DEM target as a `lestim.DemTarget`.
    """
```

<a name="lestim.DetectorErrorModel"></a>
```python
# lestim.DetectorErrorModel

# (at top-level in the lestim module)
class DetectorErrorModel:
    """An error model built out of independent error mechanics.

    This class is one of the most important classes in Stim, because it is the
    mechanism used to explain circuits to decoders. A typical workflow would
    look something like:

        1. Create a quantum error correction circuit annotated with detectors
            and observables.
        2. Fail at configuring your favorite decoder using the circuit, because
            it's a pain to convert circuit error mechanisms into a format
            understood by the decoder.
        2a. Call circuit.detector_error_model(), with decompose_errors=True
            if working with a matching-based code. This converts the circuit
            errors into a straightforward list of independent "with
            probability p these detectors and observables get flipped" terms.
        3. Write tedious but straightforward glue code to create whatever
            graph-like object the decoder needs from the detector error model.
        3a. Actually, ideally, someone has already done that for you. For
            example, pymatching can take detector error models directly and
            sinter knows how to explain a detector error model to fusion_blossom.
        4. Get samples using circuit.compile_detector_sampler(), feed them to
            the decoder, and compare its observable flip predictions to the
            actual flips recorded in the samples.
        4a. Actually, sinter will basically handle steps 2 through 4 for you.
            So you should probably have just generated your circuits, called
            `sinter collect` on them, then `sinter plot` on the results.
        5. Write the paper.

    Error mechanisms are described in terms of the visible detection events and the
    hidden observable frame changes that they causes. Error mechanisms can also
    suggest decompositions of their effects into components, which can be helpful
    for decoders that want to work with a simpler decomposed error model instead of
    the full error model.

    Examples:
        >>> import lestim
        >>> model = lestim.DetectorErrorModel('''
        ...     error(0.125) D0
        ...     error(0.125) D0 D1 L0
        ...     error(0.125) D1 D2
        ...     error(0.125) D2 D3
        ...     error(0.125) D3
        ... ''')
        >>> len(model)
        5

        >>> lestim.Circuit('''
        ...     X_ERROR(0.125) 0
        ...     X_ERROR(0.25) 1
        ...     CORRELATED_ERROR(0.375) X0 X1
        ...     M 0 1
        ...     DETECTOR rec[-2]
        ...     DETECTOR rec[-1]
        ... ''').detector_error_model()
        lestim.DetectorErrorModel('''
            error(0.125) D0
            error(0.375) D0 D1
            error(0.25) D1
        ''')
    """
```

<a name="lestim.DetectorErrorModel.__add__"></a>
```python
# lestim.DetectorErrorModel.__add__

# (in class lestim.DetectorErrorModel)
def __add__(
    self,
    second: lestim._stim_polyfill.DetectorErrorModel,
) -> lestim._stim_polyfill.DetectorErrorModel:
    """Creates a detector error model by appending two models.

    Examples:
        >>> import lestim
        >>> m1 = lestim.DetectorErrorModel('''
        ...    error(0.125) D0
        ... ''')
        >>> m2 = lestim.DetectorErrorModel('''
        ...    error(0.25) D1
        ... ''')
        >>> m1 + m2
        lestim.DetectorErrorModel('''
            error(0.125) D0
            error(0.25) D1
        ''')
    """
```

<a name="lestim.DetectorErrorModel.__eq__"></a>
```python
# lestim.DetectorErrorModel.__eq__

# (in class lestim.DetectorErrorModel)
def __eq__(
    self,
    arg0: lestim._stim_polyfill.DetectorErrorModel,
) -> bool:
    """Determines if two detector error models have identical contents.
    """
```

<a name="lestim.DetectorErrorModel.__getitem__"></a>
```python
# lestim.DetectorErrorModel.__getitem__

# (in class lestim.DetectorErrorModel)
@overload
def __getitem__(
    self,
    index_or_slice: int,
) -> Union[stim.DemInstruction, stim.DemRepeatBlock]:
    pass
@overload
def __getitem__(
    self,
    index_or_slice: slice,
) -> stim.DetectorErrorModel:
    pass
def __getitem__(
    self,
    index_or_slice: object,
) -> object:
    """Returns copies of instructions from the detector error model.

    Args:
        index_or_slice: An integer index picking out an instruction to return, or a
            slice picking out a range of instructions to return as a detector error
            model.

    Examples:
        >>> import lestim
        >>> model = lestim.DetectorErrorModel('''
        ...    error(0.125) D0
        ...    error(0.125) D1 L1
        ...    repeat 100 {
        ...        error(0.125) D1 D2
        ...        shift_detectors 1
        ...    }
        ...    error(0.125) D2
        ...    logical_observable L0
        ...    detector D5
        ... ''')
        >>> model[0]
        lestim.DemInstruction('error', [0.125], [lestim.target_relative_detector_id(0)])
        >>> model[2]
        lestim.DemRepeatBlock(100, lestim.DetectorErrorModel('''
            error(0.125) D1 D2
            shift_detectors 1
        '''))
        >>> model[1::2]
        lestim.DetectorErrorModel('''
            error(0.125) D1 L1
            error(0.125) D2
            detector D5
        ''')
    """
```

<a name="lestim.DetectorErrorModel.__iadd__"></a>
```python
# lestim.DetectorErrorModel.__iadd__

# (in class lestim.DetectorErrorModel)
def __iadd__(
    self,
    second: lestim._stim_polyfill.DetectorErrorModel,
) -> lestim._stim_polyfill.DetectorErrorModel:
    """Appends a detector error model into the receiving model (mutating it).

    Examples:
        >>> import lestim
        >>> m1 = lestim.DetectorErrorModel('''
        ...    error(0.125) D0
        ... ''')
        >>> m2 = lestim.DetectorErrorModel('''
        ...    error(0.25) D1
        ... ''')
        >>> m1 += m2
        >>> print(repr(m1))
        lestim.DetectorErrorModel('''
            error(0.125) D0
            error(0.25) D1
        ''')
    """
```

<a name="lestim.DetectorErrorModel.__imul__"></a>
```python
# lestim.DetectorErrorModel.__imul__

# (in class lestim.DetectorErrorModel)
def __imul__(
    self,
    repetitions: int,
) -> lestim._stim_polyfill.DetectorErrorModel:
    """Mutates the detector error model by putting its contents into a repeat block.

    Special case: if the repetition count is 0, the model is cleared.
    Special case: if the repetition count is 1, nothing happens.

    Args:
        repetitions: The number of times the repeat block should repeat.

    Examples:
        >>> import lestim
        >>> m = lestim.DetectorErrorModel('''
        ...    error(0.25) D0
        ...    shift_detectors 1
        ... ''')
        >>> m *= 3
        >>> print(m)
        repeat 3 {
            error(0.25) D0
            shift_detectors 1
        }
    """
```

<a name="lestim.DetectorErrorModel.__init__"></a>
```python
# lestim.DetectorErrorModel.__init__

# (in class lestim.DetectorErrorModel)
def __init__(
    self,
    detector_error_model_text: str = '',
) -> None:
    """Creates a lestim.DetectorErrorModel.

    Args:
        detector_error_model_text: Defaults to empty. Describes instructions to
            append into the circuit in the detector error model (.dem) format.

    Examples:
        >>> import lestim
        >>> empty = lestim.DetectorErrorModel()
        >>> not_empty = lestim.DetectorErrorModel('''
        ...    error(0.125) D0 L0
        ... ''')
    """
```

<a name="lestim.DetectorErrorModel.__len__"></a>
```python
# lestim.DetectorErrorModel.__len__

# (in class lestim.DetectorErrorModel)
def __len__(
    self,
) -> int:
    """Returns the number of top-level instructions/blocks in the detector error model.

    Instructions inside of blocks are not included in this count.

    Examples:
        >>> import lestim
        >>> len(lestim.DetectorErrorModel())
        0
        >>> len(lestim.DetectorErrorModel('''
        ...    error(0.1) D0 D1
        ...    shift_detectors 100
        ...    logical_observable L5
        ... '''))
        3
        >>> len(lestim.DetectorErrorModel('''
        ...    repeat 100 {
        ...        error(0.1) D0 D1
        ...        error(0.1) D1 D2
        ...    }
        ... '''))
        1
    """
```

<a name="lestim.DetectorErrorModel.__mul__"></a>
```python
# lestim.DetectorErrorModel.__mul__

# (in class lestim.DetectorErrorModel)
def __mul__(
    self,
    repetitions: int,
) -> lestim._stim_polyfill.DetectorErrorModel:
    """Repeats the detector error model using a repeat block.

    Has special cases for 0 repetitions and 1 repetitions.

    Args:
        repetitions: The number of times the repeat block should repeat.

    Returns:
        repetitions=0: An empty detector error model.
        repetitions=1: A copy of this detector error model.
        repetitions>=2: A detector error model with a single repeat block, where the
        contents of that repeat block are this detector error model.

    Examples:
        >>> import lestim
        >>> m = lestim.DetectorErrorModel('''
        ...    error(0.25) D0
        ...    shift_detectors 1
        ... ''')
        >>> m * 3
        lestim.DetectorErrorModel('''
            repeat 3 {
                error(0.25) D0
                shift_detectors 1
            }
        ''')
    """
```

<a name="lestim.DetectorErrorModel.__ne__"></a>
```python
# lestim.DetectorErrorModel.__ne__

# (in class lestim.DetectorErrorModel)
def __ne__(
    self,
    arg0: lestim._stim_polyfill.DetectorErrorModel,
) -> bool:
    """Determines if two detector error models have non-identical contents.
    """
```

<a name="lestim.DetectorErrorModel.__repr__"></a>
```python
# lestim.DetectorErrorModel.__repr__

# (in class lestim.DetectorErrorModel)
def __repr__(
    self,
) -> str:
    """Returns valid python code evaluating to an equivalent `lestim.DetectorErrorModel`.
    """
```

<a name="lestim.DetectorErrorModel.__rmul__"></a>
```python
# lestim.DetectorErrorModel.__rmul__

# (in class lestim.DetectorErrorModel)
def __rmul__(
    self,
    repetitions: int,
) -> lestim._stim_polyfill.DetectorErrorModel:
    """Repeats the detector error model using a repeat block.

    Has special cases for 0 repetitions and 1 repetitions.

    Args:
        repetitions: The number of times the repeat block should repeat.

    Returns:
        repetitions=0: An empty detector error model.
        repetitions=1: A copy of this detector error model.
        repetitions>=2: A detector error model with a single repeat block, where the
        contents of that repeat block are this detector error model.

    Examples:
        >>> import lestim
        >>> m = lestim.DetectorErrorModel('''
        ...    error(0.25) D0
        ...    shift_detectors 1
        ... ''')
        >>> 3 * m
        lestim.DetectorErrorModel('''
            repeat 3 {
                error(0.25) D0
                shift_detectors 1
            }
        ''')
    """
```

<a name="lestim.DetectorErrorModel.__str__"></a>
```python
# lestim.DetectorErrorModel.__str__

# (in class lestim.DetectorErrorModel)
def __str__(
    self,
) -> str:
    """Returns the contents of a detector error model file (.dem) encoding the model.
    """
```

<a name="lestim.DetectorErrorModel.append"></a>
```python
# lestim.DetectorErrorModel.append

# (in class lestim.DetectorErrorModel)
def append(
    self,
    instruction: object,
    parens_arguments: object = None,
    targets: List[object] = (),
) -> None:
    """Appends an instruction to the detector error model.

    Args:
        instruction: Either the name of an instruction, a lestim.DemInstruction, or a
            lestim.DemRepeatBlock. The `parens_arguments` and `targets` arguments are
            given if and only if the instruction is a name.
        parens_arguments: Numeric values parameterizing the instruction. The numbers
            inside parentheses in a detector error model file (eg. the `0.25` in
            `error(0.25) D0`). This argument can be given either a list of doubles,
            or a single double (which will be implicitly wrapped into a list).
        targets: The instruction targets, such as the `D0` in `error(0.25) D0`.

    Examples:
        >>> import lestim
        >>> m = lestim.DetectorErrorModel()
        >>> m.append("error", 0.125, [
        ...     lestim.DemTarget.relative_detector_id(1),
        ... ])
        >>> m.append("error", 0.25, [
        ...     lestim.DemTarget.relative_detector_id(1),
        ...     lestim.DemTarget.separator(),
        ...     lestim.DemTarget.relative_detector_id(2),
        ...     lestim.DemTarget.logical_observable_id(3),
        ... ])
        >>> print(repr(m))
        lestim.DetectorErrorModel('''
            error(0.125) D1
            error(0.25) D1 ^ D2 L3
        ''')

        >>> m.append("shift_detectors", (1, 2, 3), [5])
        >>> print(repr(m))
        lestim.DetectorErrorModel('''
            error(0.125) D1
            error(0.25) D1 ^ D2 L3
            shift_detectors(1, 2, 3) 5
        ''')

        >>> m += m * 3
        >>> m.append(m[0])
        >>> m.append(m[-2])
        >>> print(repr(m))
        lestim.DetectorErrorModel('''
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
        ''')
    """
```

<a name="lestim.DetectorErrorModel.approx_equals"></a>
```python
# lestim.DetectorErrorModel.approx_equals

# (in class lestim.DetectorErrorModel)
def approx_equals(
    self,
    other: object,
    *,
    atol: float,
) -> bool:
    """Checks if detector error models are approximately equal.

    Two detector error model are approximately equal if they are equal up to slight
    perturbations of instruction arguments such as probabilities. For example
    `error(0.100) D0` is approximately equal to `error(0.099) D0` within an absolute
    tolerance of 0.002. All other details of the models (such as the ordering of
    errors and their targets) must be exactly the same.

    Args:
        other: The detector error model, or other object, to compare to this one.
        atol: The absolute error tolerance. The maximum amount each probability may
            have been perturbed by.

    Returns:
        True if the given object is a detector error model approximately equal up to
        the receiving circuit up to the given tolerance, otherwise False.

    Examples:
        >>> import lestim
        >>> base = lestim.DetectorErrorModel('''
        ...    error(0.099) D0 D1
        ... ''')

        >>> base.approx_equals(base, atol=0)
        True

        >>> base.approx_equals(lestim.DetectorErrorModel('''
        ...    error(0.101) D0 D1
        ... '''), atol=0)
        False

        >>> base.approx_equals(lestim.DetectorErrorModel('''
        ...    error(0.101) D0 D1
        ... '''), atol=0.0001)
        False

        >>> base.approx_equals(lestim.DetectorErrorModel('''
        ...    error(0.101) D0 D1
        ... '''), atol=0.01)
        True

        >>> base.approx_equals(lestim.DetectorErrorModel('''
        ...    error(0.099) D0 D1 L0 L1 L2 L3 L4
        ... '''), atol=9999)
        False
    """
```

<a name="lestim.DetectorErrorModel.clear"></a>
```python
# lestim.DetectorErrorModel.clear

# (in class lestim.DetectorErrorModel)
def clear(
    self,
) -> None:
    """Clears the contents of the detector error model.

    Examples:
        >>> import lestim
        >>> model = lestim.DetectorErrorModel('''
        ...    error(0.1) D0 D1
        ... ''')
        >>> model.clear()
        >>> model
        lestim.DetectorErrorModel()
    """
```

<a name="lestim.DetectorErrorModel.compile_sampler"></a>
```python
# lestim.DetectorErrorModel.compile_sampler

# (in class lestim.DetectorErrorModel)
def compile_sampler(
    self,
    *,
    seed: object = None,
) -> lestim._stim_polyfill.CompiledDemSampler:
    """Returns a CompiledDemSampler that can batch sample from detector error models.

    Args:
        seed: PARTIALLY determines simulation results by deterministically seeding
            the random number generator.

            Must be None or an integer in range(2**64).

            Defaults to None. When None, the prng is seeded from system entropy.

            When set to an integer, making the exact same series calls on the exact
            same machine with the exact same version of Stim will produce the exact
            same simulation results.

            CAUTION: simulation results *WILL NOT* be consistent between versions of
            Stim. This restriction is present to make it possible to have future
            optimizations to the random sampling, and is enforced by introducing
            intentional differences in the seeding strategy from version to version.

            CAUTION: simulation results *MAY NOT* be consistent across machines that
            differ in the width of supported SIMD instructions. For example, using
            the same seed on a machine that supports AVX instructions and one that
            only supports SSE instructions may produce different simulation results.

            CAUTION: simulation results *MAY NOT* be consistent if you vary how many
            shots are taken. For example, taking 10 shots and then 90 shots will
            give different results from taking 100 shots in one call.

    Returns:
        A seeded lestim.CompiledDemSampler for the given detector error model.

    Examples:
        >>> import lestim
        >>> dem = lestim.DetectorErrorModel('''
        ...    error(0) D0
        ...    error(1) D1 D2 L0
        ... ''')
        >>> sampler = dem.compile_sampler()
        >>> det_data, obs_data, err_data = sampler.sample(
        ...     shots=4,
        ...     return_errors=True)
        >>> det_data
        array([[False,  True,  True],
               [False,  True,  True],
               [False,  True,  True],
               [False,  True,  True]])
        >>> obs_data
        array([[ True],
               [ True],
               [ True],
               [ True]])
        >>> err_data
        array([[False,  True],
               [False,  True],
               [False,  True],
               [False,  True]])
    """
```

<a name="lestim.DetectorErrorModel.copy"></a>
```python
# lestim.DetectorErrorModel.copy

# (in class lestim.DetectorErrorModel)
def copy(
    self,
) -> lestim._stim_polyfill.DetectorErrorModel:
    """Returns a copy of the detector error model.

    The copy is an independent detector error model with the same contents.

    Examples:
        >>> import lestim

        >>> c1 = lestim.DetectorErrorModel("error(0.1) D0 D1")
        >>> c2 = c1.copy()
        >>> c2 is c1
        False
        >>> c2 == c1
        True
    """
```

<a name="lestim.DetectorErrorModel.diagram"></a>
```python
# lestim.DetectorErrorModel.diagram

# (in class lestim.DetectorErrorModel)
def diagram(
    self,
    type: str,
) -> Any:
    """Returns a diagram of the circuit, from a variety of options.

    Args:
        type: The type of diagram. Available types are:
            "matchgraph-svg": An image of the decoding graph of the
                detector error model. Red lines are errors crossing a
                logical observable. Blue lines are undecomposed hyper
                errors.
            "matchgraph-svg-html": Same as matchgraph-svg but with the
                SVG wrapped in a resizable HTML iframe.
            "matchgraph-3d": A 3d model of the decoding graph of the
                detector error model. Red lines are errors crossing a
                logical observable. Blue lines are undecomposed hyper
                errors.

                GLTF files can be opened with a variety of programs, or
                opened online in viewers such as
                https://gltf-viewer.donmccurdy.com/ . Red lines are
                errors crossing a logical observable.
            "matchgraph-3d-html": Same 3d model as 'match-graph-3d' but
                embedded into an HTML web page containing an interactive
                THREE.js viewer for the 3d model.

    Returns:
        An object whose `__str__` method returns the diagram, so that
        writing the diagram to a file works correctly. The returned
        object also defines a `_repr_html_` method, so that ipython
        notebooks recognize it can be shown using a specialized
        viewer instead of as raw text.

    Examples:
        >>> import lestim
        >>> import tempfile
        >>> circuit = lestim.Circuit.generated(
        ...     "repetition_code:memory",
        ...     rounds=10,
        ...     distance=7,
        ...     after_clifford_depolarization=0.01)
        >>> dem = circuit.detector_error_model(decompose_errors=True)

        >>> with tempfile.TemporaryDirectory() as d:
        ...     diagram = circuit.diagram("match-graph-svg")
        ...     with open(f"{d}/dem_image.svg", "w") as f:
        ...         print(diagram, file=f)

        >>> with tempfile.TemporaryDirectory() as d:
        ...     diagram = circuit.diagram("match-graph-3d")
        ...     with open(f"{d}/dem_3d_model.gltf", "w") as f:
        ...         print(diagram, file=f)
    """
```

<a name="lestim.DetectorErrorModel.flattened"></a>
```python
# lestim.DetectorErrorModel.flattened

# (in class lestim.DetectorErrorModel)
def flattened(
    self,
) -> lestim._stim_polyfill.DetectorErrorModel:
    """Returns the detector error model without repeat or detector_shift instructions.

    Returns:
        A `lestim.DetectorErrorModel` with the same errors in the same order, but with
        repeat loops flattened into actually repeated instructions and with all
        coordinate/index shifts inlined.

    Examples:
        >>> import lestim
        >>> lestim.DetectorErrorModel('''
        ...     error(0.125) D0
        ...     REPEAT 5 {
        ...         error(0.25) D0 D1
        ...         shift_detectors 1
        ...     }
        ...     error(0.125) D0 L0
        ... ''').flattened()
        lestim.DetectorErrorModel('''
            error(0.125) D0
            error(0.25) D0 D1
            error(0.25) D1 D2
            error(0.25) D2 D3
            error(0.25) D3 D4
            error(0.25) D4 D5
            error(0.125) D5 L0
        ''')
    """
```

<a name="lestim.DetectorErrorModel.from_file"></a>
```python
# lestim.DetectorErrorModel.from_file

# (in class lestim.DetectorErrorModel)
@staticmethod
def from_file(
    file: Union[io.TextIOBase, str, pathlib.Path],
) -> stim.DetectorErrorModel:
    """Reads a detector error model from a file.

    The file format is defined at
    https://github.com/quantumlib/Stim/blob/main/doc/file_format_dem_detector_error_model.md

    Args:
        file: A file path or open file object to read from.

    Returns:
        The circuit parsed from the file.

    Examples:
        >>> import lestim
        >>> import tempfile

        >>> with tempfile.TemporaryDirectory() as tmpdir:
        ...     path = tmpdir + '/tmp.lestim'
        ...     with open(path, 'w') as f:
        ...         print('error(0.25) D2 D3', file=f)
        ...     circuit = lestim.DetectorErrorModel.from_file(path)
        >>> circuit
        lestim.DetectorErrorModel('''
            error(0.25) D2 D3
        ''')

        >>> with tempfile.TemporaryDirectory() as tmpdir:
        ...     path = tmpdir + '/tmp.lestim'
        ...     with open(path, 'w') as f:
        ...         print('error(0.25) D2 D3', file=f)
        ...     with open(path) as f:
        ...         circuit = lestim.DetectorErrorModel.from_file(path)
        >>> circuit
        lestim.DetectorErrorModel('''
            error(0.25) D2 D3
        ''')
    """
```

<a name="lestim.DetectorErrorModel.get_detector_coordinates"></a>
```python
# lestim.DetectorErrorModel.get_detector_coordinates

# (in class lestim.DetectorErrorModel)
def get_detector_coordinates(
    self,
    only: object = None,
) -> Dict[int, List[float]]:
    """Returns the coordinate metadata of detectors in the detector error model.

    Args:
        only: Defaults to None (meaning include all detectors). A list of detector
            indices to include in the result. Detector indices beyond the end of the
            detector error model cause an error.

    Returns:
        A dictionary mapping integers (detector indices) to lists of floats
        (coordinates). Detectors with no specified coordinate data are mapped to an
        empty tuple. If `only` is specified, then `set(result.keys()) == set(only)`.

    Examples:
        >>> import lestim
        >>> dem = lestim.DetectorErrorModel('''
        ...    error(0.25) D0 D1
        ...    detector(1, 2, 3) D1
        ...    shift_detectors(5) 1
        ...    detector(1, 2) D2
        ... ''')
        >>> dem.get_detector_coordinates()
        {0: [], 1: [1.0, 2.0, 3.0], 2: [], 3: [6.0, 2.0]}
        >>> dem.get_detector_coordinates(only=[1])
        {1: [1.0, 2.0, 3.0]}
    """
```

<a name="lestim.DetectorErrorModel.num_detectors"></a>
```python
# lestim.DetectorErrorModel.num_detectors

# (in class lestim.DetectorErrorModel)
@property
def num_detectors(
    self,
) -> int:
    """Counts the number of detectors (e.g. `D2`) in the error model.

    Detector indices are assumed to be contiguous from 0 up to whatever the maximum
    detector id is. If the largest detector's absolute id is n-1, then the number of
    detectors is n.

    Examples:
        >>> import lestim

        >>> lestim.Circuit('''
        ...     X_ERROR(0.125) 0
        ...     X_ERROR(0.25) 1
        ...     CORRELATED_ERROR(0.375) X0 X1
        ...     M 0 1
        ...     DETECTOR rec[-2]
        ...     DETECTOR rec[-1]
        ... ''').detector_error_model().num_detectors
        2

        >>> lestim.DetectorErrorModel('''
        ...    error(0.1) D0 D199
        ... ''').num_detectors
        200

        >>> lestim.DetectorErrorModel('''
        ...    shift_detectors 1000
        ...    error(0.1) D0 D199
        ... ''').num_detectors
        1200
    """
```

<a name="lestim.DetectorErrorModel.num_errors"></a>
```python
# lestim.DetectorErrorModel.num_errors

# (in class lestim.DetectorErrorModel)
@property
def num_errors(
    self,
) -> int:
    """Counts the number of errors (e.g. `error(0.1) D0`) in the error model.

    Error instructions inside repeat blocks count once per repetition.
    Redundant errors with the same targets count as separate errors.

    Examples:
        >>> import lestim

        >>> lestim.DetectorErrorModel('''
        ...     error(0.125) D0
        ...     repeat 100 {
        ...         repeat 5 {
        ...             error(0.25) D1
        ...         }
        ...     }
        ... ''').num_errors
        501
    """
```

<a name="lestim.DetectorErrorModel.num_observables"></a>
```python
# lestim.DetectorErrorModel.num_observables

# (in class lestim.DetectorErrorModel)
@property
def num_observables(
    self,
) -> int:
    """Counts the number of frame changes (e.g. `L2`) in the error model.

    Observable indices are assumed to be contiguous from 0 up to whatever the
    maximum observable id is. If the largest observable's id is n-1, then the number
    of observables is n.

    Examples:
        >>> import lestim

        >>> lestim.Circuit('''
        ...     X_ERROR(0.125) 0
        ...     M 0
        ...     OBSERVABLE_INCLUDE(99) rec[-1]
        ... ''').detector_error_model().num_observables
        100

        >>> lestim.DetectorErrorModel('''
        ...    error(0.1) L399
        ... ''').num_observables
        400
    """
```

<a name="lestim.DetectorErrorModel.rounded"></a>
```python
# lestim.DetectorErrorModel.rounded

# (in class lestim.DetectorErrorModel)
def rounded(
    self,
    arg0: int,
) -> lestim._stim_polyfill.DetectorErrorModel:
    """Creates an equivalent detector error model but with rounded error probabilities.

    Args:
        digits: The number of digits to round to.

    Returns:
        A `lestim.DetectorErrorModel` with the same instructions in the same order,
        but with the parens arguments of error instructions rounded to the given
        precision.

        Instructions whose error probability was rounded to zero are still
        included in the output.

    Examples:
        >>> import lestim
        >>> dem = lestim.DetectorErrorModel('''
        ...     error(0.019499) D0
        ...     error(0.000001) D0 D1
        ... ''')

        >>> dem.rounded(2)
        lestim.DetectorErrorModel('''
            error(0.02) D0
            error(0) D0 D1
        ''')

        >>> dem.rounded(3)
        lestim.DetectorErrorModel('''
            error(0.019) D0
            error(0) D0 D1
        ''')
    """
```

<a name="lestim.DetectorErrorModel.shortest_graphlike_error"></a>
```python
# lestim.DetectorErrorModel.shortest_graphlike_error

# (in class lestim.DetectorErrorModel)
def shortest_graphlike_error(
    self,
    ignore_ungraphlike_errors: bool = True,
) -> lestim._stim_polyfill.DetectorErrorModel:
    """Finds a minimum set of graphlike errors to produce an undetected logical error.

    Note that this method does not pay attention to error probabilities (other than
    ignoring errors with probability 0). It searches for a logical error with the
    minimum *number* of physical errors, not the maximum probability of those
    physical errors all occurring.

    This method works by looking for errors that have frame changes (eg.
    "error(0.1) D0 D1 L5" flips the frame of observable 5). These errors are
    converted into one or two symptoms and a net frame change. The symptoms can then
    be moved around by following errors touching that symptom. Each symptom is moved
    until it disappears into a boundary or cancels against another remaining
    symptom, while leaving the other symptoms alone (ensuring only one symptom is
    allowed to move significantly reduces waste in the search space). Eventually a
    path or cycle of errors is found that cancels out the symptoms, and if there is
    still a frame change at that point then that path or cycle is a logical error
    (otherwise all that was found was a stabilizer of the system; a dead end). The
    search process advances like a breadth first search, seeded from all the
    frame-change errors and branching them outward in tandem, until one of them wins
    the race to find a solution.

    Args:
        ignore_ungraphlike_errors: Defaults to False. When False, an exception is
            raised if there are any errors in the model that are not graphlike. When
            True, those errors are skipped as if they weren't present.

            A graphlike error is an error with less than two symptoms. For the
            purposes of this method, errors are also considered graphlike if they
            are decomposed into graphlike components:

            graphlike:
                error(0.1) D0
                error(0.1) D0 D1
                error(0.1) D0 D1 L0
            not graphlike but decomposed into graphlike components:
                error(0.1) D0 D1 ^ D2
            not graphlike, not decomposed into graphlike components:
                error(0.1) D0 D1 D2
                error(0.1) D0 D1 D2 ^ D3

    Returns:
        A detector error model containing just the error instructions corresponding
        to an undetectable logical error. There will be no other kinds of
        instructions (no `repeat`s, no `shift_detectors`, etc). The error
        probabilities will all be set to 1.

        The `len` of the returned model is the graphlike code distance of the
        circuit. But beware that in general the true code distance may be smaller.
        For example, in the XZ surface code with twists, the true minimum sized
        logical error is likely to use Y errors. But each Y error decomposes into
        two graphlike components (the X part and the Z part). As a result, the
        graphlike code distance in that context is likely to be nearly twice as
        large as the true code distance.

    Examples:
        >>> import lestim

        >>> lestim.DetectorErrorModel('''
        ...     error(0.125) D0
        ...     error(0.125) D0 D1
        ...     error(0.125) D1 L55
        ...     error(0.125) D1
        ... ''').shortest_graphlike_error()
        lestim.DetectorErrorModel('''
            error(1) D1
            error(1) D1 L55
        ''')

        >>> lestim.DetectorErrorModel('''
        ...     error(0.125) D0 D1 D2
        ...     error(0.125) L0
        ... ''').shortest_graphlike_error(ignore_ungraphlike_errors=True)
        lestim.DetectorErrorModel('''
            error(1) L0
        ''')

        >>> circuit = lestim.Circuit.generated(
        ...     "repetition_code:memory",
        ...     rounds=10,
        ...     distance=7,
        ...     before_round_data_depolarization=0.01)
        >>> model = circuit.detector_error_model(decompose_errors=True)
        >>> len(model.shortest_graphlike_error())
        7
    """
```

<a name="lestim.DetectorErrorModel.to_file"></a>
```python
# lestim.DetectorErrorModel.to_file

# (in class lestim.DetectorErrorModel)
def to_file(
    self,
    file: Union[io.TextIOBase, str, pathlib.Path],
) -> None:
    """Writes the detector error model to a file.

    The file format is defined at
    https://github.com/quantumlib/Stim/blob/main/doc/file_format_dem_detector_error_model.md

    Args:
        file: A file path or an open file to write to.

    Examples:
        >>> import lestim
        >>> import tempfile
        >>> c = lestim.DetectorErrorModel('error(0.25) D2 D3')

        >>> with tempfile.TemporaryDirectory() as tmpdir:
        ...     path = tmpdir + '/tmp.lestim'
        ...     with open(path, 'w') as f:
        ...         c.to_file(f)
        ...     with open(path) as f:
        ...         contents = f.read()
        >>> contents
        'error(0.25) D2 D3\n'

        >>> with tempfile.TemporaryDirectory() as tmpdir:
        ...     path = tmpdir + '/tmp.lestim'
        ...     c.to_file(path)
        ...     with open(path) as f:
        ...         contents = f.read()
        >>> contents
        'error(0.25) D2 D3\n'
    """
```

<a name="lestim.ExplainedError"></a>
```python
# lestim.ExplainedError

# (at top-level in the lestim module)
class ExplainedError:
    """Describes the location of an error mechanism from a lestim circuit.
    """
```

<a name="lestim.ExplainedError.__init__"></a>
```python
# lestim.ExplainedError.__init__

# (in class lestim.ExplainedError)
def __init__(
    self,
    *,
    dem_error_terms: List[lestim._stim_polyfill.DemTargetWithCoords],
    circuit_error_locations: List[lestim._stim_polyfill.CircuitErrorLocation],
) -> None:
    """Creates a lestim.ExplainedError.
    """
```

<a name="lestim.ExplainedError.circuit_error_locations"></a>
```python
# lestim.ExplainedError.circuit_error_locations

# (in class lestim.ExplainedError)
@property
def circuit_error_locations(
    self,
) -> List[lestim._stim_polyfill.CircuitErrorLocation]:
    """The locations of circuit errors that produce the symptoms in dem_error_terms.

    Note: if this list contains a single entry, it may be because a result
    with a single representative error was requested (as opposed to all possible
    errors).

    Note: if this list is empty, it may be because there was a DEM error decomposed
    into parts where one of the parts is impossible to make on its own from a single
    circuit error.
    """
```

<a name="lestim.ExplainedError.dem_error_terms"></a>
```python
# lestim.ExplainedError.dem_error_terms

# (in class lestim.ExplainedError)
@property
def dem_error_terms(
    self,
) -> List[lestim._stim_polyfill.DemTargetWithCoords]:
    """The detectors and observables flipped by this error mechanism.
    """
```

<a name="lestim.FlipSimulator"></a>
```python
# lestim.FlipSimulator

# (at top-level in the lestim module)
class FlipSimulator:
    """A simulator that tracks whether things are flipped, instead of what they are.

    Tracking flips is significantly cheaper than tracking actual values, requiring
    O(1) work per gate (compared to O(n) for unitary operations and O(n^2) for
    collapsing operations in the tableau simulator, where n is the qubit count).

    Supports interactive usage, where gates and measurements are applied on demand.

    Examples:
        >>> import lestim
        >>> sim = lestim.FlipSimulator(batch_size=256)
    """
```

<a name="lestim.FlipSimulator.__init__"></a>
```python
# lestim.FlipSimulator.__init__

# (in class lestim.FlipSimulator)
def __init__(
    self,
    *,
    batch_size: int,
    disable_stabilizer_randomization: bool = False,
    num_qubits: int = 0,
    seed: Optional[int] = None,
) -> None:
    """Initializes a lestim.FlipSimulator.

    Args:
        batch_size: For speed, the flip simulator simulates many instances in
            parallel. This argument determines the number of parallel instances.

            It's recommended to use a multiple of 256, because internally the state
            of the instances is striped across SSE (128 bit) or AVX (256 bit)
            words with one bit in the word belonging to each instance. The result is
            that, even if you only ask for 1 instance, probably the same amount of
            work is being done as if you'd asked for 256 instances. The extra
            results just aren't being used, creating waste.

        disable_stabilizer_randomization: Determines whether or not the flip
            simulator uses stabilizer randomization. Defaults to False (stabilizer
            randomization used). Set to True to disable stabilizer randomization.

            Stabilizer randomization means that, when a qubit is initialized or
            measured in the Z basis, a Z error is added to the qubit with 50%
            probability. More generally, anytime a stabilizer is introduced into
            the system by any means, an error equal to that stabilizer is applied
            with 50% probability. This ensures that observables anticommuting with
            stabilizers of the system must be maximally uncertain. In other words,
            this feature enforces Heisenberg's uncertainty principle.

            This is a safety feature that you should not turn off unless you have a
            reason to do so. Stabilizer randomization is turned on by default
            because it catches mistakes. For example, suppose you are trying to
            create a stabilizer code but you accidentally have the code measure two
            anticommuting stabilizers. With stabilizer randomization turned off, it
            will look like this code works. With stabilizer randomization turned on,
            the two measurements will correctly randomize each other revealing that
            the code doesn't work.

            In some use cases, stabilizer randomization is a hindrance instead of
            helpful. For example, if you are using the flip simulator to understand
            how an error propagates through the system, the stabilizer randomization
            will be introducing error terms that you don't want.

        num_qubits: Sets the initial number of qubits tracked by the simulation.
            The simulator will still automatically resize as needed when qubits
            beyond this limit are touched.

            This parameter exists as a way to hint at the desired size of the
            simulator's state for performance, and to ensure methods that
            peek at the size have the expected size from the start instead of
            only after the relevant qubits have been touched.

        seed: PARTIALLY determines simulation results by deterministically seeding
            the random number generator.

            Must be None or an integer in range(2**64).

            Defaults to None. When None, the prng is seeded from system entropy.

            When set to an integer, making the exact same series calls on the exact
            same machine with the exact same version of Stim will produce the exact
            same simulation results.

            CAUTION: simulation results *WILL NOT* be consistent between versions of
            Stim. This restriction is present to make it possible to have future
            optimizations to the random sampling, and is enforced by introducing
            intentional differences in the seeding strategy from version to version.

            CAUTION: simulation results *MAY NOT* be consistent across machines that
            differ in the width of supported SIMD instructions. For example, using
            the same seed on a machine that supports AVX instructions and one that
            only supports SSE instructions may produce different simulation results.

            CAUTION: simulation results *MAY NOT* be consistent if you vary how the
            circuit is executed. For example, reordering whether a reset on one
            qubit happens before or after a reset on another qubit can result in
            different measurement results being observed starting from the same
            seed.

    Returns:
        An initialized lestim.FlipSimulator.

    Examples:
        >>> import lestim
        >>> sim = lestim.FlipSimulator(batch_size=256)
    """
```

<a name="lestim.FlipSimulator.batch_size"></a>
```python
# lestim.FlipSimulator.batch_size

# (in class lestim.FlipSimulator)
@property
def batch_size(
    self,
) -> int:
    """Returns the number of instances being simulated by the simulator.

    Examples:
        >>> import lestim
        >>> sim = lestim.FlipSimulator(batch_size=256)
        >>> sim.batch_size
        256
        >>> sim = lestim.FlipSimulator(batch_size=42)
        >>> sim.batch_size
        42
    """
```

<a name="lestim.FlipSimulator.broadcast_pauli_errors"></a>
```python
# lestim.FlipSimulator.broadcast_pauli_errors

# (in class lestim.FlipSimulator)
def broadcast_pauli_errors(
    self,
    *,
    pauli: Union[str, int],
    mask: np.ndarray,
) -> None:
    """Applies a pauli error to all qubits in all instances, filtered by a mask.

    Args:
        pauli: The pauli, specified as an integer or string.
            Uses the convention 0=I, 1=X, 2=Y, 3=Z.
            Any value from [0, 1, 2, 3, 'X', 'Y', 'Z', 'I', '_'] is allowed.
        mask: A 2d numpy array specifying where to apply errors. The first axis
            is qubits, the second axis is simulation instances. The first axis
            can have a length less than the current number of qubits (or more,
            which adds qubits to the simulation). The length of the second axis
            must match the simulator's `batch_size`. The array must satisfy

                mask.dtype == np.bool_
                len(mask.shape) == 2
                mask.shape[1] == flip_sim.batch_size

            The error is only applied to qubit q in instance k when

                mask[q, k] == True.

    Examples:
        >>> import lestim
        >>> import numpy as np
        >>> sim = lestim.FlipSimulator(
        ...     batch_size=2,
        ...     num_qubits=3,
        ...     disable_stabilizer_randomization=True,
        ... )
        >>> sim.broadcast_pauli_errors(
        ...     pauli='X',
        ...     mask=np.asarray([[True, False],[False, False],[True, True]]),
        ... )
        >>> sim.peek_pauli_flips()
        [lestim.PauliString("+X_X"), lestim.PauliString("+__X")]

        >>> sim.broadcast_pauli_errors(
        ...     pauli='Z',
        ...     mask=np.asarray([[False, True],[False, False],[True, True]]),
        ... )
        >>> sim.peek_pauli_flips()
        [lestim.PauliString("+X_Y"), lestim.PauliString("+Z_Y")]
    """
```

<a name="lestim.FlipSimulator.do"></a>
```python
# lestim.FlipSimulator.do

# (in class lestim.FlipSimulator)
def do(
    self,
    obj: Union[stim.Circuit, stim.CircuitInstruction, stim.CircuitRepeatBlock],
) -> None:
    """Applies a circuit or circuit instruction to the simulator's state.

    The results of any measurements performed can be retrieved using the
    `get_measurement_flips` method.

    Args:
        obj: The circuit or instruction to apply to the simulator's state.

    Examples:
        >>> import lestim
        >>> sim = lestim.FlipSimulator(
        ...     batch_size=1,
        ...     disable_stabilizer_randomization=True,
        ... )
        >>> circuit = lestim.Circuit('''
        ...     X_ERROR(1) 0 1 3
        ...     REPEAT 5 {
        ...         H 0
        ...         C_XYZ 1
        ...     }
        ... ''')
        >>> sim.do(circuit)
        >>> sim.peek_pauli_flips()
        [lestim.PauliString("+ZZ_X")]

        >>> sim.do(circuit[0])
        >>> sim.peek_pauli_flips()
        [lestim.PauliString("+YY__")]

        >>> sim.do(circuit[1])
        >>> sim.peek_pauli_flips()
        [lestim.PauliString("+YX__")]
    """
```

<a name="lestim.FlipSimulator.get_detector_flips"></a>
```python
# lestim.FlipSimulator.get_detector_flips

# (in class lestim.FlipSimulator)
def get_detector_flips(
    self,
    *,
    detector_index: Optional[int] = None,
    instance_index: Optional[int] = None,
    bit_packed: bool = False,
) -> np.ndarray:
    """Retrieves detector flip data from the simulator's detection event record.

    Args:
        record_index: Identifies a detector to read results from.
            Setting this to None (default) returns results from all detectors.
            Otherwise this should be an integer in range(0, self.num_detectors).
        instance_index: Identifies a simulation instance to read results from.
            Setting this to None (the default) returns results from all instances.
            Otherwise this should be an integer in range(0, self.batch_size).
        bit_packed: Defaults to False. Determines whether the result is bit packed.
            If this is set to true, the returned numpy array will be bit packed as
            if by applying

                out = np.packbits(out, axis=len(out.shape) - 1, bitorder='little')

            Behind the scenes the data is always bit packed, so setting this
            argument avoids ever unpacking in the first place. This substantially
            improves performance when there is a lot of data.

    Returns:
        A numpy array containing the requested data. By default this is a 2d array
        of shape (self.num_detectors, self.batch_size), where the first index is
        the detector_index and the second index is the instance_index and the
        dtype is np.bool_.

        Specifying detector_index slices away the first index, leaving a 1d array
        with only an instance_index.

        Specifying instance_index slices away the last index, leaving a 1d array
        with only a detector_index (or a 0d array, a boolean, if detector_index
        was also specified).

        Specifying bit_packed=True bit packs the last remaining index, changing
        the dtype to np.uint8.

    Examples:
        >>> import lestim
        >>> sim = lestim.FlipSimulator(batch_size=9)
        >>> sim.do(lestim.Circuit('''
        ...     M 0 0 0
        ...     DETECTOR rec[-2] rec[-3]
        ...     DETECTOR rec[-1] rec[-2]
        ... '''))

        >>> sim.get_detector_flips()
        array([[False, False, False, False, False, False, False, False, False],
               [False, False, False, False, False, False, False, False, False]])

        >>> sim.get_detector_flips(bit_packed=True)
        array([[0, 0],
               [0, 0]], dtype=uint8)

        >>> sim.get_detector_flips(instance_index=2)
        array([False, False])

        >>> sim.get_detector_flips(detector_index=1)
        array([False, False, False, False, False, False, False, False, False])

        >>> sim.get_detector_flips(instance_index=2, detector_index=1)
        array(False)
    """
```

<a name="lestim.FlipSimulator.get_measurement_flips"></a>
```python
# lestim.FlipSimulator.get_measurement_flips

# (in class lestim.FlipSimulator)
def get_measurement_flips(
    self,
    *,
    record_index: Optional[int] = None,
    instance_index: Optional[int] = None,
    bit_packed: bool = False,
) -> np.ndarray:
    """Retrieves measurement flip data from the simulator's measurement record.

    Args:
        record_index: Identifies a measurement to read results from.
            Setting this to None (default) returns results from all measurements.
            Setting this to a non-negative integer indexes measurements by the order
                they occurred. For example, record index 0 is the first measurement.
            Setting this to a negative integer indexes measurements by recency.
                For example, recording index -1 is the most recent measurement.
        instance_index: Identifies a simulation instance to read results from.
            Setting this to None (the default) returns results from all instances.
            Otherwise this should be set to an integer in range(0, self.batch_size).
        bit_packed: Defaults to False. Determines whether the result is bit packed.
            If this is set to true, the returned numpy array will be bit packed as
            if by applying

                out = np.packbits(out, axis=len(out.shape) - 1, bitorder='little')

            Behind the scenes the data is always bit packed, so setting this
            argument avoids ever unpacking in the first place. This substantially
            improves performance when there is a lot of data.

    Returns:
        A numpy array containing the requested data. By default this is a 2d array
        of shape (self.num_measurements, self.batch_size), where the first index is
        the measurement_index and the second index is the instance_index and the
        dtype is np.bool_.

        Specifying record_index slices away the first index, leaving a 1d array
        with only an instance_index.

        Specifying instance_index slices away the last index, leaving a 1d array
        with only a measurement_index (or a 0d array, a boolean, if record_index
        was also specified).

        Specifying bit_packed=True bit packs the last remaining index, changing
        the dtype to np.uint8.

    Examples:
        >>> import lestim
        >>> sim = lestim.FlipSimulator(batch_size=9)
        >>> sim.do(lestim.Circuit('M 0 1 2'))

        >>> sim.get_measurement_flips()
        array([[False, False, False, False, False, False, False, False, False],
               [False, False, False, False, False, False, False, False, False],
               [False, False, False, False, False, False, False, False, False]])

        >>> sim.get_measurement_flips(bit_packed=True)
        array([[0, 0],
               [0, 0],
               [0, 0]], dtype=uint8)

        >>> sim.get_measurement_flips(instance_index=1)
        array([False, False, False])

        >>> sim.get_measurement_flips(record_index=2)
        array([False, False, False, False, False, False, False, False, False])

        >>> sim.get_measurement_flips(instance_index=1, record_index=2)
        array(False)
    """
```

<a name="lestim.FlipSimulator.get_observable_flips"></a>
```python
# lestim.FlipSimulator.get_observable_flips

# (in class lestim.FlipSimulator)
def get_observable_flips(
    self,
    *,
    observable_index: Optional[int] = None,
    instance_index: Optional[int] = None,
    bit_packed: bool = False,
) -> np.ndarray:
    """Retrieves observable flip data from the simulator's detection event record.

    Args:
        record_index: Identifies a observable to read results from.
            Setting this to None (default) returns results from all observables.
            Otherwise this should be an integer in range(0, self.num_observables).
        instance_index: Identifies a simulation instance to read results from.
            Setting this to None (the default) returns results from all instances.
            Otherwise this should be an integer in range(0, self.batch_size).
        bit_packed: Defaults to False. Determines whether the result is bit packed.
            If this is set to true, the returned numpy array will be bit packed as
            if by applying

                out = np.packbits(out, axis=len(out.shape) - 1, bitorder='little')

            Behind the scenes the data is always bit packed, so setting this
            argument avoids ever unpacking in the first place. This substantially
            improves performance when there is a lot of data.

    Returns:
        A numpy array containing the requested data. By default this is a 2d array
        of shape (self.num_observables, self.batch_size), where the first index is
        the observable_index and the second index is the instance_index and the
        dtype is np.bool_.

        Specifying observable_index slices away the first index, leaving a 1d array
        with only an instance_index.

        Specifying instance_index slices away the last index, leaving a 1d array
        with only a observable_index (or a 0d array, a boolean, if observable_index
        was also specified).

        Specifying bit_packed=True bit packs the last remaining index, changing
        the dtype to np.uint8.

    Examples:
        >>> import lestim
        >>> sim = lestim.FlipSimulator(batch_size=9)
        >>> sim.do(lestim.Circuit('''
        ...     M 0 0 0
        ...     OBSERVABLE_INCLUDE(0) rec[-2]
        ...     OBSERVABLE_INCLUDE(1) rec[-1]
        ... '''))

        >>> sim.get_observable_flips()
        array([[False, False, False, False, False, False, False, False, False],
               [False, False, False, False, False, False, False, False, False]])

        >>> sim.get_observable_flips(bit_packed=True)
        array([[0, 0],
               [0, 0]], dtype=uint8)

        >>> sim.get_observable_flips(instance_index=2)
        array([False, False])

        >>> sim.get_observable_flips(observable_index=1)
        array([False, False, False, False, False, False, False, False, False])

        >>> sim.get_observable_flips(instance_index=2, observable_index=1)
        array(False)
    """
```

<a name="lestim.FlipSimulator.num_detectors"></a>
```python
# lestim.FlipSimulator.num_detectors

# (in class lestim.FlipSimulator)
@property
def num_detectors(
    self,
) -> int:
    """Returns the number of detectors that have been simulated and stored.

    Examples:
        >>> import lestim
        >>> sim = lestim.FlipSimulator(batch_size=256)
        >>> sim.num_detectors
        0
        >>> sim.do(lestim.Circuit('''
        ...     M 0 0
        ...     DETECTOR rec[-1] rec[-2]
        ... '''))
        >>> sim.num_detectors
        1
    """
```

<a name="lestim.FlipSimulator.num_measurements"></a>
```python
# lestim.FlipSimulator.num_measurements

# (in class lestim.FlipSimulator)
@property
def num_measurements(
    self,
) -> int:
    """Returns the number of measurements that have been simulated and stored.

    Examples:
        >>> import lestim
        >>> sim = lestim.FlipSimulator(batch_size=256)
        >>> sim.num_measurements
        0
        >>> sim.do(lestim.Circuit('M 3 5'))
        >>> sim.num_measurements
        2
    """
```

<a name="lestim.FlipSimulator.num_observables"></a>
```python
# lestim.FlipSimulator.num_observables

# (in class lestim.FlipSimulator)
@property
def num_observables(
    self,
) -> int:
    """Returns the number of observables currently tracked by the simulator.

    Examples:
        >>> import lestim
        >>> sim = lestim.FlipSimulator(batch_size=256)
        >>> sim.num_observables
        0
        >>> sim.do(lestim.Circuit('''
        ...     M 0
        ...     OBSERVABLE_INCLUDE(4) rec[-1]
        ... '''))
        >>> sim.num_observables
        5
    """
```

<a name="lestim.FlipSimulator.num_qubits"></a>
```python
# lestim.FlipSimulator.num_qubits

# (in class lestim.FlipSimulator)
@property
def num_qubits(
    self,
) -> int:
    """Returns the number of qubits currently tracked by the simulator.

    Examples:
        >>> import lestim
        >>> sim = lestim.FlipSimulator(batch_size=256)
        >>> sim.num_qubits
        0
        >>> sim = lestim.FlipSimulator(batch_size=256, num_qubits=4)
        >>> sim.num_qubits
        4
        >>> sim.do(lestim.Circuit('H 5'))
        >>> sim.num_qubits
        6
    """
```

<a name="lestim.FlipSimulator.peek_pauli_flips"></a>
```python
# lestim.FlipSimulator.peek_pauli_flips

# (in class lestim.FlipSimulator)
@overload
def peek_pauli_flips(
    self,
) -> List[stim.PauliString]:
    pass
@overload
def peek_pauli_flips(
    self,
    *,
    instance_index: int,
) -> stim.PauliString:
    pass
def peek_pauli_flips(
    self,
    *,
    instance_index: Optional[int] = None,
) -> Union[stim.PauliString, List[stim.PauliString]]:
    """Returns the current pauli errors packed into lestim.PauliString instances.

    Args:
        instance_index: Defaults to None. When set to None, the pauli errors from
            all instances are returned as a list of `lestim.PauliString`. When set to
            an integer, a single `lestim.PauliString` is returned containing the
            errors for the indexed instance.

    Returns:
        if instance_index is None:
            A list of lestim.PauliString, with the k'th entry being the errors from
            the k'th simulation instance.
        else:
            A lestim.PauliString with the errors from the k'th simulation instance.

    Examples:
        >>> import lestim
        >>> sim = lestim.FlipSimulator(
        ...     batch_size=2,
        ...     disable_stabilizer_randomization=True,
        ...     num_qubits=10,
        ... )

        >>> sim.peek_pauli_flips()
        [lestim.PauliString("+__________"), lestim.PauliString("+__________")]

        >>> sim.peek_pauli_flips(instance_index=0)
        lestim.PauliString("+__________")

        >>> sim.do(lestim.Circuit('''
        ...     X_ERROR(1) 0 3 5
        ...     Z_ERROR(1) 3 6
        ... '''))

        >>> sim.peek_pauli_flips()
        [lestim.PauliString("+X__Y_XZ___"), lestim.PauliString("+X__Y_XZ___")]

        >>> sim = lestim.FlipSimulator(
        ...     batch_size=1,
        ...     num_qubits=100,
        ... )
        >>> flips: lestim.PauliString = sim.peek_pauli_flips(instance_index=0)
        >>> sorted(set(str(flips)))  # Should have Zs from stabilizer randomization
        ['+', 'Z', '_']
    """
```

<a name="lestim.FlipSimulator.set_pauli_flip"></a>
```python
# lestim.FlipSimulator.set_pauli_flip

# (in class lestim.FlipSimulator)
def set_pauli_flip(
    self,
    pauli: Union[str, int],
    *,
    qubit_index: int,
    instance_index: int,
) -> None:
    """Sets the pauli flip on a given qubit in a given simulation instance.

    Args:
        pauli: The pauli, specified as an integer or string.
            Uses the convention 0=I, 1=X, 2=Y, 3=Z.
            Any value from [0, 1, 2, 3, 'X', 'Y', 'Z', 'I', '_'] is allowed.
        qubit_index: The qubit to put the error on. Must be non-negative. The state
            will automatically expand as needed to store the error.
        instance_index: The simulation index to put the error inside. Use negative
            indices to index from the end of the list.

    Examples:
        >>> import lestim
        >>> sim = lestim.FlipSimulator(
        ...     batch_size=2,
        ...     num_qubits=3,
        ...     disable_stabilizer_randomization=True,
        ... )
        >>> sim.set_pauli_flip('X', qubit_index=2, instance_index=1)
        >>> sim.peek_pauli_flips()
        [lestim.PauliString("+___"), lestim.PauliString("+__X")]
    """
```

<a name="lestim.FlippedMeasurement"></a>
```python
# lestim.FlippedMeasurement

# (at top-level in the lestim module)
class FlippedMeasurement:
    """Describes a measurement that was flipped.

    Gives the measurement's index in the measurement record, and also
    the observable of the measurement.
    """
```

<a name="lestim.FlippedMeasurement.__init__"></a>
```python
# lestim.FlippedMeasurement.__init__

# (in class lestim.FlippedMeasurement)
def __init__(
    self,
    *,
    record_index: int,
    observable: object,
) -> None:
    """Creates a lestim.FlippedMeasurement.
    """
```

<a name="lestim.FlippedMeasurement.observable"></a>
```python
# lestim.FlippedMeasurement.observable

# (in class lestim.FlippedMeasurement)
@property
def observable(
    self,
) -> List[lestim._stim_polyfill.GateTargetWithCoords]:
    """Returns the observable of the flipped measurement.

    For example, an `MX 5` measurement will have the observable X5.
    """
```

<a name="lestim.FlippedMeasurement.record_index"></a>
```python
# lestim.FlippedMeasurement.record_index

# (in class lestim.FlippedMeasurement)
@property
def record_index(
    self,
) -> int:
    """The measurement record index of the flipped measurement.
    For example, the fifth measurement in a circuit has a measurement
    record index of 4.
    """
```

<a name="lestim.Flow"></a>
```python
# lestim.Flow

# (at top-level in the lestim module)
class Flow:
    """A stabilizer flow (e.g. "XI -> XX xor rec[-1]").

    Stabilizer circuits implement, and can be defined by, how they turn input
    stabilizers into output stabilizers mediated by measurements. These
    relationships are called stabilizer flows, and `lestim.Flow` is a representation
    of such a flow. For example, a `lestim.Flow` can be given to
    `lestim.Circuit.has_flow` to verify that a circuit implements the flow.

    A circuit has a stabilizer flow P -> Q if it maps the instantaneous stabilizer
    P at the start of the circuit to the instantaneous stabilizer Q at the end of
    the circuit. The flow may be mediated by certain measurements. For example,
    a lattice surgery CNOT involves an MXX measurement and an MZZ measurement, and
    the CNOT flows implemented by the circuit involve these measurements.

    A flow like P -> Q means the circuit transforms P into Q.
    A flow like 1 -> P means the circuit prepares P.
    A flow like P -> 1 means the circuit measures P.
    A flow like 1 -> 1 means the circuit contains a check (could be a DETECTOR).

    References:
        Stim's gate documentation includes the stabilizer flows of each gate.

        Appendix A of https://arxiv.org/abs/2302.02192 describes how flows are
        defined and provides a circuit construction for experimentally verifying
        their presence.

    Examples:
        >>> import lestim
        >>> c = lestim.Circuit("CNOT 2 4")

        >>> c.has_flow(lestim.Flow("__X__ -> __X_X"))
        True

        >>> c.has_flow(lestim.Flow("X2*X4 -> X2"))
        True

        >>> c.has_flow(lestim.Flow("Z4 -> Z4"))
        False
    """
```

<a name="lestim.Flow.__eq__"></a>
```python
# lestim.Flow.__eq__

# (in class lestim.Flow)
def __eq__(
    self,
    arg0: lestim._stim_polyfill.Flow,
) -> bool:
    """Determines if two flows have identical contents.
    """
```

<a name="lestim.Flow.__init__"></a>
```python
# lestim.Flow.__init__

# (in class lestim.Flow)
def __init__(
    self,
    arg: Union[None, str, stim.Flow] = None,
    /,
    *,
    input: Optional[stim.PauliString] = None,
    output: Optional[stim.PauliString] = None,
    measurements: Optional[Iterable[Union[int, GateTarget]]] = None,
) -> None:
    """Initializes a lestim.Flow.

    When given a string, the string is parsed as flow shorthand. For example,
    the string "X_ -> ZZ xor rec[-1]" will result in a flow with input pauli string
    "X_", output pauli string "ZZ", and measurement indices [-1].

    Arguments:
        arg [position-only]: Defaults to None. Must be specified by itself if used.
            str: Initializes a flow by parsing the given shorthand text.
            lestim.Flow: Initializes a copy of the given flow.
            None (default): Initializes an empty flow.
        input: Defaults to None. Can be set to a lestim.PauliString to directly
            specify the flow's input stabilizer.
        output: Defaults to None. Can be set to a lestim.PauliString to directly
            specify the flow's output stabilizer.
        measurements: Can be set to a list of integers or gate targets like
            `lestim.target_rec(-1)`, to specify the measurements that mediate the
            flow. Negative and positive measurement indices are allowed. Indexes
            follow the python convention where -1 is the last measurement in a
            circuit and 0 is the first measurement in a circuit.

    Examples:
        >>> import lestim

        >>> lestim.Flow("X2 -> -Y2*Z4 xor rec[-1]")
        lestim.Flow("__X -> -__Y_Z xor rec[-1]")

        >>> lestim.Flow("Z -> 1 xor rec[-1]")
        lestim.Flow("Z -> rec[-1]")

        >>> lestim.Flow(
        ...     input=lestim.PauliString("XX"),
        ...     output=lestim.PauliString("_X"),
        ...     measurements=[],
        ... )
        lestim.Flow("XX -> _X")
    """
```

<a name="lestim.Flow.__ne__"></a>
```python
# lestim.Flow.__ne__

# (in class lestim.Flow)
def __ne__(
    self,
    arg0: lestim._stim_polyfill.Flow,
) -> bool:
    """Determines if two flows have non-identical contents.
    """
```

<a name="lestim.Flow.__repr__"></a>
```python
# lestim.Flow.__repr__

# (in class lestim.Flow)
def __repr__(
    self,
) -> str:
    """Returns valid python code evaluating to an equivalent `lestim.Flow`.
    """
```

<a name="lestim.Flow.__str__"></a>
```python
# lestim.Flow.__str__

# (in class lestim.Flow)
def __str__(
    self,
) -> str:
    """Returns a shorthand description of the flow.
    """
```

<a name="lestim.Flow.input_copy"></a>
```python
# lestim.Flow.input_copy

# (in class lestim.Flow)
def input_copy(
    self,
) -> lestim._stim_polyfill.PauliString:
    """Returns a copy of the flow's input stabilizer.

    Examples:
        >>> import lestim
        >>> f = lestim.Flow(input=lestim.PauliString('XX'))
        >>> f.input_copy()
        lestim.PauliString("+XX")

        >>> f.input_copy() is f.input_copy()
        False
    """
```

<a name="lestim.Flow.measurements_copy"></a>
```python
# lestim.Flow.measurements_copy

# (in class lestim.Flow)
def measurements_copy(
    self,
) -> List[int]:
    """Returns a copy of the flow's measurement indices.

    Examples:
        >>> import lestim
        >>> f = lestim.Flow(measurements=[-1, 2])
        >>> f.measurements_copy()
        [-1, 2]

        >>> f.measurements_copy() is f.measurements_copy()
        False
    """
```

<a name="lestim.Flow.output_copy"></a>
```python
# lestim.Flow.output_copy

# (in class lestim.Flow)
def output_copy(
    self,
) -> lestim._stim_polyfill.PauliString:
    """Returns a copy of the flow's output stabilizer.

    Examples:
        >>> import lestim
        >>> f = lestim.Flow(output=lestim.PauliString('XX'))
        >>> f.output_copy()
        lestim.PauliString("+XX")

        >>> f.output_copy() is f.output_copy()
        False
    """
```

<a name="lestim.GateData"></a>
```python
# lestim.GateData

# (at top-level in the lestim module)
class GateData:
    """Details about a gate supported by lestim.

    Examples:
        >>> import lestim
        >>> lestim.gate_data('h').name
        'H'
        >>> lestim.gate_data('h').is_unitary
        True
        >>> lestim.gate_data('h').tableau
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+Z"),
            ],
            zs=[
                lestim.PauliString("+X"),
            ],
        )
    """
```

<a name="lestim.GateData.__eq__"></a>
```python
# lestim.GateData.__eq__

# (in class lestim.GateData)
def __eq__(
    self,
    arg0: lestim._stim_polyfill.GateData,
) -> bool:
    """Determines if two GateData instances are identical.
    """
```

<a name="lestim.GateData.__init__"></a>
```python
# lestim.GateData.__init__

# (in class lestim.GateData)
def __init__(
    self,
    name: str,
) -> None:
    """Finds gate data for the named gate.

    Examples:
        >>> import lestim
        >>> lestim.GateData('H').is_unitary
        True
    """
```

<a name="lestim.GateData.__ne__"></a>
```python
# lestim.GateData.__ne__

# (in class lestim.GateData)
def __ne__(
    self,
    arg0: lestim._stim_polyfill.GateData,
) -> bool:
    """Determines if two GateData instances are not identical.
    """
```

<a name="lestim.GateData.__repr__"></a>
```python
# lestim.GateData.__repr__

# (in class lestim.GateData)
def __repr__(
    self,
) -> str:
    """Returns text that is a valid python expression evaluating to an equivalent `lestim.GateData`.
    """
```

<a name="lestim.GateData.__str__"></a>
```python
# lestim.GateData.__str__

# (in class lestim.GateData)
def __str__(
    self,
) -> str:
    """Returns text describing the gate data.
    """
```

<a name="lestim.GateData.aliases"></a>
```python
# lestim.GateData.aliases

# (in class lestim.GateData)
@property
def aliases(
    self,
) -> List[str]:
    """Returns all aliases that can be used to name the gate.

    Although gates can be referred to by lower case and mixed
    case named, the result only includes upper cased aliases.

    Examples:
        >>> import lestim
        >>> lestim.gate_data('H').aliases
        ['H', 'H_XZ']
        >>> lestim.gate_data('cnot').aliases
        ['CNOT', 'CX', 'ZCX']
    """
```

<a name="lestim.GateData.flows"></a>
```python
# lestim.GateData.flows

# (in class lestim.GateData)
@property
def flows(
    self,
) -> Optional[List[stim.Flow]]:
    """Returns stabilizer flow generators for the gate, or else None.

    A stabilizer flow describes an input-output relationship that the gate
    satisfies, where an input pauli string is transformed into an output
    pauli string mediated by certain measurement results.

    Caution: this method returns None for variable-target-count gates like MPP.
    Not because MPP has no stabilizer flows, but because its stabilizer flows
    depend on how many qubits it targets and what basis it targets them in.

    Returns:
        A list of lestim.Flow instances representing the generators.

    Examples:
        >>> import lestim

        >>> lestim.gate_data('H').flows
        [lestim.Flow("X -> Z"), lestim.Flow("Z -> X")]

        >>> for e in lestim.gate_data('ISWAP').flows:
        ...     print(e)
        X_ -> ZY
        Z_ -> _Z
        _X -> YZ
        _Z -> Z_

        >>> for e in lestim.gate_data('MXX').flows:
        ...     print(e)
        X_ -> X_
        _X -> _X
        ZZ -> ZZ
        XX -> rec[-1]
    """
```

<a name="lestim.GateData.generalized_inverse"></a>
```python
# lestim.GateData.generalized_inverse

# (in class lestim.GateData)
@property
def generalized_inverse(
    self,
) -> lestim._stim_polyfill.GateData:
    """The closest-thing-to-an-inverse for the gate, if forced to pick something.

    The generalized inverse of a unitary gate U is its actual inverse U^-1.

    The generalized inverse of a reset or measurement gate U is a gate V such that,
    for every stabilizer flow that U has, V has the time reverse of that flow (up
    to Pauli feedback, with potentially more flows). For example, the time-reverse
    of R is MR because R has the single flow 1 -> Z and MR has the time reversed
    flow Z -> rec[-1].

    The generalized inverse of noise like X_ERROR is just the same noise.

    The generalized inverse of an annotation like TICK is just the same annotation.

    Examples:
        >>> import lestim

        >>> lestim.gate_data('H').generalized_inverse
        lestim.gate_data('H')

        >>> lestim.gate_data('CXSWAP').generalized_inverse
        lestim.gate_data('SWAPCX')

        >>> lestim.gate_data('X_ERROR').generalized_inverse
        lestim.gate_data('X_ERROR')

        >>> lestim.gate_data('MX').generalized_inverse
        lestim.gate_data('MX')

        >>> lestim.gate_data('MRY').generalized_inverse
        lestim.gate_data('MRY')

        >>> lestim.gate_data('R').generalized_inverse
        lestim.gate_data('M')

        >>> lestim.gate_data('DETECTOR').generalized_inverse
        lestim.gate_data('DETECTOR')

        >>> lestim.gate_data('TICK').generalized_inverse
        lestim.gate_data('TICK')
    """
```

<a name="lestim.GateData.inverse"></a>
```python
# lestim.GateData.inverse

# (in class lestim.GateData)
@property
def inverse(
    self,
) -> Optional[stim.GateData]:
    """The inverse of the gate, or None if it has no inverse.

    The inverse V of a gate U must have the property that V undoes the effects of U
    and that U undoes the effects of V. In particular, the circuit

        U 0 1
        V 0 1

    should be equivalent to doing nothing at all.

    Examples:
        >>> import lestim

        >>> lestim.gate_data('H').inverse
        lestim.gate_data('H')

        >>> lestim.gate_data('CX').inverse
        lestim.gate_data('CX')

        >>> lestim.gate_data('S').inverse
        lestim.gate_data('S_DAG')

        >>> lestim.gate_data('CXSWAP').inverse
        lestim.gate_data('SWAPCX')

        >>> lestim.gate_data('X_ERROR').inverse is None
        True
        >>> lestim.gate_data('M').inverse is None
        True
        >>> lestim.gate_data('R').inverse is None
        True
        >>> lestim.gate_data('DETECTOR').inverse is None
        True
        >>> lestim.gate_data('TICK').inverse is None
        True
    """
```

<a name="lestim.GateData.is_noisy_gate"></a>
```python
# lestim.GateData.is_noisy_gate

# (in class lestim.GateData)
@property
def is_noisy_gate(
    self,
) -> bool:
    """Returns whether or not the gate can produce noise.

    Note that measurement operations are considered noisy,
    because for example `M(0.001) 2 3 5` will include
    noise that flips its result 0.1% of the time.

    Examples:
        >>> import lestim

        >>> lestim.gate_data('M').is_noisy_gate
        True
        >>> lestim.gate_data('MXX').is_noisy_gate
        True
        >>> lestim.gate_data('X_ERROR').is_noisy_gate
        True
        >>> lestim.gate_data('CORRELATED_ERROR').is_noisy_gate
        True
        >>> lestim.gate_data('MPP').is_noisy_gate
        True

        >>> lestim.gate_data('H').is_noisy_gate
        False
        >>> lestim.gate_data('CX').is_noisy_gate
        False
        >>> lestim.gate_data('R').is_noisy_gate
        False
        >>> lestim.gate_data('DETECTOR').is_noisy_gate
        False
    """
```

<a name="lestim.GateData.is_reset"></a>
```python
# lestim.GateData.is_reset

# (in class lestim.GateData)
@property
def is_reset(
    self,
) -> bool:
    """Returns whether or not the gate resets qubits in any basis.

    Examples:
        >>> import lestim

        >>> lestim.gate_data('R').is_reset
        True
        >>> lestim.gate_data('RX').is_reset
        True
        >>> lestim.gate_data('MR').is_reset
        True

        >>> lestim.gate_data('M').is_reset
        False
        >>> lestim.gate_data('MXX').is_reset
        False
        >>> lestim.gate_data('MPP').is_reset
        False
        >>> lestim.gate_data('H').is_reset
        False
        >>> lestim.gate_data('CX').is_reset
        False
        >>> lestim.gate_data('HERALDED_ERASE').is_reset
        False
        >>> lestim.gate_data('DEPOLARIZE2').is_reset
        False
        >>> lestim.gate_data('X_ERROR').is_reset
        False
        >>> lestim.gate_data('CORRELATED_ERROR').is_reset
        False
        >>> lestim.gate_data('DETECTOR').is_reset
        False
    """
```

<a name="lestim.GateData.is_single_qubit_gate"></a>
```python
# lestim.GateData.is_single_qubit_gate

# (in class lestim.GateData)
@property
def is_single_qubit_gate(
    self,
) -> bool:
    """Returns whether or not the gate is a single qubit gate.

    Single qubit gates apply separately to each of their targets.

    Variable-qubit gates like CORRELATED_ERROR and MPP are not
    considered single qubit gates.

    Examples:
        >>> import lestim

        >>> lestim.gate_data('H').is_single_qubit_gate
        True
        >>> lestim.gate_data('R').is_single_qubit_gate
        True
        >>> lestim.gate_data('M').is_single_qubit_gate
        True
        >>> lestim.gate_data('X_ERROR').is_single_qubit_gate
        True

        >>> lestim.gate_data('CX').is_single_qubit_gate
        False
        >>> lestim.gate_data('MXX').is_single_qubit_gate
        False
        >>> lestim.gate_data('CORRELATED_ERROR').is_single_qubit_gate
        False
        >>> lestim.gate_data('MPP').is_single_qubit_gate
        False
        >>> lestim.gate_data('DETECTOR').is_single_qubit_gate
        False
        >>> lestim.gate_data('TICK').is_single_qubit_gate
        False
        >>> lestim.gate_data('REPEAT').is_single_qubit_gate
        False
    """
```

<a name="lestim.GateData.is_two_qubit_gate"></a>
```python
# lestim.GateData.is_two_qubit_gate

# (in class lestim.GateData)
@property
def is_two_qubit_gate(
    self,
) -> bool:
    """Returns whether or not the gate is a two qubit gate.

    Two qubit gates must be given an even number of targets.

    Variable-qubit gates like CORRELATED_ERROR and MPP are not
    considered two qubit gates.

    Examples:
        >>> import lestim

        >>> lestim.gate_data('CX').is_two_qubit_gate
        True
        >>> lestim.gate_data('MXX').is_two_qubit_gate
        True

        >>> lestim.gate_data('H').is_two_qubit_gate
        False
        >>> lestim.gate_data('R').is_two_qubit_gate
        False
        >>> lestim.gate_data('M').is_two_qubit_gate
        False
        >>> lestim.gate_data('X_ERROR').is_two_qubit_gate
        False
        >>> lestim.gate_data('CORRELATED_ERROR').is_two_qubit_gate
        False
        >>> lestim.gate_data('MPP').is_two_qubit_gate
        False
        >>> lestim.gate_data('DETECTOR').is_two_qubit_gate
        False
    """
```

<a name="lestim.GateData.is_unitary"></a>
```python
# lestim.GateData.is_unitary

# (in class lestim.GateData)
@property
def is_unitary(
    self,
) -> bool:
    """Returns whether or not the gate is a unitary gate.

    Examples:
        >>> import lestim

        >>> lestim.gate_data('H').is_unitary
        True
        >>> lestim.gate_data('CX').is_unitary
        True

        >>> lestim.gate_data('R').is_unitary
        False
        >>> lestim.gate_data('M').is_unitary
        False
        >>> lestim.gate_data('MXX').is_unitary
        False
        >>> lestim.gate_data('X_ERROR').is_unitary
        False
        >>> lestim.gate_data('CORRELATED_ERROR').is_unitary
        False
        >>> lestim.gate_data('MPP').is_unitary
        False
        >>> lestim.gate_data('DETECTOR').is_unitary
        False
    """
```

<a name="lestim.GateData.name"></a>
```python
# lestim.GateData.name

# (in class lestim.GateData)
@property
def name(
    self,
) -> str:
    """Returns the canonical name of the gate.

    Examples:
        >>> import lestim
        >>> lestim.gate_data('H').name
        'H'
        >>> lestim.gate_data('cnot').name
        'CX'
    """
```

<a name="lestim.GateData.num_parens_arguments_range"></a>
```python
# lestim.GateData.num_parens_arguments_range

# (in class lestim.GateData)
@property
def num_parens_arguments_range(
    self,
) -> range:
    """Returns the min/max parens arguments taken by the gate, as a python range.

    Examples:
        >>> import lestim

        >>> lestim.gate_data('M').num_parens_arguments_range
        range(0, 2)
        >>> list(lestim.gate_data('M').num_parens_arguments_range)
        [0, 1]
        >>> list(lestim.gate_data('R').num_parens_arguments_range)
        [0]
        >>> list(lestim.gate_data('H').num_parens_arguments_range)
        [0]
        >>> list(lestim.gate_data('X_ERROR').num_parens_arguments_range)
        [1]
        >>> list(lestim.gate_data('PAULI_CHANNEL_1').num_parens_arguments_range)
        [3]
        >>> list(lestim.gate_data('PAULI_CHANNEL_2').num_parens_arguments_range)
        [15]
        >>> lestim.gate_data('DETECTOR').num_parens_arguments_range
        range(0, 256)
        >>> list(lestim.gate_data('OBSERVABLE_INCLUDE').num_parens_arguments_range)
        [1]
    """
```

<a name="lestim.GateData.produces_measurements"></a>
```python
# lestim.GateData.produces_measurements

# (in class lestim.GateData)
@property
def produces_measurements(
    self,
) -> bool:
    """Returns whether or not the gate produces measurement results.

    Examples:
        >>> import lestim

        >>> lestim.gate_data('M').produces_measurements
        True
        >>> lestim.gate_data('MRY').produces_measurements
        True
        >>> lestim.gate_data('MXX').produces_measurements
        True
        >>> lestim.gate_data('MPP').produces_measurements
        True
        >>> lestim.gate_data('HERALDED_ERASE').produces_measurements
        True

        >>> lestim.gate_data('H').produces_measurements
        False
        >>> lestim.gate_data('CX').produces_measurements
        False
        >>> lestim.gate_data('R').produces_measurements
        False
        >>> lestim.gate_data('X_ERROR').produces_measurements
        False
        >>> lestim.gate_data('CORRELATED_ERROR').produces_measurements
        False
        >>> lestim.gate_data('DETECTOR').produces_measurements
        False
    """
```

<a name="lestim.GateData.tableau"></a>
```python
# lestim.GateData.tableau

# (in class lestim.GateData)
@property
def tableau(
    self,
) -> Optional[stim.Tableau]:
    """Returns the gate's tableau, or None if the gate has no tableau.

    Examples:
        >>> import lestim
        >>> print(lestim.gate_data('M').tableau)
        None
        >>> lestim.gate_data('H').tableau
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+Z"),
            ],
            zs=[
                lestim.PauliString("+X"),
            ],
        )
        >>> lestim.gate_data('ISWAP').tableau
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+ZY"),
                lestim.PauliString("+YZ"),
            ],
            zs=[
                lestim.PauliString("+_Z"),
                lestim.PauliString("+Z_"),
            ],
        )
    """
```

<a name="lestim.GateData.takes_measurement_record_targets"></a>
```python
# lestim.GateData.takes_measurement_record_targets

# (in class lestim.GateData)
@property
def takes_measurement_record_targets(
    self,
) -> bool:
    """Returns whether or not the gate can accept rec targets.

    For example, `CX` can take a measurement record target
    like `CX rec[-1] 1`.

    Examples:
        >>> import lestim

        >>> lestim.gate_data('CX').takes_measurement_record_targets
        True
        >>> lestim.gate_data('DETECTOR').takes_measurement_record_targets
        True

        >>> lestim.gate_data('H').takes_measurement_record_targets
        False
        >>> lestim.gate_data('SWAP').takes_measurement_record_targets
        False
        >>> lestim.gate_data('R').takes_measurement_record_targets
        False
        >>> lestim.gate_data('M').takes_measurement_record_targets
        False
        >>> lestim.gate_data('MRY').takes_measurement_record_targets
        False
        >>> lestim.gate_data('MXX').takes_measurement_record_targets
        False
        >>> lestim.gate_data('X_ERROR').takes_measurement_record_targets
        False
        >>> lestim.gate_data('CORRELATED_ERROR').takes_measurement_record_targets
        False
        >>> lestim.gate_data('MPP').takes_measurement_record_targets
        False
    """
```

<a name="lestim.GateData.takes_pauli_targets"></a>
```python
# lestim.GateData.takes_pauli_targets

# (in class lestim.GateData)
@property
def takes_pauli_targets(
    self,
) -> bool:
    """Returns whether or not the gate expects pauli targets.

    For example, `CORRELATED_ERROR` takes targets like `X0` and `Y1`
    instead of `0` or `1`.

    Examples:
        >>> import lestim

        >>> lestim.gate_data('CORRELATED_ERROR').takes_pauli_targets
        True
        >>> lestim.gate_data('MPP').takes_pauli_targets
        True

        >>> lestim.gate_data('H').takes_pauli_targets
        False
        >>> lestim.gate_data('CX').takes_pauli_targets
        False
        >>> lestim.gate_data('R').takes_pauli_targets
        False
        >>> lestim.gate_data('M').takes_pauli_targets
        False
        >>> lestim.gate_data('MRY').takes_pauli_targets
        False
        >>> lestim.gate_data('MXX').takes_pauli_targets
        False
        >>> lestim.gate_data('X_ERROR').takes_pauli_targets
        False
        >>> lestim.gate_data('DETECTOR').takes_pauli_targets
        False
    """
```

<a name="lestim.GateData.unitary_matrix"></a>
```python
# lestim.GateData.unitary_matrix

# (in class lestim.GateData)
@property
def unitary_matrix(
    self,
) -> Optional[np.ndarray]:
    """Returns the gate's unitary matrix, or None if the gate isn't unitary.

    Examples:
        >>> import lestim

        >>> print(lestim.gate_data('M').unitary_matrix)
        None

        >>> lestim.gate_data('X').unitary_matrix
        array([[0.+0.j, 1.+0.j],
               [1.+0.j, 0.+0.j]], dtype=complex64)

        >>> lestim.gate_data('ISWAP').unitary_matrix
        array([[1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j],
               [0.+0.j, 0.+0.j, 0.+1.j, 0.+0.j],
               [0.+0.j, 0.+1.j, 0.+0.j, 0.+0.j],
               [0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j]], dtype=complex64)
    """
```

<a name="lestim.GateTarget"></a>
```python
# lestim.GateTarget

# (at top-level in the lestim module)
class GateTarget:
    """Represents a gate target, like `0` or `rec[-1]`, from a circuit.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit('''
        ...     M 0 !1
        ... ''')
        >>> circuit[0].targets_copy()[0]
        lestim.GateTarget(0)
        >>> circuit[0].targets_copy()[1]
        lestim.GateTarget(lestim.target_inv(1))
    """
```

<a name="lestim.GateTarget.__eq__"></a>
```python
# lestim.GateTarget.__eq__

# (in class lestim.GateTarget)
def __eq__(
    self,
    arg0: lestim._stim_polyfill.GateTarget,
) -> bool:
    """Determines if two `lestim.GateTarget`s are identical.
    """
```

<a name="lestim.GateTarget.__init__"></a>
```python
# lestim.GateTarget.__init__

# (in class lestim.GateTarget)
def __init__(
    self,
    value: object,
) -> None:
    """Initializes a `lestim.GateTarget`.

    Args:
        value: A target like `5` or `lestim.target_rec(-1)`.
    """
```

<a name="lestim.GateTarget.__ne__"></a>
```python
# lestim.GateTarget.__ne__

# (in class lestim.GateTarget)
def __ne__(
    self,
    arg0: lestim._stim_polyfill.GateTarget,
) -> bool:
    """Determines if two `lestim.GateTarget`s are different.
    """
```

<a name="lestim.GateTarget.__repr__"></a>
```python
# lestim.GateTarget.__repr__

# (in class lestim.GateTarget)
def __repr__(
    self,
) -> str:
    """Returns text that is a valid python expression evaluating to an equivalent `lestim.GateTarget`.
    """
```

<a name="lestim.GateTarget.is_combiner"></a>
```python
# lestim.GateTarget.is_combiner

# (in class lestim.GateTarget)
@property
def is_combiner(
    self,
) -> bool:
    """Returns whether or not this is a combiner target like `*`.

    Examples:
        >>> import lestim
        >>> lestim.GateTarget(6).is_combiner
        False
        >>> lestim.target_inv(7).is_combiner
        False
        >>> lestim.target_x(8).is_combiner
        False
        >>> lestim.target_y(2).is_combiner
        False
        >>> lestim.target_z(3).is_combiner
        False
        >>> lestim.target_sweep_bit(9).is_combiner
        False
        >>> lestim.target_rec(-5).is_combiner
        False
        >>> lestim.target_combiner().is_combiner
        True
    """
```

<a name="lestim.GateTarget.is_inverted_result_target"></a>
```python
# lestim.GateTarget.is_inverted_result_target

# (in class lestim.GateTarget)
@property
def is_inverted_result_target(
    self,
) -> bool:
    """Returns whether or not this is an inverted target like `!5` or `!X4`.

    Examples:
        >>> import lestim
        >>> lestim.GateTarget(6).is_inverted_result_target
        False
        >>> lestim.target_inv(7).is_inverted_result_target
        True
        >>> lestim.target_x(8).is_inverted_result_target
        False
        >>> lestim.target_x(8, invert=True).is_inverted_result_target
        True
        >>> lestim.target_y(2).is_inverted_result_target
        False
        >>> lestim.target_z(3).is_inverted_result_target
        False
        >>> lestim.target_sweep_bit(9).is_inverted_result_target
        False
        >>> lestim.target_rec(-5).is_inverted_result_target
        False
    """
```

<a name="lestim.GateTarget.is_measurement_record_target"></a>
```python
# lestim.GateTarget.is_measurement_record_target

# (in class lestim.GateTarget)
@property
def is_measurement_record_target(
    self,
) -> bool:
    """Returns whether or not this is a measurement record target like `rec[-5]`.

    Examples:
        >>> import lestim
        >>> lestim.GateTarget(6).is_measurement_record_target
        False
        >>> lestim.target_inv(7).is_measurement_record_target
        False
        >>> lestim.target_x(8).is_measurement_record_target
        False
        >>> lestim.target_y(2).is_measurement_record_target
        False
        >>> lestim.target_z(3).is_measurement_record_target
        False
        >>> lestim.target_sweep_bit(9).is_measurement_record_target
        False
        >>> lestim.target_rec(-5).is_measurement_record_target
        True
    """
```

<a name="lestim.GateTarget.is_qubit_target"></a>
```python
# lestim.GateTarget.is_qubit_target

# (in class lestim.GateTarget)
@property
def is_qubit_target(
    self,
) -> bool:
    """Returns whether or not this is a qubit target like `5` or `!6`.

    Examples:
        >>> import lestim
        >>> lestim.GateTarget(6).is_qubit_target
        True
        >>> lestim.target_inv(7).is_qubit_target
        True
        >>> lestim.target_x(8).is_qubit_target
        False
        >>> lestim.target_y(2).is_qubit_target
        False
        >>> lestim.target_z(3).is_qubit_target
        False
        >>> lestim.target_sweep_bit(9).is_qubit_target
        False
        >>> lestim.target_rec(-5).is_qubit_target
        False
    """
```

<a name="lestim.GateTarget.is_sweep_bit_target"></a>
```python
# lestim.GateTarget.is_sweep_bit_target

# (in class lestim.GateTarget)
@property
def is_sweep_bit_target(
    self,
) -> bool:
    """Returns whether or not this is a sweep bit target like `sweep[4]`.


    Examples:
        >>> import lestim
        >>> lestim.GateTarget(6).is_sweep_bit_target
        False
        >>> lestim.target_inv(7).is_sweep_bit_target
        False
        >>> lestim.target_x(8).is_sweep_bit_target
        False
        >>> lestim.target_y(2).is_sweep_bit_target
        False
        >>> lestim.target_z(3).is_sweep_bit_target
        False
        >>> lestim.target_sweep_bit(9).is_sweep_bit_target
        True
        >>> lestim.target_rec(-5).is_sweep_bit_target
        False
    """
```

<a name="lestim.GateTarget.is_x_target"></a>
```python
# lestim.GateTarget.is_x_target

# (in class lestim.GateTarget)
@property
def is_x_target(
    self,
) -> bool:
    """Returns whether or not this is an X pauli target like `X2` or `!X7`.

    Examples:
        >>> import lestim
        >>> lestim.GateTarget(6).is_x_target
        False
        >>> lestim.target_inv(7).is_x_target
        False
        >>> lestim.target_x(8).is_x_target
        True
        >>> lestim.target_y(2).is_x_target
        False
        >>> lestim.target_z(3).is_x_target
        False
        >>> lestim.target_sweep_bit(9).is_x_target
        False
        >>> lestim.target_rec(-5).is_x_target
        False
    """
```

<a name="lestim.GateTarget.is_y_target"></a>
```python
# lestim.GateTarget.is_y_target

# (in class lestim.GateTarget)
@property
def is_y_target(
    self,
) -> bool:
    """Returns whether or not this is a Y pauli target like `Y2` or `!Y7`.

    Examples:
        >>> import lestim
        >>> lestim.GateTarget(6).is_y_target
        False
        >>> lestim.target_inv(7).is_y_target
        False
        >>> lestim.target_x(8).is_y_target
        False
        >>> lestim.target_y(2).is_y_target
        True
        >>> lestim.target_z(3).is_y_target
        False
        >>> lestim.target_sweep_bit(9).is_y_target
        False
        >>> lestim.target_rec(-5).is_y_target
        False
    """
```

<a name="lestim.GateTarget.is_z_target"></a>
```python
# lestim.GateTarget.is_z_target

# (in class lestim.GateTarget)
@property
def is_z_target(
    self,
) -> bool:
    """Returns whether or not this is a Z pauli target like `Z2` or `!Z7`.

    Examples:
        >>> import lestim
        >>> lestim.GateTarget(6).is_z_target
        False
        >>> lestim.target_inv(7).is_z_target
        False
        >>> lestim.target_x(8).is_z_target
        False
        >>> lestim.target_y(2).is_z_target
        False
        >>> lestim.target_z(3).is_z_target
        True
        >>> lestim.target_sweep_bit(9).is_z_target
        False
        >>> lestim.target_rec(-5).is_z_target
        False
    """
```

<a name="lestim.GateTarget.pauli_type"></a>
```python
# lestim.GateTarget.pauli_type

# (in class lestim.GateTarget)
@property
def pauli_type(
    self,
) -> str:
    """Returns whether this is an 'X', 'Y', or 'Z' target.

    For non-pauli targets, this property evaluates to 'I'.

    Examples:
        >>> import lestim
        >>> lestim.GateTarget(6).pauli_type
        'I'
        >>> lestim.target_inv(7).pauli_type
        'I'
        >>> lestim.target_x(8).pauli_type
        'X'
        >>> lestim.target_y(2).pauli_type
        'Y'
        >>> lestim.target_z(3).pauli_type
        'Z'
        >>> lestim.target_sweep_bit(9).pauli_type
        'I'
        >>> lestim.target_rec(-5).pauli_type
        'I'
    """
```

<a name="lestim.GateTarget.qubit_value"></a>
```python
# lestim.GateTarget.qubit_value

# (in class lestim.GateTarget)
@property
def qubit_value(
    self,
) -> Optional[int]:
    """Returns the integer value of the targeted qubit, or else None.

    Examples:
        >>> import lestim
        >>> lestim.GateTarget(6).qubit_value
        6
        >>> lestim.target_inv(7).qubit_value
        7
        >>> lestim.target_x(8).qubit_value
        8
        >>> lestim.target_y(2).qubit_value
        2
        >>> lestim.target_z(3).qubit_value
        3
        >>> print(lestim.target_sweep_bit(9).qubit_value)
        None
        >>> print(lestim.target_rec(-5).qubit_value)
        None
    """
```

<a name="lestim.GateTarget.value"></a>
```python
# lestim.GateTarget.value

# (in class lestim.GateTarget)
@property
def value(
    self,
) -> int:
    """The numeric part of the target.

    This is non-negative integer for qubit targets, and a negative integer for
    measurement record targets.

    Examples:
        >>> import lestim
        >>> lestim.GateTarget(6).value
        6
        >>> lestim.target_inv(7).value
        7
        >>> lestim.target_x(8).value
        8
        >>> lestim.target_y(2).value
        2
        >>> lestim.target_z(3).value
        3
        >>> lestim.target_sweep_bit(9).value
        9
        >>> lestim.target_rec(-5).value
        -5
    """
```

<a name="lestim.GateTargetWithCoords"></a>
```python
# lestim.GateTargetWithCoords

# (at top-level in the lestim module)
class GateTargetWithCoords:
    """A gate target with associated coordinate information.

    For example, if the gate target is a qubit from a circuit with
    QUBIT_COORDS instructions, the coords field will contain the
    coordinate data from the QUBIT_COORDS instruction for the qubit.

    This is helpful information to have available when debugging a
    problem in a circuit, instead of having to constantly manually
    look up the coordinates of a qubit index in order to understand
    what is happening.
    """
```

<a name="lestim.GateTargetWithCoords.__init__"></a>
```python
# lestim.GateTargetWithCoords.__init__

# (in class lestim.GateTargetWithCoords)
def __init__(
    self,
    *,
    gate_target: object,
    coords: List[float],
) -> None:
    """Creates a lestim.GateTargetWithCoords.
    """
```

<a name="lestim.GateTargetWithCoords.coords"></a>
```python
# lestim.GateTargetWithCoords.coords

# (in class lestim.GateTargetWithCoords)
@property
def coords(
    self,
) -> List[float]:
    """Returns the associated coordinate information as a list of floats.

    If there is no coordinate information, returns an empty list.
    """
```

<a name="lestim.GateTargetWithCoords.gate_target"></a>
```python
# lestim.GateTargetWithCoords.gate_target

# (in class lestim.GateTargetWithCoords)
@property
def gate_target(
    self,
) -> lestim._stim_polyfill.GateTarget:
    """Returns the actual gate target as a `lestim.GateTarget`.
    """
```

<a name="lestim.PauliString"></a>
```python
# lestim.PauliString

# (at top-level in the lestim module)
class PauliString:
    """A signed Pauli tensor product (e.g. "+X \u2297 X \u2297 X" or "-Y \u2297 Z".

    Represents a collection of Pauli operations (I, X, Y, Z) applied pairwise to a
    collection of qubits.

    Examples:
        >>> import lestim
        >>> lestim.PauliString("XX") * lestim.PauliString("YY")
        lestim.PauliString("-ZZ")
        >>> print(lestim.PauliString(5))
        +_____
    """
```

<a name="lestim.PauliString.__add__"></a>
```python
# lestim.PauliString.__add__

# (in class lestim.PauliString)
def __add__(
    self,
    rhs: lestim._stim_polyfill.PauliString,
) -> lestim._stim_polyfill.PauliString:
    """Returns the tensor product of two Pauli strings.

    Concatenates the Pauli strings and multiplies their signs.

    Args:
        rhs: A second lestim.PauliString.

    Examples:
        >>> import lestim

        >>> lestim.PauliString("X") + lestim.PauliString("YZ")
        lestim.PauliString("+XYZ")

        >>> lestim.PauliString("iX") + lestim.PauliString("-X")
        lestim.PauliString("-iXX")

    Returns:
        The tensor product.
    """
```

<a name="lestim.PauliString.__eq__"></a>
```python
# lestim.PauliString.__eq__

# (in class lestim.PauliString)
def __eq__(
    self,
    arg0: lestim._stim_polyfill.PauliString,
) -> bool:
    """Determines if two Pauli strings have identical contents.
    """
```

<a name="lestim.PauliString.__getitem__"></a>
```python
# lestim.PauliString.__getitem__

# (in class lestim.PauliString)
@overload
def __getitem__(
    self,
    index_or_slice: int,
) -> int:
    pass
@overload
def __getitem__(
    self,
    index_or_slice: slice,
) -> stim.PauliString:
    pass
def __getitem__(
    self,
    index_or_slice: object,
) -> object:
    """Returns an individual Pauli or Pauli string slice from the pauli string.

    Individual Paulis are returned as an int using the encoding 0=I, 1=X, 2=Y, 3=Z.
    Slices are returned as a lestim.PauliString (always with positive sign).

    Examples:
        >>> import lestim
        >>> p = lestim.PauliString("_XYZ")
        >>> p[2]
        2
        >>> p[-1]
        3
        >>> p[:2]
        lestim.PauliString("+_X")
        >>> p[::-1]
        lestim.PauliString("+ZYX_")

    Args:
        index_or_slice: The index of the pauli to return, or the slice of paulis to
            return.

    Returns:
        0: Identity.
        1: Pauli X.
        2: Pauli Y.
        3: Pauli Z.
    """
```

<a name="lestim.PauliString.__iadd__"></a>
```python
# lestim.PauliString.__iadd__

# (in class lestim.PauliString)
def __iadd__(
    self,
    rhs: lestim._stim_polyfill.PauliString,
) -> lestim._stim_polyfill.PauliString:
    """Performs an inplace tensor product.

    Concatenates the given Pauli string onto the receiving string and multiplies
    their signs.

    Args:
        rhs: A second lestim.PauliString.

    Examples:
        >>> import lestim

        >>> p = lestim.PauliString("iX")
        >>> alias = p
        >>> p += lestim.PauliString("-YY")
        >>> p
        lestim.PauliString("-iXYY")
        >>> alias is p
        True

    Returns:
        The mutated pauli string.
    """
```

<a name="lestim.PauliString.__imul__"></a>
```python
# lestim.PauliString.__imul__

# (in class lestim.PauliString)
def __imul__(
    self,
    rhs: object,
) -> lestim._stim_polyfill.PauliString:
    """Inplace right-multiplies the Pauli string.

    Can multiply by another Pauli string, a complex unit, or a tensor power.

    Args:
        rhs: The right hand side of the multiplication. This can be:
            - A lestim.PauliString to right-multiply term-by-term into the paulis of
                the pauli string.
            - A complex unit (1, -1, 1j, -1j) to multiply into the sign of the pauli
                string.
            - A non-negative integer indicating the tensor power to raise the pauli
                string to (how many times to repeat it).

    Examples:
        >>> import lestim

        >>> p = lestim.PauliString("X")
        >>> p *= 1j
        >>> p
        lestim.PauliString("+iX")

        >>> p = lestim.PauliString("iXY_")
        >>> p *= 3
        >>> p
        lestim.PauliString("-iXY_XY_XY_")

        >>> p = lestim.PauliString("X")
        >>> alias = p
        >>> p *= lestim.PauliString("Y")
        >>> alias
        lestim.PauliString("+iZ")

        >>> p = lestim.PauliString("X")
        >>> p *= lestim.PauliString("_YY")
        >>> p
        lestim.PauliString("+XYY")

    Returns:
        The mutated Pauli string.
    """
```

<a name="lestim.PauliString.__init__"></a>
```python
# lestim.PauliString.__init__

# (in class lestim.PauliString)
def __init__(
    self,
    arg: Union[None, int, str, stim.PauliString, Iterable[Union[int, 'Literal["_", "I", "X", "Y", "Z"]']]] = None,
    /,
) -> None:
    """Initializes a lestim.PauliString from the given argument.

    When given a string, the string is parsed as a pauli string. The string can
    optionally start with a sign ('+', '-', 'i', '+i', or '-i'). The rest of the
    string should be either a dense pauli string or a sparse pauli string. A dense
    pauli string is made up of characters from '_IXYZ' where '_' and 'I' mean
    identity, 'X' means Pauli X, 'Y' means Pauli Y, and 'Z' means Pauli Z. A sparse
    pauli string is a series of integers seperated by '*' and prefixed by 'I', 'X',
    'Y', or 'Z'.

    Arguments:
        arg [position-only]: This can be a variety of types, including:
            None (default): initializes an empty Pauli string.
            int: initializes an identity Pauli string of the given length.
            str: initializes by parsing the given text.
            lestim.PauliString: initializes a copy of the given Pauli string.
            Iterable: initializes by interpreting each item as a Pauli.
                Each item can be a single-qubit Pauli string (like "X"),
                or an integer. Integers use the convention 0=I, 1=X, 2=Y, 3=Z.

    Examples:
        >>> import lestim

        >>> lestim.PauliString("-XYZ")
        lestim.PauliString("-XYZ")

        >>> lestim.PauliString()
        lestim.PauliString("+")

        >>> lestim.PauliString(5)
        lestim.PauliString("+_____")

        >>> lestim.PauliString(lestim.PauliString("XX"))
        lestim.PauliString("+XX")

        >>> lestim.PauliString([0, 1, 3, 2])
        lestim.PauliString("+_XZY")

        >>> lestim.PauliString("X" for _ in range(4))
        lestim.PauliString("+XXXX")

        >>> lestim.PauliString("-X2*Y6")
        lestim.PauliString("-__X___Y")

        >>> lestim.PauliString("X6*Y6")
        lestim.PauliString("+i______Z")
    """
```

<a name="lestim.PauliString.__itruediv__"></a>
```python
# lestim.PauliString.__itruediv__

# (in class lestim.PauliString)
def __itruediv__(
    self,
    rhs: complex,
) -> lestim._stim_polyfill.PauliString:
    """Inplace divides the Pauli string by a complex unit.

    Args:
        rhs: The divisor. Can be 1, -1, 1j, or -1j.

    Examples:
        >>> import lestim

        >>> p = lestim.PauliString("X")
        >>> p /= 1j
        >>> p
        lestim.PauliString("-iX")

    Returns:
        The mutated Pauli string.

    Raises:
        ValueError: The divisor isn't 1, -1, 1j, or -1j.
    """
```

<a name="lestim.PauliString.__len__"></a>
```python
# lestim.PauliString.__len__

# (in class lestim.PauliString)
def __len__(
    self,
) -> int:
    """Returns the length the pauli string; the number of qubits it operates on.
    """
```

<a name="lestim.PauliString.__mul__"></a>
```python
# lestim.PauliString.__mul__

# (in class lestim.PauliString)
def __mul__(
    self,
    rhs: object,
) -> lestim._stim_polyfill.PauliString:
    """Right-multiplies the Pauli string.

    Can multiply by another Pauli string, a complex unit, or a tensor power.

    Args:
        rhs: The right hand side of the multiplication. This can be:
            - A lestim.PauliString to right-multiply term-by-term with the paulis of
                the pauli string.
            - A complex unit (1, -1, 1j, -1j) to multiply with the sign of the pauli
                string.
            - A non-negative integer indicating the tensor power to raise the pauli
                string to (how many times to repeat it).

    Examples:
        >>> import lestim

        >>> lestim.PauliString("X") * 1
        lestim.PauliString("+X")
        >>> lestim.PauliString("X") * -1
        lestim.PauliString("-X")
        >>> lestim.PauliString("X") * 1j
        lestim.PauliString("+iX")

        >>> lestim.PauliString("X") * 2
        lestim.PauliString("+XX")
        >>> lestim.PauliString("-X") * 2
        lestim.PauliString("+XX")
        >>> lestim.PauliString("iX") * 2
        lestim.PauliString("-XX")
        >>> lestim.PauliString("X") * 3
        lestim.PauliString("+XXX")
        >>> lestim.PauliString("iX") * 3
        lestim.PauliString("-iXXX")

        >>> lestim.PauliString("X") * lestim.PauliString("Y")
        lestim.PauliString("+iZ")
        >>> lestim.PauliString("X") * lestim.PauliString("XX_")
        lestim.PauliString("+_X_")
        >>> lestim.PauliString("XXXX") * lestim.PauliString("_XYZ")
        lestim.PauliString("+X_ZY")

    Returns:
        The product or tensor power.

    Raises:
        TypeError: The right hand side isn't a lestim.PauliString, a non-negative
            integer, or a complex unit (1, -1, 1j, or -1j).
    """
```

<a name="lestim.PauliString.__ne__"></a>
```python
# lestim.PauliString.__ne__

# (in class lestim.PauliString)
def __ne__(
    self,
    arg0: lestim._stim_polyfill.PauliString,
) -> bool:
    """Determines if two Pauli strings have non-identical contents.
    """
```

<a name="lestim.PauliString.__neg__"></a>
```python
# lestim.PauliString.__neg__

# (in class lestim.PauliString)
def __neg__(
    self,
) -> lestim._stim_polyfill.PauliString:
    """Returns the negation of the pauli string.

    Examples:
        >>> import lestim
        >>> -lestim.PauliString("X")
        lestim.PauliString("-X")
        >>> -lestim.PauliString("-Y")
        lestim.PauliString("+Y")
        >>> -lestim.PauliString("iZZZ")
        lestim.PauliString("-iZZZ")
    """
```

<a name="lestim.PauliString.__pos__"></a>
```python
# lestim.PauliString.__pos__

# (in class lestim.PauliString)
def __pos__(
    self,
) -> lestim._stim_polyfill.PauliString:
    """Returns a pauli string with the same contents.

    Examples:
        >>> import lestim
        >>> +lestim.PauliString("+X")
        lestim.PauliString("+X")
        >>> +lestim.PauliString("-YY")
        lestim.PauliString("-YY")
        >>> +lestim.PauliString("iZZZ")
        lestim.PauliString("+iZZZ")
    """
```

<a name="lestim.PauliString.__repr__"></a>
```python
# lestim.PauliString.__repr__

# (in class lestim.PauliString)
def __repr__(
    self,
) -> str:
    """Returns valid python code evaluating to an equivalent `lestim.PauliString`.
    """
```

<a name="lestim.PauliString.__rmul__"></a>
```python
# lestim.PauliString.__rmul__

# (in class lestim.PauliString)
def __rmul__(
    self,
    lhs: object,
) -> lestim._stim_polyfill.PauliString:
    """Left-multiplies the Pauli string.

    Can multiply by another Pauli string, a complex unit, or a tensor power.

    Args:
        lhs: The left hand side of the multiplication. This can be:
            - A lestim.PauliString to right-multiply term-by-term with the paulis of
                the pauli string.
            - A complex unit (1, -1, 1j, -1j) to multiply with the sign of the pauli
                string.
            - A non-negative integer indicating the tensor power to raise the pauli
                string to (how many times to repeat it).

    Examples:
        >>> import lestim

        >>> 1 * lestim.PauliString("X")
        lestim.PauliString("+X")
        >>> -1 * lestim.PauliString("X")
        lestim.PauliString("-X")
        >>> 1j * lestim.PauliString("X")
        lestim.PauliString("+iX")

        >>> 2 * lestim.PauliString("X")
        lestim.PauliString("+XX")
        >>> 2 * lestim.PauliString("-X")
        lestim.PauliString("+XX")
        >>> 2 * lestim.PauliString("iX")
        lestim.PauliString("-XX")
        >>> 3 * lestim.PauliString("X")
        lestim.PauliString("+XXX")
        >>> 3 * lestim.PauliString("iX")
        lestim.PauliString("-iXXX")

        >>> lestim.PauliString("X") * lestim.PauliString("Y")
        lestim.PauliString("+iZ")
        >>> lestim.PauliString("X") * lestim.PauliString("XX_")
        lestim.PauliString("+_X_")
        >>> lestim.PauliString("XXXX") * lestim.PauliString("_XYZ")
        lestim.PauliString("+X_ZY")

    Returns:
        The product.

    Raises:
        ValueError: The scalar phase factor isn't 1, -1, 1j, or -1j.
    """
```

<a name="lestim.PauliString.__setitem__"></a>
```python
# lestim.PauliString.__setitem__

# (in class lestim.PauliString)
def __setitem__(
    self,
    index: int,
    new_pauli: object,
) -> None:
    """Mutates an entry in the pauli string using the encoding 0=I, 1=X, 2=Y, 3=Z.

    Args:
        index: The index of the pauli to overwrite.
        new_pauli: Either a character from '_IXYZ' or an integer from range(4).

    Examples:
        >>> import lestim
        >>> p = lestim.PauliString(4)
        >>> p[2] = 1
        >>> print(p)
        +__X_
        >>> p[0] = 3
        >>> p[1] = 2
        >>> p[3] = 0
        >>> print(p)
        +ZYX_
        >>> p[0] = 'I'
        >>> p[1] = 'X'
        >>> p[2] = 'Y'
        >>> p[3] = 'Z'
        >>> print(p)
        +_XYZ
        >>> p[-1] = 'Y'
        >>> print(p)
        +_XYY
    """
```

<a name="lestim.PauliString.__str__"></a>
```python
# lestim.PauliString.__str__

# (in class lestim.PauliString)
def __str__(
    self,
) -> str:
    """Returns a text description.
    """
```

<a name="lestim.PauliString.__truediv__"></a>
```python
# lestim.PauliString.__truediv__

# (in class lestim.PauliString)
def __truediv__(
    self,
    rhs: complex,
) -> lestim._stim_polyfill.PauliString:
    """Divides the Pauli string by a complex unit.

    Args:
        rhs: The divisor. Can be 1, -1, 1j, or -1j.

    Examples:
        >>> import lestim

        >>> lestim.PauliString("X") / 1j
        lestim.PauliString("-iX")

    Returns:
        The quotient.

    Raises:
        ValueError: The divisor isn't 1, -1, 1j, or -1j.
    """
```

<a name="lestim.PauliString.after"></a>
```python
# lestim.PauliString.after

# (in class lestim.PauliString)
@overload
def after(
    self,
    operation: Union[stim.Circuit, stim.CircuitInstruction],
) -> stim.PauliString:
    pass
@overload
def after(
    self,
    operation: stim.Tableau,
    targets: Iterable[int],
) -> stim.PauliString:
    pass
def after(
    self,
    operation: Union[stim.Circuit, stim.Tableau, stim.CircuitInstruction],
    targets: Optional[Iterable[int]] = None,
) -> stim.PauliString:
    """Returns the result of conjugating the Pauli string by an operation.

    Args:
        operation: A circuit, tableau, or circuit instruction to
            conjugate the Pauli string by. Must be Clifford (e.g.
            if it's a circuit, the circuit can't have noise or
            measurements).
        targets: Required if and only if the operation is a tableau.
            Specifies which qubits to target.

    Examples:
        >>> import lestim
        >>> p = lestim.PauliString("_XYZ")

        >>> p.after(lestim.CircuitInstruction("H", [1]))
        lestim.PauliString("+_ZYZ")

        >>> p.after(lestim.Circuit('''
        ...     C_XYZ 1 2 3
        ... '''))
        lestim.PauliString("+_YZX")

        >>> p.after(lestim.Tableau.from_named_gate('CZ'), targets=[0, 1])
        lestim.PauliString("+ZXYZ")

    Returns:
        The conjugated Pauli string. The Pauli string after the
        operation that is exactly equivalent to the given Pauli
        string before the operation.
    """
```

<a name="lestim.PauliString.before"></a>
```python
# lestim.PauliString.before

# (in class lestim.PauliString)
@overload
def before(
    self,
    operation: Union[stim.Circuit, stim.CircuitInstruction],
) -> stim.PauliString:
    pass
@overload
def before(
    self,
    operation: stim.Tableau,
    targets: Iterable[int],
) -> stim.PauliString:
    pass
def before(
    self,
    operation: Union[stim.Circuit, stim.Tableau, stim.CircuitInstruction],
    targets: Optional[Iterable[int]] = None,
) -> stim.PauliString:
    """Returns the result of conjugating the Pauli string by an operation.

    Args:
        operation: A circuit, tableau, or circuit instruction to
            anti-conjugate the Pauli string by. Must be Clifford (e.g.
            if it's a circuit, the circuit can't have noise or
            measurements).
        targets: Required if and only if the operation is a tableau.
            Specifies which qubits to target.

    Examples:
        >>> import lestim
        >>> p = lestim.PauliString("_XYZ")

        >>> p.before(lestim.CircuitInstruction("H", [1]))
        lestim.PauliString("+_ZYZ")

        >>> p.before(lestim.Circuit('''
        ...     C_XYZ 1 2 3
        ... '''))
        lestim.PauliString("+_ZXY")

        >>> p.before(lestim.Tableau.from_named_gate('CZ'), targets=[0, 1])
        lestim.PauliString("+ZXYZ")

    Returns:
        The conjugated Pauli string. The Pauli string before the
        operation that is exactly equivalent to the given Pauli
        string after the operation.
    """
```

<a name="lestim.PauliString.commutes"></a>
```python
# lestim.PauliString.commutes

# (in class lestim.PauliString)
def commutes(
    self,
    other: lestim._stim_polyfill.PauliString,
) -> bool:
    """Determines if two Pauli strings commute or not.

    Two Pauli strings commute if they have an even number of matched
    non-equal non-identity Pauli terms. Otherwise they anticommute.

    Args:
        other: The other Pauli string.

    Examples:
        >>> import lestim
        >>> xx = lestim.PauliString("XX")
        >>> xx.commutes(lestim.PauliString("X_"))
        True
        >>> xx.commutes(lestim.PauliString("XX"))
        True
        >>> xx.commutes(lestim.PauliString("XY"))
        False
        >>> xx.commutes(lestim.PauliString("XZ"))
        False
        >>> xx.commutes(lestim.PauliString("ZZ"))
        True
        >>> xx.commutes(lestim.PauliString("X_Y__"))
        True
        >>> xx.commutes(lestim.PauliString(""))
        True

    Returns:
        True if the Pauli strings commute, False if they anti-commute.
    """
```

<a name="lestim.PauliString.copy"></a>
```python
# lestim.PauliString.copy

# (in class lestim.PauliString)
def copy(
    self,
) -> lestim._stim_polyfill.PauliString:
    """Returns a copy of the pauli string.

    The copy is an independent pauli string with the same contents.

    Examples:
        >>> import lestim
        >>> p1 = lestim.PauliString.random(2)
        >>> p2 = p1.copy()
        >>> p2 is p1
        False
        >>> p2 == p1
        True
    """
```

<a name="lestim.PauliString.from_numpy"></a>
```python
# lestim.PauliString.from_numpy

# (in class lestim.PauliString)
@staticmethod
def from_numpy(
    *,
    xs: np.ndarray,
    zs: np.ndarray,
    sign: Union[int, float, complex] = +1,
    num_qubits: Optional[int] = None,
) -> stim.PauliString:
    """Creates a pauli string from X bit and Z bit numpy arrays, using the encoding:

        x=0 and z=0 -> P=I
        x=1 and z=0 -> P=X
        x=1 and z=1 -> P=Y
        x=0 and z=1 -> P=Z

    Args:
        xs: The X bits of the pauli string. This array can either be a 1-dimensional
            numpy array with dtype=np.bool_, or a bit packed 1-dimensional numpy
            array with dtype=np.uint8. If the dtype is np.uint8 then the array is
            assumed to be bit packed in little endian order and the "num_qubits"
            argument must be specified. When bit packed, the x bit with offset k is
            stored at (xs[k // 8] >> (k % 8)) & 1.
        zs: The Z bits of the pauli string. This array can either be a 1-dimensional
            numpy array with dtype=np.bool_, or a bit packed 1-dimensional numpy
            array with dtype=np.uint8. If the dtype is np.uint8 then the array is
            assumed to be bit packed in little endian order and the "num_qubits"
            argument must be specified. When bit packed, the x bit with offset k is
            stored at (xs[k // 8] >> (k % 8)) & 1.
        sign: Defaults to +1. Set to +1, -1, 1j, or -1j to control the sign of the
            returned Pauli string.
        num_qubits: Must be specified if xs or zs is a bit packed array. Specifies
            the expected length of the Pauli string.

    Returns:
        The created pauli string.

    Examples:
        >>> import lestim
        >>> import numpy as np

        >>> xs = np.array([1, 1, 1, 1, 1, 1, 1, 0, 0], dtype=np.bool_)
        >>> zs = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1], dtype=np.bool_)
        >>> lestim.PauliString.from_numpy(xs=xs, zs=zs, sign=-1)
        lestim.PauliString("-XXXXYYYZZ")

        >>> xs = np.array([127, 0], dtype=np.uint8)
        >>> zs = np.array([240, 1], dtype=np.uint8)
        >>> lestim.PauliString.from_numpy(xs=xs, zs=zs, num_qubits=9)
        lestim.PauliString("+XXXXYYYZZ")
    """
```

<a name="lestim.PauliString.from_unitary_matrix"></a>
```python
# lestim.PauliString.from_unitary_matrix

# (in class lestim.PauliString)
@staticmethod
def from_unitary_matrix(
    matrix: Iterable[Iterable[Union[int, float, complex]]],
    *,
    endian: str = 'little',
    unsigned: bool = False,
) -> stim.PauliString:
    """Creates a lestim.PauliString from the unitary matrix of a Pauli group member.

    Args:
        matrix: A unitary matrix specified as an iterable of rows, with each row is
            an iterable of amplitudes. The unitary matrix must correspond to a
            Pauli string, including global phase.
        endian:
            "little": matrix entries are in little endian order, where higher index
                qubits correspond to larger changes in row/col indices.
            "big": matrix entries are in big endian order, where higher index
                qubits correspond to smaller changes in row/col indices.
        unsigned: When False, the input must only contain the values
            [0, 1, -1, 1j, -1j] and the output will have the correct global phase.
            When True, the input is permitted to be scaled by an arbitrary unit
            complex value and the output will always have positive sign.
            False is stricter but provides more information, while True is more
            flexible but provides less information.

    Returns:
        The pauli string equal to the given unitary matrix.

    Raises:
        ValueError: The given matrix isn't the unitary matrix of a Pauli string.

    Examples:
        >>> import lestim
        >>> lestim.PauliString.from_unitary_matrix([
        ...     [1j, 0],
        ...     [0, -1j],
        ... ], endian='little')
        lestim.PauliString("+iZ")

        >>> lestim.PauliString.from_unitary_matrix([
        ...     [1j**0.1, 0],
        ...     [0, -(1j**0.1)],
        ... ], endian='little', unsigned=True)
        lestim.PauliString("+Z")

        >>> lestim.PauliString.from_unitary_matrix([
        ...     [0, 1, 0, 0],
        ...     [1, 0, 0, 0],
        ...     [0, 0, 0, -1],
        ...     [0, 0, -1, 0],
        ... ], endian='little')
        lestim.PauliString("+XZ")
    """
```

<a name="lestim.PauliString.iter_all"></a>
```python
# lestim.PauliString.iter_all

# (in class lestim.PauliString)
@staticmethod
def iter_all(
    num_qubits: int,
    *,
    min_weight: int = 0,
    max_weight: object = None,
    allowed_paulis: str = 'XYZ',
) -> lestim._stim_polyfill.PauliStringIterator:
    """Returns an iterator that iterates over all matching pauli strings.

    Args:
        num_qubits: The desired number of qubits in the pauli strings.
        min_weight: Defaults to 0. The minimum number of non-identity terms that
            must be present in each yielded pauli string.
        max_weight: Defaults to None (unused). The maximum number of non-identity
            terms that must be present in each yielded pauli string.
        allowed_paulis: Defaults to "XYZ". Set this to a string containing the
            non-identity paulis that are allowed to appear in each yielded pauli
            string. This argument must be a string made up of only "X", "Y", and
            "Z" characters. A non-identity Pauli is allowed if it appears in the
            string, and not allowed if it doesn't. Identity Paulis are always
            allowed.

    Returns:
        An Iterable[lestim.PauliString] that yields the requested pauli strings.

    Examples:
        >>> import lestim
        >>> pauli_string_iterator = lestim.PauliString.iter_all(
        ...     num_qubits=3,
        ...     min_weight=1,
        ...     max_weight=2,
        ...     allowed_paulis="XZ",
        ... )
        >>> for p in pauli_string_iterator:
        ...     print(p)
        +X__
        +Z__
        +_X_
        +_Z_
        +__X
        +__Z
        +XX_
        +XZ_
        +ZX_
        +ZZ_
        +X_X
        +X_Z
        +Z_X
        +Z_Z
        +_XX
        +_XZ
        +_ZX
        +_ZZ
    """
```

<a name="lestim.PauliString.pauli_indices"></a>
```python
# lestim.PauliString.pauli_indices

# (in class lestim.PauliString)
def pauli_indices(
    self,
    included_paulis: str = "XYZ",
) -> List[int]:
    """Returns the indices of non-identity Paulis, or of specified Paulis.

    Args:
        include: A string containing the Pauli types to include.
            X type Pauli indices are included if "X" or "x" is in the string.
            Y type Pauli indices are included if "Y" or "y" is in the string.
            Z type Pauli indices are included if "Z" or "z" is in the string.
            I type Pauli indices are included if "I" or "_" is in the string.
            An exception is thrown if other characters are in the string.

    Returns:
        A list containing the ascending indices of matching Pauli terms.

    Examples:
        >>> import lestim
        >>> lestim.PauliString("_____X___Y____Z___").pauli_indices()
        [5, 9, 14]

        >>> lestim.PauliString("_____X___Y____Z___").pauli_indices("XZ")
        [5, 14]

        >>> lestim.PauliString("_____X___Y____Z___").pauli_indices("X")
        [5]

        >>> lestim.PauliString("_____X___Y____Z___").pauli_indices("Y")
        [9]

        >>> lestim.PauliString("_____X___Y____Z___").pauli_indices("IY")
        [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17]

        >>> lestim.PauliString("-X103*Y100").pauli_indices()
        [100, 103]
    """
```

<a name="lestim.PauliString.random"></a>
```python
# lestim.PauliString.random

# (in class lestim.PauliString)
@staticmethod
def random(
    num_qubits: int,
    *,
    allow_imaginary: bool = False,
) -> lestim._stim_polyfill.PauliString:
    """Samples a uniformly random Hermitian Pauli string.

    Args:
        num_qubits: The number of qubits the Pauli string should act on.
        allow_imaginary: Defaults to False. If True, the sign of the result may be
            1j or -1j in addition to +1 or -1. In other words, setting this to True
            allows the result to be non-Hermitian.

    Examples:
        >>> import lestim
        >>> p = lestim.PauliString.random(5)
        >>> len(p)
        5
        >>> p.sign in [-1, +1]
        True

        >>> p2 = lestim.PauliString.random(3, allow_imaginary=True)
        >>> len(p2)
        3
        >>> p2.sign in [-1, +1, 1j, -1j]
        True

    Returns:
        The sampled Pauli string.
    """
```

<a name="lestim.PauliString.sign"></a>
```python
# lestim.PauliString.sign

# (in class lestim.PauliString)
@property
def sign(
    self,
) -> complex:
    """The sign of the Pauli string. Can be +1, -1, 1j, or -1j.

    Examples:
        >>> import lestim
        >>> lestim.PauliString("X").sign
        (1+0j)
        >>> lestim.PauliString("-X").sign
        (-1+0j)
        >>> lestim.PauliString("iX").sign
        1j
        >>> lestim.PauliString("-iX").sign
        (-0-1j)
    """
@sign.setter
def sign(self, value: complex):
    pass
```

<a name="lestim.PauliString.to_numpy"></a>
```python
# lestim.PauliString.to_numpy

# (in class lestim.PauliString)
def to_numpy(
    self,
    *,
    bit_packed: bool = False,
) -> Tuple[np.ndarray, np.ndarray]:
    """Decomposes the contents of the pauli string into X bit and Z bit numpy arrays.

    Args:
        bit_packed: Defaults to False. Determines whether the output numpy arrays
            use dtype=bool_ or dtype=uint8 with 8 bools packed into each byte.

    Returns:
        An (xs, zs) tuple encoding the paulis from the string. The k'th Pauli from
        the string is encoded into k'th bit of xs and the k'th bit of zs using
        the "xz" encoding:

            P=I -> x=0 and z=0
            P=X -> x=1 and z=0
            P=Y -> x=1 and z=1
            P=Z -> x=0 and z=1

        The dtype and shape of the result depends on the bit_packed argument.

        If bit_packed=False:
            Each bit gets its own byte.
            xs.dtype = zs.dtype = np.bool_
            xs.shape = zs.shape = len(self)
            xs_k = xs[k]
            zs_k = zs[k]

        If bit_packed=True:
            Equivalent to applying np.packbits(bitorder='little') to the result.
            xs.dtype = zs.dtype = np.uint8
            xs.shape = zs.shape = math.ceil(len(self) / 8)
            xs_k = (xs[k // 8] >> (k % 8)) & 1
            zs_k = (zs[k // 8] >> (k % 8)) & 1

    Examples:
        >>> import lestim

        >>> xs, zs = lestim.PauliString("XXXXYYYZZ").to_numpy()
        >>> xs
        array([ True,  True,  True,  True,  True,  True,  True, False, False])
        >>> zs
        array([False, False, False, False,  True,  True,  True,  True,  True])

        >>> xs, zs = lestim.PauliString("XXXXYYYZZ").to_numpy(bit_packed=True)
        >>> xs
        array([127,   0], dtype=uint8)
        >>> zs
        array([240,   1], dtype=uint8)
    """
```

<a name="lestim.PauliString.to_tableau"></a>
```python
# lestim.PauliString.to_tableau

# (in class lestim.PauliString)
def to_tableau(
    self,
) -> lestim._stim_polyfill.Tableau:
    """Creates a Tableau equivalent to this Pauli string.

    The tableau represents a Clifford operation that multiplies qubits
    by the corresponding Pauli operations from this Pauli string.
    The global phase of the pauli operation is lost in the conversion.

    Returns:
        The created tableau.

    Examples:
        >>> import lestim
        >>> p = lestim.PauliString("ZZ")
        >>> p.to_tableau()
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("-X_"),
                lestim.PauliString("-_X"),
            ],
            zs=[
                lestim.PauliString("+Z_"),
                lestim.PauliString("+_Z"),
            ],
        )
        >>> q = lestim.PauliString("YX_Z")
        >>> q.to_tableau()
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("-X___"),
                lestim.PauliString("+_X__"),
                lestim.PauliString("+__X_"),
                lestim.PauliString("-___X"),
            ],
            zs=[
                lestim.PauliString("-Z___"),
                lestim.PauliString("-_Z__"),
                lestim.PauliString("+__Z_"),
                lestim.PauliString("+___Z"),
            ],
        )
    """
```

<a name="lestim.PauliString.to_unitary_matrix"></a>
```python
# lestim.PauliString.to_unitary_matrix

# (in class lestim.PauliString)
def to_unitary_matrix(
    self,
    *,
    endian: str,
) -> np.ndarray[np.complex64]:
    """Converts the pauli string into a unitary matrix.

    Args:
        endian:
            "little": The first qubit is the least significant (corresponds
                to an offset of 1 in the matrix).
            "big": The first qubit is the most significant (corresponds
                to an offset of 2**(n - 1) in the matrix).

    Returns:
        A numpy array with dtype=np.complex64 and
        shape=(1 << len(pauli_string), 1 << len(pauli_string)).

    Example:
        >>> import lestim
        >>> lestim.PauliString("-YZ").to_unitary_matrix(endian="little")
        array([[0.+0.j, 0.+1.j, 0.+0.j, 0.+0.j],
               [0.-1.j, 0.+0.j, 0.+0.j, 0.+0.j],
               [0.+0.j, 0.+0.j, 0.+0.j, 0.-1.j],
               [0.+0.j, 0.+0.j, 0.+1.j, 0.+0.j]], dtype=complex64)
    """
```

<a name="lestim.PauliString.weight"></a>
```python
# lestim.PauliString.weight

# (in class lestim.PauliString)
@property
def weight(
    self,
) -> int:
    """Returns the number of non-identity pauli terms in the pauli string.

    Examples:
        >>> import lestim
        >>> lestim.PauliString("+___").weight
        0
        >>> lestim.PauliString("+__X").weight
        1
        >>> lestim.PauliString("+XYZ").weight
        3
        >>> lestim.PauliString("-XXX___XXYZ").weight
        7
    """
```

<a name="lestim.PauliStringIterator"></a>
```python
# lestim.PauliStringIterator

# (at top-level in the lestim module)
class PauliStringIterator:
    """Iterates over all pauli strings matching specified patterns.

    Examples:
        >>> import lestim
        >>> pauli_string_iterator = lestim.PauliString.iter_all(
        ...     2,
        ...     min_weight=1,
        ...     max_weight=1,
        ...     allowed_paulis="XZ",
        ... )
        >>> for p in pauli_string_iterator:
        ...     print(p)
        +X_
        +Z_
        +_X
        +_Z
    """
```

<a name="lestim.PauliStringIterator.__iter__"></a>
```python
# lestim.PauliStringIterator.__iter__

# (in class lestim.PauliStringIterator)
def __iter__(
    self,
) -> lestim._stim_polyfill.PauliStringIterator:
    """Returns an independent copy of the pauli string iterator.

    Since for-loops and loop-comprehensions call `iter` on things they
    iterate, this effectively allows the iterator to be iterated
    multiple times.
    """
```

<a name="lestim.PauliStringIterator.__next__"></a>
```python
# lestim.PauliStringIterator.__next__

# (in class lestim.PauliStringIterator)
def __next__(
    self,
) -> lestim._stim_polyfill.PauliString:
    """Returns the next iterated pauli string.
    """
```

<a name="lestim.Tableau"></a>
```python
# lestim.Tableau

# (at top-level in the lestim module)
class Tableau:
    """A stabilizer tableau.

    Represents a Clifford operation by explicitly storing how that operation
    conjugates a list of Pauli group generators into composite Pauli products.

    Examples:
        >>> import lestim
        >>> lestim.Tableau.from_named_gate("H")
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+Z"),
            ],
            zs=[
                lestim.PauliString("+X"),
            ],
        )

        >>> t = lestim.Tableau.random(5)
        >>> t_inv = t**-1
        >>> print(t * t_inv)
        +-xz-xz-xz-xz-xz-
        | ++ ++ ++ ++ ++
        | XZ __ __ __ __
        | __ XZ __ __ __
        | __ __ XZ __ __
        | __ __ __ XZ __
        | __ __ __ __ XZ

        >>> x2z3 = t.x_output(2) * t.z_output(3)
        >>> t_inv(x2z3)
        lestim.PauliString("+__XZ_")
    """
```

<a name="lestim.Tableau.__add__"></a>
```python
# lestim.Tableau.__add__

# (in class lestim.Tableau)
def __add__(
    self,
    rhs: lestim._stim_polyfill.Tableau,
) -> lestim._stim_polyfill.Tableau:
    """Returns the direct sum (diagonal concatenation) of two Tableaus.

    Args:
        rhs: A second lestim.Tableau.

    Examples:
        >>> import lestim

        >>> s = lestim.Tableau.from_named_gate("S")
        >>> cz = lestim.Tableau.from_named_gate("CZ")
        >>> print(s + cz)
        +-xz-xz-xz-
        | ++ ++ ++
        | YZ __ __
        | __ XZ Z_
        | __ Z_ XZ

    Returns:
        The direct sum.
    """
```

<a name="lestim.Tableau.__call__"></a>
```python
# lestim.Tableau.__call__

# (in class lestim.Tableau)
def __call__(
    self,
    pauli_string: lestim._stim_polyfill.PauliString,
) -> lestim._stim_polyfill.PauliString:
    """Returns the conjugation of a PauliString by the Tableau's Clifford operation.

    The conjugation of P by C is equal to C**-1 * P * C. If P is a Pauli product
    before C, then P2 = C**-1 * P * C is an equivalent Pauli product after C.

    Args:
        pauli_string: The pauli string to conjugate.

    Returns:
        The new conjugated pauli string.

    Examples:
        >>> import lestim
        >>> t = lestim.Tableau.from_named_gate("CNOT")
        >>> p = lestim.PauliString("XX")
        >>> result = t(p)
        >>> print(result)
        +X_
    """
```

<a name="lestim.Tableau.__eq__"></a>
```python
# lestim.Tableau.__eq__

# (in class lestim.Tableau)
def __eq__(
    self,
    arg0: lestim._stim_polyfill.Tableau,
) -> bool:
    """Determines if two tableaus have identical contents.
    """
```

<a name="lestim.Tableau.__iadd__"></a>
```python
# lestim.Tableau.__iadd__

# (in class lestim.Tableau)
def __iadd__(
    self,
    rhs: lestim._stim_polyfill.Tableau,
) -> lestim._stim_polyfill.Tableau:
    """Performs an inplace direct sum (diagonal concatenation).

    Args:
        rhs: A second lestim.Tableau.

    Examples:
        >>> import lestim

        >>> s = lestim.Tableau.from_named_gate("S")
        >>> cz = lestim.Tableau.from_named_gate("CZ")
        >>> alias = s
        >>> s += cz
        >>> alias is s
        True
        >>> print(s)
        +-xz-xz-xz-
        | ++ ++ ++
        | YZ __ __
        | __ XZ Z_
        | __ Z_ XZ

    Returns:
        The mutated tableau.
    """
```

<a name="lestim.Tableau.__init__"></a>
```python
# lestim.Tableau.__init__

# (in class lestim.Tableau)
def __init__(
    self,
    num_qubits: int,
) -> None:
    """Creates an identity tableau over the given number of qubits.

    Examples:
        >>> import lestim
        >>> t = lestim.Tableau(3)
        >>> print(t)
        +-xz-xz-xz-
        | ++ ++ ++
        | XZ __ __
        | __ XZ __
        | __ __ XZ

    Args:
        num_qubits: The number of qubits the tableau's operation acts on.
    """
```

<a name="lestim.Tableau.__len__"></a>
```python
# lestim.Tableau.__len__

# (in class lestim.Tableau)
def __len__(
    self,
) -> int:
    """Returns the number of qubits operated on by the tableau.
    """
```

<a name="lestim.Tableau.__mul__"></a>
```python
# lestim.Tableau.__mul__

# (in class lestim.Tableau)
def __mul__(
    self,
    rhs: lestim._stim_polyfill.Tableau,
) -> lestim._stim_polyfill.Tableau:
    """Returns the product of two tableaus.

    If the tableau T1 represents the Clifford operation with unitary C1,
    and the tableau T2 represents the Clifford operation with unitary C2,
    then the tableau T1*T2 represents the Clifford operation with unitary C1*C2.

    Args:
        rhs: The tableau  on the right hand side of the multiplication.

    Examples:
        >>> import lestim
        >>> t1 = lestim.Tableau.random(4)
        >>> t2 = lestim.Tableau.random(4)
        >>> t3 = t2 * t1
        >>> p = lestim.PauliString.random(4)
        >>> t3(p) == t2(t1(p))
        True
    """
```

<a name="lestim.Tableau.__ne__"></a>
```python
# lestim.Tableau.__ne__

# (in class lestim.Tableau)
def __ne__(
    self,
    arg0: lestim._stim_polyfill.Tableau,
) -> bool:
    """Determines if two tableaus have non-identical contents.
    """
```

<a name="lestim.Tableau.__pow__"></a>
```python
# lestim.Tableau.__pow__

# (in class lestim.Tableau)
def __pow__(
    self,
    exponent: int,
) -> lestim._stim_polyfill.Tableau:
    """Raises the tableau to an integer power.

    Large powers are reached efficiently using repeated squaring.
    Negative powers are reached by inverting the tableau.

    Args:
        exponent: The power to raise to. Can be negative, zero, or positive.

    Examples:
        >>> import lestim
        >>> s = lestim.Tableau.from_named_gate("S")
        >>> s**0 == lestim.Tableau(1)
        True
        >>> s**1 == s
        True
        >>> s**2 == lestim.Tableau.from_named_gate("Z")
        True
        >>> s**-1 == s**3 == lestim.Tableau.from_named_gate("S_DAG")
        True
        >>> s**5 == s
        True
        >>> s**(400000000 + 1) == s
        True
        >>> s**(-400000000 + 1) == s
        True
    """
```

<a name="lestim.Tableau.__repr__"></a>
```python
# lestim.Tableau.__repr__

# (in class lestim.Tableau)
def __repr__(
    self,
) -> str:
    """Returns valid python code evaluating to an equal `lestim.Tableau`.
    """
```

<a name="lestim.Tableau.__str__"></a>
```python
# lestim.Tableau.__str__

# (in class lestim.Tableau)
def __str__(
    self,
) -> str:
    """Returns a text description.
    """
```

<a name="lestim.Tableau.append"></a>
```python
# lestim.Tableau.append

# (in class lestim.Tableau)
def append(
    self,
    gate: stim.Tableau,
    targets: Sequence[int],
) -> None:
    """Appends an operation's effect into this tableau, mutating this tableau.

    Time cost is O(n*m*m) where n=len(self) and m=len(gate).

    Args:
        gate: The tableau of the operation being appended into this tableau.
        targets: The qubits being targeted by the gate.

    Examples:
        >>> import lestim
        >>> cnot = lestim.Tableau.from_named_gate("CNOT")
        >>> t = lestim.Tableau(2)
        >>> t.append(cnot, [0, 1])
        >>> t.append(cnot, [1, 0])
        >>> t.append(cnot, [0, 1])
        >>> t == lestim.Tableau.from_named_gate("SWAP")
        True
    """
```

<a name="lestim.Tableau.copy"></a>
```python
# lestim.Tableau.copy

# (in class lestim.Tableau)
def copy(
    self,
) -> lestim._stim_polyfill.Tableau:
    """Returns a copy of the tableau. An independent tableau with the same contents.

    Examples:
        >>> import lestim
        >>> t1 = lestim.Tableau.random(2)
        >>> t2 = t1.copy()
        >>> t2 is t1
        False
        >>> t2 == t1
        True
    """
```

<a name="lestim.Tableau.from_circuit"></a>
```python
# lestim.Tableau.from_circuit

# (in class lestim.Tableau)
@staticmethod
def from_circuit(
    circuit: stim.Circuit,
    *,
    ignore_noise: bool = False,
    ignore_measurement: bool = False,
    ignore_reset: bool = False,
) -> stim.Tableau:
    """Converts a circuit into an equivalent stabilizer tableau.

    Args:
        circuit: The circuit to compile into a tableau.
        ignore_noise: Defaults to False. When False, any noise operations in the
            circuit will cause the conversion to fail with an exception. When True,
            noise operations are skipped over as if they weren't even present in the
            circuit.
        ignore_measurement: Defaults to False. When False, any measurement
            operations in the circuit will cause the conversion to fail with an
            exception. When True, measurement operations are skipped over as if they
            weren't even present in the circuit.
        ignore_reset: Defaults to False. When False, any reset operations in the
            circuit will cause the conversion to fail with an exception. When True,
            reset operations are skipped over as if they weren't even present in the
            circuit.

    Returns:
        The tableau equivalent to the given circuit (up to global phase).

    Raises:
        ValueError:
            The circuit contains noise operations but ignore_noise=False.
            OR
            The circuit contains measurement operations but
            ignore_measurement=False.
            OR
            The circuit contains reset operations but ignore_reset=False.

    Examples:
        >>> import lestim
        >>> lestim.Tableau.from_circuit(lestim.Circuit('''
        ...     H 0
        ...     CNOT 0 1
        ... '''))
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+Z_"),
                lestim.PauliString("+_X"),
            ],
            zs=[
                lestim.PauliString("+XX"),
                lestim.PauliString("+ZZ"),
            ],
        )
    """
```

<a name="lestim.Tableau.from_conjugated_generators"></a>
```python
# lestim.Tableau.from_conjugated_generators

# (in class lestim.Tableau)
@staticmethod
def from_conjugated_generators(
    *,
    xs: List[lestim._stim_polyfill.PauliString],
    zs: List[lestim._stim_polyfill.PauliString],
) -> lestim._stim_polyfill.Tableau:
    """Creates a tableau from the given outputs for each generator.

    Verifies that the tableau is well formed.

    Args:
        xs: A List[lestim.PauliString] with the results of conjugating X0, X1, etc.
        zs: A List[lestim.PauliString] with the results of conjugating Z0, Z1, etc.

    Returns:
        The created tableau.

    Raises:
        ValueError: The given outputs are malformed. Their lengths are inconsistent,
            or they don't satisfy the required commutation relationships.

    Examples:
        >>> import lestim
        >>> identity3 = lestim.Tableau.from_conjugated_generators(
        ...     xs=[
        ...         lestim.PauliString("X__"),
        ...         lestim.PauliString("_X_"),
        ...         lestim.PauliString("__X"),
        ...     ],
        ...     zs=[
        ...         lestim.PauliString("Z__"),
        ...         lestim.PauliString("_Z_"),
        ...         lestim.PauliString("__Z"),
        ...     ],
        ... )
        >>> identity3 == lestim.Tableau(3)
        True
    """
```

<a name="lestim.Tableau.from_named_gate"></a>
```python
# lestim.Tableau.from_named_gate

# (in class lestim.Tableau)
@staticmethod
def from_named_gate(
    name: str,
) -> lestim._stim_polyfill.Tableau:
    """Returns the tableau of a named Clifford gate.

    Args:
        name: The name of the Clifford gate.

    Returns:
        The gate's tableau.

    Examples:
        >>> import lestim
        >>> print(lestim.Tableau.from_named_gate("H"))
        +-xz-
        | ++
        | ZX
        >>> print(lestim.Tableau.from_named_gate("CNOT"))
        +-xz-xz-
        | ++ ++
        | XZ _Z
        | X_ XZ
        >>> print(lestim.Tableau.from_named_gate("S"))
        +-xz-
        | ++
        | YZ
    """
```

<a name="lestim.Tableau.from_numpy"></a>
```python
# lestim.Tableau.from_numpy

# (in class lestim.Tableau)
def from_numpy(
    self,
    *,
    x2x: np.ndarray,
    x2z: np.ndarray,
    z2x: np.ndarray,
    z2z: np.ndarray,
    x_signs: Optional[np.ndarray] = None,
    z_signs: Optional[np.ndarray] = None,
) -> stim.Tableau:
    """Creates a tableau from numpy arrays x2x, x2z, z2x, z2z, x_signs, and z_signs.

    The x2x, x2z, z2x, z2z arrays are the four quadrants of the table defined in
    Aaronson and Gottesman's "Improved Simulation of Stabilizer Circuits"
    ( https://arxiv.org/abs/quant-ph/0406196 ).

    Args:
        x2x: A 2d numpy array containing the x-to-x coupling bits. The bits can be
            bit packed (dtype=uint8) or not (dtype=bool_). When not bit packed, the
            result will satisfy result.x_output_pauli(i, j) in [1, 2] == x2x[i, j].
            Bit packing must be in little endian order and only applies to the
            second axis.
        x2z: A 2d numpy array containing the x-to-z coupling bits. The bits can be
            bit packed (dtype=uint8) or not (dtype=bool_). When not bit packed, the
            result will satisfy result.x_output_pauli(i, j) in [2, 3] == x2z[i, j].
            Bit packing must be in little endian order and only applies to the
            second axis.
        z2x: A 2d numpy array containing the z-to-x coupling bits. The bits can be
            bit packed (dtype=uint8) or not (dtype=bool_). When not bit packed, the
            result will satisfy result.z_output_pauli(i, j) in [1, 2] == z2x[i, j].
            Bit packing must be in little endian order and only applies to the
            second axis.
        z2z: A 2d numpy array containing the z-to-z coupling bits. The bits can be
            bit packed (dtype=uint8) or not (dtype=bool_). When not bit packed, the
            result will satisfy result.z_output_pauli(i, j) in [2, 3] == z2z[i, j].
            Bit packing must be in little endian order and only applies to the
            second axis.
        x_signs: Defaults to all-positive if not specified. A 1d numpy array
            containing the sign bits for the X generator outputs. False means
            positive and True means negative. The bits can be bit packed
            (dtype=uint8) or not (dtype=bool_). Bit packing must be in little endian
            order.
        z_signs: Defaults to all-positive if not specified. A 1d numpy array
            containing the sign bits for the Z generator outputs. False means
            positive and True means negative. The bits can be bit packed
            (dtype=uint8) or not (dtype=bool_). Bit packing must be in little endian
            order.

    Returns:
        The tableau created from the numpy data.

    Examples:
        >>> import lestim
        >>> import numpy as np

        >>> tableau = lestim.Tableau.from_numpy(
        ...     x2x=np.array([[1, 1], [0, 1]], dtype=np.bool_),
        ...     z2x=np.array([[0, 0], [0, 0]], dtype=np.bool_),
        ...     x2z=np.array([[0, 0], [0, 0]], dtype=np.bool_),
        ...     z2z=np.array([[1, 0], [1, 1]], dtype=np.bool_),
        ... )
        >>> tableau
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+XX"),
                lestim.PauliString("+_X"),
            ],
            zs=[
                lestim.PauliString("+Z_"),
                lestim.PauliString("+ZZ"),
            ],
        )
        >>> tableau == lestim.Tableau.from_named_gate("CNOT")
        True

        >>> lestim.Tableau.from_numpy(
        ...     x2x=np.array([[9], [5], [7], [6]], dtype=np.uint8),
        ...     x2z=np.array([[13], [13], [0], [3]], dtype=np.uint8),
        ...     z2x=np.array([[8], [5], [9], [15]], dtype=np.uint8),
        ...     z2z=np.array([[6], [11], [2], [3]], dtype=np.uint8),
        ...     x_signs=np.array([7], dtype=np.uint8),
        ...     z_signs=np.array([9], dtype=np.uint8),
        ... )
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("-Y_ZY"),
                lestim.PauliString("-Y_YZ"),
                lestim.PauliString("-XXX_"),
                lestim.PauliString("+ZYX_"),
            ],
            zs=[
                lestim.PauliString("-_ZZX"),
                lestim.PauliString("+YZXZ"),
                lestim.PauliString("+XZ_X"),
                lestim.PauliString("-YYXX"),
            ],
        )
    """
```

<a name="lestim.Tableau.from_stabilizers"></a>
```python
# lestim.Tableau.from_stabilizers

# (in class lestim.Tableau)
@staticmethod
def from_stabilizers(
    stabilizers: Iterable[stim.PauliString],
    *,
    allow_redundant: bool = False,
    allow_underconstrained: bool = False,
) -> stim.Tableau:
    """Creates a tableau representing a state with the given stabilizers.

    Args:
        stabilizers: A list of `lestim.PauliString`s specifying the stabilizers that
            the state must have. It is permitted for stabilizers to have different
            lengths. All stabilizers are padded up to the length of the longest
            stabilizer by appending identity terms.
        allow_redundant: Defaults to False. If set to False, then the given
            stabilizers must all be independent. If any one of them is a product of
            the others (including the empty product), an exception will be raised.
            If set to True, then redundant stabilizers are simply ignored.
        allow_underconstrained: Defaults to False. If set to False, then the given
            stabilizers must form a complete set of generators. They must exactly
            specify the desired stabilizer state, with no degrees of freedom left
            over. For an n-qubit state there must be n independent stabilizers. If
            set to True, then there can be leftover degrees of freedom which can be
            set arbitrarily.

    Returns:
        A tableau which, when applied to the all-zeroes state, produces a state
        with the given stabilizers.

        Guarantees that result.z_output(k) will be equal to the k'th independent
        stabilizer from the `stabilizers` argument.

    Raises:
        ValueError:
            A stabilizer is redundant but allow_redundant=True wasn't set.
            OR
            The given stabilizers are contradictory (e.g. "+Z" and "-Z" both
            specified).
            OR
            The given stabilizers anticommute (e.g. "+Z" and "+X" both specified).
            OR
            The stabilizers left behind a degree of freedom but
            allow_underconstrained=True wasn't set.
            OR
            A stabilizer has an imaginary sign (i or -i).

    Examples:

        >>> import lestim
        >>> lestim.Tableau.from_stabilizers([
        ...     lestim.PauliString("XX"),
        ...     lestim.PauliString("ZZ"),
        ... ])
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+Z_"),
                lestim.PauliString("+_X"),
            ],
            zs=[
                lestim.PauliString("+XX"),
                lestim.PauliString("+ZZ"),
            ],
        )

        >>> lestim.Tableau.from_stabilizers([
        ...     lestim.PauliString("XX_"),
        ...     lestim.PauliString("ZZ_"),
        ...     lestim.PauliString("-YY_"),
        ...     lestim.PauliString(""),
        ... ], allow_underconstrained=True, allow_redundant=True)
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+Z__"),
                lestim.PauliString("+_X_"),
                lestim.PauliString("+__X"),
            ],
            zs=[
                lestim.PauliString("+XX_"),
                lestim.PauliString("+ZZ_"),
                lestim.PauliString("+__Z"),
            ],
        )
    """
```

<a name="lestim.Tableau.from_state_vector"></a>
```python
# lestim.Tableau.from_state_vector

# (in class lestim.Tableau)
@staticmethod
def from_state_vector(
    state_vector: Iterable[float],
    *,
    endian: str,
) -> stim.Tableau:
    """Creates a tableau representing the stabilizer state of the given state vector.

    Args:
        state_vector: A list of complex amplitudes specifying a superposition. The
            vector must correspond to a state that is reachable using Clifford
            operations, and must be normalized (i.e. it must be a unit vector).
        endian:
            "little": state vector is in little endian order, where higher index
                qubits correspond to larger changes in the state index.
            "big": state vector is in big endian order, where higher index qubits
                correspond to smaller changes in the state index.

    Returns:
        A tableau which, when applied to the all-zeroes state, produces a state
        with the given state vector.

    Raises:
        ValueError:
            The given state vector isn't a list of complex values specifying a
            stabilizer state.
            OR
            The given endian value isn't 'little' or 'big'.

    Examples:

        >>> import lestim
        >>> lestim.Tableau.from_state_vector([
        ...     0.5**0.5,
        ...     0.5**0.5 * 1j,
        ... ], endian='little')
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+Z"),
            ],
            zs=[
                lestim.PauliString("+Y"),
            ],
        )
        >>> lestim.Tableau.from_state_vector([
        ...     0.5**0.5,
        ...     0,
        ...     0,
        ...     0.5**0.5,
        ... ], endian='little')
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+Z_"),
                lestim.PauliString("+_X"),
            ],
            zs=[
                lestim.PauliString("+XX"),
                lestim.PauliString("+ZZ"),
            ],
        )
    """
```

<a name="lestim.Tableau.from_unitary_matrix"></a>
```python
# lestim.Tableau.from_unitary_matrix

# (in class lestim.Tableau)
@staticmethod
def from_unitary_matrix(
    matrix: Iterable[Iterable[float]],
    *,
    endian: str = 'little',
) -> stim.Tableau:
    """Creates a tableau from the unitary matrix of a Clifford operation.

    Args:
        matrix: A unitary matrix specified as an iterable of rows, with each row is
            an iterable of amplitudes. The unitary matrix must correspond to a
            Clifford operation.
        endian:
            "little": matrix entries are in little endian order, where higher index
                qubits correspond to larger changes in row/col indices.
            "big": matrix entries are in big endian order, where higher index
                qubits correspond to smaller changes in row/col indices.
    Returns:
        The tableau equivalent to the given unitary matrix (up to global phase).

    Raises:
        ValueError: The given matrix isn't the unitary matrix of a Clifford
            operation.

    Examples:
        >>> import lestim
        >>> lestim.Tableau.from_unitary_matrix([
        ...     [1, 0],
        ...     [0, 1j],
        ... ], endian='little')
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+Y"),
            ],
            zs=[
                lestim.PauliString("+Z"),
            ],
        )

        >>> lestim.Tableau.from_unitary_matrix([
        ...     [1, 0, 0, 0],
        ...     [0, 1, 0, 0],
        ...     [0, 0, 0, -1j],
        ...     [0, 0, 1j, 0],
        ... ], endian='little')
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+XZ"),
                lestim.PauliString("+YX"),
            ],
            zs=[
                lestim.PauliString("+ZZ"),
                lestim.PauliString("+_Z"),
            ],
        )
    """
```

<a name="lestim.Tableau.inverse"></a>
```python
# lestim.Tableau.inverse

# (in class lestim.Tableau)
def inverse(
    self,
    *,
    unsigned: bool = False,
) -> lestim._stim_polyfill.Tableau:
    """Computes the inverse of the tableau.

    The inverse T^-1 of a tableau T is the unique tableau with the property that
    T * T^-1 = T^-1 * T = I where I is the identity tableau.

    Args:
        unsigned: Defaults to false. When set to true, skips computing the signs of
            the output observables and instead just set them all to be positive.
            This is beneficial because computing the signs takes O(n^3) time and the
            rest of the inverse computation is O(n^2) where n is the number of
            qubits in the tableau. So, if you only need the Pauli terms (not the
            signs), it is significantly cheaper.

    Returns:
        The inverse tableau.

    Examples:
        >>> import lestim

        >>> # Check that the inverse agrees with hard-coded tableaus.
        >>> s = lestim.Tableau.from_named_gate("S")
        >>> s_dag = lestim.Tableau.from_named_gate("S_DAG")
        >>> s.inverse() == s_dag
        True
        >>> z = lestim.Tableau.from_named_gate("Z")
        >>> z.inverse() == z
        True

        >>> # Check that multiplying by the inverse produces the identity.
        >>> t = lestim.Tableau.random(10)
        >>> t_inv = t.inverse()
        >>> identity = lestim.Tableau(10)
        >>> t * t_inv == t_inv * t == identity
        True

        >>> # Check a manual case.
        >>> t = lestim.Tableau.from_conjugated_generators(
        ...     xs=[
        ...         lestim.PauliString("-__Z"),
        ...         lestim.PauliString("+XZ_"),
        ...         lestim.PauliString("+_ZZ"),
        ...     ],
        ...     zs=[
        ...         lestim.PauliString("-YYY"),
        ...         lestim.PauliString("+Z_Z"),
        ...         lestim.PauliString("-ZYZ")
        ...     ],
        ... )
        >>> print(t.inverse())
        +-xz-xz-xz-
        | -- +- --
        | XX XX YX
        | XZ Z_ X_
        | X_ YX Y_
        >>> print(t.inverse(unsigned=True))
        +-xz-xz-xz-
        | ++ ++ ++
        | XX XX YX
        | XZ Z_ X_
        | X_ YX Y_
    """
```

<a name="lestim.Tableau.inverse_x_output"></a>
```python
# lestim.Tableau.inverse_x_output

# (in class lestim.Tableau)
def inverse_x_output(
    self,
    input_index: int,
    *,
    unsigned: bool = False,
) -> lestim._stim_polyfill.PauliString:
    """Conjugates a single-qubit X Pauli generator by the inverse of the tableau.

    A faster version of `tableau.inverse(unsigned).x_output(input_index)`.

    Args:
        input_index: Identifies the column (the qubit of the X generator) to return
            from the inverse tableau.
        unsigned: Defaults to false. When set to true, skips computing the result's
            sign and instead just sets it to positive. This is beneficial because
            computing the sign takes O(n^2) time whereas all other parts of the
            computation take O(n) time where n is the number of qubits in the
            tableau.

    Returns:
        The result of conjugating an X generator by the inverse of the tableau.

    Examples:
        >>> import lestim

        # Check equivalence with the inverse's x_output.
        >>> t = lestim.Tableau.random(4)
        >>> expected = t.inverse().x_output(0)
        >>> t.inverse_x_output(0) == expected
        True
        >>> expected.sign = +1
        >>> t.inverse_x_output(0, unsigned=True) == expected
        True
    """
```

<a name="lestim.Tableau.inverse_x_output_pauli"></a>
```python
# lestim.Tableau.inverse_x_output_pauli

# (in class lestim.Tableau)
def inverse_x_output_pauli(
    self,
    input_index: int,
    output_index: int,
) -> int:
    """Constant-time version of `tableau.inverse().x_output(input_index)[output_index]`

    Args:
        input_index: Identifies the column (the qubit of the input X generator) in
            the inverse tableau.
        output_index: Identifies the row (the output qubit) in the inverse tableau.

    Returns:
        An integer identifying Pauli at the given location in the inverse tableau:

            0: I
            1: X
            2: Y
            3: Z

    Examples:
        >>> import lestim

        >>> t_inv = lestim.Tableau.from_conjugated_generators(
        ...     xs=[lestim.PauliString("-Y_"), lestim.PauliString("+YZ")],
        ...     zs=[lestim.PauliString("-ZY"), lestim.PauliString("+YX")],
        ... ).inverse()
        >>> t_inv.inverse_x_output_pauli(0, 0)
        2
        >>> t_inv.inverse_x_output_pauli(0, 1)
        0
        >>> t_inv.inverse_x_output_pauli(1, 0)
        2
        >>> t_inv.inverse_x_output_pauli(1, 1)
        3
    """
```

<a name="lestim.Tableau.inverse_y_output"></a>
```python
# lestim.Tableau.inverse_y_output

# (in class lestim.Tableau)
def inverse_y_output(
    self,
    input_index: int,
    *,
    unsigned: bool = False,
) -> lestim._stim_polyfill.PauliString:
    """Conjugates a single-qubit Y Pauli generator by the inverse of the tableau.

    A faster version of `tableau.inverse(unsigned).y_output(input_index)`.

    Args:
        input_index: Identifies the column (the qubit of the Y generator) to return
            from the inverse tableau.
        unsigned: Defaults to false. When set to true, skips computing the result's
            sign and instead just sets it to positive. This is beneficial because
            computing the sign takes O(n^2) time whereas all other parts of the
            computation take O(n) time where n is the number of qubits in the
            tableau.

    Returns:
        The result of conjugating a Y generator by the inverse of the tableau.

    Examples:
        >>> import lestim

        # Check equivalence with the inverse's y_output.
        >>> t = lestim.Tableau.random(4)
        >>> expected = t.inverse().y_output(0)
        >>> t.inverse_y_output(0) == expected
        True
        >>> expected.sign = +1
        >>> t.inverse_y_output(0, unsigned=True) == expected
        True
    """
```

<a name="lestim.Tableau.inverse_y_output_pauli"></a>
```python
# lestim.Tableau.inverse_y_output_pauli

# (in class lestim.Tableau)
def inverse_y_output_pauli(
    self,
    input_index: int,
    output_index: int,
) -> int:
    """Constant-time version of `tableau.inverse().y_output(input_index)[output_index]`

    Args:
        input_index: Identifies the column (the qubit of the input Y generator) in
            the inverse tableau.
        output_index: Identifies the row (the output qubit) in the inverse tableau.

    Returns:
        An integer identifying Pauli at the given location in the inverse tableau:

            0: I
            1: X
            2: Y
            3: Z

    Examples:
        >>> import lestim

        >>> t_inv = lestim.Tableau.from_conjugated_generators(
        ...     xs=[lestim.PauliString("-Y_"), lestim.PauliString("+YZ")],
        ...     zs=[lestim.PauliString("-ZY"), lestim.PauliString("+YX")],
        ... ).inverse()
        >>> t_inv.inverse_y_output_pauli(0, 0)
        1
        >>> t_inv.inverse_y_output_pauli(0, 1)
        2
        >>> t_inv.inverse_y_output_pauli(1, 0)
        0
        >>> t_inv.inverse_y_output_pauli(1, 1)
        2
    """
```

<a name="lestim.Tableau.inverse_z_output"></a>
```python
# lestim.Tableau.inverse_z_output

# (in class lestim.Tableau)
def inverse_z_output(
    self,
    input_index: int,
    *,
    unsigned: bool = False,
) -> lestim._stim_polyfill.PauliString:
    """Conjugates a single-qubit Z Pauli generator by the inverse of the tableau.

    A faster version of `tableau.inverse(unsigned).z_output(input_index)`.

    Args:
        input_index: Identifies the column (the qubit of the Z generator) to return
            from the inverse tableau.
        unsigned: Defaults to false. When set to true, skips computing the result's
            sign and instead just sets it to positive. This is beneficial because
            computing the sign takes O(n^2) time whereas all other parts of the
            computation take O(n) time where n is the number of qubits in the
            tableau.

    Returns:
        The result of conjugating a Z generator by the inverse of the tableau.

    Examples:
        >>> import lestim

        >>> import lestim

        # Check equivalence with the inverse's z_output.
        >>> t = lestim.Tableau.random(4)
        >>> expected = t.inverse().z_output(0)
        >>> t.inverse_z_output(0) == expected
        True
        >>> expected.sign = +1
        >>> t.inverse_z_output(0, unsigned=True) == expected
        True
    """
```

<a name="lestim.Tableau.inverse_z_output_pauli"></a>
```python
# lestim.Tableau.inverse_z_output_pauli

# (in class lestim.Tableau)
def inverse_z_output_pauli(
    self,
    input_index: int,
    output_index: int,
) -> int:
    """Constant-time version of `tableau.inverse().z_output(input_index)[output_index]`

    Args:
        input_index: Identifies the column (the qubit of the input Z generator) in
            the inverse tableau.
        output_index: Identifies the row (the output qubit) in the inverse tableau.

    Returns:
        An integer identifying Pauli at the given location in the inverse tableau:

            0: I
            1: X
            2: Y
            3: Z

    Examples:
        >>> import lestim

        >>> t_inv = lestim.Tableau.from_conjugated_generators(
        ...     xs=[lestim.PauliString("-Y_"), lestim.PauliString("+YZ")],
        ...     zs=[lestim.PauliString("-ZY"), lestim.PauliString("+YX")],
        ... ).inverse()
        >>> t_inv.inverse_z_output_pauli(0, 0)
        3
        >>> t_inv.inverse_z_output_pauli(0, 1)
        2
        >>> t_inv.inverse_z_output_pauli(1, 0)
        2
        >>> t_inv.inverse_z_output_pauli(1, 1)
        1
    """
```

<a name="lestim.Tableau.iter_all"></a>
```python
# lestim.Tableau.iter_all

# (in class lestim.Tableau)
@staticmethod
def iter_all(
    num_qubits: int,
    *,
    unsigned: bool = False,
) -> lestim._stim_polyfill.TableauIterator:
    """Returns an iterator that iterates over all Tableaus of a given size.

    Args:
        num_qubits: The size of tableau to iterate over.
        unsigned: Defaults to False. If set to True, only tableaus where
            all columns have positive sign are yielded by the iterator.
            This substantially reduces the total number of tableaus to
            iterate over.

    Returns:
        An Iterable[lestim.Tableau] that yields the requested tableaus.

    Examples:
        >>> import lestim
        >>> single_qubit_gate_reprs = set()
        >>> for t in lestim.Tableau.iter_all(1):
        ...     single_qubit_gate_reprs.add(repr(t))
        >>> len(single_qubit_gate_reprs)
        24

        >>> num_2q_gates_mod_paulis = 0
        >>> for _ in lestim.Tableau.iter_all(2, unsigned=True):
        ...     num_2q_gates_mod_paulis += 1
        >>> num_2q_gates_mod_paulis
        720
    """
```

<a name="lestim.Tableau.prepend"></a>
```python
# lestim.Tableau.prepend

# (in class lestim.Tableau)
def prepend(
    self,
    gate: stim.Tableau,
    targets: Sequence[int],
) -> None:
    """Prepends an operation's effect into this tableau, mutating this tableau.

    Time cost is O(n*m*m) where n=len(self) and m=len(gate).

    Args:
        gate: The tableau of the operation being prepended into this tableau.
        targets: The qubits being targeted by the gate.

    Examples:
        >>> import lestim
        >>> t = lestim.Tableau.from_named_gate("H")
        >>> t.prepend(lestim.Tableau.from_named_gate("X"), [0])
        >>> t == lestim.Tableau.from_named_gate("SQRT_Y_DAG")
        True
    """
```

<a name="lestim.Tableau.random"></a>
```python
# lestim.Tableau.random

# (in class lestim.Tableau)
@staticmethod
def random(
    num_qubits: int,
) -> lestim._stim_polyfill.Tableau:
    """Samples a uniformly random Clifford operation and returns its tableau.

    Args:
        num_qubits: The number of qubits the tableau should act on.

    Returns:
        The sampled tableau.

    Examples:
        >>> import lestim
        >>> t = lestim.Tableau.random(42)

    References:
        "Hadamard-free circuits expose the structure of the Clifford group"
        Sergey Bravyi, Dmitri Maslov
        https://arxiv.org/abs/2003.09412
    """
```

<a name="lestim.Tableau.then"></a>
```python
# lestim.Tableau.then

# (in class lestim.Tableau)
def then(
    self,
    second: lestim._stim_polyfill.Tableau,
) -> lestim._stim_polyfill.Tableau:
    """Returns the result of composing two tableaus.

    If the tableau T1 represents the Clifford operation with unitary C1,
    and the tableau T2 represents the Clifford operation with unitary C2,
    then the tableau T1.then(T2) represents the Clifford operation with unitary
    C2*C1.

    Args:
        second: The result is equivalent to applying the second tableau after
            the receiving tableau.

    Examples:
        >>> import lestim
        >>> t1 = lestim.Tableau.random(4)
        >>> t2 = lestim.Tableau.random(4)
        >>> t3 = t1.then(t2)
        >>> p = lestim.PauliString.random(4)
        >>> t3(p) == t2(t1(p))
        True
    """
```

<a name="lestim.Tableau.to_circuit"></a>
```python
# lestim.Tableau.to_circuit

# (in class lestim.Tableau)
def to_circuit(
    self,
    method: 'Literal["elimination", "graph_state"]' = 'elimination',
) -> stim.Circuit:
    """Synthesizes a circuit that implements the tableau's Clifford operation.

    The circuits returned by this method are not guaranteed to be stable
    from version to version, and may be produced using randomization.

    Args:
        method: The method to use when synthesizing the circuit. Available values:
            "elimination": Cancels off-diagonal terms using Gaussian elimination.
                Gate set: H, S, CX
                Circuit qubit count: n
                Circuit operation count: O(n^2)
                Circuit depth: O(n^2)
            "graph_state": Prepares the tableau's state using a graph state circuit.
                Gate set: RX, CZ, H, S, X, Y, Z
                Circuit qubit count: n
                Circuit operation count: O(n^2)

                The circuit will be made up of three layers:
                    1. An RX layer initializing all qubits.
                    2. A CZ layer coupling the qubits.
                        (Each CZ is an edge in the graph state.)
                    3. A single qubit rotation layer.

                Note: "graph_state" treats the tableau as a state instead of as a
                Clifford operation. It will preserve the set of stabilizers, but
                not the exact choice of generators.
            "mpp_state": Prepares the tableau's state using MPP and feedback.
                Gate set: MPP, CX rec, CY rec, CZ rec
                Circuit qubit count: n
                Circuit operation count: O(n^2)

                The circuit will be made up of two layers:
                    1. An MPP layer measuring each of the tableau's stabilizers.
                    2. A feedback layer using the measurement results to control
                        whether or not to apply each of the tableau's destabilizers
                        in order to get the correct sign for each stabilizer.

                Note: "mpp_state" treats the tableau as a state instead of as a
                Clifford operation. It will preserve the set of stabilizers, but
                not the exact choice of generators.
            "mpp_state_unsigned": Prepares the tableau's state up to sign using MPP.
                Gate set: MPP
                Circuit qubit count: n
                Circuit operation count: O(n^2)

                The circuit will contain a series of MPP measurements measuring each
                of the tableau's stabilizers. The stabilizers are measured in the
                order used by the tableau (i.e. tableau.z_output(k) is the k'th
                stabilizer measured).

                Note: "mpp_state_unsigned" treats the tableau as a state instead of
                as a Clifford operation. It will preserve the set of stabilizers,
                but not the exact choice of generators.
    Returns:
        The synthesized circuit.

    Example:
        >>> import lestim
        >>> tableau = lestim.Tableau.from_conjugated_generators(
        ...     xs=[
        ...         lestim.PauliString("+YZ__"),
        ...         lestim.PauliString("-Y_XY"),
        ...         lestim.PauliString("+___Y"),
        ...         lestim.PauliString("+YZX_"),
        ...     ],
        ...     zs=[
        ...         lestim.PauliString("+XZYY"),
        ...         lestim.PauliString("-XYX_"),
        ...         lestim.PauliString("-ZXXZ"),
        ...         lestim.PauliString("+XXZ_"),
        ...     ],
        ... )

        >>> tableau.to_circuit()
        lestim.Circuit('''
            S 0
            H 0 1 3
            CX 0 1 0 2 0 3
            S 1 3
            H 1 3
            CX 1 0 3 0 3 1 1 3 3 1
            H 1
            S 1
            CX 1 3
            H 2 3
            CX 2 1 3 1 3 2 2 3 3 2
            H 3
            CX 2 3
            S 3
            H 3 0 1 2
            S 0 0 1 1 2 2
            H 0 1 2
            S 3 3
        ''')

        >>> tableau.to_circuit("graph_state")
        lestim.Circuit('''
            RX 0 1 2 3
            TICK
            CZ 0 3 1 2 1 3
            TICK
            X 0 1
            Z 2
            S 2 3
            H 3
            S 3
        ''')

        >>> tableau.to_circuit("mpp_state_unsigned")
        lestim.Circuit('''
            MPP X0*Z1*Y2*Y3 !X0*Y1*X2 !Z0*X1*X2*Z3 X0*X1*Z2
        ''')

        >>> tableau.to_circuit("mpp_state")
        lestim.Circuit('''
            MPP X0*Z1*Y2*Y3 !X0*Y1*X2 !Z0*X1*X2*Z3 X0*X1*Z2
            CX rec[-3] 2 rec[-1] 2
            CY rec[-4] 0 rec[-3] 0 rec[-3] 3 rec[-2] 3 rec[-1] 0
            CZ rec[-4] 1 rec[-1] 1
        ''')
    """
```

<a name="lestim.Tableau.to_numpy"></a>
```python
# lestim.Tableau.to_numpy

# (in class lestim.Tableau)
def to_numpy(
    self,
    *,
    bit_packed: bool = False,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Decomposes the contents of the tableau into six numpy arrays.

    The first four numpy arrays correspond to the four quadrants of the table
    defined in Aaronson and Gottesman's "Improved Simulation of Stabilizer Circuits"
    ( https://arxiv.org/abs/quant-ph/0406196 ).

    The last two numpy arrays are the X and Z sign bit vectors of the tableau.

    Args:
        bit_packed: Defaults to False. Determines whether the output numpy arrays
            use dtype=bool_ or dtype=uint8 with 8 bools packed into each byte.

    Returns:
        An (x2x, x2z, z2x, z2z, x_signs, z_signs) tuple encoding the tableau.

        x2x: A 2d table of whether tableau(X_i)_j is X or Y (instead of I or Z).
        x2z: A 2d table of whether tableau(X_i)_j is Z or Y (instead of I or X).
        z2x: A 2d table of whether tableau(Z_i)_j is X or Y (instead of I or Z).
        z2z: A 2d table of whether tableau(Z_i)_j is Z or Y (instead of I or X).
        x_signs: A vector of whether tableau(X_i) is negative.
        z_signs: A vector of whether tableau(Z_i) is negative.

        If bit_packed=False then:
            x2x.dtype = np.bool_
            x2z.dtype = np.bool_
            z2x.dtype = np.bool_
            z2z.dtype = np.bool_
            x_signs.dtype = np.bool_
            z_signs.dtype = np.bool_
            x2x.shape = (len(tableau), len(tableau))
            x2z.shape = (len(tableau), len(tableau))
            z2x.shape = (len(tableau), len(tableau))
            z2z.shape = (len(tableau), len(tableau))
            x_signs.shape = len(tableau)
            z_signs.shape = len(tableau)
            x2x[i, j] = tableau.x_output_pauli(i, j) in [1, 2]
            x2z[i, j] = tableau.x_output_pauli(i, j) in [2, 3]
            z2x[i, j] = tableau.z_output_pauli(i, j) in [1, 2]
            z2z[i, j] = tableau.z_output_pauli(i, j) in [2, 3]

        If bit_packed=True then:
            x2x.dtype = np.uint8
            x2z.dtype = np.uint8
            z2x.dtype = np.uint8
            z2z.dtype = np.uint8
            x_signs.dtype = np.uint8
            z_signs.dtype = np.uint8
            x2x.shape = (len(tableau), math.ceil(len(tableau) / 8))
            x2z.shape = (len(tableau), math.ceil(len(tableau) / 8))
            z2x.shape = (len(tableau), math.ceil(len(tableau) / 8))
            z2z.shape = (len(tableau), math.ceil(len(tableau) / 8))
            x_signs.shape = math.ceil(len(tableau) / 8)
            z_signs.shape = math.ceil(len(tableau) / 8)
            (x2x[i, j // 8] >> (j % 8)) & 1 = tableau.x_output_pauli(i, j) in [1, 2]
            (x2z[i, j // 8] >> (j % 8)) & 1 = tableau.x_output_pauli(i, j) in [2, 3]
            (z2x[i, j // 8] >> (j % 8)) & 1 = tableau.z_output_pauli(i, j) in [1, 2]
            (z2z[i, j // 8] >> (j % 8)) & 1 = tableau.z_output_pauli(i, j) in [2, 3]

    Examples:
        >>> import lestim
        >>> cnot = lestim.Tableau.from_named_gate("CNOT")
        >>> print(repr(cnot))
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+XX"),
                lestim.PauliString("+_X"),
            ],
            zs=[
                lestim.PauliString("+Z_"),
                lestim.PauliString("+ZZ"),
            ],
        )
        >>> x2x, x2z, z2x, z2z, x_signs, z_signs = cnot.to_numpy()
        >>> x2x
        array([[ True,  True],
               [False,  True]])
        >>> x2z
        array([[False, False],
               [False, False]])
        >>> z2x
        array([[False, False],
               [False, False]])
        >>> z2z
        array([[ True, False],
               [ True,  True]])
        >>> x_signs
        array([False, False])
        >>> z_signs
        array([False, False])

        >>> t = lestim.Tableau.from_conjugated_generators(
        ...     xs=[
        ...         lestim.PauliString("-Y_ZY"),
        ...         lestim.PauliString("-Y_YZ"),
        ...         lestim.PauliString("-XXX_"),
        ...         lestim.PauliString("+ZYX_"),
        ...     ],
        ...     zs=[
        ...         lestim.PauliString("-_ZZX"),
        ...         lestim.PauliString("+YZXZ"),
        ...         lestim.PauliString("+XZ_X"),
        ...         lestim.PauliString("-YYXX"),
        ...     ],
        ... )

        >>> x2x, x2z, z2x, z2z, x_signs, z_signs = t.to_numpy()
        >>> x2x
        array([[ True, False, False,  True],
               [ True, False,  True, False],
               [ True,  True,  True, False],
               [False,  True,  True, False]])
        >>> x2z
        array([[ True, False,  True,  True],
               [ True, False,  True,  True],
               [False, False, False, False],
               [ True,  True, False, False]])
        >>> z2x
        array([[False, False, False,  True],
               [ True, False,  True, False],
               [ True, False, False,  True],
               [ True,  True,  True,  True]])
        >>> z2z
        array([[False,  True,  True, False],
               [ True,  True, False,  True],
               [False,  True, False, False],
               [ True,  True, False, False]])
        >>> x_signs
        array([ True,  True,  True, False])
        >>> z_signs
        array([ True, False, False,  True])

        >>> x2x, x2z, z2x, z2z, x_signs, z_signs = t.to_numpy(bit_packed=True)
        >>> x2x
        array([[9],
               [5],
               [7],
               [6]], dtype=uint8)
        >>> x2z
        array([[13],
               [13],
               [ 0],
               [ 3]], dtype=uint8)
        >>> z2x
        array([[ 8],
               [ 5],
               [ 9],
               [15]], dtype=uint8)
        >>> z2z
        array([[ 6],
               [11],
               [ 2],
               [ 3]], dtype=uint8)
        >>> x_signs
        array([7], dtype=uint8)
        >>> z_signs
        array([9], dtype=uint8)
    """
```

<a name="lestim.Tableau.to_pauli_string"></a>
```python
# lestim.Tableau.to_pauli_string

# (in class lestim.Tableau)
def to_pauli_string(
    self,
) -> lestim._stim_polyfill.PauliString:
    """Return a Pauli string equivalent to the tableau.

    If the tableau is equivalent to a pauli product, creates
    an equivalent pauli string. If not, then an error is raised.

    Returns:
        The created pauli string

    Raises:
        ValueError: The Tableau isn't equivalent to a Pauli product.

    Example:
        >>> import lestim
        >>> t = (lestim.Tableau.from_named_gate("Z") +
        ...      lestim.Tableau.from_named_gate("Y") +
        ...      lestim.Tableau.from_named_gate("I") +
        ...      lestim.Tableau.from_named_gate("X"))
        >>> print(t)
        +-xz-xz-xz-xz-
        | -+ -- ++ +-
        | XZ __ __ __
        | __ XZ __ __
        | __ __ XZ __
        | __ __ __ XZ
        >>> print(t.to_pauli_string())
        +ZY_X
    """
```

<a name="lestim.Tableau.to_stabilizers"></a>
```python
# lestim.Tableau.to_stabilizers

# (in class lestim.Tableau)
def to_stabilizers(
    self,
    *,
    canonicalize: bool = False,
) -> List[lestim._stim_polyfill.PauliString]:
    """Returns the stabilizer generators of the tableau, optionally canonicalized.

    The stabilizer generators of the tableau are its Z outputs. Canonicalizing
    standardizes the generators, so that states that are equal will produce the
    same generators. For example, [ZI, IZ], [ZI, ZZ], amd [ZZ, ZI] describe equal
    states and all canonicalize to [ZI, IZ].

    The canonical form is computed as follows:

        1. Get a list of stabilizers using `tableau.z_output(k)` for each k.
        2. Perform Gaussian elimination. pivoting on standard generators.
            2a) Pivot on g=X0 first, then Z0, X1, Z1, X2, Z2, etc.
            2b) Find a stabilizer that uses the generator g. If there are none,
                go to the next g.
            2c) Multiply that stabilizer into all other stabilizers that use the
                generator g.
            2d) Swap that stabilizer with the stabilizer at position `r` then
                increment `r`. `r` starts at 0.

    Args:
        canonicalize: Defaults to False. When False, the tableau's Z outputs
            are returned unchanged. When True, the Z outputs are rewritten
            into a standard form. Two stabilizer states have the same standard
            form if and only if they describe equivalent quantum states.

    Returns:
        A List[lestim.PauliString] of the tableau's stabilizer generators.

    Examples:
        >>> import lestim
        >>> t = lestim.Tableau.from_named_gate("CNOT")

        >>> raw_stabilizers = t.to_stabilizers()
        >>> for e in raw_stabilizers:
        ...     print(repr(e))
        lestim.PauliString("+Z_")
        lestim.PauliString("+ZZ")

        >>> canonical_stabilizers = t.to_stabilizers(canonicalize=True)
        >>> for e in canonical_stabilizers:
        ...     print(repr(e))
        lestim.PauliString("+Z_")
        lestim.PauliString("+_Z")
    """
```

<a name="lestim.Tableau.to_state_vector"></a>
```python
# lestim.Tableau.to_state_vector

# (in class lestim.Tableau)
def to_state_vector(
    self,
    *,
    endian: str = 'little',
) -> np.ndarray[np.complex64]:
    """Returns the state vector produced by applying the tableau to the |0..0> state.

    This function takes O(n * 2**n) time and O(2**n) space, where n is the number of
    qubits. The computation is done by initialization a random state vector and
    iteratively projecting it into the +1 eigenspace of each stabilizer of the
    state. The state is then canonicalized so that zero values are actually exactly
    0, and so that the first non-zero entry is positive.

    Args:
        endian:
            "little" (default): state vector is in little endian order, where higher
                index qubits correspond to larger changes in the state index.
            "big": state vector is in big endian order, where higher index qubits
                correspond to smaller changes in the state index.

    Returns:
        A `numpy.ndarray[numpy.complex64]` of computational basis amplitudes.

        If the result is in little endian order then the amplitude at offset
        b_0 + b_1*2 + b_2*4 + ... + b_{n-1}*2^{n-1} is the amplitude for the
        computational basis state where the qubit with index 0 is storing the bit
        b_0, the qubit with index 1 is storing the bit b_1, etc.

        If the result is in big endian order then the amplitude at offset
        b_0 + b_1*2 + b_2*4 + ... + b_{n-1}*2^{n-1} is the amplitude for the
        computational basis state where the qubit with index 0 is storing the bit
        b_{n-1}, the qubit with index 1 is storing the bit b_{n-2}, etc.

    Examples:
        >>> import lestim
        >>> import numpy as np
        >>> i2 = lestim.Tableau.from_named_gate('I')
        >>> x = lestim.Tableau.from_named_gate('X')
        >>> h = lestim.Tableau.from_named_gate('H')

        >>> (x + i2).to_state_vector(endian='little')
        array([0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j], dtype=complex64)

        >>> (i2 + x).to_state_vector(endian='little')
        array([0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j], dtype=complex64)

        >>> (i2 + x).to_state_vector(endian='big')
        array([0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j], dtype=complex64)

        >>> (h + h).to_state_vector(endian='little')
        array([0.5+0.j, 0.5+0.j, 0.5+0.j, 0.5+0.j], dtype=complex64)
    """
```

<a name="lestim.Tableau.to_unitary_matrix"></a>
```python
# lestim.Tableau.to_unitary_matrix

# (in class lestim.Tableau)
def to_unitary_matrix(
    self,
    *,
    endian: str,
) -> np.ndarray[np.complex64]:
    """Converts the tableau into a unitary matrix.

    For an n-qubit tableau, this method performs O(n 4^n) work. It uses the state
    channel duality to transform the tableau into a list of stabilizers, then
    generates a random state vector and projects it into the +1 eigenspace of each
    stabilizer.

    Note that tableaus don't have a defined global phase, so the result's global
    phase may be different from what you expect. For example, the square of
    SQRT_X's unitary might equal -X instead of +X.

    Args:
        endian:
            "little": The first qubit is the least significant (corresponds
                to an offset of 1 in the state vector).
            "big": The first qubit is the most significant (corresponds
                to an offset of 2**(n - 1) in the state vector).

    Returns:
        A numpy array with dtype=np.complex64 and
        shape=(1 << len(tableau), 1 << len(tableau)).

    Example:
        >>> import lestim
        >>> cnot = lestim.Tableau.from_conjugated_generators(
        ...     xs=[
        ...         lestim.PauliString("XX"),
        ...         lestim.PauliString("_X"),
        ...     ],
        ...     zs=[
        ...         lestim.PauliString("Z_"),
        ...         lestim.PauliString("ZZ"),
        ...     ],
        ... )
        >>> cnot.to_unitary_matrix(endian='big')
        array([[1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j],
               [0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j],
               [0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j],
               [0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j]], dtype=complex64)
    """
```

<a name="lestim.Tableau.x_output"></a>
```python
# lestim.Tableau.x_output

# (in class lestim.Tableau)
def x_output(
    self,
    target: int,
) -> lestim._stim_polyfill.PauliString:
    """Returns the result of conjugating a Pauli X by the tableau's Clifford operation.

    Args:
        target: The qubit targeted by the Pauli X operation.

    Examples:
        >>> import lestim
        >>> h = lestim.Tableau.from_named_gate("H")
        >>> h.x_output(0)
        lestim.PauliString("+Z")

        >>> cnot = lestim.Tableau.from_named_gate("CNOT")
        >>> cnot.x_output(0)
        lestim.PauliString("+XX")
        >>> cnot.x_output(1)
        lestim.PauliString("+_X")
    """
```

<a name="lestim.Tableau.x_output_pauli"></a>
```python
# lestim.Tableau.x_output_pauli

# (in class lestim.Tableau)
def x_output_pauli(
    self,
    input_index: int,
    output_index: int,
) -> int:
    """Constant-time version of `tableau.x_output(input_index)[output_index]`

    Args:
        input_index: Identifies the tableau column (the qubit of the input X
            generator).
        output_index: Identifies the tableau row (the output qubit).

    Returns:
        An integer identifying Pauli at the given location in the tableau:

            0: I
            1: X
            2: Y
            3: Z

    Examples:
        >>> import lestim

        >>> t = lestim.Tableau.from_conjugated_generators(
        ...     xs=[lestim.PauliString("-Y_"), lestim.PauliString("+YZ")],
        ...     zs=[lestim.PauliString("-ZY"), lestim.PauliString("+YX")],
        ... )
        >>> t.x_output_pauli(0, 0)
        2
        >>> t.x_output_pauli(0, 1)
        0
        >>> t.x_output_pauli(1, 0)
        2
        >>> t.x_output_pauli(1, 1)
        3
    """
```

<a name="lestim.Tableau.x_sign"></a>
```python
# lestim.Tableau.x_sign

# (in class lestim.Tableau)
def x_sign(
    self,
    target: int,
) -> int:
    """Returns just the sign of the result of conjugating an X generator.

    This operation runs in constant time.

    Args:
        target: The qubit the X generator applies to.

    Examples:
        >>> import lestim
        >>> lestim.Tableau.from_named_gate("S_DAG").x_sign(0)
        -1
        >>> lestim.Tableau.from_named_gate("S").x_sign(0)
        1
    """
```

<a name="lestim.Tableau.y_output"></a>
```python
# lestim.Tableau.y_output

# (in class lestim.Tableau)
def y_output(
    self,
    target: int,
) -> lestim._stim_polyfill.PauliString:
    """Returns the result of conjugating a Pauli Y by the tableau's Clifford operation.

    Args:
        target: The qubit targeted by the Pauli Y operation.

    Examples:
        >>> import lestim
        >>> h = lestim.Tableau.from_named_gate("H")
        >>> h.y_output(0)
        lestim.PauliString("-Y")

        >>> cnot = lestim.Tableau.from_named_gate("CNOT")
        >>> cnot.y_output(0)
        lestim.PauliString("+YX")
        >>> cnot.y_output(1)
        lestim.PauliString("+ZY")
    """
```

<a name="lestim.Tableau.y_output_pauli"></a>
```python
# lestim.Tableau.y_output_pauli

# (in class lestim.Tableau)
def y_output_pauli(
    self,
    input_index: int,
    output_index: int,
) -> int:
    """Constant-time version of `tableau.y_output(input_index)[output_index]`

    Args:
        input_index: Identifies the tableau column (the qubit of the input Y
            generator).
        output_index: Identifies the tableau row (the output qubit).

    Returns:
        An integer identifying Pauli at the given location in the tableau:

            0: I
            1: X
            2: Y
            3: Z

    Examples:
        >>> import lestim

        >>> t = lestim.Tableau.from_conjugated_generators(
        ...     xs=[lestim.PauliString("-Y_"), lestim.PauliString("+YZ")],
        ...     zs=[lestim.PauliString("-ZY"), lestim.PauliString("+YX")],
        ... )
        >>> t.y_output_pauli(0, 0)
        1
        >>> t.y_output_pauli(0, 1)
        2
        >>> t.y_output_pauli(1, 0)
        0
        >>> t.y_output_pauli(1, 1)
        2
    """
```

<a name="lestim.Tableau.y_sign"></a>
```python
# lestim.Tableau.y_sign

# (in class lestim.Tableau)
def y_sign(
    self,
    target: int,
) -> int:
    """Returns just the sign of the result of conjugating a Y generator.

    Unlike x_sign and z_sign, this operation runs in linear time.
    The Y generator has to be computed by multiplying the X and Z
    outputs and the sign depends on all terms.

    Args:
        target: The qubit the Y generator applies to.

    Examples:
        >>> import lestim
        >>> lestim.Tableau.from_named_gate("S_DAG").y_sign(0)
        1
        >>> lestim.Tableau.from_named_gate("S").y_sign(0)
        -1
    """
```

<a name="lestim.Tableau.z_output"></a>
```python
# lestim.Tableau.z_output

# (in class lestim.Tableau)
def z_output(
    self,
    target: int,
) -> lestim._stim_polyfill.PauliString:
    """Returns the result of conjugating a Pauli Z by the tableau's Clifford operation.

    Args:
        target: The qubit targeted by the Pauli Z operation.

    Examples:
        >>> import lestim
        >>> h = lestim.Tableau.from_named_gate("H")
        >>> h.z_output(0)
        lestim.PauliString("+X")

        >>> cnot = lestim.Tableau.from_named_gate("CNOT")
        >>> cnot.z_output(0)
        lestim.PauliString("+Z_")
        >>> cnot.z_output(1)
        lestim.PauliString("+ZZ")
    """
```

<a name="lestim.Tableau.z_output_pauli"></a>
```python
# lestim.Tableau.z_output_pauli

# (in class lestim.Tableau)
def z_output_pauli(
    self,
    input_index: int,
    output_index: int,
) -> int:
    """Constant-time version of `tableau.z_output(input_index)[output_index]`

    Args:
        input_index: Identifies the tableau column (the qubit of the input Z
            generator).
        output_index: Identifies the tableau row (the output qubit).

    Returns:
        An integer identifying Pauli at the given location in the tableau:

            0: I
            1: X
            2: Y
            3: Z

    Examples:
        >>> import lestim

        >>> t = lestim.Tableau.from_conjugated_generators(
        ...     xs=[lestim.PauliString("-Y_"), lestim.PauliString("+YZ")],
        ...     zs=[lestim.PauliString("-ZY"), lestim.PauliString("+YX")],
        ... )
        >>> t.z_output_pauli(0, 0)
        3
        >>> t.z_output_pauli(0, 1)
        2
        >>> t.z_output_pauli(1, 0)
        2
        >>> t.z_output_pauli(1, 1)
        1
    """
```

<a name="lestim.Tableau.z_sign"></a>
```python
# lestim.Tableau.z_sign

# (in class lestim.Tableau)
def z_sign(
    self,
    target: int,
) -> int:
    """Returns just the sign of the result of conjugating a Z generator.

    This operation runs in constant time.

    Args:
        target: The qubit the Z generator applies to.

    Examples:
        >>> import lestim
        >>> lestim.Tableau.from_named_gate("SQRT_X_DAG").z_sign(0)
        1
        >>> lestim.Tableau.from_named_gate("SQRT_X").z_sign(0)
        -1
    """
```

<a name="lestim.TableauIterator"></a>
```python
# lestim.TableauIterator

# (at top-level in the lestim module)
class TableauIterator:
    """Iterates over all stabilizer tableaus of a specified size.

    Examples:
        >>> import lestim
        >>> tableau_iterator = lestim.Tableau.iter_all(1)
        >>> n = 0
        >>> for single_qubit_clifford in tableau_iterator:
        ...     n += 1
        >>> n
        24
    """
```

<a name="lestim.TableauIterator.__iter__"></a>
```python
# lestim.TableauIterator.__iter__

# (in class lestim.TableauIterator)
def __iter__(
    self,
) -> lestim._stim_polyfill.TableauIterator:
    """Returns an independent copy of the tableau iterator.

    Since for-loops and loop-comprehensions call `iter` on things they
    iterate, this effectively allows the iterator to be iterated
    multiple times.
    """
```

<a name="lestim.TableauIterator.__next__"></a>
```python
# lestim.TableauIterator.__next__

# (in class lestim.TableauIterator)
def __next__(
    self,
) -> lestim._stim_polyfill.Tableau:
    """Returns the next iterated tableau.
    """
```

<a name="lestim.TableauSimulator"></a>
```python
# lestim.TableauSimulator

# (at top-level in the lestim module)
class TableauSimulator:
    """A stabilizer circuit simulator that tracks an inverse stabilizer tableau.

    Supports interactive usage, where gates and measurements are applied on demand.

    Examples:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.h(0)
        >>> if s.measure(0):
        ...     s.h(1)
        ...     s.cnot(1, 2)
        >>> s.measure(1) == s.measure(2)
        True

        >>> s = lestim.TableauSimulator()
        >>> s.h(0)
        >>> s.cnot(0, 1)
        >>> s.current_inverse_tableau()
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+ZX"),
                lestim.PauliString("+_X"),
            ],
            zs=[
                lestim.PauliString("+X_"),
                lestim.PauliString("+XZ"),
            ],
        )
    """
```

<a name="lestim.TableauSimulator.__init__"></a>
```python
# lestim.TableauSimulator.__init__

# (in class lestim.TableauSimulator)
def __init__(
    self,
    *,
    seed: Optional[int] = None,
) -> None:
    """Initializes a lestim.TableauSimulator.

    Args:
        seed: PARTIALLY determines simulation results by deterministically seeding
            the random number generator.

            Must be None or an integer in range(2**64).

            Defaults to None. When None, the prng is seeded from system entropy.

            When set to an integer, making the exact same series calls on the exact
            same machine with the exact same version of Stim will produce the exact
            same simulation results.

            CAUTION: simulation results *WILL NOT* be consistent between versions of
            Stim. This restriction is present to make it possible to have future
            optimizations to the random sampling, and is enforced by introducing
            intentional differences in the seeding strategy from version to version.

            CAUTION: simulation results *MAY NOT* be consistent across machines that
            differ in the width of supported SIMD instructions. For example, using
            the same seed on a machine that supports AVX instructions and one that
            only supports SSE instructions may produce different simulation results.

            CAUTION: simulation results *MAY NOT* be consistent if you vary how the
            circuit is executed. For example, reordering whether a reset on one
            qubit happens before or after a reset on another qubit can result in
            different measurement results being observed starting from the same
            seed.

    Returns:
        An initialized lestim.TableauSimulator.

    Examples:
        >>> import lestim
        >>> s = lestim.TableauSimulator(seed=0)
        >>> s2 = lestim.TableauSimulator(seed=0)
        >>> s.h(0)
        >>> s2.h(0)
        >>> s.measure(0) == s2.measure(0)
        True
    """
```

<a name="lestim.TableauSimulator.c_xyz"></a>
```python
# lestim.TableauSimulator.c_xyz

# (in class lestim.TableauSimulator)
def c_xyz(
    self,
    *targets,
) -> None:
    """Applies a C_XYZ gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
    """
```

<a name="lestim.TableauSimulator.c_zyx"></a>
```python
# lestim.TableauSimulator.c_zyx

# (in class lestim.TableauSimulator)
def c_zyx(
    self,
    *targets,
) -> None:
    """Applies a C_ZYX gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
    """
```

<a name="lestim.TableauSimulator.canonical_stabilizers"></a>
```python
# lestim.TableauSimulator.canonical_stabilizers

# (in class lestim.TableauSimulator)
def canonical_stabilizers(
    self,
) -> List[lestim._stim_polyfill.PauliString]:
    """Returns a standardized list of the simulator's current stabilizer generators.

    Two simulators have the same canonical stabilizers if and only if their current
    quantum state is equal (and tracking the same number of qubits).

    The canonical form is computed as follows:

        1. Get a list of stabilizers using the `z_output`s of
            `simulator.current_inverse_tableau()**-1`.
        2. Perform Gaussian elimination on each generator g.
            2a) The generators are considered in order X0, Z0, X1, Z1, X2, Z2, etc.
            2b) Pick any stabilizer that uses the generator g. If there are none,
                go to the next g.
            2c) Multiply that stabilizer into all other stabilizers that use the
                generator g.
            2d) Swap that stabilizer with the stabilizer at position `next_output`
                then increment `next_output`.

    Returns:
        A List[lestim.PauliString] of the simulator's state's stabilizers.

    Examples:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.h(0)
        >>> s.cnot(0, 1)
        >>> s.x(2)
        >>> for e in s.canonical_stabilizers():
        ...     print(repr(e))
        lestim.PauliString("+XX_")
        lestim.PauliString("+ZZ_")
        lestim.PauliString("-__Z")

        >>> # Scramble the stabilizers then check the canonical form is unchanged.
        >>> s.set_inverse_tableau(s.current_inverse_tableau()**-1)
        >>> s.cnot(0, 1)
        >>> s.cz(0, 2)
        >>> s.s(0, 2)
        >>> s.cy(2, 1)
        >>> s.set_inverse_tableau(s.current_inverse_tableau()**-1)
        >>> for e in s.canonical_stabilizers():
        ...     print(repr(e))
        lestim.PauliString("+XX_")
        lestim.PauliString("+ZZ_")
        lestim.PauliString("-__Z")
    """
```

<a name="lestim.TableauSimulator.cnot"></a>
```python
# lestim.TableauSimulator.cnot

# (in class lestim.TableauSimulator)
def cnot(
    self,
    *targets,
) -> None:
    """Applies a controlled X gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
            Applies the gate to the first two targets, then the next two targets,
            and so forth. There must be an even number of targets.
    """
```

<a name="lestim.TableauSimulator.copy"></a>
```python
# lestim.TableauSimulator.copy

# (in class lestim.TableauSimulator)
def copy(
    self,
    *,
    copy_rng: bool = False,
    seed: Optional[int] = None,
) -> stim.TableauSimulator:
    """Returns a simulator with the same internal state, except perhaps its prng.

    Args:
        copy_rng: By default, new simulator's prng is reinitialized with a random
            seed. However, one can set this argument to True in order to have the
            prng state copied together with the rest of the original simulator's
            state. Consequently, in this case the two simulators will produce the
            same measurement outcomes for the same quantum circuits.  If both seed
            and copy_rng are set, an exception is raised. Defaults to False.
        seed: PARTIALLY determines simulation results by deterministically seeding
            the random number generator.

            Must be None or an integer in range(2**64).

            Defaults to None. When None, the prng state is either copied from the
            original simulator or reseeded from system entropy, depending on the
            copy_rng argument.

            When set to an integer, making the exact same series calls on the exact
            same machine with the exact same version of Stim will produce the exact
            same simulation results.

            CAUTION: simulation results *WILL NOT* be consistent between versions of
            Stim. This restriction is present to make it possible to have future
            optimizations to the random sampling, and is enforced by introducing
            intentional differences in the seeding strategy from version to version.

            CAUTION: simulation results *MAY NOT* be consistent across machines that
            differ in the width of supported SIMD instructions. For example, using
            the same seed on a machine that supports AVX instructions and one that
            only supports SSE instructions may produce different simulation results.

            CAUTION: simulation results *MAY NOT* be consistent if you vary how the
            circuit is executed. For example, reordering whether a reset on one
            qubit happens before or after a reset on another qubit can result in
            different measurement results being observed starting from the same
            seed.

    Examples:
        >>> import lestim

        >>> s1 = lestim.TableauSimulator()
        >>> s1.set_inverse_tableau(lestim.Tableau.random(1))
        >>> s2 = s1.copy()
        >>> s2 is s1
        False
        >>> s2.current_inverse_tableau() == s1.current_inverse_tableau()
        True

        >>> s1 = lestim.TableauSimulator()
        >>> s2 = s1.copy(copy_rng=True)
        >>> s1.h(0)
        >>> s2.h(0)
        >>> assert s1.measure(0) == s2.measure(0)

        >>> s = lestim.TableauSimulator()
        >>> def brute_force_post_select(qubit, desired_result):
        ...     global s
        ...     while True:
        ...         s2 = s.copy()
        ...         if s2.measure(qubit) == desired_result:
        ...             s = s2
        ...             break
        >>> s.h(0)
        >>> brute_force_post_select(qubit=0, desired_result=True)
        >>> s.measure(0)
        True
    """
```

<a name="lestim.TableauSimulator.current_inverse_tableau"></a>
```python
# lestim.TableauSimulator.current_inverse_tableau

# (in class lestim.TableauSimulator)
def current_inverse_tableau(
    self,
) -> lestim._stim_polyfill.Tableau:
    """Returns a copy of the internal state of the simulator as a lestim.Tableau.

    Returns:
        A lestim.Tableau copy of the simulator's state.

    Examples:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.h(0)
        >>> s.current_inverse_tableau()
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+Z"),
            ],
            zs=[
                lestim.PauliString("+X"),
            ],
        )
        >>> s.cnot(0, 1)
        >>> s.current_inverse_tableau()
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+ZX"),
                lestim.PauliString("+_X"),
            ],
            zs=[
                lestim.PauliString("+X_"),
                lestim.PauliString("+XZ"),
            ],
        )
    """
```

<a name="lestim.TableauSimulator.current_measurement_record"></a>
```python
# lestim.TableauSimulator.current_measurement_record

# (in class lestim.TableauSimulator)
def current_measurement_record(
    self,
) -> List[bool]:
    """Returns a copy of the record of all measurements performed by the simulator.

    Examples:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.current_measurement_record()
        []
        >>> s.measure(0)
        False
        >>> s.x(0)
        >>> s.measure(0)
        True
        >>> s.current_measurement_record()
        [False, True]
        >>> s.do(lestim.Circuit("M 0"))
        >>> s.current_measurement_record()
        [False, True, True]

    Returns:
        A list of booleans containing the result of every measurement performed by
        the simulator so far.
    """
```

<a name="lestim.TableauSimulator.cx"></a>
```python
# lestim.TableauSimulator.cx

# (in class lestim.TableauSimulator)
def cx(
    self,
    *targets,
) -> None:
    """Applies a controlled X gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
            Applies the gate to the first two targets, then the next two targets,
            and so forth. There must be an even number of targets.
    """
```

<a name="lestim.TableauSimulator.cy"></a>
```python
# lestim.TableauSimulator.cy

# (in class lestim.TableauSimulator)
def cy(
    self,
    *targets,
) -> None:
    """Applies a controlled Y gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
            Applies the gate to the first two targets, then the next two targets,
            and so forth. There must be an even number of targets.
    """
```

<a name="lestim.TableauSimulator.cz"></a>
```python
# lestim.TableauSimulator.cz

# (in class lestim.TableauSimulator)
def cz(
    self,
    *targets,
) -> None:
    """Applies a controlled Z gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
            Applies the gate to the first two targets, then the next two targets,
            and so forth. There must be an even number of targets.
    """
```

<a name="lestim.TableauSimulator.depolarize1"></a>
```python
# lestim.TableauSimulator.depolarize1

# (in class lestim.TableauSimulator)
def depolarize1(
    self,
    *targets: int,
    p: float,
):
    """Probabilistically applies single-qubit depolarization to targets.

    Args:
        *targets: The indices of the qubits to target with the noise.
        p: The chance of the error being applied,
            independently, to each qubit.
    """
```

<a name="lestim.TableauSimulator.depolarize2"></a>
```python
# lestim.TableauSimulator.depolarize2

# (in class lestim.TableauSimulator)
def depolarize2(
    self,
    *targets: int,
    p: float,
):
    """Probabilistically applies two-qubit depolarization to targets.

    Args:
        *targets: The indices of the qubits to target with the noise.
            The pairs of qubits are formed by
            zip(targets[::1], targets[1::2]).
        p: The chance of the error being applied,
            independently, to each qubit pair.
    """
```

<a name="lestim.TableauSimulator.do"></a>
```python
# lestim.TableauSimulator.do

# (in class lestim.TableauSimulator)
def do(
    self,
    circuit_or_pauli_string: Union[stim.Circuit, stim.PauliString, stim.CircuitInstruction, stim.CircuitRepeatBlock],
) -> None:
    """Applies a circuit or pauli string to the simulator's state.

    Args:
        circuit_or_pauli_string: A lestim.Circuit, lestim.PauliString,
            lestim.CircuitInstruction, or lestim.CircuitRepeatBlock
            with operations to apply to the simulator's state.

    Examples:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.do(lestim.Circuit('''
        ...     X 0
        ...     M 0
        ... '''))
        >>> s.current_measurement_record()
        [True]

        >>> s = lestim.TableauSimulator()
        >>> s.do(lestim.PauliString("IXYZ"))
        >>> s.measure_many(0, 1, 2, 3)
        [False, True, True, False]
    """
```

<a name="lestim.TableauSimulator.do_circuit"></a>
```python
# lestim.TableauSimulator.do_circuit

# (in class lestim.TableauSimulator)
def do_circuit(
    self,
    circuit: lestim._stim_polyfill.Circuit,
) -> None:
    """Applies a circuit to the simulator's state.

    Args:
        circuit: A lestim.Circuit containing operations to apply.

    Examples:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.do_circuit(lestim.Circuit('''
        ...     X 0
        ...     M 0
        ... '''))
        >>> s.current_measurement_record()
        [True]
    """
```

<a name="lestim.TableauSimulator.do_pauli_string"></a>
```python
# lestim.TableauSimulator.do_pauli_string

# (in class lestim.TableauSimulator)
def do_pauli_string(
    self,
    pauli_string: lestim._stim_polyfill.PauliString,
) -> None:
    """Applies the paulis from a pauli string to the simulator's state.

    Args:
        pauli_string: A lestim.PauliString containing Paulis to apply.

    Examples:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.do_pauli_string(lestim.PauliString("IXYZ"))
        >>> s.measure_many(0, 1, 2, 3)
        [False, True, True, False]
    """
```

<a name="lestim.TableauSimulator.do_tableau"></a>
```python
# lestim.TableauSimulator.do_tableau

# (in class lestim.TableauSimulator)
def do_tableau(
    self,
    tableau: lestim._stim_polyfill.Tableau,
    targets: List[int],
) -> None:
    """Applies a custom tableau operation to qubits in the simulator.

    Note that this method has to compute the inverse of the tableau, because the
    simulator's internal state is an inverse tableau.

    Args:
        tableau: A lestim.Tableau representing the Clifford operation to apply.
        targets: The indices of the qubits to operate on.

    Examples:
        >>> import lestim
        >>> sim = lestim.TableauSimulator()
        >>> sim.h(1)
        >>> sim.h_yz(2)
        >>> [str(sim.peek_bloch(k)) for k in range(4)]
        ['+Z', '+X', '+Y', '+Z']
        >>> rot3 = lestim.Tableau.from_conjugated_generators(
        ...     xs=[
        ...         lestim.PauliString("_X_"),
        ...         lestim.PauliString("__X"),
        ...         lestim.PauliString("X__"),
        ...     ],
        ...     zs=[
        ...         lestim.PauliString("_Z_"),
        ...         lestim.PauliString("__Z"),
        ...         lestim.PauliString("Z__"),
        ...     ],
        ... )

        >>> sim.do_tableau(rot3, [1, 2, 3])
        >>> [str(sim.peek_bloch(k)) for k in range(4)]
        ['+Z', '+Z', '+X', '+Y']

        >>> sim.do_tableau(rot3, [1, 2, 3])
        >>> [str(sim.peek_bloch(k)) for k in range(4)]
        ['+Z', '+Y', '+Z', '+X']
    """
```

<a name="lestim.TableauSimulator.h"></a>
```python
# lestim.TableauSimulator.h

# (in class lestim.TableauSimulator)
def h(
    self,
    *targets,
) -> None:
    """Applies a Hadamard gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
    """
```

<a name="lestim.TableauSimulator.h_xy"></a>
```python
# lestim.TableauSimulator.h_xy

# (in class lestim.TableauSimulator)
def h_xy(
    self,
    *targets,
) -> None:
    """Applies an operation that swaps the X and Y axes to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
    """
```

<a name="lestim.TableauSimulator.h_xz"></a>
```python
# lestim.TableauSimulator.h_xz

# (in class lestim.TableauSimulator)
def h_xz(
    self,
    *targets,
) -> None:
    """Applies a Hadamard gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
    """
```

<a name="lestim.TableauSimulator.h_yz"></a>
```python
# lestim.TableauSimulator.h_yz

# (in class lestim.TableauSimulator)
def h_yz(
    self,
    *targets,
) -> None:
    """Applies an operation that swaps the Y and Z axes to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
    """
```

<a name="lestim.TableauSimulator.iswap"></a>
```python
# lestim.TableauSimulator.iswap

# (in class lestim.TableauSimulator)
def iswap(
    self,
    *targets,
) -> None:
    """Applies an ISWAP gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
            Applies the gate to the first two targets, then the next two targets,
            and so forth. There must be an even number of targets.
    """
```

<a name="lestim.TableauSimulator.iswap_dag"></a>
```python
# lestim.TableauSimulator.iswap_dag

# (in class lestim.TableauSimulator)
def iswap_dag(
    self,
    *targets,
) -> None:
    """Applies an ISWAP_DAG gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
            Applies the gate to the first two targets, then the next two targets,
            and so forth. There must be an even number of targets.
    """
```

<a name="lestim.TableauSimulator.measure"></a>
```python
# lestim.TableauSimulator.measure

# (in class lestim.TableauSimulator)
def measure(
    self,
    target: int,
) -> bool:
    """Measures a single qubit.

    Unlike the other methods on TableauSimulator, this one does not broadcast
    over multiple targets. This is to avoid returning a list, which would
    create a pitfall where typing `if sim.measure(qubit)` would be a bug.

    To measure multiple qubits, use `TableauSimulator.measure_many`.

    Args:
        target: The index of the qubit to measure.

    Returns:
        The measurement result as a bool.
    """
```

<a name="lestim.TableauSimulator.measure_kickback"></a>
```python
# lestim.TableauSimulator.measure_kickback

# (in class lestim.TableauSimulator)
def measure_kickback(
    self,
    target: int,
) -> tuple:
    """Measures a qubit and returns the result as well as its Pauli kickback (if any).

    The "Pauli kickback" of a stabilizer circuit measurement is a set of Pauli
    operations that flip the post-measurement system state between the two possible
    post-measurement states. For example, consider measuring one of the qubits in
    the state |00>+|11> in the Z basis. If the measurement result is False, then the
    system projects into the state |00>. If the measurement result is True, then the
    system projects into the state |11>. Applying a Pauli X operation to both qubits
    flips between |00> and |11>. Therefore the Pauli kickback of the measurement is
    `lestim.PauliString("XX")`. Note that there are often many possible equivalent
    Pauli kickbacks. For example, if in the previous example there was a third qubit
    in the |0> state, then both `lestim.PauliString("XX_")` and
    `lestim.PauliString("XXZ")` are valid kickbacks.

    Measurements with deterministic results don't have a Pauli kickback.

    Args:
        target: The index of the qubit to measure.

    Returns:
        A (result, kickback) tuple.
        The result is a bool containing the measurement's output.
        The kickback is either None (meaning the measurement was deterministic) or a
        lestim.PauliString (meaning the measurement was random, and the operations in
        the Pauli string flip between the two possible post-measurement states).

    Examples:
        >>> import lestim
        >>> s = lestim.TableauSimulator()

        >>> s.measure_kickback(0)
        (False, None)

        >>> s.h(0)
        >>> s.measure_kickback(0)[1]
        lestim.PauliString("+X")

        >>> def pseudo_post_select(qubit, desired_result):
        ...     m, kick = s.measure_kickback(qubit)
        ...     if m != desired_result:
        ...         if kick is None:
        ...             raise ValueError("Post-selected the impossible!")
        ...         s.do(kick)
        >>> s = lestim.TableauSimulator()
        >>> s.h(0)
        >>> s.cnot(0, 1)
        >>> s.cnot(0, 2)
        >>> pseudo_post_select(qubit=2, desired_result=True)
        >>> s.measure_many(0, 1, 2)
        [True, True, True]
    """
```

<a name="lestim.TableauSimulator.measure_many"></a>
```python
# lestim.TableauSimulator.measure_many

# (in class lestim.TableauSimulator)
def measure_many(
    self,
    *targets,
) -> List[bool]:
    """Measures multiple qubits.

    Args:
        *targets: The indices of the qubits to measure.

    Returns:
        The measurement results as a list of bools.
    """
```

<a name="lestim.TableauSimulator.measure_observable"></a>
```python
# lestim.TableauSimulator.measure_observable

# (in class lestim.TableauSimulator)
def measure_observable(
    self,
    observable: lestim._stim_polyfill.PauliString,
    *,
    flip_probability: float = 0.0,
) -> bool:
    """Measures an pauli string observable, as if by an MPP instruction.

    Args:
        observable: The observable to measure, specified as a lestim.PauliString.
        flip_probability: Probability of the recorded measurement result being
            flipped.

    Returns:
        The result of the measurement.

        The result is also recorded into the measurement record.

    Raises:
        ValueError: The given pauli string isn't Hermitian, or the given probability
            isn't a valid probability.

    Examples:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.h(0)
        >>> s.cnot(0, 1)

        >>> s.measure_observable(lestim.PauliString("XX"))
        False

        >>> s.measure_observable(lestim.PauliString("YY"))
        True

        >>> s.measure_observable(lestim.PauliString("-ZZ"))
        True
    """
```

<a name="lestim.TableauSimulator.num_qubits"></a>
```python
# lestim.TableauSimulator.num_qubits

# (in class lestim.TableauSimulator)
@property
def num_qubits(
    self,
) -> int:
    """Returns the number of qubits currently being tracked by the simulator.

    Note that the number of qubits being tracked will implicitly increase if qubits
    beyond the current limit are touched. Untracked qubits are always assumed to be
    in the |0> state.

    Examples:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.num_qubits
        0
        >>> s.h(2)
        >>> s.num_qubits
        3
    """
```

<a name="lestim.TableauSimulator.peek_bloch"></a>
```python
# lestim.TableauSimulator.peek_bloch

# (in class lestim.TableauSimulator)
def peek_bloch(
    self,
    target: int,
) -> lestim._stim_polyfill.PauliString:
    """Returns the state of the qubit as a single-qubit lestim.PauliString stabilizer.

    This is a non-physical operation. It reports information about the qubit without
    disturbing it.

    Args:
        target: The qubit to peek at.

    Returns:
        lestim.PauliString("I"):
            The qubit is entangled. Its bloch vector is x=y=z=0.
        lestim.PauliString("+Z"):
            The qubit is in the |0> state. Its bloch vector is z=+1, x=y=0.
        lestim.PauliString("-Z"):
            The qubit is in the |1> state. Its bloch vector is z=-1, x=y=0.
        lestim.PauliString("+Y"):
            The qubit is in the |i> state. Its bloch vector is y=+1, x=z=0.
        lestim.PauliString("-Y"):
            The qubit is in the |-i> state. Its bloch vector is y=-1, x=z=0.
        lestim.PauliString("+X"):
            The qubit is in the |+> state. Its bloch vector is x=+1, y=z=0.
        lestim.PauliString("-X"):
            The qubit is in the |-> state. Its bloch vector is x=-1, y=z=0.

    Examples:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.peek_bloch(0)
        lestim.PauliString("+Z")
        >>> s.x(0)
        >>> s.peek_bloch(0)
        lestim.PauliString("-Z")
        >>> s.h(0)
        >>> s.peek_bloch(0)
        lestim.PauliString("-X")
        >>> s.sqrt_x(1)
        >>> s.peek_bloch(1)
        lestim.PauliString("-Y")
        >>> s.cz(0, 1)
        >>> s.peek_bloch(0)
        lestim.PauliString("+_")
    """
```

<a name="lestim.TableauSimulator.peek_observable_expectation"></a>
```python
# lestim.TableauSimulator.peek_observable_expectation

# (in class lestim.TableauSimulator)
def peek_observable_expectation(
    self,
    observable: lestim._stim_polyfill.PauliString,
) -> int:
    """Determines the expected value of an observable.

    Because the simulator's state is always a stabilizer state, the expectation will
    always be exactly -1, 0, or +1.

    This is a non-physical operation.
    It reports information about the quantum state without disturbing it.

    Args:
        observable: The observable to determine the expected value of.
            This observable must have a real sign, not an imaginary sign.

    Returns:
        +1: Observable will be deterministically false when measured.
        -1: Observable will be deterministically true when measured.
        0: Observable will be random when measured.

    Examples:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.peek_observable_expectation(lestim.PauliString("+Z"))
        1
        >>> s.peek_observable_expectation(lestim.PauliString("+X"))
        0
        >>> s.peek_observable_expectation(lestim.PauliString("-Z"))
        -1

        >>> s.do(lestim.Circuit('''
        ...     H 0
        ...     CNOT 0 1
        ... '''))
        >>> queries = ['XX', 'YY', 'ZZ', '-ZZ', 'ZI', 'II', 'IIZ']
        >>> for q in queries:
        ...     print(q, s.peek_observable_expectation(lestim.PauliString(q)))
        XX 1
        YY -1
        ZZ 1
        -ZZ -1
        ZI 0
        II 1
        IIZ 1
    """
```

<a name="lestim.TableauSimulator.peek_x"></a>
```python
# lestim.TableauSimulator.peek_x

# (in class lestim.TableauSimulator)
def peek_x(
    self,
    target: int,
) -> int:
    """Returns the expected value of a qubit's X observable.

    Because the simulator's state is always a stabilizer state, the expectation will
    always be exactly -1, 0, or +1.

    This is a non-physical operation.
    It reports information about the quantum state without disturbing it.

    Args:
        target: The qubit to analyze.

    Returns:
        +1: Qubit is in the |+> state.
        -1: Qubit is in the |-> state.
        0: Qubit is in some other state.

    Example:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.reset_z(0)
        >>> s.peek_x(0)
        0
        >>> s.reset_x(0)
        >>> s.peek_x(0)
        1
        >>> s.z(0)
        >>> s.peek_x(0)
        -1
    """
```

<a name="lestim.TableauSimulator.peek_y"></a>
```python
# lestim.TableauSimulator.peek_y

# (in class lestim.TableauSimulator)
def peek_y(
    self,
    target: int,
) -> int:
    """Returns the expected value of a qubit's Y observable.

    Because the simulator's state is always a stabilizer state, the expectation will
    always be exactly -1, 0, or +1.

    This is a non-physical operation.
    It reports information about the quantum state without disturbing it.

    Args:
        target: The qubit to analyze.

    Returns:
        +1: Qubit is in the |i> state.
        -1: Qubit is in the |-i> state.
        0: Qubit is in some other state.

    Example:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.reset_z(0)
        >>> s.peek_y(0)
        0
        >>> s.reset_y(0)
        >>> s.peek_y(0)
        1
        >>> s.z(0)
        >>> s.peek_y(0)
        -1
    """
```

<a name="lestim.TableauSimulator.peek_z"></a>
```python
# lestim.TableauSimulator.peek_z

# (in class lestim.TableauSimulator)
def peek_z(
    self,
    target: int,
) -> int:
    """Returns the expected value of a qubit's Z observable.

    Because the simulator's state is always a stabilizer state, the expectation will
    always be exactly -1, 0, or +1.

    This is a non-physical operation.
    It reports information about the quantum state without disturbing it.

    Args:
        target: The qubit to analyze.

    Returns:
        +1: Qubit is in the |0> state.
        -1: Qubit is in the |1> state.
        0: Qubit is in some other state.

    Example:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.reset_x(0)
        >>> s.peek_z(0)
        0
        >>> s.reset_z(0)
        >>> s.peek_z(0)
        1
        >>> s.x(0)
        >>> s.peek_z(0)
        -1
    """
```

<a name="lestim.TableauSimulator.postselect_observable"></a>
```python
# lestim.TableauSimulator.postselect_observable

# (in class lestim.TableauSimulator)
def postselect_observable(
    self,
    observable: lestim._stim_polyfill.PauliString,
    *,
    desired_value: bool = False,
) -> None:
    """Projects into a desired observable, or raises an exception if it was impossible.

    Postselecting an observable forces it to collapse to a specific eigenstate,
    as if it was measured and that state was the result of the measurement.

    Args:
        observable: The observable to postselect, specified as a pauli string.
            The pauli string's sign must be -1 or +1 (not -i or +i).
        desired_value:
            False (default): Postselect into the +1 eigenstate of the observable.
            True: Postselect into the -1 eigenstate of the observable.

    Raises:
        ValueError:
            The given observable had an imaginary sign.
            OR
            The postselection was impossible. The observable was in the opposite
            eigenstate, so measuring it would never ever return the desired result.

    Examples:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.postselect_observable(lestim.PauliString("+XX"))
        >>> s.postselect_observable(lestim.PauliString("+ZZ"))
        >>> s.peek_observable_expectation(lestim.PauliString("+YY"))
        -1
    """
```

<a name="lestim.TableauSimulator.postselect_x"></a>
```python
# lestim.TableauSimulator.postselect_x

# (in class lestim.TableauSimulator)
def postselect_x(
    self,
    targets: Union[int, Iterable[int]],
    *,
    desired_value: bool,
) -> None:
    """Postselects qubits in the X basis, or raises an exception.

    Postselecting a qubit forces it to collapse to a specific state, as
    if it was measured and that state was the result of the measurement.

    Args:
        targets: The qubit index or indices to postselect.
        desired_value:
            False: postselect targets into the |+> state.
            True: postselect targets into the |-> state.

    Raises:
        ValueError:
            The postselection failed. One of the qubits was in a state
            orthogonal to the desired state, so it was literally
            impossible for a measurement of the qubit to return the
            desired result.

    Examples:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.peek_x(0)
        0
        >>> s.postselect_x(0, desired_value=False)
        >>> s.peek_x(0)
        1
        >>> s.h(0)
        >>> s.peek_x(0)
        0
        >>> s.postselect_x(0, desired_value=True)
        >>> s.peek_x(0)
        -1
    """
```

<a name="lestim.TableauSimulator.postselect_y"></a>
```python
# lestim.TableauSimulator.postselect_y

# (in class lestim.TableauSimulator)
def postselect_y(
    self,
    targets: Union[int, Iterable[int]],
    *,
    desired_value: bool,
) -> None:
    """Postselects qubits in the Y basis, or raises an exception.

    Postselecting a qubit forces it to collapse to a specific state, as
    if it was measured and that state was the result of the measurement.

    Args:
        targets: The qubit index or indices to postselect.
        desired_value:
            False: postselect targets into the |i> state.
            True: postselect targets into the |-i> state.

    Raises:
        ValueError:
            The postselection failed. One of the qubits was in a state
            orthogonal to the desired state, so it was literally
            impossible for a measurement of the qubit to return the
            desired result.

    Examples:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.peek_y(0)
        0
        >>> s.postselect_y(0, desired_value=False)
        >>> s.peek_y(0)
        1
        >>> s.reset_x(0)
        >>> s.peek_y(0)
        0
        >>> s.postselect_y(0, desired_value=True)
        >>> s.peek_y(0)
        -1
    """
```

<a name="lestim.TableauSimulator.postselect_z"></a>
```python
# lestim.TableauSimulator.postselect_z

# (in class lestim.TableauSimulator)
def postselect_z(
    self,
    targets: Union[int, Iterable[int]],
    *,
    desired_value: bool,
) -> None:
    """Postselects qubits in the Z basis, or raises an exception.

    Postselecting a qubit forces it to collapse to a specific state, as if it was
    measured and that state was the result of the measurement.

    Args:
        targets: The qubit index or indices to postselect.
        desired_value:
            False: postselect targets into the |0> state.
            True: postselect targets into the |1> state.

    Raises:
        ValueError:
            The postselection failed. One of the qubits was in a state
            orthogonal to the desired state, so it was literally
            impossible for a measurement of the qubit to return the
            desired result.

    Examples:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.h(0)
        >>> s.peek_z(0)
        0
        >>> s.postselect_z(0, desired_value=False)
        >>> s.peek_z(0)
        1
        >>> s.h(0)
        >>> s.peek_z(0)
        0
        >>> s.postselect_z(0, desired_value=True)
        >>> s.peek_z(0)
        -1
    """
```

<a name="lestim.TableauSimulator.reset"></a>
```python
# lestim.TableauSimulator.reset

# (in class lestim.TableauSimulator)
def reset(
    self,
    *targets,
) -> None:
    """Resets qubits to the |0> state.

    Args:
        *targets: The indices of the qubits to reset.

    Example:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.x(0)
        >>> s.reset(0)
        >>> s.peek_bloch(0)
        lestim.PauliString("+Z")
    """
```

<a name="lestim.TableauSimulator.reset_x"></a>
```python
# lestim.TableauSimulator.reset_x

# (in class lestim.TableauSimulator)
def reset_x(
    self,
    *targets,
) -> None:
    """Resets qubits to the |+> state.

    Args:
        *targets: The indices of the qubits to reset.

    Example:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.reset_x(0)
        >>> s.peek_bloch(0)
        lestim.PauliString("+X")
    """
```

<a name="lestim.TableauSimulator.reset_y"></a>
```python
# lestim.TableauSimulator.reset_y

# (in class lestim.TableauSimulator)
def reset_y(
    self,
    *targets,
) -> None:
    """Resets qubits to the |i> state.

    Args:
        *targets: The indices of the qubits to reset.

    Example:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.reset_y(0)
        >>> s.peek_bloch(0)
        lestim.PauliString("+Y")
    """
```

<a name="lestim.TableauSimulator.reset_z"></a>
```python
# lestim.TableauSimulator.reset_z

# (in class lestim.TableauSimulator)
def reset_z(
    self,
    *targets,
) -> None:
    """Resets qubits to the |0> state.

    Args:
        *targets: The indices of the qubits to reset.

    Example:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> s.h(0)
        >>> s.reset_z(0)
        >>> s.peek_bloch(0)
        lestim.PauliString("+Z")
    """
```

<a name="lestim.TableauSimulator.s"></a>
```python
# lestim.TableauSimulator.s

# (in class lestim.TableauSimulator)
def s(
    self,
    *targets,
) -> None:
    """Applies a SQRT_Z gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
    """
```

<a name="lestim.TableauSimulator.s_dag"></a>
```python
# lestim.TableauSimulator.s_dag

# (in class lestim.TableauSimulator)
def s_dag(
    self,
    *targets,
) -> None:
    """Applies a SQRT_Z_DAG gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
    """
```

<a name="lestim.TableauSimulator.set_inverse_tableau"></a>
```python
# lestim.TableauSimulator.set_inverse_tableau

# (in class lestim.TableauSimulator)
def set_inverse_tableau(
    self,
    new_inverse_tableau: lestim._stim_polyfill.Tableau,
) -> None:
    """Overwrites the simulator's internal state with the given inverse tableau.

    The inverse tableau specifies how Pauli product observables of qubits at the
    current time transform into equivalent Pauli product observables at the
    beginning of time, when all qubits were in the |0> state. For example, if the Z
    observable on qubit 5 maps to a product of Z observables at the start of time
    then a Z basis measurement on qubit 5 will be deterministic and equal to the
    sign of the product. Whereas if it mapped to a product of observables including
    an X or a Y then the Z basis measurement would be random.

    Any qubits not within the length of the tableau are implicitly in the |0> state.

    Args:
        new_inverse_tableau: The tableau to overwrite the internal state with.

    Examples:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> t = lestim.Tableau.random(4)
        >>> s.set_inverse_tableau(t)
        >>> s.current_inverse_tableau() == t
        True
    """
```

<a name="lestim.TableauSimulator.set_num_qubits"></a>
```python
# lestim.TableauSimulator.set_num_qubits

# (in class lestim.TableauSimulator)
def set_num_qubits(
    self,
    new_num_qubits: int,
) -> None:
    """Resizes the simulator's internal state.

    This forces the simulator's internal state to track exactly the qubits whose
    indices are in `range(new_num_qubits)`.

    Note that untracked qubits are always assumed to be in the |0> state. Therefore,
    calling this method will effectively force any qubit whose index is outside
    `range(new_num_qubits)` to be reset to |0>.

    Note that this method does not prevent future operations from implicitly
    expanding the size of the tracked state (e.g. setting the number of qubits to 5
    will not prevent a Hadamard from then being applied to qubit 100, increasing the
    number of qubits back to 101).

    Args:
        new_num_qubits: The length of the range of qubits the internal simulator
            should be tracking.

    Examples:
        >>> import lestim
        >>> s = lestim.TableauSimulator()
        >>> len(s.current_inverse_tableau())
        0

        >>> s.set_num_qubits(5)
        >>> len(s.current_inverse_tableau())
        5

        >>> s.x(0, 1, 2, 3)
        >>> s.set_num_qubits(2)
        >>> s.measure_many(0, 1, 2, 3)
        [True, True, False, False]
    """
```

<a name="lestim.TableauSimulator.set_state_from_stabilizers"></a>
```python
# lestim.TableauSimulator.set_state_from_stabilizers

# (in class lestim.TableauSimulator)
def set_state_from_stabilizers(
    self,
    stabilizers: Iterable[stim.PauliString],
    *,
    allow_redundant: bool = False,
    allow_underconstrained: bool = False,
) -> None:
    """Sets the tableau simulator's state to a state satisfying the given stabilizers.

    The old quantum state is completely overwritten, even if the new state is
    underconstrained by the given stabilizers. The number of qubits is changed to
    exactly match the number of qubits in the longest given stabilizer.

    Args:
        stabilizers: A list of `lestim.PauliString`s specifying the stabilizers that
            the new state must have. It is permitted for stabilizers to have
            different lengths. All stabilizers are padded up to the length of the
            longest stabilizer by appending identity terms.
        allow_redundant: Defaults to False. If set to False, then the given
            stabilizers must all be independent. If any one of them is a product of
            the others (including the empty product), an exception will be raised.
            If set to True, then redundant stabilizers are simply ignored.
        allow_underconstrained: Defaults to False. If set to False, then the given
            stabilizers must form a complete set of generators. They must exactly
            specify the desired stabilizer state, with no degrees of freedom left
            over. For an n-qubit state there must be n independent stabilizers. If
            set to True, then there can be leftover degrees of freedom which can be
            set arbitrarily.

    Returns:
        Nothing. Mutates the states of the simulator to match the desired
        stabilizers.

        Guarantees that self.current_inverse_tableau().inverse_z_output(k) will be
        equal to the k'th independent stabilizer from the `stabilizers` argument.

    Raises:
        ValueError:
            A stabilizer is redundant but allow_redundant=True wasn't set.
            OR
            The given stabilizers are contradictory (e.g. "+Z" and "-Z" both
            specified).
            OR
            The given stabilizers anticommute (e.g. "+Z" and "+X" both specified).
            OR
            The stabilizers left behind a degree of freedom but
            allow_underconstrained=True wasn't set.
            OR
            A stabilizer has an imaginary sign (i or -i).

    Examples:

        >>> import lestim
        >>> tab_sim = lestim.TableauSimulator()
        >>> tab_sim.set_state_from_stabilizers([
        ...     lestim.PauliString("XX"),
        ...     lestim.PauliString("ZZ"),
        ... ])
        >>> tab_sim.current_inverse_tableau().inverse()
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+Z_"),
                lestim.PauliString("+_X"),
            ],
            zs=[
                lestim.PauliString("+XX"),
                lestim.PauliString("+ZZ"),
            ],
        )

        >>> tab_sim.set_state_from_stabilizers([
        ...     lestim.PauliString("XX_"),
        ...     lestim.PauliString("ZZ_"),
        ...     lestim.PauliString("-YY_"),
        ...     lestim.PauliString(""),
        ... ], allow_underconstrained=True, allow_redundant=True)
        >>> tab_sim.current_inverse_tableau().inverse()
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+Z__"),
                lestim.PauliString("+_X_"),
                lestim.PauliString("+__X"),
            ],
            zs=[
                lestim.PauliString("+XX_"),
                lestim.PauliString("+ZZ_"),
                lestim.PauliString("+__Z"),
            ],
        )
    """
```

<a name="lestim.TableauSimulator.set_state_from_state_vector"></a>
```python
# lestim.TableauSimulator.set_state_from_state_vector

# (in class lestim.TableauSimulator)
def set_state_from_state_vector(
    self,
    state_vector: Iterable[float],
    *,
    endian: str,
) -> None:
    """Sets the simulator's state to a superposition specified by an amplitude vector.

    Args:
        state_vector: A list of complex amplitudes specifying a superposition. The
            vector must correspond to a state that is reachable using Clifford
            operations, and must be normalized (i.e. it must be a unit vector).
        endian:
            "little": state vector is in little endian order, where higher index
                qubits correspond to larger changes in the state index.
            "big": state vector is in big endian order, where higher index qubits
                correspond to smaller changes in the state index.

    Returns:
        Nothing. Mutates the states of the simulator to match the desired state.

    Raises:
        ValueError:
            The given state vector isn't a list of complex values specifying a
            stabilizer state.
            OR
            The given endian value isn't 'little' or 'big'.

    Examples:

        >>> import lestim
        >>> tab_sim = lestim.TableauSimulator()
        >>> tab_sim.set_state_from_state_vector([
        ...     0.5**0.5,
        ...     0.5**0.5 * 1j,
        ... ], endian='little')
        >>> tab_sim.current_inverse_tableau().inverse()
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+Z"),
            ],
            zs=[
                lestim.PauliString("+Y"),
            ],
        )
        >>> tab_sim.set_state_from_state_vector([
        ...     0.5**0.5,
        ...     0,
        ...     0,
        ...     0.5**0.5,
        ... ], endian='little')
        >>> tab_sim.current_inverse_tableau().inverse()
        lestim.Tableau.from_conjugated_generators(
            xs=[
                lestim.PauliString("+Z_"),
                lestim.PauliString("+_X"),
            ],
            zs=[
                lestim.PauliString("+XX"),
                lestim.PauliString("+ZZ"),
            ],
        )
    """
```

<a name="lestim.TableauSimulator.sqrt_x"></a>
```python
# lestim.TableauSimulator.sqrt_x

# (in class lestim.TableauSimulator)
def sqrt_x(
    self,
    *targets,
) -> None:
    """Applies a SQRT_X gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
    """
```

<a name="lestim.TableauSimulator.sqrt_x_dag"></a>
```python
# lestim.TableauSimulator.sqrt_x_dag

# (in class lestim.TableauSimulator)
def sqrt_x_dag(
    self,
    *targets,
) -> None:
    """Applies a SQRT_X_DAG gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
    """
```

<a name="lestim.TableauSimulator.sqrt_y"></a>
```python
# lestim.TableauSimulator.sqrt_y

# (in class lestim.TableauSimulator)
def sqrt_y(
    self,
    *targets,
) -> None:
    """Applies a SQRT_Y gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
    """
```

<a name="lestim.TableauSimulator.sqrt_y_dag"></a>
```python
# lestim.TableauSimulator.sqrt_y_dag

# (in class lestim.TableauSimulator)
def sqrt_y_dag(
    self,
    *targets,
) -> None:
    """Applies a SQRT_Y_DAG gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
    """
```

<a name="lestim.TableauSimulator.state_vector"></a>
```python
# lestim.TableauSimulator.state_vector

# (in class lestim.TableauSimulator)
def state_vector(
    self,
    *,
    endian: str = 'little',
) -> np.ndarray[np.complex64]:
    """Returns a wavefunction for the simulator's current state.

    This function takes O(n * 2**n) time and O(2**n) space, where n is the number of
    qubits. The computation is done by initialization a random state vector and
    iteratively projecting it into the +1 eigenspace of each stabilizer of the
    state. The state is then canonicalized so that zero values are actually exactly
    0, and so that the first non-zero entry is positive.

    Args:
        endian:
            "little" (default): state vector is in little endian order, where higher
                index qubits correspond to larger changes in the state index.
            "big": state vector is in big endian order, where higher index qubits
                correspond to smaller changes in the state index.

    Returns:
        A `numpy.ndarray[numpy.complex64]` of computational basis amplitudes.

        If the result is in little endian order then the amplitude at offset
        b_0 + b_1*2 + b_2*4 + ... + b_{n-1}*2^{n-1} is the amplitude for the
        computational basis state where the qubit with index 0 is storing the bit
        b_0, the qubit with index 1 is storing the bit b_1, etc.

        If the result is in big endian order then the amplitude at offset
        b_0 + b_1*2 + b_2*4 + ... + b_{n-1}*2^{n-1} is the amplitude for the
        computational basis state where the qubit with index 0 is storing the bit
        b_{n-1}, the qubit with index 1 is storing the bit b_{n-2}, etc.

    Examples:
        >>> import lestim
        >>> import numpy as np
        >>> s = lestim.TableauSimulator()
        >>> s.x(2)
        >>> list(s.state_vector(endian='little'))
        [0j, 0j, 0j, 0j, (1+0j), 0j, 0j, 0j]

        >>> list(s.state_vector(endian='big'))
        [0j, (1+0j), 0j, 0j, 0j, 0j, 0j, 0j]

        >>> s.sqrt_x(1, 2)
        >>> list(s.state_vector())
        [(0.5+0j), 0j, -0.5j, 0j, 0.5j, 0j, (0.5+0j), 0j]
    """
```

<a name="lestim.TableauSimulator.swap"></a>
```python
# lestim.TableauSimulator.swap

# (in class lestim.TableauSimulator)
def swap(
    self,
    *targets,
) -> None:
    """Applies a swap gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
            Applies the gate to the first two targets, then the next two targets,
            and so forth. There must be an even number of targets.
    """
```

<a name="lestim.TableauSimulator.x"></a>
```python
# lestim.TableauSimulator.x

# (in class lestim.TableauSimulator)
def x(
    self,
    *targets,
) -> None:
    """Applies a Pauli X gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
    """
```

<a name="lestim.TableauSimulator.x_error"></a>
```python
# lestim.TableauSimulator.x_error

# (in class lestim.TableauSimulator)
def x_error(
    self,
    *targets: int,
    p: float,
):
    """Probabilistically applies X errors to targets.

    Args:
        *targets: The indices of the qubits to target with the noise.
        p: The chance of the X error being applied,
            independently, to each qubit.
    """
```

<a name="lestim.TableauSimulator.xcx"></a>
```python
# lestim.TableauSimulator.xcx

# (in class lestim.TableauSimulator)
def xcx(
    self,
    *targets,
) -> None:
    """Applies an X-controlled X gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
            Applies the gate to the first two targets, then the next two targets,
            and so forth. There must be an even number of targets.
    """
```

<a name="lestim.TableauSimulator.xcy"></a>
```python
# lestim.TableauSimulator.xcy

# (in class lestim.TableauSimulator)
def xcy(
    self,
    *targets,
) -> None:
    """Applies an X-controlled Y gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
            Applies the gate to the first two targets, then the next two targets,
            and so forth. There must be an even number of targets.
    """
```

<a name="lestim.TableauSimulator.xcz"></a>
```python
# lestim.TableauSimulator.xcz

# (in class lestim.TableauSimulator)
def xcz(
    self,
    *targets,
) -> None:
    """Applies an X-controlled Z gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
            Applies the gate to the first two targets, then the next two targets,
            and so forth. There must be an even number of targets.
    """
```

<a name="lestim.TableauSimulator.y"></a>
```python
# lestim.TableauSimulator.y

# (in class lestim.TableauSimulator)
def y(
    self,
    *targets,
) -> None:
    """Applies a Pauli Y gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
    """
```

<a name="lestim.TableauSimulator.y_error"></a>
```python
# lestim.TableauSimulator.y_error

# (in class lestim.TableauSimulator)
def y_error(
    self,
    *targets: int,
    p: float,
):
    """Probabilistically applies Y errors to targets.

    Args:
        *targets: The indices of the qubits to target with the noise.
        p: The chance of the Y error being applied,
            independently, to each qubit.
    """
```

<a name="lestim.TableauSimulator.ycx"></a>
```python
# lestim.TableauSimulator.ycx

# (in class lestim.TableauSimulator)
def ycx(
    self,
    *targets,
) -> None:
    """Applies a Y-controlled X gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
            Applies the gate to the first two targets, then the next two targets,
            and so forth. There must be an even number of targets.
    """
```

<a name="lestim.TableauSimulator.ycy"></a>
```python
# lestim.TableauSimulator.ycy

# (in class lestim.TableauSimulator)
def ycy(
    self,
    *targets,
) -> None:
    """Applies a Y-controlled Y gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
            Applies the gate to the first two targets, then the next two targets,
            and so forth. There must be an even number of targets.
    """
```

<a name="lestim.TableauSimulator.ycz"></a>
```python
# lestim.TableauSimulator.ycz

# (in class lestim.TableauSimulator)
def ycz(
    self,
    *targets,
) -> None:
    """Applies a Y-controlled Z gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
            Applies the gate to the first two targets, then the next two targets,
            and so forth. There must be an even number of targets.
    """
```

<a name="lestim.TableauSimulator.z"></a>
```python
# lestim.TableauSimulator.z

# (in class lestim.TableauSimulator)
def z(
    self,
    *targets,
) -> None:
    """Applies a Pauli Z gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
    """
```

<a name="lestim.TableauSimulator.z_error"></a>
```python
# lestim.TableauSimulator.z_error

# (in class lestim.TableauSimulator)
def y_error(
    self,
    *targets: int,
    p: float,
):
    """Probabilistically applies Z errors to targets.

    Args:
        *targets: The indices of the qubits to target with the noise.
        p: The chance of the Z error being applied,
            independently, to each qubit.
    """
```

<a name="lestim.TableauSimulator.zcx"></a>
```python
# lestim.TableauSimulator.zcx

# (in class lestim.TableauSimulator)
def zcx(
    self,
    *targets,
) -> None:
    """Applies a controlled X gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
            Applies the gate to the first two targets, then the next two targets,
            and so forth. There must be an even number of targets.
    """
```

<a name="lestim.TableauSimulator.zcy"></a>
```python
# lestim.TableauSimulator.zcy

# (in class lestim.TableauSimulator)
def zcy(
    self,
    *targets,
) -> None:
    """Applies a controlled Y gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
            Applies the gate to the first two targets, then the next two targets,
            and so forth. There must be an even number of targets.
    """
```

<a name="lestim.TableauSimulator.zcz"></a>
```python
# lestim.TableauSimulator.zcz

# (in class lestim.TableauSimulator)
def zcz(
    self,
    *targets,
) -> None:
    """Applies a controlled Z gate to the simulator's state.

    Args:
        *targets: The indices of the qubits to target with the gate.
            Applies the gate to the first two targets, then the next two targets,
            and so forth. There must be an even number of targets.
    """
```

<a name="lestim.gate_data"></a>
```python
# lestim.gate_data

# (at top-level in the lestim module)
@overload
def gate_data(
    name: str,
) -> stim.GateData:
    pass
@overload
def gate_data(
) -> Dict[str, stim.GateData]:
    pass
def gate_data(
    name: Optional[str] = None,
) -> Union[str, Dict[str, stim.GateData]]:
    """Returns gate data for the given named gate, or all gates.

    Examples:
        >>> import lestim
        >>> lestim.gate_data('cnot').aliases
        ['CNOT', 'CX', 'ZCX']
        >>> lestim.gate_data('cnot').is_two_qubit_gate
        True
        >>> gate_dict = lestim.gate_data()
        >>> len(gate_dict) > 50
        True
        >>> gate_dict['MX'].produces_measurements
        True
    """
```

<a name="lestim.main"></a>
```python
# lestim.main

# (at top-level in the lestim module)
def main(
    *,
    command_line_args: List[str],
) -> int:
    """Runs the command line tool version of lestim on the given arguments.

    Note that by default any input will be read from stdin, any output
    will print to stdout (as opposed to being intercepted). For most
    commands, you can use arguments like `--out` to write to a file
    instead of stdout and `--in` to read from a file instead of stdin.

    Returns:
        An exit code (0 means success, not zero means failure).

    Raises:
        A large variety of errors, depending on what you are doing and
        how it failed! Beware that many errors are caught by the main
        method itself and printed to stderr, with the only indication
        that something went wrong being the return code.

    Example:
        >>> import lestim
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     path = f'{d}/tmp.out'
        ...     return_code = lestim.main(command_line_args=[
        ...         "gen",
        ...         "--code=repetition_code",
        ...         "--task=memory",
        ...         "--rounds=1000",
        ...         "--distance=2",
        ...         "--out",
        ...         path,
        ...     ])
        ...     assert return_code == 0
        ...     with open(path) as f:
        ...         print(f.read(), end='')
        # Generated repetition_code circuit.
        # task: memory
        # rounds: 1000
        # distance: 2
        # before_round_data_depolarization: 0
        # before_measure_flip_probability: 0
        # after_reset_flip_probability: 0
        # after_clifford_depolarization: 0
        # layout:
        # L0 Z1 d2
        # Legend:
        #     d# = data qubit
        #     L# = data qubit with logical observable crossing
        #     Z# = measurement qubit
        R 0 1 2
        TICK
        CX 0 1
        TICK
        CX 2 1
        TICK
        MR 1
        DETECTOR(1, 0) rec[-1]
        REPEAT 999 {
            TICK
            CX 0 1
            TICK
            CX 2 1
            TICK
            MR 1
            SHIFT_COORDS(0, 1)
            DETECTOR(1, 0) rec[-1] rec[-2]
        }
        M 0 2
        DETECTOR(1, 1) rec[-1] rec[-2] rec[-3]
        OBSERVABLE_INCLUDE(0) rec[-1]
    """
```

<a name="lestim.read_shot_data_file"></a>
```python
# lestim.read_shot_data_file

# (at top-level in the lestim module)
@overload
def read_shot_data_file(
    *,
    path: Union[str, pathlib.Path],
    format: Union[str, 'Literal["01", "b8", "r8", "ptb64", "hits", "dets"]'],
    bit_packed: bool = False,
    num_measurements: int = 0,
    num_detectors: int = 0,
    num_observables: int = 0,
) -> np.ndarray:
    pass
@overload
def read_shot_data_file(
    *,
    path: Union[str, pathlib.Path],
    format: Union[str, 'Literal["01", "b8", "r8", "ptb64", "hits", "dets"]'],
    bit_packed: bool = False,
    num_measurements: int = 0,
    num_detectors: int = 0,
    num_observables: int = 0,
    separate_observables: 'Literal[True]',
) -> Tuple[np.ndarray, np.ndarray]:
    pass
def read_shot_data_file(
    *,
    path: Union[str, pathlib.Path],
    format: Union[str, 'Literal["01", "b8", "r8", "ptb64", "hits", "dets"]'],
    bit_packed: bool = False,
    num_measurements: int = 0,
    num_detectors: int = 0,
    num_observables: int = 0,
    separate_observables: bool = False,
) -> Union[Tuple[np.ndarray, np.ndarray], np.ndarray]:
    """Reads shot data, such as measurement samples, from a file.

    Args:
        path: The path to the file to read the data from.
        format: The format that the data is stored in, such as 'b8'.
            See https://github.com/quantumlib/Stim/blob/main/doc/result_formats.md
        bit_packed: Defaults to false. Determines whether the result is a bool_
            numpy array with one bit per byte, or a uint8 numpy array with 8 bits
            per byte.
        num_measurements: How many measurements there are per shot.
        num_detectors: How many detectors there are per shot.
        num_observables: How many observables there are per shot.
            Note that this only refers to observables *stored in the file*, not to
            observables from the original circuit that was sampled.
        separate_observables: When set to True, the result is a tuple of two arrays,
            one containing the detection event data and the other containing the
            observable data, instead of a single array.

    Returns:
        If separate_observables=True:
            A tuple (dets, obs) of numpy arrays containing the loaded data.

            If bit_packed=False:
                dets.dtype = np.bool_
                dets.shape = (num_shots, num_measurements + num_detectors)
                det bit b from shot s is at dets[s, b]
                obs.dtype = np.bool_
                obs.shape = (num_shots, num_observables)
                obs bit b from shot s is at dets[s, b]
            If bit_packed=True:
                dets.dtype = np.uint8
                dets.shape = (num_shots, math.ceil(
                    (num_measurements + num_detectors) / 8))
                obs.dtype = np.uint8
                obs.shape = (num_shots, math.ceil(num_observables / 8))
                det bit b from shot s is at dets[s, b // 8] & (1 << (b % 8))
                obs bit b from shot s is at obs[s, b // 8] & (1 << (b % 8))

        If separate_observables=False:
            A numpy array containing the loaded data.

            If bit_packed=False:
                dtype = np.bool_
                shape = (num_shots,
                         num_measurements + num_detectors + num_observables)
                bit b from shot s is at result[s, b]
            If bit_packed=True:
                dtype = np.uint8
                shape = (num_shots, math.ceil(
                    (num_measurements + num_detectors + num_observables) / 8))
                bit b from shot s is at result[s, b // 8] & (1 << (b % 8))

    Examples:
        >>> import lestim
        >>> import pathlib
        >>> import tempfile
        >>> with tempfile.TemporaryDirectory() as d:
        ...     path = pathlib.Path(d) / 'shots'
        ...     with open(path, 'w') as f:
        ...         print("0000", file=f)
        ...         print("0101", file=f)
        ...
        ...     read = lestim.read_shot_data_file(
        ...         path=str(path),
        ...         format='01',
        ...         num_measurements=4)
        >>> read
        array([[False, False, False, False],
               [False,  True, False,  True]])
    """
```

<a name="lestim.target_combined_paulis"></a>
```python
# lestim.target_combined_paulis

# (at top-level in the lestim module)
def target_combined_paulis(
    paulis: Union[stim.PauliString, List[stim.GateTarget]],
    invert: bool = False,
) -> stim.GateTarget:
    """Returns a list of targets encoding a pauli product for instructions like MPP.

    Args:
        paulis: The paulis to encode into the targets. This can be a
            `lestim.PauliString` or a list of pauli targets from `lestim.target_x`,
            `lestim.target_pauli`, etc.
        invert: Defaults to False. If True, the product is inverted (like "!X2*Y3").
            Note that this is in addition to any inversions specified by the
            `paulis` argument.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit()
        >>> circuit.append("MPP", [
        ...     *lestim.target_combined_paulis(lestim.PauliString("-XYZ")),
        ...     *lestim.target_combined_paulis([lestim.target_x(2), lestim.target_y(5)]),
        ...     *lestim.target_combined_paulis([lestim.target_z(9)], invert=True),
        ... ])
        >>> circuit
        lestim.Circuit('''
            MPP !X0*Y1*Z2 X2*Y5 !Z9
        ''')
    """
```

<a name="lestim.target_combiner"></a>
```python
# lestim.target_combiner

# (at top-level in the lestim module)
def target_combiner(
) -> lestim._stim_polyfill.GateTarget:
    """Returns a target combiner that can be used to build Pauli products.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit()
        >>> circuit.append("MPP", [
        ...     lestim.target_x(2),
        ...     lestim.target_combiner(),
        ...     lestim.target_y(3),
        ...     lestim.target_combiner(),
        ...     lestim.target_z(5),
        ... ])
        >>> circuit
        lestim.Circuit('''
            MPP X2*Y3*Z5
        ''')
    """
```

<a name="lestim.target_inv"></a>
```python
# lestim.target_inv

# (at top-level in the lestim module)
def target_inv(
    qubit_index: Union[int, stim.GateTarget],
) -> stim.GateTarget:
    """Returns a target flagged as inverted.

    Inverted targets are used to indicate measurement results should be flipped.

    Args:
        qubit_index: The underlying qubit index of the inverted target.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit()
        >>> circuit.append("M", [2, lestim.target_inv(3)])
        >>> circuit
        lestim.Circuit('''
            M 2 !3
        ''')

    For example, the '!1' in 'M 0 !1 2' is qubit 1 flagged as inverted,
    meaning the measurement result from qubit 1 should be inverted when reported.
    """
```

<a name="lestim.target_logical_observable_id"></a>
```python
# lestim.target_logical_observable_id

# (at top-level in the lestim module)
def target_logical_observable_id(
    index: int,
) -> lestim._stim_polyfill.DemTarget:
    """Returns a logical observable id identifying a frame change.

    Args:
        index: The index of the observable.

    Returns:
        The logical observable target.

    Examples:
        >>> import lestim
        >>> m = lestim.DetectorErrorModel()
        >>> m.append("error", 0.25, [
        ...     lestim.target_logical_observable_id(13)
        ... ])
        >>> print(repr(m))
        lestim.DetectorErrorModel('''
            error(0.25) L13
        ''')
    """
```

<a name="lestim.target_pauli"></a>
```python
# lestim.target_pauli

# (at top-level in the lestim module)
def target_pauli(
    qubit_index: int,
    pauli: Union[str, int],
    invert: bool = False,
) -> stim.GateTarget:
    """Returns a pauli target that can be passed into `lestim.Circuit.append`.

    Args:
        qubit_index: The qubit that the Pauli applies to.
        pauli: The pauli gate to use. This can either be a string identifying the
            pauli by name ("x", "X", "y", "Y", "z", or "Z") or an integer following
            the convention (1=X, 2=Y, 3=Z). Setting this argument to "I" or to
            0 will return a qubit target instead of a pauli target.
        invert: Defaults to False. If True, the target is inverted (like "!X10"),
            indicating that, for example, measurement results should be inverted).

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit()
        >>> circuit.append("MPP", [
        ...     lestim.target_pauli(2, "X"),
        ...     lestim.target_combiner(),
        ...     lestim.target_pauli(3, "y", invert=True),
        ...     lestim.target_pauli(5, 3),
        ... ])
        >>> circuit
        lestim.Circuit('''
            MPP X2*!Y3 Z5
        ''')

        >>> circuit.append("M", [
        ...     lestim.target_pauli(7, "I"),
        ... ])
        >>> circuit
        lestim.Circuit('''
            MPP X2*!Y3 Z5
            M 7
        ''')
    """
```

<a name="lestim.target_rec"></a>
```python
# lestim.target_rec

# (at top-level in the lestim module)
def target_rec(
    lookback_index: int,
) -> lestim._stim_polyfill.GateTarget:
    """Returns a measurement record target with the given lookback.

    Measurement record targets are used to refer back to the measurement record;
    the list of measurements that have been performed so far. Measurement record
    targets always specify an index relative to the *end* of the measurement record.
    The latest measurement is `lestim.target_rec(-1)`, the next most recent
    measurement is `lestim.target_rec(-2)`, and so forth. Indexing is done this way
    in order to make it possible to write loops.

    Args:
        lookback_index: A negative integer indicating how far to look back, relative
            to the end of the measurement record.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit()
        >>> circuit.append("M", [5, 7, 11])
        >>> circuit.append("CX", [lestim.target_rec(-2), 3])
        >>> circuit
        lestim.Circuit('''
            M 5 7 11
            CX rec[-2] 3
        ''')
    """
```

<a name="lestim.target_relative_detector_id"></a>
```python
# lestim.target_relative_detector_id

# (at top-level in the lestim module)
def target_relative_detector_id(
    index: int,
) -> lestim._stim_polyfill.DemTarget:
    """Returns a relative detector id (e.g. "D5" in a .dem file).

    Args:
        index: The index of the detector, relative to the current detector offset.

    Returns:
        The relative detector target.

    Examples:
        >>> import lestim
        >>> m = lestim.DetectorErrorModel()
        >>> m.append("error", 0.25, [
        ...     lestim.target_relative_detector_id(13)
        ... ])
        >>> print(repr(m))
        lestim.DetectorErrorModel('''
            error(0.25) D13
        ''')
    """
```

<a name="lestim.target_separator"></a>
```python
# lestim.target_separator

# (at top-level in the lestim module)
def target_separator(
) -> lestim._stim_polyfill.DemTarget:
    """Returns a target separator (e.g. "^" in a .dem file).

    Examples:
        >>> import lestim
        >>> m = lestim.DetectorErrorModel()
        >>> m.append("error", 0.25, [
        ...     lestim.target_relative_detector_id(1),
        ...     lestim.target_separator(),
        ...     lestim.target_relative_detector_id(2),
        ... ])
        >>> print(repr(m))
        lestim.DetectorErrorModel('''
            error(0.25) D1 ^ D2
        ''')
    """
```

<a name="lestim.target_sweep_bit"></a>
```python
# lestim.target_sweep_bit

# (at top-level in the lestim module)
def target_sweep_bit(
    sweep_bit_index: int,
) -> lestim._stim_polyfill.GateTarget:
    """Returns a sweep bit target that can be passed into `lestim.Circuit.append`.

    Args:
        sweep_bit_index: The index of the sweep bit to target.

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit()
        >>> circuit.append("CX", [lestim.target_sweep_bit(2), 5])
        >>> circuit
        lestim.Circuit('''
            CX sweep[2] 5
        ''')
    """
```

<a name="lestim.target_x"></a>
```python
# lestim.target_x

# (at top-level in the lestim module)
def target_x(
    qubit_index: Union[int, stim.GateTarget],
    invert: bool = False,
) -> stim.GateTarget:
    """Returns a Pauli X target that can be passed into `lestim.Circuit.append`.

    Args:
        qubit_index: The qubit that the Pauli applies to.
        invert: Defaults to False. If True, the target is inverted (indicating
            that, for example, measurement results should be inverted).

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit()
        >>> circuit.append("MPP", [
        ...     lestim.target_x(2),
        ...     lestim.target_combiner(),
        ...     lestim.target_y(3, invert=True),
        ...     lestim.target_combiner(),
        ...     lestim.target_z(5),
        ... ])
        >>> circuit
        lestim.Circuit('''
            MPP X2*!Y3*Z5
        ''')
    """
```

<a name="lestim.target_y"></a>
```python
# lestim.target_y

# (at top-level in the lestim module)
def target_y(
    qubit_index: Union[int, stim.GateTarget],
    invert: bool = False,
) -> stim.GateTarget:
    """Returns a Pauli Y target that can be passed into `lestim.Circuit.append`.

    Args:
        qubit_index: The qubit that the Pauli applies to.
        invert: Defaults to False. If True, the target is inverted (indicating
            that, for example, measurement results should be inverted).

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit()
        >>> circuit.append("MPP", [
        ...     lestim.target_x(2),
        ...     lestim.target_combiner(),
        ...     lestim.target_y(3, invert=True),
        ...     lestim.target_combiner(),
        ...     lestim.target_z(5),
        ... ])
        >>> circuit
        lestim.Circuit('''
            MPP X2*!Y3*Z5
        ''')
    """
```

<a name="lestim.target_z"></a>
```python
# lestim.target_z

# (at top-level in the lestim module)
def target_z(
    qubit_index: Union[int, stim.GateTarget],
    invert: bool = False,
) -> stim.GateTarget:
    """Returns a Pauli Z target that can be passed into `lestim.Circuit.append`.

    Args:
        qubit_index: The qubit that the Pauli applies to.
        invert: Defaults to False. If True, the target is inverted (indicating
            that, for example, measurement results should be inverted).

    Examples:
        >>> import lestim
        >>> circuit = lestim.Circuit()
        >>> circuit.append("MPP", [
        ...     lestim.target_x(2),
        ...     lestim.target_combiner(),
        ...     lestim.target_y(3, invert=True),
        ...     lestim.target_combiner(),
        ...     lestim.target_z(5),
        ... ])
        >>> circuit
        lestim.Circuit('''
            MPP X2*!Y3*Z5
        ''')
    """
```

<a name="lestim.write_shot_data_file"></a>
```python
# lestim.write_shot_data_file

# (at top-level in the lestim module)
def write_shot_data_file(
    *,
    data: np.ndarray,
    path: Union[str, pathlib.Path],
    format: str,
    num_measurements: int = 0,
    num_detectors: int = 0,
    num_observables: int = 0,
) -> None:
    """Writes shot data, such as measurement samples, to a file.

    Args:
        data: The data to write to the file. This must be a numpy array. The dtype
            of the array determines whether or not the data is bit packed, and the
            shape must match the bits per shot.

            dtype=np.bool_: Not bit packed. Shape must be
                (num_shots, num_measurements + num_detectors + num_observables).
            dtype=np.uint8: Yes bit packed. Shape must be
                (num_shots, math.ceil(
                    (num_measurements + num_detectors + num_observables) / 8)).
        path: The path to the file to write the data to.
        format: The format that the data is stored in, such as 'b8'.
            See https://github.com/quantumlib/Stim/blob/main/doc/result_formats.md
        num_measurements: How many measurements there are per shot.
        num_detectors: How many detectors there are per shot.
        num_observables: How many observables there are per shot.
            Note that this only refers to observables *in the given shot data*, not
            to observables from the original circuit that was sampled.

    Examples:
        >>> import lestim
        >>> import pathlib
        >>> import tempfile
        >>> import numpy as np
        >>> with tempfile.TemporaryDirectory() as d:
        ...     path = pathlib.Path(d) / 'shots'
        ...     shot_data = np.array([
        ...         [0, 1, 0],
        ...         [0, 1, 1],
        ...     ], dtype=np.bool_)
        ...
        ...     lestim.write_shot_data_file(
        ...         path=str(path),
        ...         data=shot_data,
        ...         format='01',
        ...         num_measurements=3)
        ...
        ...     with open(path) as f:
        ...         written = f.read()
        >>> written
        '010\n011\n'
    """
```
