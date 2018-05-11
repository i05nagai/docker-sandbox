#!/bin/bash

usage() {
  cat <<EOF
lint.sh is a tool for lint terraform formatter.

Usage:
    lint.sh <path-to-dir>

Options:
    --debug -d  debug
EOF
}

version() {
  echo "lint.sh version 0.0.1"
}

while [ $# -gt 0 ];
do
  case ${1} in
    --debug|-d)
      set -x
    ;;

    --help|-h)
      usage
      exit 0
    ;;

    --recrusive|-r)
      shift
    ;;

    --version|-v)
      version
      exit 0
    ;;

    --*)
      echo "[ERROR] Invalid option '${1}'"
      usage
      exit 1
    ;;

    *)
      PATH_TO_DIR=$1
      shift
    ;;
  esac
  shift
done

terraform fmt -list=false -write=false -check=true ${PATH_TO_DIR}
ret=$?
if [ $ret -ne 0 ]; then
  echo "Error! Terraform lint failed."
  echo "Following files must be formatted."
  echo ""
  terraform fmt -write=false -list=true ${PATH_TO_DIR}
  exit $ret
fi
