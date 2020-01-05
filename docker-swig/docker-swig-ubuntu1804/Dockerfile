FROM ubuntu:18.04
ARG SWIG_VERSION=4.0.1

RUN \
    apt-get update \
    # Install Java.
    && apt-get install -y \
        g++ \
        libpcre3  \
        curl \
        build-essential \
        libpcre3-dev

RUN \
    curl \
        -L https://downloads.sourceforge.net/swig/swig-${SWIG_VERSION}.tar.gz \
        -o /tmp/swig-${SWIG_VERSION}.tar.gz \
    && cd /tmp \
    && tar xzf swig-${SWIG_VERSION}.tar.gz

RUN \
    cd /tmp/swig-${SWIG_VERSION} \
    && ./configure --prefix=/usr --without-maximum-compile-warnings \
    && make \
    && make install \
    && install -v -m755 -d /usr/share/doc/swig-4.0.1 \
    && cp -v -R Doc/* /usr/share/doc/swig-4.0.1

RUN \
    apt-get install -y \
        python3 \
        python3-dev
