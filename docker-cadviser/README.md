## Overview

```
docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:rw \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  --privileged \
  google/cadvisor:latest \
  --log_dir=/
```

## Reference
* [google/cadvisor: Analyzes resource usage and performance characteristics of running containers.](https://github.com/google/cadvisor)
