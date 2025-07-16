include ../../script/make/build_docker_image.mk

DOCKER_BUILD_PATH = ..
TOP_MAKEFILE := $(word 1, $(MAKEFILE_LIST))
BASE_PATH := $(abspath $(dir $(abspath $(TOP_MAKEFILE)))..)

docker-run-server:
	$(DOCKER) \
		run \
		--rm \
		 -it \
		-U postgres \
		--name postgresql-server \
		--env POSTGRES_PASSWORD=password \
		-p 5432:5432 \
		$(IMAGE)

docker-run-server-attach:
	$(DOCKER) \
		exec \
		-it \
		--user postgres \
		postgresql-server \
		/bin/bash

docker-run-client:
	$(DOCKER) \
		run \
		--rm \
		 -it \
		--name postgresql-server \
		--env POSTGRES_PASSWORD=password \
		-p 5432:5432 \
		$(IMAGE) \
		/bin/bash
