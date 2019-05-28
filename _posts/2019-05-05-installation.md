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
      http://localhost:8081
      ```    
    - (optional) you can also use those other docker commands : 
      ```sh
       
      ### for local dev 
      # local DB
      make up
      make restart
      make down
      # distant DB - you will need to set up your mongodb URI in "app/config/config_secret_vars_example.py"  
      make up-dist
      make restart-dist
      make down-dist

      ### for testing mode
      # local DB 
      make up-test
      make restart-test
      make down-test
      # distant DB - you will need to set up your mongodb URI in "app/config/config_secret_vars_example.py"  
      make up-test-dist
      make restart-test-dist
      make down-test-dist
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
    - you can also use those other docker commands : 
      ```sh
       
      ### for production 
      # distant DB 
      make up-prod
      make restart-prod
      make down-prod
      # server DB 
      make up-prod-server
      make restart-prod-server
      make down-prod-server

      ### for preprod 
      # distant DB 
      make up-preprod
      make restart-preprod
      make down-preprod
      # server DB 
      make up-preprod-server
      make restart-preprod-server
      make down-preprod-server

      ### for testing 
      # distant DB 
      make up-test-dist
      make restart-test-dist
      make down-test-dist
      # server DB 
      make up-test-server
      make restart-test-server
      make down-test-server

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
	pythom run_apiviz.py --port=8200 --mode=preprod
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


