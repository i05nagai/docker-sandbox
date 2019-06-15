## Overview
Create docker container which is accesible by ssh with SSH keys registered in GitHub.

## Build docker image

```
make
```

## Usage

```
./docker_run.sh <your-github-user-name>
ssh -i /path/to/private/key <your-github-user-name>@localhost -p 1122
```

## Reference
- [sshd\(8\)](https://www.freebsd.org/cgi/man.cgi?sshd(8))
