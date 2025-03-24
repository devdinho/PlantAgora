#!/usr/bin/env sh

set -e

echo "Executando Black"
black -q service/src
echo "Executando Isort"
isort -q service/src
echo "Executando Flake8"
flake8 --ignore=E211,E999,F821,W503,E203 --max-line-length=121 --exclude=migrations,settings,__pycache__,tests service/src
echo "Fim"