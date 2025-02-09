FROM ubuntu:24.04
MAINTAINER i05nagai

RUN \
    apt-get update \
    && apt-get install -y \
        curl \
        gpg \
    && curl https://packages.fluentbit.io/fluentbit.key | gpg --dearmor > /usr/share/keyrings/fluentbit-keyring.gpg \
    && curl https://raw.githubusercontent.com/fluent/fluent-bit/master/install.sh | sh

ENV PATH=/opt/fluent-bit/bin:$PATH
ADD ./template /
