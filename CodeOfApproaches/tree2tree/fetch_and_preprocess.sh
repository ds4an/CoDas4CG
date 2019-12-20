#!/bin/bash
set -e
 python scripts/download.py

#! sudo sh build_java.sh

export PYTHONPATH="$PYTHONPATH:."
#!python scripts/preprocess_hs.py
python scripts/preprocess_django.py
