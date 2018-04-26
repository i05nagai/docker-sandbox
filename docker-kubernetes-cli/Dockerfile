FROM ubuntu:16.04

RUN \
    apt-get update \
    && apt-get install -y \
        curl \
        python \
        make \
        apt-transport-https

# gcp
RUN \
    mkdir /tmp/gcloud \
    && cd /tmp/gcloud \
    && curl -L https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-188.0.1-linux-x86_64.tar.gz -o /tmp/gcloud/gcloud.tar.gz \
    && tar -xvzf /tmp/gcloud/gcloud.tar.gz \
    && ./google-cloud-sdk/install.sh \
    && rm -rf /tmp/gcloud

# Init apt
RUN \
    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add \
    && echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list \
    && apt-get update \
    && apt-get install -y \
        docker.io \
        kubelet \
        kubeadm \
        kubectl \
        kubernetes-cni

COPY ./opt /opt
ENTRYPOINT ["/opt/local/kubernetes-cli/entrypoint.sh"]
