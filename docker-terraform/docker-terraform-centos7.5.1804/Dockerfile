FROM centos:centos7.5.1804

RUN \
    yum update \
    && yum install -y \
        curl \
        unzip

RUN \
    cd /tmp \
    && curl -L -O https://releases.hashicorp.com/terraform/0.11.13/terraform_0.11.13_linux_amd64.zip \
    && unzip ./terraform_0.11.13_linux_amd64.zip -d /usr/bin \
    && rm terraform_0.11.13_linux_amd64.zip
