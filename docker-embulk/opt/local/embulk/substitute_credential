#!/bin/bash

function usage {
  cat <<EOF
substitute_credential is a tool for ...

Usage:
    substitute_credential --credential credential [<options>]

Options:
    --version, -v     print basename version
    --credential, -c  credential strings. required.
    --path, -p        path to credential.
    --help, -h        print this
EOF
}

function version {
  echo "substitute_credential version 0.0.1"
}

function substitute_aws {
  if [ ! -z ${AWS_CREDENTIALS+x} ]
  then
    mkdir -p ${HOME}/.aws
    echo ${AWS_CREDENTIALS} > ${HOME}/.aws/credentials
  fi

  if [ ! -z ${AWS_CONFIG+x} ]
  then
    mkdir -p ${HOME}/.aws
    echo ${AWS_CONFIG} > ${HOME}/.aws/config
  fi
}

function substitute_gcp {
  if [ ! -z ${GCP_CREDENTIALS+x} ]
  then
    mkdir -p ${HOME}/.config/gcloud
    echo ${GCP_CREDENTIALS} > ${HOME}/.config/gcloud/credentials
  fi

  if [ ! -z ${GCP_CONFIG+x} ]
  then
    mkdir -p ${HOME}/.config/gcloud/configuration
    echo ${AWS_CONFIG} > ${HOME}/.config/gcloud/configuration/config_default
  fi
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

    --credential|-c)
      shift
      credential=$1
    ;;

    --path|-p)
      shift
      path_to_credential=$1
    ;;

    --aws|-a)
      substitute_aws
      exit 0
    ;;

    --gcp|-g)
      substitute_gcp
      exit 0
    ;;

    --version|-v)
      version
      exit 0
    ;;

    *)
      echo "[ERROR] Invalid option '${1}'"
      usage
      exit 1
    ;;
  esac
  shift
done

if [ -z ${credential+x} ]
then
  usage
  exit 1
fi

# default path to credential
if [ -z ${path_to_credential+x} ]
then
  path_to_credential=${HOME}/.config/gcloud/credential.json
fi

mkdir -p $(basename ${path_to_credential})
echo ${credential} > ${path_to_credential}
