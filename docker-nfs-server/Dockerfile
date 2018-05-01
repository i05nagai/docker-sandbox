FROM ubuntu:16.04
MAINTAINER i05nagai

RUN apt-get update \
    && apt-get install -y \
        nfs-kernel-server \
    && mkdir -p /srv/volume/shared/home

EXPOSE 111/udp 2049/tcp
COPY ./skelton /
ENTRYPOINT ["/opt/local/nfs-server/entrypoint.sh"]
