include ../../script/make/build_docker_image.mk

docker-run:
	docker run --rm -it \
		--name spark \
		--volume $(shell cd .. && pwd)/examples:/tmp/examples \
		--workdir /tmp/examples \
		$(IMAGE) \
		/bin/bash
