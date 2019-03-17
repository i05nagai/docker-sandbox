FROM ubuntu:16.04

RUN \
    apt-get update \
    && apt-get install -y \
        curl \
        git \
        gnupg \
    && curl -sL https://deb.nodesource.com/setup_10.x | bash - \
    && apt-get install -y nodejs
