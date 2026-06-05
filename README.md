# LeStim

Leakage-Stim (abbrv. LeStim) is a [Stim](https://github.com/quantumlib/Stim) fork extending its functionalities to leakage. It consists of a set of instructions to handle single qubit leakage within Stim's API definition. Specifically:

- A leakage reset `RL` as a new `GateType`. It returns the indexed qubits in the sealed state, that is the encoded quantum state.
- A leakage channel `LEAKAGE` as a new `GateType`. It creates a noisy channel for leakage. 
- A heralded leakage event `HERALD_LEAKAGE_EVENT` as a new `GateType`. It records the noise event in the measurement record.

Further usage information can be found in the joint documentation.


## Installation as a dependency

Whenever using [`hatch`](https://hatch.pypa.io/latest/), [`uv`](https://docs.astral.sh/uv/) or any pyproject-compatible Python manager, edit file `pyproject.toml` to add the line

```toml
  "lestim"
```

to the list of `dependencies`.

Please refer to the [documentation](docs/installation.md) to install in development mode. 
