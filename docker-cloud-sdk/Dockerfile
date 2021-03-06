FROM ubuntu:16.04
MAINTAINER i05nagai

ENV CLOUD_SDK_VERSION 196.0.0
RUN \
    apt-get -qqy update \
    && apt-get install -qqy \
        curl \
        gcc \
        python-dev \
        python-pip \
        python-setuptools \
        apt-transport-https \
        lsb-release \
        openssh-client \
        git \
        docker.io

RUN \
    curl -L https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python get-pip.py pip==9.0.3
    && pip install -U crcmod \
    && export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" \
    && echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" > /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - \
    && apt-get update \
    && apt-get install -y \
        google-cloud-sdk=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-app-engine-python=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-app-engine-java=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-app-engine-go=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-datalab=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-datastore-emulator=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-pubsub-emulator=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-bigtable-emulator=${CLOUD_SDK_VERSION}-0 \
        google-cloud-sdk-cbt=${CLOUD_SDK_VERSION}-0 \
        kubectl \
    && gcloud config set core/disable_usage_reporting true \
    && gcloud config set component_manager/disable_update_check true \
    && gcloud config set metrics/environment github_docker_image \
    && gcloud --version \
    && docker --version \
    && kubectl version --client
ENTRYPOINT ["/opt/local/cloud-sdk/entrypoint.sh"]
