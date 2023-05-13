FROM ubuntu:22.04
MAINTAINER i05nagai

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN \
    groupadd -r mysql \
    && useradd -r -g mysql mysql \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        gnupg \
        dirmngr \
    && rm -rf /var/lib/apt/lists/*

ENV MYSQL_MAJOR=8.0 \
    MYSQL_VERSION=8.0.31-0ubuntu0.22.04.1

# Install MySQL.
RUN \
  apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
      mysql-server \
      mysql-client \
  && rm -rf /var/lib/apt/lists/*

COPY ./template /

EXPOSE 3306
