ARG DOCKER_IMAGE_PREFIX
FROM ${DOCKER_IMAGE_PREFIX}core:latest

RUN \
    apt-get update \
    && apt-get install -y \
        curl \
        python2.7 \
        python2.7-dev \
        build-essential \
    # pip
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python2.7 get-pip.py \
    && pip install --user apache-beam[gcp]

RUN \
    pip install nose
