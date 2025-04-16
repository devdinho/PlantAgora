#!/usr/bin/env bash

cd src
python manage.py test --settings=plantagora.settings
pytest --ds=plantagora.settings --durations=0 -p no:warnings