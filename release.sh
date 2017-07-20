#!/bin/bash
set -euo pipefail; IFS=$'\n\t'

NAME=$( python setup.py --name | tail -1 )
VER=$( python setup.py --version | tail -1 )

echo "========================================================================"
echo "Tagging $NAME v$VER"
echo "========================================================================"

git tag -a v$VER
git push origin v$VER

echo "========================================================================"
echo "Releasing $NAME v$VER on PyPI"
echo "========================================================================"

python setup.py sdist
twine upload dist/*
rm -r dist/ *.egg-info
