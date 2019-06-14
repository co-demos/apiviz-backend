# -*- encoding: utf-8 -*-


from .. import app, os, PyMongo, log_app, pformat, json, json_util


# set as OK to run with app.context()
with app.app_context():

  mongo = PyMongo(app)

  log_app.info(">>> starting app --- MongoDB connected")

  ### access mongodb collections ###
  # mongo_users      = mongo.db[ app.config["MONGO_COLL_USERS"] ]
  mongo_config_global         = mongo.db[ app.config["MONGO_COLL_CONFIG_GLOBAL"] ]
  mongo_config_navbar         = mongo.db[ app.config["MONGO_COLL_CONFIG_NAVBAR"] ]
  mongo_config_tabs           = mongo.db[ app.config["MONGO_COLL_CONFIG_TABS"] ]
  mongo_config_data_endpoints = mongo.db[ app.config["MONGO_COLL_CONFIG_DATA_ENDPOINTS"] ]
  mongo_config_app_styles     = mongo.db[ app.config["MONGO_COLL_CONFIG_APP_STYLES"] ]
  mongo_config_routes         = mongo.db[ app.config["MONGO_COLL_CONFIG_ROUTES"] ]
  mongo_config_footer         = mongo.db[ app.config["MONGO_COLL_CONFIG_FOOTER"] ]
  mongo_config_socials        = mongo.db[ app.config["MONGO_COLL_CONFIG_SOCIALS"] ]
  # mongo_feedbacks  = mongo.db[ app.config["MONGO_COLL_FEEDBACKS"] ]
  # mongo_join_message_referenced_project_carrier = mongo.db[ app.config["MONGO_COLL_JOIN_MESSAGE_REFERENCED_PROJECT_CARRIER"] ]
  # mongo_join_message_not_referenced_project_carrier = mongo.db[ app.config["MONGO_COLL_JOIN_MESSAGE_NOT_REFERENCED_PROJECT_CARRIER"] ]
  # mongo_join_message_structures = mongo.db[ app.config["MONGO_COLL_JOIN_MESSAGE_STRUCTURES"] ]

  mongo_uuids_auth          = mongo.db[ app.config["MONGO_COLL_UUIDS_AUTH"] ]


  mongoColls = {
    # "users"  : mongo_users,
    app.config["MONGO_COLL_CONFIG_GLOBAL"]          : mongo_config_global,
    app.config["MONGO_COLL_CONFIG_NAVBAR"]          : mongo_config_navbar,
    app.config["MONGO_COLL_CONFIG_TABS"]            : mongo_config_tabs,
    app.config["MONGO_COLL_CONFIG_DATA_ENDPOINTS"]  : mongo_config_data_endpoints,
    app.config["MONGO_COLL_CONFIG_APP_STYLES"]      : mongo_config_app_styles,
    app.config["MONGO_COLL_CONFIG_ROUTES"]          : mongo_config_routes,
    app.config["MONGO_COLL_CONFIG_FOOTER"]          : mongo_config_footer,
    app.config["MONGO_COLL_CONFIG_SOCIALS"]         : mongo_config_socials,
    # app.config["MONGO_COLL_USERS"]                : mongo_users,
    # app.config["MONGO_COLL_FEEDBACKS"]            : mongo_feedbacks,
    app.config["MONGO_COLL_UUIDS_AUTH"]             : mongo_uuids_auth,

  }

mongoConfigColls ={
  "global"     : mongo_config_global,
  "navbar"     : mongo_config_navbar,
  "tabs"       : mongo_config_tabs,
  "endpoints"  : mongo_config_data_endpoints,
  "styles"     : mongo_config_app_styles,
  "routes"     : mongo_config_routes,
  "footer"     : mongo_config_footer,
  "socials"    : mongo_config_socials,

  "uuids_auth" : mongo_uuids_auth,
}

log_app.debug(">>> MongoDB / mongoColls.keys() : \n %s", pformat( mongoColls.keys() ) )

# log_app.info(">>> MongoDB : mongo_users     : \n %s", mongo_users  )
# log_app.info(">>> MongoDB : mongo_feedbacks   : \n %s", mongo_feedbacks  )


### - - - - - - - - - - - - - - - - - - - - - - - - - - - - ###
### CREATE DEFAULT GLOBAL CONFIG IF COLLECTION IS EMPTY
### - - - - - - - - - - - - - - - - - - - - - - - - - - - - ###
def setupDefaultConfig(collection, defaultList) :
  """ 
  main function to set up config collections
  """
  
  ### delete all previous default items in collection
  collection.delete_many({"is_default" : True }) 
  
  ### set up 
  for config_app_item in defaultList : 
    
    collection.insert(config_app_item)

### - - - - - - - - - - - - - - - - - - - - - - - - - - - - ###

from backend.config_app.config_app_global         import default_global_config
from backend.config_app.config_app_navbar         import default_app_navbar
from backend.config_app.config_app_tabs           import default_app_tabs
from backend.config_app.config_app_data_endpoints import default_data_endpoints_config
from backend.config_app.config_app_styles         import default_app_styles_config
from backend.config_app.config_app_routes         import default_routes_config
from backend.config_app.config_app_footer         import default_app_footer
from backend.config_app.config_app_socials        import default_socials_config

from backend.config_app.default_uuids_auth        import default_uuids_auth
log_app.debug(">>> MongoDB / default_uuids_auth : \n%s", pformat(default_uuids_auth) )

### retrieve default config for every collection
existing_app_config             = list( mongo_config_global.find({}) )
existing_app_navbar_config      = list( mongo_config_navbar.find({}) )
existing_app_tabs_config        = list( mongo_config_tabs.find({}) )
existing_data_endpoints_config  = list( mongo_config_data_endpoints.find({}) )
existing_app_styles_config      = list( mongo_config_app_styles.find({}) )
existing_routes_config          = list( mongo_config_routes.find({}) )
existing_app_footer_config      = list( mongo_config_footer.find({}) )
existing_socials_config         = list( mongo_config_socials.find({}) )

existing_uuids_auth             = list( mongo_uuids_auth.find({}) )

### setup every collection with default
setupDefaultConfig( mongo_config_global,         default_global_config )
setupDefaultConfig( mongo_config_navbar,         default_app_navbar )
setupDefaultConfig( mongo_config_tabs,           default_app_tabs )
setupDefaultConfig( mongo_config_data_endpoints, default_data_endpoints_config )
setupDefaultConfig( mongo_config_app_styles,     default_app_styles_config )
setupDefaultConfig( mongo_config_routes,         default_routes_config )
setupDefaultConfig( mongo_config_footer,         default_app_footer )
setupDefaultConfig( mongo_config_socials,        default_socials_config )

setupDefaultConfig( mongo_uuids_auth,            default_uuids_auth )

def backup_mongo_collection(coll, filepath) :
  """
  dumps all documents in collection in _backups_collections 
  """

  cursor      = coll.find({})
  backup_file = open(filepath, "w")
  backup_file.write('[')
  for document in cursor:
    backup_file.write(json.dumps(document,indent=4, default=json_util.default))
    backup_file.write(',')
  backup_file.write(']')

print 


# backup all collections when restart in ./_backups_collections
cwd = os.getcwd()
log_app.debug('>>> BACKUP MONGO COLLECITONS : cwd : %s', cwd )