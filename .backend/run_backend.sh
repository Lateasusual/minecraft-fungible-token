#!/bin/bash
echo "Starting flask backend"
export FLASK_APP=backend.py
export FLASK_ENV=development
python3 -m flask run
