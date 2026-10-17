PROJECT_NAME := surveys
TAG := dev
IMAGE := $(PROJECT_NAME)/$(PROJECT_NAME)

build_image_local:
	docker build -t $(IMAGE):$(TAG) -f docker/Dockerfile .

project_up: build_image_local
	docker compose -f docker/docker-compose.yml up -d --force-recreate

project_stop:
	docker compose -f docker/docker-compose.yml stop

project_logs:
	docker compose -f docker/docker-compose.yml logs -f