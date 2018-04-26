## Overview
Docker container for supervisord.

## Usage
Just add your configuration into `./templates/etc/supervisor/conf.d`.
Then build docker

```sh
./docker_build.sh
docker run --rm -it i05nagai/supervisord:latest /usr/bin/supervisord

```

```sh
./docker_run_bash.sh
# generate configuration templates
$ echo_supervisord_conf > /host/supervisord.conf
# show preinstalled configuration
$ cat /etc/supervisor/supervisord.conf
```
