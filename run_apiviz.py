# -*- encoding: utf-8 -*-

import os
import click 
from pprint import pprint, pformat
from dotenv import load_dotenv
from pathlib import Path  # python3 only

debug = True


@click.command()
@click.option('--mode',     default="default",     nargs=1,  help="The <mode> you need to run the app : default | testing | preprod | production" )
@click.option('--docker',   default="docker_off",  nargs=1,  help="Are you running the app with <docker> : docker_off | docker_on" )
@click.option('--mongodb',  default="local",       nargs=1,  help="The <mongodb> you need to run the app : local | distant | server" )
@click.option('--auth',     default="default",     nargs=1,  help="The <auth> mode you need to run the app : default | default_docker | server | server_docker | distant_preprod | distant_prod" )
@click.option('--host',     default="localhost",   nargs=1,  help="The <host> name you want the app to run on : <IP_NUMBER> " )
@click.option('--port',     default="8100",        nargs=1,  help="The <port> number you want the app to run on : <PORT_NUMBER>")
@click.option('--https',    default="false",       nargs=1,  help="The <https> mode you want the app to run on : true | false")
def app_runner(mode, docker, mongodb, auth, host, port, https) :
  """
  app_runner

  """

  print ("= "*50)
  print ("= = = RERUN FLASK APP FROM APP RUNNER = = =")
  print ("= "*50)


  ### WARNING : CLIck will treat every input as string as defaults values are string too
  print ("\n=== CUSTOM CONFIG FROM CLI ===\n")
  print ("=== mode    : ", mode)
  print ("=== docker  : ", docker)
  print ("=== mongodb : ", mongodb)
  print ("=== host    : ", host)
  print ("=== port    : ", port)
  print ("=== auth    : ", auth)
  print ("=== https   : ", https)

  ### READ ENV VARS DEPENDING ON MODE
  
  try :
    env_path_superAdmins = Path('.') / '.env.superadmins'
    if env_path_superAdmins.is_file() == False :
      raise FileNotFoundError 
    load_dotenv(env_path_superAdmins, verbose=True)
  except : 
    env_path_superAdmins = Path('.') / 'example.env.superadmins'
    load_dotenv(env_path_superAdmins, verbose=True)

  if mode in ['default', 'testing']:
    env_path_global = Path('.') / 'example.env.global'
  
    if mongodb in ['local'] : 
      env_path_mongodb = Path('.') / 'example.env.mongodb'
    else : 
      env_path_mongodb = Path('.') / '.env.mongodb'

  else : 
    env_path_global = Path('.') / '.env.global'
    env_path_mongodb = Path('.') / '.env.mongodb'

  load_dotenv(env_path_global, verbose=True)
  load_dotenv(env_path_mongodb, verbose=True)


  # if https == "true" : 
  #   http_mode = "https"
  # else : 
  #   http_mode = "http"

  ### apply / overwrites host configuration
  if mode != "default" : 
    print ("=== mode : ", mode)
    # os.environ["FLASK_CONFIGURATION"] = str(mode)
    os.environ["RUN_MODE"] = str(mode)
    # config_name = os.getenv('FLASK_CONFIGURATION', 'default') ### 'default' for local dev
    config_name = os.getenv('RUN_MODE', 'default') ### 'default' for local dev
    print ("=== config_name : ", config_name)

  ### OVERRIDE ENV VARS FROM CLI 
  os.environ["DOMAIN_ROOT"]   = host
  os.environ["DOMAIN_PORT"]   = port
  os.environ["DOCKER_MODE"]   = docker
  os.environ["MONGODB_MODE"]  = mongodb
  os.environ["AUTH_MODE"]     = auth

  # os.environ["SERVER_NAME"]   = host + ":" + port
  # os.environ["DOMAIN_NAME"]   = http_mode + "://" + host + ":" + port

  ### create app by importing app.__init__
  from backend import app

  print  ("= = = APP.CONFIG / to understand WTF is goin on ..." )
  pprint({ k:v for k,v in  app.config.items() } )
    
  ### simple flask runner
  print ("= = = STARTING app.run = = =")
  app.run( debug=debug, host=host, port=int(port), threaded=True )



if __name__ == '__main__':
  """ 
  runner for the CIS front Flask app 
  - gets most of its variables at start from environment variables
  - 

  in command line just type : 
  "python run_apiviz.py" + CLI args (optional)

  """

  app_runner()
