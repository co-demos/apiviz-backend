
import os

from .. import log_app, pformat


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

def formatEnvVar(var_name, format_type='boolean', separator=',') : 

  print("formatEnvVar / var_name : ", var_name)
  env_var = os.getenv(var_name)
  print("formatEnvVar / env_var : ", env_var)

  if format_type == 'boolean' : 
    if env_var in ['yes', 'Yes', 'YES', 'true', 'True', 'TRUE', '1'] : 
      return True
    else :
      return False
  
  elif format_type == 'integer' : 
    return int(env_var)

  elif format_type == 'float' : 
    return float(env_var)

  elif format_type == 'list' : 
    return env_var.split(separator)

  else : 
    if env_var in ['none', 'None', 'NONE', 'nan', 'Nan', 'NAN', 'null', 'Null','NULL', 'undefined'] : 
      return None
    else : 
      return env_var

### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

config_name    = os.getenv('FLASK_CONFIGURATION', 'default')
config_mongodb = os.getenv('MONGODB_MODE',        'local')
config_docker  = os.getenv('DOCKER_MODE',         'docker_off')
config_auth    = os.getenv('AUTH_MODE',           'default')

print
log_app.info("$ config_name : %s", config_name)  
log_app.info("$ config_mongodb : %s", config_mongodb)  
log_app.info("$ config_docker : %s", config_docker)  


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### READ ENV VARS / MONGO
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

MONGO_ROOT_LOCAL           = os.getenv('MONGO_ROOT_LOCAL',  'localhost') 
MONGO_ROOT_DOCKER          = os.getenv('MONGO_ROOT_DOCKER', 'host.docker.internal') 

MONGO_PORT_LOCAL           = os.getenv('MONGO_PORT_LOCAL', '27017') 

MONGO_ROOT_SERVER          = os.getenv('MONGO_ROOT_SERVER', '127.0.0.1') # IP depending on your server's mongoDB configuration
MONGO_PORT_SERVER          = os.getenv('MONGO_PORT_SERVER', '27017')
MONGO_USER_SERVER          = os.getenv('MONGO_USER_SERVER') 
MONGO_PASS_SERVER          = os.getenv('MONGO_PASS_SERVER') 
MONGO_OPTIONS_SERVER       = formatEnvVar('MONGO_OPTIONS_SERVER', format_type="value") # ""

MONGO_DISTANT_URI          = os.getenv('MONGO_DISTANT_URI') # "mongodb://<DISTANT-USERNAME>:<DISTANT-PASSWORD>@<DISTANT-HOST>:<DISTANT-PORT>"  
MONGO_DISTANT_URI_OPTIONS  = formatEnvVar('MONGO_DISTANT_URI_OPTIONS', format_type="value") # "?ssl=true&replicaSet=<REPLICA-SET>&authSource=admin&retryWrites=true"


# temporary dicts
mongodb_roots_dict = {
  "local"  : { 
    "docker_off" : MONGO_ROOT_LOCAL,  
    "docker_on"  : MONGO_ROOT_DOCKER  
  },
  "server" : { 
    "docker_off" : MONGO_ROOT_SERVER, 
    "docker_on"  : MONGO_ROOT_DOCKER  
  },
}

mongodb_ports_dict = {
  "local"  : MONGO_PORT_LOCAL,
  "server" : MONGO_PORT_SERVER,
}

mongodb_dbnames_dict = {
  "default"     : os.getenv("MONGO_DBNAME",         "apiviz"),
  "testing"     : os.getenv("MONGO_DBNAME_TEST",    "apiviz-test"),
  "preprod"     : os.getenv("MONGO_DBNAME_PREPROD", "apiviz-preprod"),
  "production"  : os.getenv("MONGO_DBNAME",         "apiviz-prod")
}

### get DB name
mongodb_dbname = mongodb_dbnames_dict[config_name]

### get MONGODB FULL URI 
### format : mongodb://<USER>:<PASSWORD>@<HOST>:<PORT>/<DBNAME>?<OPTIONS>

if config_mongodb == "distant" :
  mongodb_uri = "{}/{}{}".format(MONGO_DISTANT_URI, mongodb_dbname, MONGO_DISTANT_URI_OPTIONS)

else : 
  mongodb_root = mongodb_roots_dict[config_mongodb][config_docker]
  mongodb_port = mongodb_ports_dict[config_mongodb]

  ### get login if mongodb hosted on a server
  mongodb_login = "" 
  mongodb_options = "" 
  if config_name == "server" : 
    mongodb_login = "{}:{}@".format(MONGO_USER_SERVER, MONGO_PASS_SERVER)
    mongodb_options = MONGO_OPTIONS_SERVER ### must begin with "?"

  mongodb_uri = "mongodb://{}{}:{}/{}{}".format(mongodb_login, mongodb_root, mongodb_port, mongodb_dbname, mongodb_options)

log_app.debug(" --- MONGODB_URI : %s ", mongodb_uri) 
os.environ["MONGODB_URI"] = mongodb_uri 


class Config(object):
  
  """ BASIC Config Class """
  RUN_MODE = os.getenv("RUN_MODE")
  DEBUG = formatEnvVar('DEBUG', format_type='boolean')
 
  """ GLOBAL_FLASK """
  static_dir  = '/static'
  uploads_dir = '/static/uploads'

  # SITE_ROOT      = os.path.realpath(os.path.dirname(__file__))
  # SITE_STATIC    = SITE_ROOT   +  static_dir
  # SITE_UPLOADS  = SITE_ROOT   +  uploads_dir

  """ HOST """
  if config_docker != 'docker_on' :
    DOMAIN_ROOT      =  os.getenv("DOMAIN_ROOT")

    # DOMAIN_PORT      =  formatEnvVar("DOMAIN_PORT", format_type='integer')
    DOMAIN_PORT      =  os.getenv("DOMAIN_PORT")

    http_mode = "http"
    if formatEnvVar("HTTPS_MODE", format_type='boolean') == True : 
      http_mode = "https"
    os.environ["SERVER_NAME"]   = DOMAIN_ROOT + ":" + str(DOMAIN_PORT)
    os.environ["DOMAIN_NAME"]   = http_mode + "://" + DOMAIN_ROOT + ":" + str(DOMAIN_PORT)
    DOMAIN_NAME =  os.getenv("DOMAIN_NAME")
    
    # SERVER_NAME    =  os.getenv("SERVER_NAME")
    SERVER_NAME_TEST  = os.getenv("SERVER_NAME_TEST")
    if SERVER_NAME_TEST == "True" :
      SERVER_NAME    =  os.getenv("SERVER_NAME")

  """ SESSIONS """
  SECRET_KEY          = os.getenv("SECRET_KEY")
  
  """ MONGODB """
  MONGO_URI  = os.getenv("MONGODB_URI")
  MONGO_COLL_CONFIG_GLOBAL          = os.getenv('MONGO_COLL_CONFIG_GLOBAL', 'config_global') 
  MONGO_COLL_CONFIG_NAVBAR          = os.getenv('MONGO_COLL_CONFIG_NAVBAR', 'config_navbar') 
  MONGO_COLL_CONFIG_TABS            = os.getenv('MONGO_COLL_CONFIG_TABS',   'config_tabs') 
  MONGO_COLL_CONFIG_APP_STYLES      = os.getenv('MONGO_COLL_CONFIG_APP_STYLES',     'config_app_styles') 
  MONGO_COLL_CONFIG_DATA_ENDPOINTS  = os.getenv('MONGO_COLL_CONFIG_DATA_ENDPOINTS', 'config_data_endpoints') 
  MONGO_COLL_CONFIG_ROUTES          = os.getenv('MONGO_COLL_CONFIG_ROUTES',  'config_routes') 
  MONGO_COLL_CONFIG_FOOTER          = os.getenv('MONGO_COLL_CONFIG_FOOTER',  'config_footer') 
  MONGO_COLL_CONFIG_SOCIALS         = os.getenv('MONGO_COLL_CONFIG_SOCIALS', 'config_socials') 

  """ AUTH MODE """
  AUTH_MODE = os.getenv('AUTH_MODE')


### main function to configure app
def configure_app(app):
  """ configure Flask app from object created above """

  log_app.info("$ creating app.config from object...")
  app.config.from_object( Config )

  # log_app.info("$ app.config['RUN_MODE']  : %s ", app.config["RUN_MODE"] )
  # log_app.info("$ app.config['MONGO_DBNAME'] : %s ", app.config["MONGO_DBNAME"] ) 
  print