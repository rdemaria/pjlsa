#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast
import os
import setuptools

REQUIREMENTS: dict = {
    "core": ["cmmnbuild-dep-manager>=2.5.0,<3.*", "jpype1>=1.2.1,<2.*", "numpy"],
    "test": ["pytest", ],
}


def get_version_from_init():
    init_file = os.path.join(os.path.dirname(__file__), "pjlsa", "__init__.py")
    with open(init_file, "r") as fd:
        for line in fd:
            if line.startswith("__version__"):
                return ast.literal_eval(line.split("=", 1)[1].strip())


ALL_PYI = [('*/' * depth) + '*.pyi' for depth in range(0, 10)]

VERSION = get_version_from_init()

setuptools.setup(
    name="pjlsa",
    version=VERSION,
    description="A Python wrapping of Java LSA API",
    author="LSA / InCA team",
    author_email="inca-support@cern.ch",
    url="https://gitlab.cern.ch/scripting-tools/pjlsa",
    packages=["pjlsa", "cern-stubs", "com-stubs", "java-stubs"],
    package_dir={"pjlsa": "pjlsa", "cern-stubs": "cern-stubs", "com-stubs": "com-stubs", "java-stubs": "java-stubs"},
    python_requires='~=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS["core"],
    extras_require={
        **REQUIREMENTS,
        # The 'dev' extra is the union of 'test' and 'doc', with an option
        # to have explicit development dependencies listed.
        "dev": [
            req
            for extra in ["dev", "test", "doc"]
            for req in REQUIREMENTS.get(extra, [])
        ],
        # The 'all' extra is the union of all requirements.
        "all": [req for reqs in REQUIREMENTS.values() for req in reqs],
    },
    entry_points={
        # Register with cmmnbuild_dep_manager.
        "cmmnbuild_dep_manager": [f"pjlsa={VERSION}"],
    },
    package_data={'cern-stubs': ALL_PYI, 'java-stubs': ALL_PYI, 'com-stubs': ALL_PYI},
)
