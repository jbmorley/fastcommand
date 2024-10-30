#!/usr/bin/env python3

# Copyright (c) 2021-2024 Jason Morley
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess

from setuptools import setup, find_packages


ROOT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
CHANGES_DIRECTORY = os.path.join(ROOT_DIRECTORY, "scripts", "changes")

CHANGES_PATH = os.path.join(CHANGES_DIRECTORY, "changes")


# Use changes to determine the package version.
version = subprocess.check_output(["changes", "version"]).decode("utf-8").strip()


setup(
    name='quickcli',
    version=version,
    packages=find_packages(),
    install_requires=[]
)
