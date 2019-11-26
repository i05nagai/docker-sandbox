ARG DOCKER_IMAGE_PREFIX
FROM ${DOCKER_IMAGE_PREFIX}core:latest

#
# python3
#
RUN \
    apt-get update \
    && apt-get install -y \
        python3 \
        curl \
    # pip
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py

#
# python3.5
#
RUN \
    apt-get update \
    && apt-get install -y \
        python3.5 \
        curl \
    # pip
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py

#
# python3.6
#
RUN \
    apt-get update \
    && apt-get install -y \
        software-properties-common \
    && add-apt-repository ppa:jonathonf/python-3.6 \
    && apt-get update \
    && apt-get install python3.6 \
    && apt-get install -y \
        curl \
    # pip
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py
