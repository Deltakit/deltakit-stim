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

To get started with deltakit-stim, an example demonstrating how deltakit-stim handles lekage will be introduced. Qubits are designed to operate in two computational states: |0⟩ and |1⟩. However, qubits can sometimes "leak" into higher energy states (|2⟩, |3⟩, etc.) that are outside the computational sub-space. Leakage is a significant source of error as leaked qubits can spread errors to other qubits through multi-qubit gates.

**How Deltakit-Stim models leakage differently:**

1. **Specify where leakage occurs**: Use `LEAKAGE(p)` gates at locations where leakage is introduced.
2. **Automatic propagation**: Deltakit-stim tracks how leakage spreads through sub-sequent gate operations.
3. **Detect accumulated leakage**: `HERALD_LEAKAGE_EVENT` converts the accumulated leakage throughout the circuit into heralded errors in the DEM.
4. **Leakage-aware decoding**: The DEM contains heralded errors with probabilities calculated from this accumulated leakage, enabling better decoding decisions.

This is different from Stim's `HERALDED_ERASE`, where you must specify the exact space-time location of each heralded error without tracking how leakage propagates.

The example below demonstrates how `HERALD_LEAKAGE_EVENT` enables leakage detection.

### Prerequisites

To run the examples below, you'll need:
1. A Deltakit account and API token from [deltakit.riverlane.com](https://deltakit.riverlane.com/dashboard/token)
2. Deltakit explorer installed: `pip install deltakit-explorer`
3. Set your token: `Client.set_token('<your-token>')` or via the `DELTAKIT_TOKEN` environment variable

### Leakage Detection with HERALD_LEAKAGE_EVENT

This example demonstrates the key capability of `HERALD_LEAKAGE_EVENT`: enabling detection of which specific qubits have leaked, which is essential for leakage-aware error correction.

```python
import numpy as np
import deltakit_stim as stim
from deltakit.explorer import Client
from deltakit.explorer.simulation import simulate_with_stim

client = Client.get_instance()
```

#### Without Leakage Detection

This circuit uses the `LEAKAGE(0.1)` gate to simulate leakage on qubit 1, but without `HERALD_LEAKAGE_EVENT`, we cannot detect which qubits leaked. The leakage information is not tracked.

```python
circuit_no_herald = """
QUBIT_COORDS(0, 0) 0
QUBIT_COORDS(1, 0) 1
QUBIT_COORDS(2, 0) 2
RZ 0 1 2
CZ 0 1
CZ 1 2
LEAKAGE(0.1) 1
MZ 0 1 2
DETECTOR(0, 0) rec[-3]
DETECTOR(1, 0) rec[-2]
DETECTOR(2, 0) rec[-1]
OBSERVABLE_INCLUDE(0) rec[-1]
"""

measurements_no_herald, leakage_no_herald = simulate_with_stim(
    circuit_no_herald, shots=1000, client=client
)
print(f"Without herald - Measurements: {measurements_no_herald.as_numpy().shape}")
print(f"Without herald - Leakage: {leakage_no_herald.as_numpy().shape} (empty)")

# Generate the DEM to see how errors are modeled
circuit_obj_no_herald = stim.Circuit(circuit_no_herald)
dem_no_herald = circuit_obj_no_herald.detector_error_model()
print(f"\nDEM without herald:\n{dem_no_herald}")
```

#### With Leakage Detection

By adding `HERALD_LEAKAGE_EVENT`, we can now detect which qubits leaked. The leakage array will flag leaked qubits, and the DEM will include heralded error entries.

```python
circuit_with_herald = """
QUBIT_COORDS(0, 0) 0
QUBIT_COORDS(1, 0) 1
QUBIT_COORDS(2, 0) 2
RZ 0 1 2
CZ 0 1
CZ 1 2
LEAKAGE(0.1) 1
HERALD_LEAKAGE_EVENT 1
MZ 0 1 2
DETECTOR(0, 0) rec[-3]
DETECTOR(1, 0) rec[-2]
DETECTOR(2, 0) rec[-1]
OBSERVABLE_INCLUDE(0) rec[-1]
"""

measurements_with_herald, leakage_with_herald = simulate_with_stim(
    circuit_with_herald, shots=1000, client=client
)
print(f"With herald - Measurements: {measurements_with_herald.as_numpy().shape}")
print(f"With herald - Leakage: {leakage_with_herald.as_numpy().shape}")

leakage_detected = np.sum(leakage_with_herald.as_numpy())
total_possible = leakage_with_herald.as_numpy().shape[0] * leakage_with_herald.as_numpy().shape[1]
print(f"\nLeakage events detected: {leakage_detected} out of {total_possible} possible")
print(f"Leakage rate: {leakage_detected / total_possible * 100:.2f}%")

# Generate the DEM to see the heralded error entries
circuit_obj_with_herald = stim.Circuit(circuit_with_herald)
dem_with_herald = circuit_obj_with_herald.detector_error_model()
print(f"\nDEM with herald:\n{dem_with_herald}")
```

The simulation shows that adding `HERALD_LEAKAGE_EVENT` enables leakage detection. Without the herald, no leakage information is recorded. With the herald, the leakage array tracks all qubits, detecting approximately 90 leakage events out of 3000 possible measurements (3.0% rate).

The Detector Error Models also differ:

**DEM without herald:**
```
detector D0
detector D1
detector D2
```

**DEM with herald:**
```
error(0.5) D1 D2 D3
detector D0
```

Without `HERALD_LEAKAGE_EVENT`, the DEM only contains detector definitions. With `HERALD_LEAKAGE_EVENT`, a herald detector D3 is added, and the heralded error `error(0.5) D1 D2 D3` appears. This error indicates that when the herald detector D3 fires ( which signals that qubit 1 leaked), detectors D1 and D2 are affected with 50% probability due to the random measurement outcome of the leaked qubit.
### Use in Error Correction

Leakage-aware decoders use the herald information from `HERALD_LEAKAGE_EVENT` to make better correction decisions. Studies show this can reduce the required code distance by up to 50% for the same target logical error rate. The [Local Clustering Decoder](https://arxiv.org/abs/2411.10343) supports leakage-aware decoding with Deltakit-Stim.

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
