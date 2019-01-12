FROM ubuntu:16.04

RUN \
    apt-get update \
    && apt-get install -y \
        curl \
        build-essential \
    && curl -O -L https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh \
    && bash Miniconda2-latest-Linux-x86_64.sh -b -p $HOME/miniconda

RUN \
    export PATH="/root/miniconda/bin:$PATH" \
    && conda create -n default python=2.7 \
    && conda install -n default -y \
        numpy \
    && echo 'export PATH="/root/miniconda/bin:$PATH"' >> /root/.bashrc \
    && echo 'source activate default' >> /root/.bashrc
