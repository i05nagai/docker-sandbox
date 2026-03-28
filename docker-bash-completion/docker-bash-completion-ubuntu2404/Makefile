PATH_TO_THIS_DIR := $(dir $(realpath $(lastword ${MAKEFILE_LIST})))
PATH_TO_PARENT_DIR := $(dir $(realpath $(PATH_TO_THIS_DIR)))
include ../../script/make/build_docker_image.mk
DOCKER_BUILD_PATH = ..
DOCKER_DOCKERFILE_PATH := Dockerfile


docker-run:
	$(DOCKER) run --rm -it \
		--name bash-completion \
		-w /opt/local/bash-completion/sample \
		$(IMAGE) \
		/bin/bash
