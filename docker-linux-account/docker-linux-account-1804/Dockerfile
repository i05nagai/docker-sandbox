FROM ubuntu:18.04

RUN \
    apt-get update \
    && apt-get install -y \
        sudo

RUN \
    sudo useradd \
        --create-home \
        --shell /bin/bash \
        i05nagai
