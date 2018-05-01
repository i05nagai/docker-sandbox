include ../script/make/build_docker_image.mk

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
