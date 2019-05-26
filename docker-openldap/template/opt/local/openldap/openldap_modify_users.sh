#!/bin/bash

# modify as admin
ldapmodify \
    -x \
    -W \
    -v \
    -D "cn=admin,dc=example,dc=com" \
    -f modify.ldif

# modify as i05nagai
ldapmodify \
    -x \
    -W \
    -v \
    -D "uid=i05nagai,ou=People,dc=example,dc=com" \
    -f modify.ldif
