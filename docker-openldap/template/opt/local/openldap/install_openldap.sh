#!/bin/bash

set -e
set -x

LDAP_ADMIN_PASSWORD=${LDAP_ADMIN_PASSWORD:-"admin"}
LDAP_DOMAIN=${LDAP_DOMAIN:-"example.com"}
LDAP_ORGANISATION=${LDAP_ORGANISATION:-"Example com"}
LDAP_BACKEND=${LDAP_BACKEND:-"MDB"}

cat <<EOF | debconf-set-selections
slapd slapd/internal/generated_adminpw password ${LDAP_ADMIN_PASSWORD}
slapd slapd/internal/adminpw password ${LDAP_ADMIN_PASSWORD}
slapd slapd/password2 password ${LDAP_ADMIN_PASSWORD}
slapd slapd/password1 password ${LDAP_ADMIN_PASSWORD}
slapd slapd/dump_database_destdir string /var/backups/slapd-VERSION
slapd slapd/domain string ${LDAP_DOMAIN}
slapd shared/organization string ${LDAP_ORGANISATION}
slapd slapd/backend select ${LDAP_BACKEND}
slapd slapd/purge_database boolean true
slapd slapd/move_old_database boolean false
slapd slapd/allow_ldap_v2 boolean false
slapd slapd/no_configuration boolean false
slapd slapd/dump_database select when needed
slapd slapd/password_mismatch note
slapd slapd/invalid_config boolean true
slapd slapd/ppolicy_schema_needs_update select abort installation
slapd slapd/unsafe_selfwrite_acl note
EOF
# slapd slapd/backend string ${LDAP_BACKEND}
