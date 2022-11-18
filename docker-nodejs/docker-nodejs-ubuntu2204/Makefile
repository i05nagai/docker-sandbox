PATH_TO_PARENT_DIR := $(dir $(realpath $(lastword ${MAKEFILE_LIST})/..))

include ../../script/make/build_docker_image.mk

run:
	docker run -it -v $(PATH_TO_PARENT_DIR)/examples:/nodejs -w /nodejs $(IMAGE) /bin/bash
