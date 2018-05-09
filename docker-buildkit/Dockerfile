ARG DOCKER_IMAGE_PREFIX
FROM ${DOCKER_IMAGE_PREFIX}core:latest

RUN \
    apt-get update \
    && apt-get install -y \
        git \
        build-essential \
        runc \
        containerd \
        curl \
    && curl -fsSL get.docker.com -o get-docker.sh \
    && sh get-docker.sh \
    # Cleanups
    && /opt/local/core/build_cleanup.sh

RUN \
    cd /tmp \
    && export DOCKER_HOST=tcp://docker:2375 \
    && git clone https://github.com/moby/buildkit.git \
    && cd buildkit \
    && make \
    && make install

#
# GO
#
ENV GOPATH=/opt/local/golang \
    PATH=$PATH:/usr/lib/go-1.10/bin
RUN \
    mkdir -p \
        $GOPATH \
        $GOPATH/bin \
    && apt-get update \
    && apt-get install -y \
        software-properties-common \
    && add-apt-repository ppa:gophers/archive \
    && apt-get update \
    && apt-get install -y \
        curl \
        git \
        golang-1.10-go \
    # go dep
    && curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh

#
# install build-using-dockerfile
#
RUN \
    cd /tmp/buildkit \
    && go get github.com/containerd/containerd \
    && go get github.com/moby/buildkit \
    && go build ./examples/build-using-dockerfile \
    && install build-using-dockerfile /usr/local/bin
COPY ./opt /opt
ENV PATH="$PATH:/opt/local/buildkit/bin"
