FROM centos:centos7.5.1804

RUN \
    yum update -y \
    && yum install -y \
        autoconf \
        git \
        make


RUN \
    yum install -y automake

RUN \
    yum install -y https://centos7.iuscommunity.org/ius-release.rpm \
    && yum update -y \
    && yum install -y \
        python36u \
        python36u-libs \
        python36u-devel \
        python36u-pip

RUN \
    git clone --depth 1 https://github.com/scop/bash-completion.git /tmp/bash-completion \
    # For running "make check"
    # && pip3.6 install -r /tmp/bash-completion/test/requirements.txt \
    && cd /tmp/bash-completion \
    # if not installing from prepared release tarball
    && autoreconf -i \
    && ./configure \
    && make \
    # optional, requires dejagnu and tcllib
    # && make check \
    # Run as root
    && make install

COPY ./skelton /
