FROM ubuntu:18.04
MAINTAINER i05nagai

# SSH
RUN \
  apt-get update \
  && apt-get install -y \
      openssh-server\
      ssh \
      netcat \
      vim \
      build-essential \
  && mkdir /var/run/sshd \
  && chmod 0755 /var/run/sshd


RUN \
  apt-get install -y \
    sudo

RUN \
  apt-get install -y \
    curl

# You can put your configurations here.
COPY ./skelton /

EXPOSE 22

# Bootstrap

ENTRYPOINT ["/opt/local/sshd/entrypoint.sh"]
