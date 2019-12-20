#!/usr/bin/bash

set -e

for model in `ls $1 -t | grep '\.bin$' | grep -v optim`; do
  echo evaluating $model >&2
  bash scripts/geo/test.sh $1/$model
done
