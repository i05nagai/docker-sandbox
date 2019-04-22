FROM ubuntu:18.04
MAINTAINER i05nagai

# Install all OS dependencies for notebook server that starts but lacks all
# features (e.g., download as all possible file formats)
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
    && apt-get -yq dist-upgrade \
    && apt-get install -yq --no-install-recommends \
        curl \
        bzip2 \
        ca-certificates \
        sudo \
        locales \
        fonts-liberation

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen


RUN \
    apt-get update \
    && apt-get install -y \
        python3 \
        python3-dev \
        curl \
    # pip
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py

RUN \
    pip install jupyterhub

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

RUN \
    npm install -g configurable-http-proxy
