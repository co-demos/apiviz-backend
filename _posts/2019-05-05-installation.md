---
title : INSTALLATION WALKTHROUGH
categories:
  - guide
tags:
  - documentation
  - configuration
  - installation
toc: true
toc_label: " contents"
toc_sticky: true
---


--------

## Warning

You need to install Apiviz-backend to enjoy **[Apiviz-frontend](https://github.com/co-demos/apiviz-frontend)** to serve your configuration to the frontend.


--------

## Build and run 

You have two different options to run (locally) Apiviz on your computer/server : with **Python** or with **Docker**, depending where your heart leans...

--------


### _WITH DOCKER (locally or in production)_


- **locally - in your browser check this url**
    - install [Docker (here for mac OS)](https://docs.docker.com/docker-for-mac/install/) 
    - clone or [download](https://github.com/co-demos/ApiViz/archive/master.zip) the repo
    - [install MongoDB](https://docs.mongodb.com/manual/installation/) locally/on your server or get the URI of the MongoDB you're using
    - go to your apiviz folder
    - launch docker and run : 
        ```sh
        make up
        ```
    - check the following URL in your browser : 
      ```
      http://localhost:8100
      ```    

- **in production** 
    - install [Docker](https://phoenixnap.com/kb/how-to-install-docker-on-ubuntu-18-04) on your server (here for Ubuntu 18) 
      ```sh
      sudo apt-get update
      sudo apt-get remove docker docker-engine docker.io
      sudo apt install docker.io
      sudo systemctl start docker
      sudo systemctl enable docker
      ```
    - set up UFW, GIT, NGINX, ...
    - (optional) [install MongoDB](https://docs.mongodb.com/manual/installation/) (if the ApiViz's DB for config is hosted on your own server)
    - add the github repo
    - create and set of secret variables in a file (`backend/config_app/config_secret_vars_prod.py`) based on `config_secret_vars_example.py` structure
    - lauch docker and run the command : 
      ```sh
      make up-prod
      ```

    - test the following url in your browser : 
    [`http://localhost:8100/backend/api/config/global?uuid=c5efafab-1733-4ad1-9eb8-d529bc87c481`](http://localhost:8100/backend/api/config/global?uuid=c5efafab-1733-4ad1-9eb8-d529bc87c481)

<hr>

### _WITHOUT DOCKER - LOCALLY_

1. **clone or [download](https://github.com/co-demos/ApiViz/archive/master.zip) the repo**
1. **[install MongoDB](https://docs.mongodb.com/manual/installation/) locally** or get the URI of the MongoDB you're using
1. **go to your apiviz folder**
1. **use Python 2**
1. **install python pip and virtualenv**
	```sh 
	sudo apt install python-pip
	sudo apt install virtualenv
	```


1. **install a [virtual environment](https://pypi.python.org/pypi/virtualenv)**
	```sh
	virtualenv -p python3 venv
	source venv/bin/activate
	````
		
1. **install the libraries**

	```sh
	sudo pip install -r requirements.txt
	```

1. if any problem occur here try to reinstall pip with 

    ```sh
      curl https://bootstrap.pypa.io/get-pip.py | python
    ```


1. **optional** : _update the `backend/config_app/config_secret_vars_example.py` file with your mongoDB URI (if you're not using default mongoDB connection_
	>

1. **Go to your app folder and run :**

	```sh
	python run_apiviz.py
	````
1. **optional** : you can also use some variables in the command line : 
	```sh
	# get the list of available CLI options
	python run_apiviz.py --help

	# for example : run with a custom port number in testing mode
	python run_apiviz.py --port=8200 --mode=preprod
	```

1. **test the following url in your browser** : 
[`http://localhost:8081/backend/api/config/global?uuid=c5efafab-1733-4ad1-9eb8-d529bc87c481`](http://localhost:8081/backend/api/config/global?uuid=c5efafab-1733-4ad1-9eb8-d529bc87c481)


### _WITHOUT DOCKER - IN PRODUCTION_

1. **get a server** - check digital ocean, OVH, ...
1. optionnal : get a domain name : check OVH, namecheap, godaddy.... + setup DNS
1. **follow (most of) these [instructions](https://github.com/entrepreneur-interet-general/tutos-2018/wiki/Admin-Sys)**
1. **create a `backend/config_app/config_secret_vars_prod.py` file** based on `config_secret_vars_example.py` structure
1. **go to app folder and create a virtual env** (for instance called "venv")
1. **set up the [gunicorn service](./unit/working_service_config.service) and [NGINX](./nginx/working_nginx_config)** accordingly 

1. ... pray for all that to work as expected, and keep calm... 

1. **update code and (re-)deploy**

    ```sh
    cd /<your_app_folder>/<username>/app_apiviz
    git pull origin master
    cd backend/frontend

    # build the frontend
    npm install
    npm run build

    # rerun app
    sudo systemctl restart apiviz
    ```
    
--------

## Environment variables


### the `.env` files

The environment variables are stored in a couple of files at the root of the project : 

- `example.env.global`
- `example.env.mongodb`

If you want or need to use Apiviz in production you will have to duplicate those files at the same level with those new names : 

- `.env.global`
- `.env.mongodb`

... then you will be able to change the environment variable you want and begin to use all of the available arguments like :

```sh
# with Docker
make up-prod
```

```sh
# with Python only
python run_apiviz.py mongodb=distant mode=dev_email
```

```sh
# with Gunicorn
gunicorn wsgi_prod:app --bind=0.0.0.0:4100
```


### the variables

At the CLI level you can use :

``` python
@click.option('--mode',     default="default",     nargs=1,  help="The <mode> you need to run the app : default | testing | preprod | production" )
@click.option('--docker',   default="docker_off",  nargs=1,  help="Are you running the app with <docker> : docker_off | docker_on" )
@click.option('--mongodb',  default="local",       nargs=1,  help="The <mongodb> you need to run the app : local | distant | server" )
@click.option('--auth',     default="default",     nargs=1,  help="The <auth> mode you need to run the app : default | default_docker | server | server_docker | distant_preprod | distant_prod" )
@click.option('--host',     default="localhost",   nargs=1,  help="The <host> name you want the app to run on : <IP_NUMBER> " )
@click.option('--port',     default="8100",        nargs=1,  help="The <port> number you want the app to run on : <PORT_NUMBER>")
@click.option('--https',    default="false",       nargs=1,  help="The <https> mode you want the app to run on : true | false")
```

Within the `.env`files you can change the following variables : 

- `example.env.global`

``` bash
RUN_MODE=preprod
DOCKER_MODE=docker_on
AUTH_MODE=distant_prod
HTTPS_MODE=false

### FLASK RELATED 
DEBUG=true
TESTING=true
DOMAIN_ROOT=localhost
DOMAIN_PORT=8100
SECRET_KEY=qJxDaGacUT4Df5nx2UgGUx2VNNnjgxd9BKKVdLYQ
SERVER_NAME_TEST=True


### MONGO DB RELATED
MONGODB_MODE=local
MONGO_ROOT_LOCAL=localhost
MONGO_ROOT_DOCKER=host.docker.internal
MONGO_PORT_LOCAL=27017
MONGO_COLL_CONFIG_GLOBAL=config_global
MONGO_COLL_CONFIG_NAVBAR=config_navbar
MONGO_COLL_CONFIG_TABS=config_tabs
MONGO_COLL_CONFIG_APP_STYLES=config_app_styles
MONGO_COLL_CONFIG_DATA_ENDPOINTS=config_data_endpoints
MONGO_COLL_CONFIG_ROUTES=config_routes
MONGO_COLL_CONFIG_FOOTER=config_footer
MONGO_COLL_CONFIG_SOCIALS=config_socials
```

- `example.env.mongodb`

``` bash
MONGO_DBNAME=apiviz
MONGO_DBNAME_TEST=apiviz-test
MONGO_DBNAME_PREPROD=apiviz-preprod
MONGO_DBNAME_PROD=apiviz-prod

MONGO_ROOT_SERVER=127.0.0.1
MONGO_PORT_SERVER=27017
MONGO_USER_SERVER=MY-MONGODB-SERVER-USERNAME
MONGO_PASS_SERVER=MY-MONGODB-SERVER-USER-PASSWORD
MONGO_OPTIONS_SERVER=?MY-MONGODB-SERVER-OPTIONS

### for instance on MongodbAtlas
MONGO_DISTANT_URI=mongodb://<DISTANT-USERNAME>:<DISTANT-PASSWORD>@<DISTANT-HOST>:<DISTANT-PORT>
MONGO_DISTANT_URI_OPTIONS=?ssl=true&replicaSet=<REPLICA-SET>&authSource=admin&retryWrites=true


```