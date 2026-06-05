# Notes

This document is a draft for my notes about building and executing `le-stim` in the intend to become a Python package for `Deltakit`. It summarises my current understanding and findings and could serve as a basis for a future documentation.

## Requirements 

Currently, the build manager is [Bazel](https://bazel.build/about), which must be installed on the system alongside Python<=3.13. Depending on your system, a C++ compilation toolchain must be present and configured. On my Mac this is clang coming with the XCode suite. For this repo, the requirement are:

- Bazel 8.4.2
- Python 3.13

Note: Bazel >= 7 encourages to migrate to Bzlmod instead of the previous `WORKSPACE` files as stated [here](https://bazel.build/external/migration). Since `Stim` still supports a `WORKSPACE` file, I kept it in `le-stim` but it is unnecessary here.

## Building and executing le-stim

`Stim` itself is a C++ package with Python bindings that can be built within `le-stim` using:

```bash
bazel build //:stim
```

This creates an executable binary that can be run using:

```bash
bazel run //:stim
```

## Building and execting tests & benchmarks

Similarly as before, the test suite and benchmarks can be built and executed using:

```bash
bazel build //:stim_test && bazel run //:stim_test
```

```bash
bazel build //:stim_benchmark && bazel run //:stim_benchmark
```

Currently, my setup fails 7 tests out of 933. I fixed few type errors in the tests that prevents from building correctly.

## Building the Python wheel

The Python 3.13 wheel can be built using:

```bash
bazel build //:stim_dev_wheel
```

It produces a `stim-0.0.dev0-py3-none-any.whl` file in `/bazel-bin` that can be installed locally:

```bash
pip install --force-reinstall bazel-bin/stim-0.0.dev0-py3-none-any.whl
```

You can check it works by importing it in a Python interpretor:

```bash
>python
Python 3.13.9 (main, Nov 11 2025, 14:37:46) [Clang 17.0.0 (clang-1700.4.4.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import stim
>>> dir(stim)
['Circuit', 'CircuitErrorLocation', 'CircuitErrorLocationStackFrame', 'CircuitInstruction', 'CircuitRepeatBlock', 'CircuitTargetsInsideInstruction', 'CompiledDemSampler', 'CompiledDetectorSampler', 'CompiledMeasurementSampler', 'CompiledMeasurementsToDetectionEventsConverter', 'DemInstruction', 'DemRepeatBlock', 'DemTarget', 'DemTargetWithCoords', 'DetectorErrorModel', 'ExplainedError', 'FlipSimulator', 'FlippedMeasurement', 'Flow', 'GateData', 'GateTarget', 'GateTargetWithCoords', 'PauliString', 'PauliStringIterator', 'Tableau', 'TableauIterator', 'TableauSimulator', '_DiagramHelper', '_UNSTABLE_raw_format_data', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'gate_data', 'main', 'read_shot_data_file', 'target_combined_paulis', 'target_combiner', 'target_inv', 'target_logical_observable_id', 'target_pauli', 'target_rec', 'target_relative_detector_id', 'target_separator', 'target_sweep_bit', 'target_x', 'target_y', 'target_z', 'write_shot_data_file']
```



