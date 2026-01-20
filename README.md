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

## Build Wheels for Internal PyPI Release

* Branch out of default branch for your feature branch.
* Bump version in `setup.py`.
* Make a pull request with `release` as the target branch.
* Upon merge, source and wheel distributions will be built and published on [Riverlane's internal PyPI index](https://riv-pypi.azurewebsites.net/home/)
* Finally, merge `release` branch back into default branch.
