#!/usr/bin/env bash
time python -m cProfile -o valid.prof main.py -dataset django -cuda -mode validate -data_dir ./preprocessed/django -output_dir ./results/django
