#!/bin/sh
# These steps must be executed once the host /var and /lib volumes have
# been mounted, and therefore cannot be done in the docker build stage.

# For systems without journald
mkdir -p /var/log/journal

PATH=${PATH}:/usr/local/bin
# exec /usr/local/bin/fluentd "$@"
exec "$@"
