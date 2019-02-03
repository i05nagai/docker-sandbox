#!/bin/bash

docker run --rm -it \
  --name datadog-agent \
  --volume /var/run/docker.sock:/var/run/docker.sock:ro \
  --volume /proc/:/host/proc/:ro \
  --volume /sys/fs/cgroup/:/host/sys/fs/cgroup:ro \
  --volume $HOME/.local/var/log:/host/var/log:ro \
  --env DD_API_KEY=${DATADOG_API_KEY} \
  --env DD_LOGS_ENABLED="true" \
  --env DD_PROCESS_AGENT_ENABLED="true" \
  --env DD_DOCKER_LABELS_AS_TAGS="true" \
  --env DD_LOGS_CONFIG_CONTAINER_COLLECT_ALL="true" \
  --env DD_AC_EXCLUDE="name:datadog-agent" \
  i05nagai/datadog-agent:latest
