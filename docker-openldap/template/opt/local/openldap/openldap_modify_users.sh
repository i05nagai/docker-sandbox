#!/bin/bash

set -e
set -x

PATH_THIS_DIR=$(cd $(dirname ${0});pwd)
PASSWORD_I05NAGAI="${PASSWORD_I05NAGAI:-"$(slappasswd -s i05nagai)"}"
cat ${PATH_THIS_DIR}/_modify.ldif > modify.ldif

# modify as admin
ldapmodify \
    -x \
    -W \
    -v \
    -D "cn=admin,dc=example,dc=com" \
    -f modify.ldif

# modify as i05nagai
# ldapmodify \
#     -x \
#     -W \
#     -v \
#     -D "uid=i05nagai,ou=People,dc=example,dc=com" \
#     -f modify.ldif
