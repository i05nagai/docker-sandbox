FROM ubuntu:24.04

RUN \
    apt-get update \
    && apt-get install -y \
        python3 \
        python3-dev \
        curl \
    # pip
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py

