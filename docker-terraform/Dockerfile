FROM ubuntu:16.04
MAINTAINER i05nagai

ENV TERRAFORM_VERSION=0.11.5 \
    TERRAFORM_SHA256SUM=131c440263382c79c7f783b70ff35cd1d03eb31c44f7738d153d95a0b8436ac9

RUN \
    apt-get update \
    && apt-get install -y \
        curl \
        unzip \
        git \
        make \
    && curl https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip > /tmp/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
    && echo "${TERRAFORM_SHA256SUM}  /tmp/terraform_${TERRAFORM_VERSION}_linux_amd64.zip" > /tmp/terraform_${TERRAFORM_VERSION}_SHA256SUMS

RUN \
    echo "" \
    && sha256sum -c --strict /tmp/terraform_${TERRAFORM_VERSION}_SHA256SUMS \
    && unzip /tmp/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/bin \
    && rm -f /tmp/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
COPY ./opt /opt
ENTRYPOINT ["/opt/local/terraform/entrypoint.sh"]
