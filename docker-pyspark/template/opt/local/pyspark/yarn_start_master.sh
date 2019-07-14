#!/bin/bash

PATH_THIS_DIR=$(cd $(dirname ${0});pwd)

${PATH_THIS_DIR}/yarn_entrypoint.sh -d -namenode
