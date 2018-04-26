FROM ubuntu:16.04
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
