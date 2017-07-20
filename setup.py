#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
from setuptools.command.install import install as _install

import pjlsa

class install(_install):
    def run(self):
        try:
            import cmmnbuild_dep_manager
            mgr = cmmnbuild_dep_manager.Manager()
            mgr.install('pjlsa')
            print('registered pjlsa with cmmnbuild_dep_manager')
        except ImportError:
            pass
        _install.run(self)

setuptools.setup(
    name='pjlsa',
    version=pjlsa.__version__,
    description='A Python wrapping of Java LSA API',
    author='Riccardo De Maria',
    author_email='riccardo.de.maria@cern.ch',
    url='https://github.com/rdemaria/pjlsa',
    packages=['pjlsa'],
    package_dir={'pjlsa': 'pjlsa'},
    install_requires=['JPype1>=0.6.2',
                      'cmmnbuild-dep-manager>=2.1.2' ],
    cmdclass={ 'install': install },
)

