# Deltakit-Stim

Deltakit-Stim is a [Stim](https://github.com/quantumlib/Stim) fork that adds support for non-computational leakage errors and an adaptive detector error model (DEM). It consists of a set of instructions to handle single qubit leakage within Stim's API definition. Specifically:

- A leakage reset `RL` as a new `GateType`. It returns the indexed qubits in the sealed state, that is the encoded quantum state.
- A leakage channel `LEAKAGE` as a new `GateType`. It creates a noisy channel for leakage. 
- A heralded leakage event `HERALD_LEAKAGE_EVENT` as a new `GateType`. It records the noise event in the measurement record.

The adaptive DEM is an extension to current Stim's DEM datastructure to hold metadata associated with non-computational errors (leakage, erasure, atom loss) to be further interpreted by the decoder. It provides additional edge updates to the decoding graph from heralded leakage events which can be pre-processed by the decoder to improve the qubit footprint.


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

## How Deltakit-Stim works

To get started with deltakit-stim, an example demonstrating how deltakit-stim handles leakage will be introduced. Qubits are designed to operate in two computational states: |0⟩ and |1⟩. However, qubits can sometimes "leak" into higher energy states (|2⟩, |3⟩, etc.) that are outside the computational sub-space. Leakage is a significant source of error as leaked qubits can spread errors to other qubits through multi-qubit gates.

**How Deltakit-Stim models leakage differently:**

1. **Specify where leakage occurs**: Use `LEAKAGE(p)` gates to introduce leakage, where `p` is the probability of each specified qubit leaking.
2. **Leakage propagation through gates**: Deltakit-Stim models how two-qubit gates (CZ, CX, CY, etc.) spread leakage between qubits and introduce depolarizing errors when leaked qubits interact. Users can configure leakage spreading and transfer rates using optional gate parameters (see gate documentation for details).
3. **Detect accumulated leakage**: `HERALD_LEAKAGE_EVENT` adds a bit to the measurement record (accessible via `rec[-...]`) indicating whether a qubit has leaked, based on the accumulated leakage from `LEAKAGE` gates and propagation through 2-qubit gates. Reset gates (R, RX etc.) clear the accumulated leakage for their target qubits.
4. **Leakage-aware decoding**: The DEM contains heralded errors with probabilities derived from the accumulated leakage, enabling leakage-aware decoding strategies.

This differs from Stim's `HERALDED_ERASE`, which requires explicitly specifying each heralded error at a particular qubit and time step, without automatic tracking of leakage accumulation and propagation.

The example below demonstrates how `HERALD_LEAKAGE_EVENT` enables leakage detection.

## Getting Started

This example demonstrates the use of the `LEAKAGE` and `HERALD_LEAKAGE_EVENT` gates. This is essential for leakage-aware error correction and represents the key difference from Stim.

```python
import numpy as np
import deltakit_stim

circuit = deltakit_stim.Circuit("""
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

sampler = circuit.compile_detector_sampler()
detection_events = sampler.sample(shots=1000)

print(f"Detection events shape: {detection_events.shape}")
print(f"Number of detectors: {detection_events.shape[1]}")

# The first detector (index 0) references rec[-4], the result of HERALD_LEAKAGE_EVENT
herald_events = detection_events[:, 0]
leakage_detected = np.sum(herald_events)
print(f"\nLeakage events detected: {leakage_detected} out of {len(herald_events)} shots")
print(f"Leakage rate: {leakage_detected / len(herald_events) * 100:.2f}%")

# Generate the DEM to see the heralded errors
dem = circuit.detector_error_model()
print(f"\nDetector Error Model:\n{dem}")
```

The circuit uses `LEAKAGE(0.1)` to simulate a 10% probability of leakage on qubit 1. The `HERALD_LEAKAGE_EVENT` instruction adds an entry to the measurement record, which is captured by the first detector (`DETECTOR rec[-4]`, labeled D0 in the DEM), creating a fourth detector specifically for heralding in this circuit. Running this circuit for 1000 shots detects approximately 100 leakage events, matching the 10% leakage probability.

The generated Detector Error Model includes heralded errors showing how leakage affects the detectors:

```
error(0.5) D0 D2
```

This heralded error indicates that when the herald detector D0 fires (showing qubit 1 leaked), detector D2 is affected with 50% probability because measuring a leaked qubit produces a random outcome. Without `HERALD_LEAKAGE_EVENT`, the DEM would only show three detectors without any errors.

### Use in Error Correction

Leakage-aware decoders use the herald information from `HERALD_LEAKAGE_EVENT` to make better correction decisions. The [Local Clustering Decoder](https://www.nature.com/articles/s41467-025-66773-x) demonstrates that leakage-aware decoding can reduce physical qubit requirements by a factor of 4 compared to standard non-adaptive decoding.

For complete examples of leakage-aware decoding workflows, see the [Deltakit Decoding guide](https://deltakit-docs.riverlane.com/en/docs/guide/decoding.html#leakage-aware-decoding).

## Citation

For any reference to Stim, please consider using the citation:

```
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

If you use Deltakit-Stim's leakage-aware features, please also consider citing the Local Clustering Decoder paper, which details the leakage-aware decoding method:

```
@article{locher2025local,
  doi = {10.1038/s41467-025-66773-x},
  url = {https://doi.org/10.1038/s41467-025-66773-x},
  title = {Local clustering decoder: beating the trade-off of code distance and circuit depth in quantum error correction},
  author = {Locher, Dominik F. and Bohdanowicz, Thomas C. and Lao, Lingling and Leroux, Ian and Beale, Stefanie J. and Verdon, Guillaume and Vuillot, Christophe and Brown, Natalie C.},
  journal = {Nature Communications},
  volume = {16},
  number = {1},
  pages = {554},
  year = {2025},
  publisher = {Nature Publishing Group}
}
```
