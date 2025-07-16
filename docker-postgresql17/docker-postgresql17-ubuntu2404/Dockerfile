FROM ubuntu:24.04
MAINTAINER i05nagai

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN \
    groupadd -r postgresql --gid=999 \
    && useradd -r -g postgresql --uid=999 --home-dir=/var/lib/postgresql --shell=/bin/bash postgresql \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        gnupg \
        dirmngr \
    && rm -rf /var/lib/apt/lists/*

RUN \
    install --verbose --directory --owner postgresql --group postgresql --mode 1777 /var/lib/postgresql

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        locales \
    && rm -rf /var/lib/apt/lists/* \
    && echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen \
    && locale-gen \
    && locale -a | grep 'en_US.utf8'

ENV LANG en_US.utf8

ENV POSTGRESQL_MAJOR 16
ENV PATH $PATH:/usr/lib/postgresql/$POSTGRESQL_MAJOR/bin

RUN \
  apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
      postgresql-$POSTGRESQL_MAJOR=$POSTGRESQL_MAJOR \
  && rm -rf /var/lib/apt/lists/*

COPY ./template /


USER postgresql
