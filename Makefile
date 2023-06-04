SHELL := /bin/bash
PWD := $(shell pwd)

default: build

all:

docker-image:
	docker build -f ./scrappers/preciosClaros/Dockerfile -t "preciosclarosscrapper:latest" .
	docker build -f ./priceProcessor/Dockerfile -t "priceprocessor:latest" .
	docker build -f ./elasticManager/Dockerfile -t "elasticmanager:latest" .
.PHONY: build

docker-compose-up: docker-image
	docker-compose -f docker-compose.yml up -d --build
	docker-compose -f docker-compose.yml logs -f
.PHONY: docker-compose-up

docker-compose-down:
	docker-compose -f docker-compose.yml stop -t 1
	docker-compose -f docker-compose.yml down
.PHONY: docker-compose-down

docker-compose-reset:
	docker-compose -f docker-compose.yml stop -t 1
	docker-compose -f docker-compose.yml down
	docker-compose -f docker-compose.yml up -d --build
	docker-compose -f docker-compose.yml logs -f
.PHONY: docker-compose-reset

docker-compose-logs:
	docker-compose -f docker-compose.yml logs -f
.PHONY: docker-compose-logs


