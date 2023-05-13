FROM ubuntu:22.04

RUN \
    apt update \
    && apt install -y \
        build-essential \
        libncursesw5-dev \
        libssl-dev \
        libsqlite3-dev \
        zlib1g-dev \
        curl \
    && cd /usr/src \
    && curl -L -O https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz \
    && tar xzf Python-3.8.0.tgz \
    && cd Python-3.8.0 \
    && ./configure --enable-optimizations \
    && make install \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py pip==21.2.4
