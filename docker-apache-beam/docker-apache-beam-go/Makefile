include ../../script/make/build_docker_image.mk

docker-run:
	docker run --rm -it \
		--network kafka \
		--name apache-beam-go \
		-v $(shell cd .. && pwd):/workspace \
		-w /workspace \
		$(IMAGE) \
		bash
