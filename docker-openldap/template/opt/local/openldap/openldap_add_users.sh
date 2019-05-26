#!/bin/bash

set -e
set -x

PATH_THIS_DIR=$(cd $(dirname ${0});pwd)
PASSWORD_I05NAGAI="${PASSWORD_I05NAGAI:-"$(slappasswd -s i05nagai)"}"
cat ${PATH_THIS_DIR}/_add_content.ldif > add_content.ldif

ldapadd \
    -x \
    -D cn=admin,dc=example,dc=com \
    -W -f add_content.ldif

# ldapadd -x -D cn=i05nagai,dc=example,dc=com -W -f add_content.ldif
