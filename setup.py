# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
import platform

from setuptools import setup, Extension
import glob
import pybind11

ALL_SOURCE_FILES = glob.glob("src/**/*.cc", recursive=True)
MUX_SOURCE_FILES = glob.glob("src/**/march.pybind.cc", recursive=True)
TEST_FILES = glob.glob("src/**/*.test.cc", recursive=True)
PERF_FILES = glob.glob("src/**/*.perf.cc", recursive=True)
MAIN_FILES = glob.glob("src/**/main.cc", recursive=True)
HEADER_FILES = glob.glob("src/**/*.h", recursive=True) + glob.glob("src/**/*.inl", recursive=True)
RELEVANT_SOURCE_FILES = sorted(set(ALL_SOURCE_FILES) - set(TEST_FILES + PERF_FILES + MAIN_FILES + MUX_SOURCE_FILES))

__version__ = '1.15'

# Detect architecture
def is_arm_architecture():
    """Detect if we're building for ARM/ARM64 architecture."""
    machine = platform.machine().lower()
    return machine.startswith('arm') or machine.startswith('aarch64') or machine == 'arm64'

IS_ARM = is_arm_architecture()

if sys.platform.startswith('win'):
    common_compile_args = [
        '/std:c++20',
        '/O2',
        f'/DVERSION_INFO={__version__}',
    ]
    if not IS_ARM:
        arch_avx = ['/arch:AVX2']
        arch_sse = ['/arch:SSE2']
    else:
        # Windows on ARM - no SSE/AVX support
        arch_avx = []
        arch_sse = []
    arch_basic = []
else:
    common_compile_args = [
        '-std=c++20',
        '-fno-strict-aliasing',
        '-O3',
        '-g0',
        f'-DVERSION_INFO={__version__}',
    ]
    if not IS_ARM:
        # x86/x86_64 architecture
        arch_avx = ['-mavx2']
        arch_sse = ['-msse2', '-mno-avx2']
    else:
        # ARM/ARM64 architecture - no SSE/AVX, but we can use ARM-specific optimizations
        arch_avx = []
        arch_sse = []
    arch_basic = []

# Always build the basic extensions
ext_modules = []

stim_detect_machine_architecture = Extension(
    'deltakit_stim._detect_machine_architecture',
    sources=MUX_SOURCE_FILES,
    include_dirs=[pybind11.get_include(), "src"],
    language='c++',
    extra_compile_args=[
        *common_compile_args,
        *arch_basic,
    ],
)
ext_modules.append(stim_detect_machine_architecture)

stim_polyfill = Extension(
    'deltakit_stim._stim_polyfill',
    sources=RELEVANT_SOURCE_FILES,
    include_dirs=[pybind11.get_include(), "src"],
    language='c++',
    extra_compile_args=[
        *common_compile_args,
        *arch_basic,
        '-DSTIM_PYBIND11_MODULE_NAME=_stim_polyfill',
    ],
)
ext_modules.append(stim_polyfill)

# Only build SSE2 extension on x86/x86_64 architectures
if not IS_ARM:
    stim_sse2 = Extension(
        'deltakit_stim._stim_sse2',
        sources=RELEVANT_SOURCE_FILES,
        include_dirs=[pybind11.get_include(), "src"],
        language='c++',
        extra_compile_args=[
            *common_compile_args,
            *arch_sse,
            '-DSTIM_PYBIND11_MODULE_NAME=_stim_sse2',
        ],
    )
    ext_modules.append(stim_sse2)
else:
    # On ARM, we could create an ARM-optimized version or just skip the SSE2 variant
    print("Note: Skipping SSE2 extension on ARM architecture")

# NOTE: disabled until https://github.com/quantumlib/Stim/issues/432 is fixed
# if not IS_ARM:
#     stim_avx2 = Extension(
#         'deltakit_stim._stim_avx2',
#         sources=RELEVANT_SOURCE_FILES,
#         include_dirs=[pybind11.get_include(), "src"],
#         language='c++',
#         extra_compile_args=[
#             *common_compile_args,
#             *arch_avx,
#             '-DSTIM_PYBIND11_MODULE_NAME=_stim_avx2',
#         ],
#     )
#     ext_modules.append(stim_avx2)

with open('glue/python/README.md', encoding='UTF-8') as f:
    long_description = f.read()

setup(
    name='deltakit-stim',
    version=__version__,
    author='Craig Gidney',
    author_email='craig.gidney@gmail.com',
    url='https://github.com/quantumlib/stim',
    license='Apache 2',
    description='A fast library for analyzing with quantum stabilizer circuits.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    ext_modules=ext_modules,
    python_requires='>=3.8.0',
    packages=['deltakit_stim'],
    package_dir={'deltakit_stim': 'glue/python/src/deltakit_stim'},
    package_data={'': [*HEADER_FILES, 'glue/python/src/stim/__init__.pyi', 'glue/python/README.md', 'pyproject.toml']},
    include_package_data=True,
    install_requires=['numpy'],
    entry_points={
        'console_scripts': ['stim=stim._main_argv:main_argv'],
    },
    # Needed on Windows to avoid the default `build` colliding with Bazel's `BUILD`.
    options={'build': {'build_base': 'python_build_stim'}},
)
