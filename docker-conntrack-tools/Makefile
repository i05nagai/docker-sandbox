
IMAGE=conntrack-tools
TAG=latest
CONTAINER=conntrack

build:
	docker build -t ${IMAGE}:${TAG} .

run:
	docker run \
		--rm -it \
		--privileged \
		--name ${CONTAINER} \
		${IMAGE}:${TAG} \
		/bin/bash

attach:
	docker exec \
		-it \
		${CONTAINER} \
		/bin/bash
