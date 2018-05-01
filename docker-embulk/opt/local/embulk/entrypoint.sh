#!/bin/bash
set -e

if [ "$1" = 'embulk' ]; then
  ${PATH_TO_EMBULK}/substitute_credential --aws
  ${PATH_TO_EMBULK}/substitute_credential --gcp

  # drop $1
  shift
  exec embulk "$@"
fi

exec "$@"
