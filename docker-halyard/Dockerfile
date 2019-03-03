FROM ubuntu:18.04

RUN \
    apt-get update \
    && apt-get install -y \
        curl \
        software-properties-common \
        git

RUN useradd --create-home --shell /bin/bash halyard
# accept all default options
# install as halyard
RUN \
    curl -O https://raw.githubusercontent.com/spinnaker/halyard/master/install/debian/InstallHalyard.sh \
    && bash InstallHalyard.sh --user halyard -y
USER halyard

WORKDIR /opt/local/halyard
