FROM ubuntu:18.04

RUN \
    apt-get update \
    && apt-get install -y \
        build-essential \
        libssl-dev \
        git \
        zlib1g-dev \
    && git clone https://github.com/giltene/wrk2.git /tmp/wrk2 \
    && cd /tmp/wrk2 \
    && make \
    && cp wrk /usr/local/bin

COPY ./template /
