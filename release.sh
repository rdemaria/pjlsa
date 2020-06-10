#!/bin/bash

mkdir dist
pip download -i https://acc-py-repo.cern.ch/repository/vr-py-releases/simple --trusted-host acc-py-repo.cern.ch --no-deps --only-binary=:all: --dest=dist pjlsa
pip download -i https://acc-py-repo.cern.ch/repository/vr-py-releases/simple --trusted-host acc-py-repo.cern.ch --no-deps --no-binary=:all: --dest=dist pjlsa
twine upload dist/*
rm -rf dist