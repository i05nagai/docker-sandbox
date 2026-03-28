FROM ubuntu:24.04


RUN \
    apt-get update && \
    apt-get install \
        -y --no-install-recommends \
        ca-certificates \
        curl \
        git \
        unzip

WORKDIR /tmp
RUN \
    AQUA_VERSION=v2.55.2 && \
    curl -sSfL https://github.com/aquaproj/aqua/releases/download/${AQUA_VERSION}/aqua_linux_amd64.tar.gz | tar xz -C /usr/local/bin aqua

# export PATH="${AQUA_ROOT_DIR:-${XDG_DATA_HOME:-$HOME/.local/share}/aquaproj-aqua}/bin:$PATH"

COPY ./template /
