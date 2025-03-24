#!/usr/bin/env bash

set -e

echo "Executando Black"
black --check -q src
echo "Executando Isort"
isort --check -q src
echo "Executando Flake8"
flake8 --ignore=E211,E999,F821,W503,E203 --max-line-length=121 --exclude=migrations,settings,__pycache__,tests src
echo "Fim"