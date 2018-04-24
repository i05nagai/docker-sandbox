FROM ubuntu:16.04

RUN \
    apt-get update \
    && apt-get install -y \
        autoconf \
        git \
        make

RUN \
    git clone https://github.com/scop/bash-completion.git /tmp/bash-completion \
    && cd /tmp/bash-completion \
    # if not installing from prepared release tarball
    && autoreconf -i \
    && ./configure \
    && make \
    # optional, requires dejagnu and tcllib
    && make check \
    # as root
    && make install 

COPY ./skelton /
ENTRYPOINT ["/opt/local/bash-completion/entrypoint.sh"]
