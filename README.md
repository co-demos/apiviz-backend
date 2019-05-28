
<h2 align=center>
	<img src="./backend/static/logos/logo_apiviz_15.png"><br>
  BACKEND
</h2>


-------
## PRESENTATION

Visualize data coming from an API in a CMS-like app. 
If your data is stored somewhere and accessible via an API, ApiViz can transform it into a full website to show it at its best. 

ApiViz includes "out-the-box" a back-office to fully configure an original datavisualisation website : 
  - **navbar** : define the logo, links, and menus in your apiviz instance's navabr. 
  - **styles** : define the CSS styles for your apiviz instance.
  - **routes** : define the pages and routes of your apiviz instance, either statics contents or data views.
  - **data endpoints** : define the data endpoints feeding your apiviz instance and the fields you want to display.
  - **global** : define some metadata for your apiviz instance.
  - **footer** : define the links present in the apiviz instance's footer.

--------

## DOCUMENTATION

Check our brand new [documentation website](https://co-demos.github.io/apiviz-backend/) here : https://co-demos.github.io/apiviz-backend/

--------

#### warning : 

**apiviz-backend** is the backend of the APIVIZ-FRONTEND application, it provides the API for serving its configuration to any **[apiviz-frontend](https://github.com/co-demos/apiviz-frontend)** instance.


--------

## THE APIVIZ ECOSYSTEM

ApiViz is designed to **agnosticaly display data** and provide an engine to deploy a **datavisualisation website** without (too much) pain, not regarding to the service(s) serving and storing the data. 

Nevertheless to do so an instance of ApiViz must be connected to several external services : one for authentication, one for serving the data, one for storing the static contents (html pages, images...).

The goal of ApiViz is to **work with any external service** fulfilling those roles, but we developed an **eco-system of open source applications** allowing a complete and free way to deploy such a datavisualisation service. 

<br>

| logo | <div style="text-align:center">the open source eco-system ( aka TADATA! )</div> |
|    :----:   |          :--- |
| <img src="./backend/static/logos/logo_apiviz_icon_15.png" height="33"> | **[Apiviz](https://github.com/co-demos/ApiViz)** as the high-level app for visualisation, a sort of open source CMS for data-visualisation ;   |
| <img src="./backend/static/logos/logo_solidata.png" height="33"> | **[Solidata](https://github.com/entrepreneur-interet-general/solidata_frontend)** to "API-fy" your data and manage open data projects ; |
| <img src="./backend/static/logos/logo_auth_microservice.png" height="33"> | **[TokTok](https://github.com/co-demos/toktok)** for a dedicated authentication service to manage users, JWT, and roles.  |
| <img src="./backend/static/logos/logo_openscraper_01.png" height="33"> | **[OpenScraper](https://github.com/entrepreneur-interet-general/OpenScraper)** is a generic web scraper serving the results of the scraping via its API  |


In the following illustration you can have a general idea of how those several services could work altogether. Check the [`/documentation/configurations`](./documentation/configurations) folder to have a broader look to [other configurations](./documentation/configurations/APIVIZ_CONFIGURATIONS-export.pdf).

<h2 align=center>
	<img src="./documentation/configurations/APIVIZ CONFIGURATIONS-export-details-light.jpg">
</h2>

You can also check those several projects and repository to find some layout for your specific new datavisualisation website : 
- Sonum repo ;
- CIS repo ;
- ... and more to come... 

**Note** : all the schemas were realized with [VUE - Visual Understanding Environment](https://vue.tufts.edu/index.cfm), an open source mind mapping tool. The source file for the schemas is [here](./documentation/configurations/APIVIZ_CONFIGURATIONS.vue)


--------

## INSTALLATION WALKTHROUGH 

<hr>

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




-------

## SCREENSHOTS (development)

------------

#### API RESPONSE (Sonum client configuration, 'global' collection)
serves your **[apiviz-backend](https://github.com/co-demos/apiviz-frontend)** configuration 
<h2 align=center>
	<img src="./documentation/screenshots/backend-api-global-01.png">
</h2>

--------

## THE APIVIZ ECOSYSTEM - DETAILED SCHEMA

<hr>

#### OPEN SOURCE SERVICES FOR A SOVEREIGN AND DECENTRALIZED DATA FLOW
In the following illustration you can grasp a more detailed comprehension of how every application of the ApiViz's "ecosystem" are in dialog one with the other : 

- **[TokTok](https://github.com/co-demos/toktok)** centralizes requests concerning user's authentication : 

    - login : given an email and a password responds with an `access_token` and a `refresh_token`
    - register an new user : 
    - modify an user :  
    - retrieves user's infos : 
    - confirm an `access_token` is authorized, valid, or not.
  <br>

- **[Solidata](https://github.com/entrepreneur-interet-general/solidata_frontend)** centralizes data management : 

    - stores data as open data projects.
    - "API-fy" your tabular data. 
    - allows distant modifications on data thanks to its backend API.
    - allows you to gather and normalize several datasets into a single open data project / dataset output.
<br>

- **Github/Gitlab repo** centralizes html pages, images and external scripts you'll need for your original wabapp : 

    - by storing your static contents on a Github/Gitlab repo, modifying a content for your online server doesn't need to change your app source code anymore, you just need to modify your html/images/scripts on Github/Gitlab, and a few minute after your content is changed directly online.
    - that way you can separate in your team those in charge to modify contents, and those in charge of code maintenance.
<br>

- **[Apiviz](https://github.com/co-demos/ApiViz)** gathers data and app configuration to display an original website : 

    - navbar configuration : define the logo, links, and menus in your apiviz instance's navabr. 
    - footer configuration : define the links present in the apiviz instance's footer.
    - styles configuration : define the CSS styles for your apiviz instance.
    - global configuration : define some metadata for your apiviz instance.
    - routes configuration : define the pages and routes of your apiviz instance, either statics contents or data views.
    - data endpoints configuration : define the data endpoints feeding your apiviz instance and the fields you want to display.

<hr>

#### GLOBAL BLUEPRINT - MAIN DATA FLOWS AND APPS SERVICES
<h2 align=center>
	<img src="./documentation/configurations/APIVIZ CONFIGURATIONS-export-details-full.jpg">
</h2>

---------

## DEPLOYMENT CONFIGURATIONS


<h2 align=center>
	<img src="./documentation/configurations/APIVIZ CONFIGURATIONS-export-legends.jpg">
</h2>

------

#### DEPLOYMENT AS FULL MUTUALIZED MICROSERVICES SYTEM
<h2 align=center>
	<img src="./documentation/configurations/APIVIZ CONFIGURATIONS-export-paas-D.jpg">
</h2>

------

#### DEPLOYMENT AS FULL CLIENT SOVEREIGNETY ON SERVICES 
<h2 align=center>
	<img src="./documentation/configurations/APIVIZ CONFIGURATIONS-export-server-C.jpg">
</h2>