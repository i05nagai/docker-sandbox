FROM ubuntu:18.04

RUN \
    apt-get update

ARG LDAP_ADMIN_PASSWORD
ARG LDAP_DOMAIN
ARG LDAP_ORGANISATION
ARG LDAP_BACKEND
COPY ./template/opt/local/openldap/install_openldap.sh /opt/local/openldap/install_openldap.sh
RUN  /opt/local/openldap/install_openldap.sh

RUN \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y \
        slapd \
        ldap-utils
