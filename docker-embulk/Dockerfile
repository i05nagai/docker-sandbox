ARG DOCKER_IMAGE_PREFIX
FROM ${DOCKER_IMAGE_PREFIX}java8:latest
MAINTAINER i05nagai

ENV EMBULK_VERSION=0.8.38 \
    PATH_TO_EMBULK=/opt/local/embulk \
    PATH=${PATH}:/opt/local/embulk

RUN \
    apt-get update \
    && apt-get install -y \
        curl \
    && mkdir -p ${PATH_TO_EMBULK} \
    && curl -L "https://bintray.com/artifact/download/embulk/maven/embulk-${EMBULK_VERSION}.jar" -o "${PATH_TO_EMBULK}/embulk" \
    && chmod +x "${PATH_TO_EMBULK}/embulk" \
    && /opt/local/core/build_cleanup.sh

WORKDIR "${PATH_TO_EMBULK}"
COPY ./opt/local/embulk/Gemfile "${PATH_TO_EMBULK}/"
RUN ${PATH_TO_EMBULK}/embulk bundle install

COPY ./opt /opt
ENTRYPOINT ["bash", "./entrypoint.sh"]
CMD ["--help"]
