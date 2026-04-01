# Deltakit-Stim

Deltakit-Stim is a [Stim](https://github.com/quantumlib/Stim) fork extending its functionalities to the non-computational leakage error and a new adaptive detector error model (DEM). It consists of a set of instructions to handle single qubit leakage within Stim's API definition. Specifically:

- A leakage reset `RL` as a new `GateType`. It returns the indexed qubits in the sealed state, that is the encoded quantum state.
- A leakage channel `LEAKAGE` as a new `GateType`. It creates a noisy channel for leakage. 
- A heralded leakage event `HERALD_LEAKAGE_EVENT` as a new `GateType`. It records the noise event in the measurement record.

The adaptative DEM is an extension to current Stim's DEM datastructure to hold metadata associated with non-computational errors (leakage, erasure, atom loss) to be further interpreted by the decoder. It provides additional edge updates to the decoding graph from heralded leakage events which can be pre-processed by the decoder to improve the qubit footprint.


## Installation as a Python dependency

Whenever using [`hatch`](https://hatch.pypa.io/latest/), [`uv`](https://docs.astral.sh/uv/) or any pyproject-compatible Python manager, edit file `pyproject.toml` to add the line

```toml
  "deltakit-stim"
```

to the list of `dependencies`.

## Installation from source

The simplest way to contribute is to `git clone` Deltakit-Stim from the GitHub [repository](https://github.com/Deltakit/deltakit-stim.git)

```bash
git clone https://github.com/Deltakit/deltakit-stim.git
```

Then, the C++ package can be installed either using build managers [CMake](https://cmake.org/) 

```bash
cd deltakit-stim
mkdir build
cd build
cmake ..
```

or [Bazel](https://bazel.build/)

```bash
bazel build //:stim
```

provided a C++ compiler is installed on the system. 

[!WARNING]
There is a known issue when both `stim` and `deltakit-stim` are installed in the same Python runtime. This is currently under investigation but the recommendation is not to install both.

## Getting Started

To get started with deltakit-stim, an example demonstrating how deltakit-stim handles leakage will be introduced. Qubits are designed to operate in two computational states: |0⟩ and |1⟩. However, qubits can sometimes "leak" into higher energy states (|2⟩, |3⟩, etc.) that are outside the computational sub-space. Leakage is a significant source of error as leaked qubits can spread errors to other qubits through multi-qubit gates.

**How Deltakit-Stim models leakage differently:**

1. **Specify where leakage occurs**: Use `LEAKAGE(p)` gates to introduce leakage, where `p` is the probability of each specified qubit leaking.
2. **Leakage propagation through gates**: Deltakit-Stim models how two-qubit gates (CZ, CX, CY, etc.) spread leakage between qubits and introduce depolarizing errors when leaked qubits interact. users can configure leakage spreading and transfer rates using optional gate parameters (see gate documentation for details).
3. **Detect accumulated leakage**: `HERALD_LEAKAGE_EVENT` records a heralded error in the DEM based on the total accumulated leakage probability at that qubit up to that point in the circuit. Reset gates (R, RX etc.) clear the accumulated leakage for their target qubits.
4. **Leakage-aware decoding**: The DEM contains heralded errors with probabilities derived from the accumulated leakage, enabling leakage-aware decoding strategies.

This differs from Stim's `HERALDED_ERASE`, which requires explicitly specifying each heralded error at a particular qubit and time step, without automatic tracking of leakage accumulation and propagation.

The example below demonstrates how `HERALD_LEAKAGE_EVENT` enables leakage detection.

### Leakage Detection with HERALD_LEAKAGE_EVENT

This example demonstrates the use of `HERALD_LEAKAGE_EVENT`, which enables the detection of qubits that have leaked, which is essential for leakage-aware error correction.

```python
import numpy as np
import deltakit_stim
```

#### Without Leakage Detection

This circuit uses the `LEAKAGE(0.1)` gate to simulate leakage on qubit 1, but without `HERALD_LEAKAGE_EVENT`, we cannot detect which qubits leaked. The leakage information is not tracked.

```python
circuit_no_herald = deltakit_stim.Circuit("""
R 0 1 2
CZ 0 1
CZ 1 2
LEAKAGE(0.1) 1
M 0 1 2
DETECTOR rec[-3]
DETECTOR rec[-2]
DETECTOR rec[-1]
""")

sampler = circuit_no_herald.compile_detector_sampler()
detection_events = sampler.sample(shots=1000)

print(f"Without herald - Detection events shape: {detection_events.shape}")
print(f"Without herald - Number of detectors: {detection_events.shape[1]}")

# Generate the DEM
dem_no_herald = circuit_no_herald.detector_error_model()
print(f"\nDEM without herald:\n{dem_no_herald}")
```

#### With Leakage Detection

Adding `HERALD_LEAKAGE_EVENT` enables detection of leaked qubits. The herald results are recorded in the measurement record and accessed by a specified detector.

```python
circuit_with_herald = deltakit_stim.Circuit("""
R 0 1 2
CZ 0 1
CZ 1 2
LEAKAGE(0.1) 1
HERALD_LEAKAGE_EVENT 1
M 0 1 2
DETECTOR rec[-4]
DETECTOR rec[-3]
DETECTOR rec[-2]
DETECTOR rec[-1]
""")

sampler = circuit_with_herald.compile_detector_sampler()
detection_events = sampler.sample(shots=1000)

print(f"With herald - Detection events shape: {detection_events.shape}")
print(f"With herald - Number of detectors: {detection_events.shape[1]}")

# The first detector (use index 0 to capture this below) captures the herald event as rec[-4] is the HERALD_LEAKAGE_EVENT
herald_events = detection_events[:, 0]
leakage_detected = np.sum(herald_events)
print(f"\nLeakage events detected: {leakage_detected} out of {len(herald_events)} shots")
print(f"Leakage rate: {leakage_detected / len(herald_events) * 100:.2f}%")

# Generate the DEM to see the heralded errors
dem_with_herald = circuit_with_herald.detector_error_model()
print(f"\nDEM with herald:\n{dem_with_herald}")
```

The simulation shows that adding `HERALD_LEAKAGE_EVENT` enables leakage detection. Without the herald, there are only 3 detectors (one per measurement). With the herald, there are 4 detectors, where the additional detector captures the herald event, detecting 104 leakage events out of 1000 shots, giving approximtely a 10% rate and matching the 0.1 leakage probability.

The Detector Error Models also differ:

**DEM without herald:**
```
detector D0
detector D1
detector D2
```

**DEM with herald:**
```
error(0.5) D0 D2
```

Without `HERALD_LEAKAGE_EVENT`, the DEM only contains detector definitions. With `HERALD_LEAKAGE_EVENT`, heralded errors appear in the DEM showing how the leakage affects the relevant detectors. The heralded error `error(0.5) D0 D2` indicates that when the herald detector D0 fires (showing qubit 1 leaked), detector D2 is affected with 50% probability because measuring a leaked qubit produces a random outcome.

### Use in Error Correction

Leakage-aware decoders use the herald information from `HERALD_LEAKAGE_EVENT` to make better correction decisions. The [Local Clustering Decoder](https://www.nature.com/articles/s41467-025-66773-x) demonstrates that leakage-aware decoding can reduce physical qubit requirements by a factor of 4 compared to standard non-adaptive decoding.

For complete examples of leakage-aware decoding workflows, see the [Deltakit Decoding guide](https://deltakit-docs.riverlane.com/en/docs/guide/decoding.html#leakage-aware-decoding).

## Citation

For any reference to Stim, please consider using the citation:

@article{gidney2021stim,
  doi = {10.22331/q-2021-07-06-497},
  url = {https://doi.org/10.22331/q-2021-07-06-497},
  title = {Stim: a fast stabilizer circuit simulator},
  author = {Gidney, Craig},
  journal = {{Quantum}},
  issn = {2521-327X},
  publisher = {{Verein zur F{\"{o}}rderung des Open Access Publizierens in den Quantenwissenschaften}},
  volume = {5},
  pages = {497},
  month = jul,
  year = {2021}
}
```
