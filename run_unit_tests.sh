#!/usr/bin/env bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
pytest --cov=src/ test/unit/

