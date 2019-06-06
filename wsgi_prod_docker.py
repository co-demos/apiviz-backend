# -*- encoding: utf-8 -*-

"""
wsgi file to run app in production mode from gunicorn
"""

import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### ENV VARS
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
from dotenv import load_dotenv
from pathlib import Path  # python3 only
env_path_global = Path('.') / '.env.global'
env_path_mongodb = Path('.') / '.env.mongodb'
load_dotenv(env_path_global, verbose=True)
load_dotenv(env_path_mongodb, verbose=True)

### overide env var for Docker
os.environ["DOCKER_MODE"]	 = 'docker_on'

### READ ENV VARS
run=os.getenv('RUN_MODE', 'default')
docker=os.getenv('DOCKER_MODE', 'docker_off')
mongodb=os.getenv('MONGODB_MODE', 'local')

print ("= = = WSGI_DEV / run : ", run)
print ("= = = WSGI_DEV / docker : ", docker)
print ("= = = WSGI_DEV / mongodb : ", mongodb)


from backend import app, log_app


if __name__ == '__main__':
	"""
	runner for the CIS front Flask app
	- warning : gets most of its variables at start from environment variables

	in command line just type :
	"python wsgi_prod.py"
	or
	"gunicorn --bind 0.0.0.0:8100 --workers=1 wsgi_prod:app" for instance

	"""

	# set environment variable to set config later in config_app.config_env.py

	print ("= "*25)
	print ("= = = WSGI / RERUN FLASK APP = = =")
	log_app.info
	print ("= "*25)

	# simple flask runner
	app.run()
