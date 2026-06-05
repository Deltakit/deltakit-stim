#!/bin/bash
set -e

#########################################################################
# Regenerates doc files using the installed version of stim.
#########################################################################

# Get to this script's git repo root.
cd "$( dirname "${BASH_SOURCE[0]}" )"
cd "$(git rev-parse --show-toplevel)"

python dev/gen_lestim_api_reference.py -dev > doc/lestim_python_api_reference_vDev.md
python dev/gen_lestim_stub_file.py -dev > glue/python/src/lestim/__init__.pyi
python dev/gen_lestim_stub_file.py -dev > doc/lestim.pyi
python -c "import lestim; lestim.main(command_line_args=['help', 'gates_markdown'])" > doc/lestim_gates.md
