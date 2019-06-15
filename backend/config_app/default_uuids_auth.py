from . import version, uuid_models

import  time, datetime
from    datetime import timedelta
from    datetime import date
from    pprint import pprint, pformat

from .config_env import formatEnvVar

APIVIZ_SUPER_ADMINS = formatEnvVar('SUPER_ADMIN_LIST', format_type="list", separator=",") 

uuid_auth_model = {
  
  "apiviz_front_uuid" : None,
  "apiviz_front_name" : None,
  "uuid_is_authorized" : True,
  "date_added" : None,
  "added_by" : {
    "name" : None,
    "email" : None,
  },

  "months_renewal" : 1,

  ### apiviz free/pro options
  "private_instance" : False,
  "apiviz_options" : {
    "datasets" : 1,
    "admins" : 1,
    "staff" : 1,
    "statics" : -1,
    "js_plugins" : True,
    "can_push_data" : False,
    "backoffice" : True,
    "users_management" : True,
    "options_management" : False,
  },

  "logs" : {
    "user_logs" : [],
    "total_logs" : 0,
    "view_logs" : {
      "static" : [],
      "map" : [],
      "list" : [],
      "stat" : [],
      "table" : [],
      "backoffice" : [],
    }
  },

  "auth_role_users" : {
    "admin_list" : [], ### 
    "staff_list" : [], ###
    "guest_list" : [], ###
  },

  "is_default" : False,
}



default_uuids_auth = [
]

for key, val in uuid_models.items() : 

  ### copy uuid_auth_model
  temp_auth = uuid_auth_model.copy()
  # print ("... temp_auth : \n", pformat(temp_auth))

  ### setting main specs
  temp_auth["apiviz_front_name"] = key
  temp_auth["apiviz_front_uuid"] = val

  ### setting options
  temp_auth["private_instance"] = False
  temp_auth["months_renewal"] = 120

  temp_auth["apiviz_options"]["datasets"] = 3
  temp_auth["apiviz_options"]["admins"] = 1
  temp_auth["apiviz_options"]["staff"] = 5
  temp_auth["apiviz_options"]["statics"] = -1
  temp_auth["apiviz_options"]["js_plugins"] = True
  temp_auth["apiviz_options"]["can_push_data"] = True
  temp_auth["apiviz_options"]["backoffice"] = True
  temp_auth["apiviz_options"]["users_management"] = True
  temp_auth["apiviz_options"]["options_management"] = True

  ### setting admin list
  temp_auth["auth_role_users"]["admin_list"] = APIVIZ_SUPER_ADMINS

  ### define as default model
  temp_auth["is_default"] = True
  
  ### setting added infos
  temp_auth["date_added"] = datetime.datetime.now()
  temp_auth["added_by"] = {
    "name" : "system",
    "email" : APIVIZ_SUPER_ADMINS[0],
  }

  # print ("... temp_auth : \n", pformat(temp_auth))

  ### append to list to add / renew in mongodb
  default_uuids_auth.append(temp_auth)
