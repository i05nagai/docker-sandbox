#!/bin/bash

set -e
set -x

PATH_THIS_DIR=$(cd $(dirname ${0});pwd)
export PASSWORD_I05NAGAI="${PASSWORD_I05NAGAI:-"$(slappasswd -s i05nagai)"}"
# ' ' is delimiter for sed since password contain '/'
cat ${PATH_THIS_DIR}/_add_content.ldif | sed "s __PASSWORD_I05NAGAI__ ${PASSWORD_I05NAGAI} " > ${PATH_THIS_DIR}/add_content.ldif

ldapadd \
    -x \
    -D cn=admin,dc=example,dc=com \
    -W \
    -f ${PATH_THIS_DIR}/add_content.ldif

# ldapadd -x -D cn=i05nagai,dc=example,dc=com -W -f add_content.ldif
