#!/bin/bash

set -e

PATH_TO_THIS_DIR=$(cd $(dirname ${0});pwd)
if [ "${1}" = "fmt" ]; then
  shift
  ${PATH_TO_THIS_DIR}/formatter.sh $@
elif [ "${1}" = "lint" ]; then
  shift
  ${PATH_TO_THIS_DIR}/lint.sh $@
else
  exec "$@"
fi
