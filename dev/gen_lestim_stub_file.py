#!/usr/bin/env python3

"""
Produces a .pyi file for lestim, describing the contained classes and functions.
"""

import lestim
import sys

from util_gen_stub_file import generate_documentation


def main():
    version = lestim.__version__
    if "dev" in version or version == "VERSION_INFO" or "-dev" in sys.argv:
        version = "(Development Version)"
    else:
        version = "v" + version
    print(f'''
"""Lestim {version}: a fast quantum stabilizer circuit library."""
# (This is a stubs file describing the classes and methods in lestim.)
from __future__ import annotations
from typing import overload, TYPE_CHECKING, List, Dict, Tuple, Any, Union, Iterable, Optional
if TYPE_CHECKING:
    import io
    import pathlib
    import numpy as np
    import lestim
'''.strip())

    for obj in generate_documentation(obj=lestim, full_name="lestim", level=-1):
        text = '\n'.join(("    " * obj.level + line).rstrip()
                        for paragraph in obj.lines
                        for line in paragraph.splitlines())
        assert "lestim::" not in text, "CONTAINS C++ STYLE TYPE SIGNATURE!!:\n" + text
        print(text)


if __name__ == '__main__':
    main()
