include ../script/make/build_docker_image.mk

pre-build:
	if [ -z `docker volume ls --filter name=docker --quiet` ]; then \
		docker volume create docker; \
	fi; \
	if [ -z `docker network ls --filter name=docker_network --quiet` ]; then \
		docker network create docker_network; \
	fi; \
	if [ -z `docker ps --filter name=docker --quiet` ]; then \
		docker run \
			--rm -it \
			--privileged \
			--name docker \
			--network docker_network \
			--volume docker:/var/lib/docker \
			-d \
			docker:dind; \
	fi

docker-build:
	docker build --network docker_network -t ${IMAGE}:${VERSION} ${DOCKER_BUILD_ARGS} .

post-build:
	docker kill docker
