FROM ubuntu:16.04

ENV DEFAULT_PYTHON_VERSION=3.6.5 \
    VIRTUALENV=default \
    PYENV_ROOT="/root/.pyenv" \
    PATH="/root/$HOME/.pyenv/bin:$PATH"

RUN \
    apt-get update \
    && apt-get install -y \
        git \
        curl \
        build-essential \
        zlib1g-dev \
        libssl-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        llvm \
        libncurses5-dev \
        xz-utils \
        ca-certificates \
    # pyenv
    && git clone https://github.com/pyenv/pyenv.git ~/.pyenv \
    && echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile \
    && export PYENV_ROOT="$HOME/.pyenv" \
    && echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile \
    && export PATH="$PYENV_ROOT/bin:$PATH" \
    && echo 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile \
    # pyenv-virtualenv
    && git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv \
    && echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile \
    # setup
    && pyenv install 2.7.14 \
    && pyenv install ${DEFAULT_PYTHON_VERSION} \
    && echo "source ~/.bash_profile" >> ~/.bashrc \
    && pyenv virtualenv ${DEFAULT_PYTHON_VERSION} ${VIRTUALENV}

# setup for virtualenv
COPY ./opt /opt
ENTRYPOINT ["/opt/local/pyenv/entrypoint.sh"]
