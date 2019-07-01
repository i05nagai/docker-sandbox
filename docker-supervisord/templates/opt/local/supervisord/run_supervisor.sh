#!/bin/bash

set -e
set -x

# supervisord --configuration /etc/supervisor/supervisord.conf
supervisord --configuration /etc/supervisor/supervisord.conf --nodaemon
