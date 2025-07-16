include ../../script/make/build_docker_image.mk

DOCKER_BUILD_PATH = ..
TOP_MAKEFILE := $(word 1, $(MAKEFILE_LIST))
BASE_PATH := $(abspath $(dir $(abspath $(TOP_MAKEFILE)))..)

docker-run:
	$(DOCKER) \
		run \
		--rm \
		 -it \
		--name postgresql17 \
		-u postgresql \
		-w /workingdir \
		-v $(BASE_PATH)/template:/workingdir \
		--env POSTGRESQL_ROOT_PASSWORD \
		-p 5432:5432 \
		$(IMAGE) \
		/bin/bash

docker-mysql-server:
	$(DOCKER) \
		run \
		--rm \
		-it \
		-e POSTGRESQL_ROOT_PASSWORD \
		-p 5432:5432 \
		$(IMAGE) \
		mysqld -D
