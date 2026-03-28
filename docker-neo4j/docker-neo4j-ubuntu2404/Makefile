include ../../script/make/build_docker_image.mk

DOCKER_BUILD_PATH = ..
DOCKER_NETWORK := neo4j

docker-network-create:
	docker network create \
	$(DOCKER_NETWORK)

docker-network-delete:
	docker network rm \
	$(DOCKER_NETWORK)

docker-run-server:
	$(DOCKER) \
		run \
		--rm \
		-it \
		--network $(DOCKER_NETWORK) \
		--name neo4j-server \
		-v $(shell realpath ${DOCKER_BUILD_PATH}):/workdir \
		-w /workdir \
		-p 7474:7474 \
		$(IMAGE) \
		/bin/bash

docker-run-client:
	$(DOCKER) \
		run \
		--rm \
		-it \
		--network $(DOCKER_NETWORK) \
		--name neo4j-client \
		-v $(shell realpath ${DOCKER_BUILD_PATH}):/workdir \
		-w /workdir \
		$(IMAGE) \
		/bin/bash
