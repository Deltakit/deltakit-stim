#!/usr/bin/env python3

#########################################################
# Sets version numbers to a date-based dev version.
#
# Does nothing if not on a dev version.
#########################################################
# Example usage (from repo root):
#
# ./dev/overwrite_dev_versions_with_date.sh
#########################################################

import os
import pathlib
import subprocess
import sys

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


def main():
    os.chdir(pathlib.Path(__file__).parent)
    os.chdir(subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode().strip())

    # Generate dev version starting from major.minor version.
    # (Requires the existing version to have a 'dev' suffix.)
    # (Uses the timestamp of the HEAD commit, to ensure consistency when run multiple times.)
    with open("pyproject.toml", "rb") as f:
        version = tomllib.load(f)["project"]["version"]
    maj_version, min_version, patch = version.split(".", 2)
    if "dev" not in patch:
        return  # Do nothing for non-dev versions.
    timestamp = subprocess.check_output(["git", "show", "-s", "--format=%ct", "HEAD"]).decode().strip()
    new_version = f"{maj_version}.{min_version}.dev{timestamp}"

    # Overwrite existing versions.
    package_setup_files = [
        "pyproject.toml",
        "glue/cirq/setup.py",
        "glue/cirq/stimcirq/__init__.py",
        "glue/zx/stimzx/__init__.py",
        "glue/zx/setup.py",
        "glue/sample/setup.py",
        "glue/sample/src/sinter/__init__.py",
    ]
    for path in package_setup_files:
        with open(path) as f:
            content = f.read()
        if path.endswith(".toml"):
            old_line = f'version = "{version}"'
            new_line = f'version = "{new_version}"'
        else:
            old_line = f"__version__ = '{version}'"
            new_line = f"__version__ = '{new_version}'"
        assert old_line in content, f"{old_line!r} not found in {path}"
        content = content.replace(old_line, new_line)
        with open(path, "w") as f:
            print(content, file=f, end="")


if __name__ == '__main__':
    main()
