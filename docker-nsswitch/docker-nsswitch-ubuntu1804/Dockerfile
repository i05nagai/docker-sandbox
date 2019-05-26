FROM ubuntu:18.04

RUN \
    apt-get update \
    && apt-get install -y \
        libnss-ldap \
        ldap-utils \
        apt-utils

RUN \
    getent passwd

RUN \
    apt-get install -y \
      openssh-server\
      ssh \
      netcat \
      vim \
      build-essential \
  && mkdir /var/run/sshd \
  && chmod 0755 /var/run/sshd

RUN \
    apt-get install -y \
      nscd

COPY ./template /
