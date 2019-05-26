#!/bin/bash

ldapadd \
    -x \
    -D cn=admin,dc=example,dc=com \
    -W -f add_content.ldif

# ldapadd -x -D cn=i05nagai,dc=example,dc=com -W -f add_content.ldif
