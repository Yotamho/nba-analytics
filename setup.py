#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for nba_analytics.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 3.1.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
import sys

from pkg_resources import require, VersionConflict
from setuptools import setup

try:
    require('setuptools>=38.3')
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)

if __name__ == "__main__":
    setup(use_pyscaffold=True,
          install_requires=["basketball_reference_web_scraper==4.3.0"],
          dependency_links=["https://github.com/jaebradley/basketball_reference_web_scraper/tarball/a704bc16ae55449c64b5c5e5ce4e6263d731f471#egg=basketball_reference_web_scraper-4.3.0"]
          )
