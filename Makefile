
# include .env file
# include example.env.global
# include example.env.mongodb
# include .env.global
# include .env.mongodb

export APP=apiviz-back-only

export D_FOLDER=docker-files
export DC_FOLDER=dockercomposes
export DF_FOLDER=dockerfiles

#other variable definition
# DC    := docker-compose
# DF    := Dockerfile.

export DC=docker-compose
export DF=Dockerfile.

export DC_PREFIX= $(shell pwd)/${DC}
export DC_PREFIX_FOLDER= $(shell pwd)/${D_FOLDER}/${DC_FOLDER}/${DC}

export DC_FOLDER_SUBPATH= ${D_FOLDER}/${DC_FOLDER}
export DF_FOLDER_SUBPATH= ${D_FOLDER}/${DF_FOLDER}

export APP_PATH := $(shell pwd)

export BACKEND=${APP_PATH}
export FRONTEND=${APP_PATH}

# this is usefull with most python apps in dev mode because if stdout is
# buffered logs do not shows in realtime
PYTHONUNBUFFERED=1
export PYTHONUNBUFFERED


### ============ ###
### network
### ============ ###

network-stop:
	docker network rm ${APP}
network:
	@docker network create ${APP} 2> /dev/null; true

### ============ ###
### nginx
### ============ ###

nginx:
	${DC} -f ${DC_PREFIX_FOLDER}-nginx.yml up --build 
nginx-stop:
	${DC} -f ${DC_PREFIX_FOLDER}-nginx.yml down

### ============ ###
### backend
### ============ ###

# ------------------
# default - dev 
backend-gunicorn-dev:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-dev.yml up --build 
backend-gunicorn-dev-stop:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-dev.yml down

# default - prod
backend-gunicorn-prod:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-prod.yml up --build -d
backend-gunicorn-prod-stop:
	${DC} -f ${DC_PREFIX_FOLDER}-backend-gunicorn-prod.yml down


### ============================= ###
### main make / docker commands
### ============================= ###

# --------------------
# # default - dev
# up: network backend-gunicorn-dev
# down: backend-gunicorn-dev-stop network-stop
# restart: down up

# # default - prod
# up-prod: network backend-gunicorn-prod
# down-prod: backend-gunicorn-prod-stop network-stop
# restart-prod: down-prod up-prod

# default - dev
up: network backend-gunicorn-dev
down: backend-gunicorn-dev-stop network-stop
restart: down up

# default - prod
up-prod: network backend-gunicorn-prod
down-prod: backend-gunicorn-prod-stop network-stop
restart-prod: down-prod up-prod