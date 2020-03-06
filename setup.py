#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast
import os
import setuptools

from setuptools.command.install import install as _install


def get_version_from_init():
    init_file = os.path.join(
        os.path.dirname(__file__), 'pjlsa', '__init__.py'
    )
    with open(init_file, 'r') as fd:
        for line in fd:
            if line.startswith('__version__'):
                return ast.literal_eval(line.split('=', 1)[1].strip())


VERSION=get_version_from_init()

setuptools.setup(
    name='pjlsa',
    version=VERSION,
    description='A Python wrapping of Java LSA API',
    author='Riccardo De Maria',
    author_email='riccardo.de.maria@cern.ch',
    url='https://github.com/rdemaria/pjlsa',
    packages=['pjlsa'],
    package_dir={'pjlsa': 'pjlsa'},
    install_requires=['JPype1>=0.7.1',
                      'cmmnbuild-dep-manager>=2.4.0' ],
    extras_require={"dev": ["pytest"]},
     entry_points={
         # Register with cmmnbuild_dep_manager.
         'cmmnbuild_dep_manager': [f'pytimber={VERSION}'],
        },
)

