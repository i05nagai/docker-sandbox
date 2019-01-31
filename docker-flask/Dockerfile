FROM ubuntu:18.04

RUN \
    apt-get update \
    && apt-get install -y \
        python3 \
        python3-distutils \
        curl \
    # pip
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py

RUN \
    pip install \
        flask \
        gunicorn
