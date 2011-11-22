#!/usr/bin/env python
#Copyright (c) 2011 Fabula Solutions. All rights reserved.
#Use of this source code is governed by a BSD-style license that can be
#found in the license.txt file.

import distutils.core
import sys
# Importing setuptools adds some features like "setup.py develop", but
# it's optional so swallow the error if it's not there.
try:
    import setuptools
except ImportError:
    pass

kwargs = {}

version = "0.1.0"

distutils.core.setup(
    name="leveldb-server client",
    version=version,
    packages = ["leveldbClient"],
    author="Srini",
    author_email="srini@fabulasolutions.com",
    url="https://github.com/srinikom/leveldb-server",
    license="BSD",
    description="client for leveldb-server",
    **kwargs
)
