FROM ubuntu:18.04

RUN \
    apt-get update \
    && apt-get install -y \
        curl \
        git \
        gnupg \
        gcc \
        g++ \
        make \
    && curl -sL https://deb.nodesource.com/setup_10.x | bash - \
    && apt-get install -y nodejs
