FROM ubuntu:22.04

RUN \
    apt update \
    && apt install -y \
        ruby-full

COPY ./template /

RUN \
    apt install -y \
        make \
        gcc-aarch64-linux-gnu \
        git \
        sqlite3 \
    && gem install bundler -v 2.3.25

#    && apt-get install -y \
#        build-essential \
#        checkinstall \
#        libreadline-gplv2-dev \
#        libncursesw5-dev \
#        libssl-dev \
#        libsqlite3-dev \
#        tk-dev \
#        libgdbm-dev \
#        libc6-dev \
#        libbz2-dev \
#        curl \
#    && cd /usr/src \
#    && curl -L -O https://www.python.org/ftp/python/3.4.8/Python-3.4.8.tgz \
#    && tar xzf Python-3.4.8.tgz \
#    && cd Python-3.4.8 \
#    && ./configure --enable-optimizations \
#    && make install \
#    # pip
#    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
#    && python get-pip.py pip==9.0.3

