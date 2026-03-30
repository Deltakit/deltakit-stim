#!/usr/bin/env python3

"""
Produces a .pyi file for deltakit_stim, describing the contained classes and functions.
"""

import deltakit_stim
import sys

from util_gen_stub_file import generate_documentation


def main():
    version = deltakit_stim.__version__
    if "dev" in version or version == "VERSION_INFO" or "-dev" in sys.argv:
        version = "(Development Version)"
    else:
        version = "v" + version
    print(f'''
"""Deltakit-Stim {version}: a fast quantum stabilizer circuit library."""
# (This is a stubs file describing the classes and methods in deltakit_stim.)
from __future__ import annotations
from typing import overload, TYPE_CHECKING, List, Dict, Tuple, Any, Union, Iterable, Optional
if TYPE_CHECKING:
    import io
    import pathlib
    import numpy as np
    import deltakit_stim
'''.strip())

    for obj in generate_documentation(obj=deltakit_stim, full_name="deltakit_stim", level=-1):
        text = '\n'.join(("    " * obj.level + line).rstrip()
                        for paragraph in obj.lines
                        for line in paragraph.splitlines())
        assert "deltakit_stim::" not in text, "CONTAINS C++ STYLE TYPE SIGNATURE!!:\n" + text
        print(text)


if __name__ == '__main__':
    main()
