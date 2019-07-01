#!/bin/bash

set -e
set -x

PATH_THIS_DIR=$(cd $(dirname ${0});pwd)
export PASSWORD_I05NAGAI="${PASSWORD_I05NAGAI:-"$(slappasswd -s i05nagai)"}"
# ' ' is delimiter for sed since password contain '/'
cat ${PATH_THIS_DIR}/_modify.ldif | sed -e "s __PASSWORD_I05NAGAI__ ${PASSWORD_I05NAGAI} " > ${PATH_THIS_DIR}/modify.ldif

# modify as admin
# ldapmodify \
#     -x \
#     -W \
#     -v \
#     -D "cn=admin,dc=example,dc=com" \
#     -f ${PATH_THIS_DIR}/modify.ldif

# modify as i05nagai
ldapmodify \
    -x \
    -W \
    -v \
    -D "uid=i05nagai,ou=People,dc=example,dc=com" \
    -f ${PATH_THIS_DIR}/modify.ldif
