## Overview

* embulk
    * 0.8.38
* base image
    * java:8
* workdir
    * `/opt/local/embulk` in image
* path to embulk jar file
    * `/opt/local/embulk/embulk` in image

## Usage

```sh
git clone https://github.com/i05nagai/docker-sandbox.git
cd docker-sandbox/docker-embulk
make
```

To run emblulk command with this image,

```sh
docker run -it --rm image_name embulk_subcommand
```

For instance,

```sh
docker run \
    -it \
    --rm \
    --volume $(pwd)/opt/local/embulk/example:/opt/local/embulk/example \
    image_name \
    embulk guess example/seed.yml -o example/config.yml
docker run \
    -it \
    --rm \
    --volume $(pwd)/opt/local/embulk/example:/opt/local/embulk/example \
    image_name \
    embulk preview example/config.yml
docker run \
    -it \
    --rm \
    --volume $(pwd)/opt/local/embulk/example:/opt/local/embulk/example \
    image_name \
    embulk run example/config.yml
```

Enrypoint of this image is path to `embulk` jar file.
So if you want to attach to container, you need to override entrypoint.

```
docker run -it --rm --entrypoint /bin/bash image_name
```

### With plugins
You can install plugins by adding the plugins in `Gemfile` before building your image.

### With credentials
You can pass some credentails into container through environment variable when you execute `docker-run` commnad.

For GCP, `$HOME/.config/gcloud/credentials` is created with the value of `GCP_CREDENTIALS`.
If `GCP_CREDENTIALS` is not defined, no file will create.

```sh
docker run \
    -it \
    --rm \
    --env \
        GCP_CREDENTIALS="json string" \
    image_name \
    embulk preview path/to/config.yml
```

For AWS, `$HOME/.aws/credentials` is created with the value of `AWS_CREDENTIALS`.
If `AWS_CREDENTIALS` is not defined, no file will create.

```sh
docker run \
    -it \
    --rm \
    --env \
        AWS_CREDENTIALS="config string" \
    image_name \
    embulk preview path/to/config.yml
```
