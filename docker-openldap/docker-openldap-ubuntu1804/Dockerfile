FROM ubuntu:18.04

RUN \
    apt-get update

ARG LDAP_ADMIN_PASSWORD
ARG LDAP_DOMAIN
ARG LDAP_ORGANISATION
ARG LDAP_BACKEND

RUN \
    apt-get install -y \
        apt-utils
COPY ./template/opt/local/openldap/install_openldap.sh /opt/local/openldap/install_openldap.sh

RUN \
    /opt/local/openldap/install_openldap.sh \
    && DEBIAN_FRONTEND=noninteractive \
        apt-get install -y \
            slapd \
            ldap-utils

# for sladp logging
RUN \
    apt-get install -y \
        rsyslog
#RUN dpkg-reconfigure -f noninteractive slapd

COPY ./template /
