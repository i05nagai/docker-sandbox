include ../../script/make/build_docker_image.mk

docker-run:
	docker run --rm -it \
		--name golang \
		-v $(shell pwd):/workdir \
		-w /workdir \
		$(IMAGE) \
		/bin/bash
