#!/bin/bash

ldapadd -x -D cn=admin,dc=example,dc=com -W -f add_content.ldif
