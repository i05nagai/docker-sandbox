PATH_TO_THIS_DIR := $(dir $(realpath $(lastword ${MAKEFILE_LIST})))
PATH_TO_PARENT_DIR := $(dir $(realpath $(PATH_TO_THIS_DIR)))
include ../../script/make/build_docker_image.mk
DOCKER_BUILD_PATH = ..
DOCKER_DOCKERFILE_PATH := Dockerfile

docker-run:
	docker run --rm -it \
		docker.io/i05nagai/locust-ubuntu1804 \
		--volume $(shell cd .. && pwd):/workdir \
		--entrypoint /bin/bash \
		-w /workdir
