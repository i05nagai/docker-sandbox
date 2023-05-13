PATH_TO_THIS_DIR := $(dir $(realpath $(lastword ${MAKEFILE_LIST})))
PATH_TO_PARENT_DIR := $(dir $(realpath $(PATH_TO_THIS_DIR)))
include ../../script/make/build_docker_image.mk
DOCKER_BUILD_PATH = ..
DOCKER_DOCKERFILE_PATH := Dockerfile
DOCKER_NETWORK := flink-network

docker-run:
	$(DOCKER) run \
		--rm \
		-it \
		--workdir /tmp/repository/opt/local/flink \
		--name flink \
		-p 8081:8081 \
		--env FLINK_PROPERTIES="${FLINK_PROPERTIES}" \
		--volume $(PATH_TO_PARENT_DIR)/template/:/tmp/repository \
		$(IMAGE) \
		/bin/bash

docker-network-create:
	$(DOCKER) network \
		create \
		${DOCKER_NETWORK}

docker-network-rm:
	$(DOCKER) network \
		rm \
		${DOCKER_NETWORK}

docker-jobmanager:
	$(DOCKER) run \
		--rm \
		-it \
		--workdir /tmp/repository/opt/local/flink \
		--network ${DOCKER_NETWORK} \
		--name jobmanager \
		-p 8081:8081 \
		--env FLINK_PROPERTIES \
		--volume $(PATH_TO_PARENT_DIR)/template/:/tmp/repository \
		$(IMAGE) \
		bash -c '$${FLINK_HOME}/bin/jobmanager.sh start-foreground'

docker-taskmanager:
	$(DOCKER) run \
		--rm \
		-it \
		--workdir /tmp/repository/opt/local/flink \
		--network ${DOCKER_NETWORK} \
		--name taskmanager \
		--env FLINK_PROPERTIES \
		--volume $(PATH_TO_PARENT_DIR)/template/:/tmp/repository \
		$(IMAGE) \
		bash -c '$${FLINK_HOME}/bin/taskmanager.sh start-foreground'

