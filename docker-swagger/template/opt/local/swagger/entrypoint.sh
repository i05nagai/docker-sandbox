#!/bin/bash

set -x

export PATH="${SWAGGER_PATH}:${PATH}"
alias swagger-codegen="java -jar ${SWAGGER_PATH}/swagger-codegen-cli.jar"

java -jar ${SWAGGER_PATH}/swagger-codegen-cli.jar $@
