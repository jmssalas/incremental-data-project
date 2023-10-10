include .env

.PHONY: help test
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#' Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done


build: # Build the docker images
	docker-compose build

run: # Run docker containers in the background
	docker-compose up -d --build
	docker exec ${MODULE_NAME}_app pip install -r requirements.txt
	docker exec ${MODULE_NAME}_app python src/main.py

enter: # Enter into app container
	docker exec -it ${MODULE_NAME}_app bash

down: # Down docker containers
	docker-compose down

test: run # Run tests on the container
	docker exec -it ${MODULE_NAME}_app npm test

delete-branches: # Delete all git branches except 'master'
	git branch | grep -v "master" | xargs git branch -D

update-master: # Update master branch
	git fetch origin && git checkout master && git pull
