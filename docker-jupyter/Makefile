include ../script/make/build_docker_image.mk

docker-run:
	docker run --rm -it \
		--workdir /tmp/opt/local/jupyter \
		--volume $(shell pwd)/template/opt:/tmp/opt \
		--name jupyter \
		-p 9999:8000 \
		$(IMAGE) \
		/bin/bash
