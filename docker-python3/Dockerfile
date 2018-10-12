ARG DOCKER_IMAGE_PREFIX
FROM ${DOCKER_IMAGE_PREFIX}core:latest

RUN \
    apt-get update \
    && apt-get install -y \
        python3 \
        curl \
    # pip
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py
