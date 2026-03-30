#!/bin/bash
set -e

#########################################################################
# Regenerates doc files using the installed version of stim.
#########################################################################

# Get to this script's git repo root.
cd "$( dirname "${BASH_SOURCE[0]}" )"
cd "$(git rev-parse --show-toplevel)"

python dev/gen_deltakit_stim_api_reference.py -dev > doc/deltakit_stim_python_api_reference_vDev.md
python dev/gen_deltakit_stim_stub_file.py -dev > glue/python/src/deltakit_stim/__init__.pyi
python dev/gen_deltakit_stim_stub_file.py -dev > doc/deltakit_stim.pyi
python -c "import deltakit_stim; deltakit_stim.main(command_line_args=['help', 'gates_markdown'])" > doc/deltakit_stim_gates.md
