#!/bin/bash

set -e
set -x

for i in $(seq 10); do
  echo $(date)
  echo $i
  cat /dev/urandom | tr -dc 'a-zA-Z0-9' | head --byte 100
  sleep 1
done
