include ../../script/make/build_docker_image.mk
PATH_TO_THIS_DIR := $(dir $(realpath $(lastword ${MAKEFILE_LIST})))
PATH_TO_PARENT_DIR := $(dir $(realpath $(PATH_TO_THIS_DIR)))

run:
	docker run \
		--rm \
		-it \
		--workdir /tmp/repository/opt/local/octave \
		--name octave \
		--volume $(PATH_TO_PARENT_DIR)/template/:/tmp/repository \
		$(IMAGE) \
		/bin/bash
