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
    && curl -sL https://deb.nodesource.com/setup_12.x | bash - \
    && apt-get install -y nodejs

RUN \
    npm install -g snyk
