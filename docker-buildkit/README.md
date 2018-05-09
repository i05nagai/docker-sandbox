## Overview
Sample docker image for running buildkit.

### build docker image

```
make
```

You can run the built image.

### Run buildkit
Launch a container.

```
./docker_run.sh
```

Launch another terminal and attach to the container.
Then run `buildkitd` via a shell script.

```
docker exec -it buildkit /bin/bash
cd /tmp/host
buildkitd.sh
```

Then you can use buildkit.

### Build docker images with Dockerfile

In the container, you can use `build-using-dockerfile` command like

```
build-using-dockerfile -t <image>:<tag> .
build-using-dockerfile -t <image>:<tag> -f /path/to/Dockerfile .
```
