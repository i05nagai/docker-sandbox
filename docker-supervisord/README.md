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

```
./run_supervisor.sh
```

## Configuration
[Configuration File — Supervisor 4\.0\.2 documentation](http://supervisord.org/configuration.html#environment-variables)

- Environment variables
    - `%(ENV_X)s` for the value of the environment variable `ENV_X`


- `[unix_http_server]`
    - configuration for a HTTP server that listens on a Unix socket 
- `[inet_http_server]`
    - configuration for a HTTP server that listens on a TCP socket
- `[supervisord]`
    - configration for supervisord 
- `[supervisorctl]`
    - configuration for superviosrctl
- `[program:x]`
    - A header value of [program:foo] describes a program with the name of “foo”. 


## Reference
- [Supervisor: A Process Control System — Supervisor 4\.0\.2 documentation](http://supervisord.org/)
