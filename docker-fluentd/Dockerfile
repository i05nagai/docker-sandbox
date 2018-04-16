FROM ubuntu:16.04

COPY ./skelton/opt/local/fluentd/Gemfile /opt/local/fluentd/Gemfile

RUN \
    BUILD_DEPS="make gcc g++ libc6-dev ruby-dev libffi-dev" \
    &&  apt-get update \
    && apt-get install -y \
        $BUILD_DEPS \
        ca-certificates \
        libjemalloc1 \
        liblz4-1 \
        ruby \
        curl \
    && echo 'gem: --no-document' >> /etc/gemrc \
    && gem install --file /opt/local/fluentd/Gemfile

COPY ./skelton /
ENTRYPOINT ["/opt/local/fluentd/entrypoint.sh"]
