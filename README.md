# LeStim

Leakage-Stim (abbrv. LeStim) is a [Stim](https://github.com/quantumlib/Stim) fork extending its functionalities to the non-computational leakage error and a new adaptive detector error model (DEM). It consists of a set of instructions to handle single qubit leakage within Stim's API definition. Specifically:

- A leakage reset `RL` as a new `GateType`. It returns the indexed qubits in the sealed state, that is the encoded quantum state.
- A leakage channel `LEAKAGE` as a new `GateType`. It creates a noisy channel for leakage. 
- A heralded leakage event `HERALD_LEAKAGE_EVENT` as a new `GateType`. It records the noise event in the measurement record.

The adaptative DEM is an extension to current Stim's DEM datastructure to hold metadata associated with non-computational errors (leakage, erasure, atom loss) to be further interpreted by the decoder. It provides additional edge updates to the decoding graph from heralded leakage events which can be pre-processed by the decoder to improve the qubit footprint.


## Installation as a Python dependency

Whenever using [`hatch`](https://hatch.pypa.io/latest/), [`uv`](https://docs.astral.sh/uv/) or any pyproject-compatible Python manager, edit file `pyproject.toml` to add the line

```toml
  "lestim"
```

to the list of `dependencies`.

## Installation from source

The simplest way to contribute is to `git clone` LeStim from the private GitHub [repository](https://github.com/riverlane/le-stim)

```bash
git clone https://github.com/riverlane/le-stim
```

Then, the C++ package can be installed either using build managers [CMake](https://cmake.org/) 

```bash
cd le-stim
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
There is a known issue when both `stim` and `lestim` are installed in the same Python runtime. This is currently under investigation but the recommendation is not to install both.

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
