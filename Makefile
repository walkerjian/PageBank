
# PageBank Makefile

IMAGE_NAME=pagebank
ENV_FILE=.env

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm -it \
		--env-file $(ENV_FILE) \
		-v "$(PWD)":/app \
		$(IMAGE_NAME)

log:
	docker run --rm -it \
		--env-file $(ENV_FILE) \
		-v "$(PWD)":/app \
		$(IMAGE_NAME) > summary.log

clean:
	docker system prune -a --volumes -f

rebuild: clean build

.PHONY: build run log clean rebuild
