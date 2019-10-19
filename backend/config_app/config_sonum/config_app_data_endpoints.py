# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_data_endpoints_config = [

  ### - - - - - - - - - - - - - - - ###
  ### CONFIG SONUM 
    
    ### - - - - - - - - - - - - - - - ###
    ### USER MANAGEMENT
    ### - - - - - - - - - - - - - - - ###

      ### AUTH ROOT URLS
      { "field"          : "app_data_API_root_auth",
        "data_type"      : "user",
        "endpoint_type"  : "auth_root",
        "content"        : u"apiviz default API endpoint for user authentication (root urls)",
        "auth_activated" : True,
        "root_url"       : {
          ### needs a local instance of toktok if not changed
          "default"         : "http://localhost:4100/api",            # toktok instance on local machine
          "default_docker"  : "http://host.docker.internal:4100/api", # toktok instance on local machine + docker
          ### on server ...
          "server"          : "http://localhost:4100/api",            # toktok instance on server
          "server_docker"   : "http://host.docker.internal:4100/api", # toktok instance on server + docker
          "distant_preprod" : "https://preprod.toktok-auth.com/api",
          "distant_prod"    : "https://toktok-auth.com/api"
        },
        "args_options"   : [
        ],
        "request_header_auth_options" : [
          { "header_field" : u"Accept",        "header_value" : "application/json", "is_var" : False, "app_var_name" : None,    "header_value_prefix" : None },
          { "header_field" : u"Content-type",  "header_value" : "application/json", "is_var" : False, "app_var_name" : None,    "header_value_prefix" : None },
          { "header_field" : u"Authorization", "header_value" : None,               "is_var" : True,  "app_var_name" : "token", "header_value_prefix" : None },
        ],
        "app_version"    : version,
        "method"         : "GET",
        "help"           : u"define the endpoints for authentication",
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"     : True
      },

      ### CONFIRM JWT
      { "field"         : "app_data_API_user_auth",
        "data_type"     : "user",
        "endpoint_type" : "confirm_jwt",
        "content"       : u"apiviz default API endpoint for user authentication (confirm acces)",
        "root_url"      : "/auth/tokens/confirm_access",
        "args_options"  : [
          { "app_arg" : "authToken", "arg" : "token", "optional" : False, "in" : ["url","header"], "default" : "", "type" : "str" },
        ],
        "resp_fields" : {
          "access_token"  : { "path" : "tokens/access_token" },
          "refresh_token" : { "path" : "tokens/refresh_token" },
          "msg"           : { "path" : "msg" },
          "user_role"     : { "path" : "data/auth/role" },
          "user_id"       : { "path" : "data/_id" },
          "user_name"     : { "path" : "data/infos/name" },
          "user_surname"  : { "path" : "data/infos/surname" },
          "user_pseudo"   : { "path" : "data/infos/pseudo"  },
          "user_email"    : { "path" : "data/infos/email" },
        },
        "roles" : { 
          ### defining roles in frontend
          "admin"     : { "resp_role" : "admin",     "help" : "can access all backoffice (lox level access)" },
          "staff"     : { "resp_role" : "staff",     "help" : "can access backoffice (high level access)" },
          "registred" : { "resp_role" : "registred", "help" : "registred user" },
          "guest"     : { "resp_role" : "guest",     "help" : "logged but not registred" },
          "anonymous" : { "resp_role" : "anonymous", "help" : "logged as anonymous" },
        },
        "app_version"   : version,
        "method"        : "GET",
        "help"          : u"define the endpoint for a JWT check",
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"    : True
      },

      ### NEW ACCESS JWT
      { "field"         : "app_data_API_user_new_access_token",
        "data_type"     : "user",
        "endpoint_type" : "new_access_token",
        "content"       : u"apiviz default API endpoint for user authentication (new acces token) : needs a valid refresh token as token ",
        "root_url"      : "/auth/tokens/new_access_token",
        "args_options"  : [
          { "app_arg" : "authToken", "arg" : "token", "optional" : False, "in" : ["url","header"], "default" : "", "type" : "str" },
        ],
        "app_version"   : version,
        "method"        : "GET",
        "help"          : u"define the endpoint for a new access JWT ",
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"    : True
      },

      ### REGISTER
      { "field"         : "app_data_API_user_register",
        "data_type"     : "user",
        "endpoint_type" : "register",
        "content"       : u"apiviz default API endpoint for registering a new user",
        "root_url"      : "/usr/register",
        "args_options"  : [
          { "app_arg" : "name",      "arg" : "name",      "optional" : False, "in" : ["payload"], "default" : "", "type" : "str" },
          { "app_arg" : "surname",   "arg" : "surname",   "optional" : False, "in" : ["payload"], "default" : "", "type" : "str" },
          { "app_arg" : "email",     "arg" : "email",     "optional" : False, "in" : ["payload"], "default" : "", "type" : "str" },
          { "app_arg" : "password",  "arg" : "pwd",       "optional" : False, "in" : ["payload"], "default" : "", "type" : "str" },
          { "app_arg" : "agreement", "arg" : "agreement", "optional" : False, "in" : ["payload"], "default" : "", "type" : "str" },
          { "app_arg" : "locale",    "arg" : "lang",      "optional" : False, "in" : ["payload"], "default" : "", "type" : "str" },
          { "app_arg" : "u_data",    "arg" : "u_data",    "optional" : False, "in" : ["payload"], "default" : "", "type" : "str" },
        ],
        "resp_fields" : {
        },
        "app_version"   : version,
        "method"        : "POST",
        "help"          : u"define the endpoint for registering a new user",
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "needs_form"    : True,
        "is_default"    : True
      },

      ### LOGIN
      { "field"         : "app_data_API_user_login",
        "data_type"     : "user",
        "endpoint_type" : "login",
        "content"       : u"apiviz default API endpoint for login",
        "root_url"      : "/auth/login",
        "args_options"  : [
          { "app_arg" : "email",    "arg" : "email", "optional" : False, "in" : ["payload"], "default" : "", "type" : "str" },
          { "app_arg" : "password", "arg" : "pwd",   "optional" : False, "in" : ["payload"], "default" : "", "type" : "str" },
        ],
        "resp_fields" : {
        },
        "app_version"   : version,
        "method"        : "POST",
        "help"          : u"define the endpoint for login an user",
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "needs_form"    : True,
        "is_default"    : True
      },

      ### USER LIST
      { "field"         : "app_data_API_user_list",
        "data_type"     : "user",
        "endpoint_type" : "user_modif",
        "content"       : u"apiviz default API endpoint for users list",
        "root_url"      : "/usr/infos/list",
        "args_options"  : [
          { "app_arg" : "authToken",    "arg" : "token",    "optional" : False,  "in" : ["url","header"],  "default" : "", "type" : "str" },
          { "app_arg" : "pageUser",     "arg" : "page_n",   "optional" : True,   "in" : ["url"],           "default" : 1,   "type": "int" },
          { "app_arg" : "perPageUser",  "arg" : "per_page", "optional" : True,   "in" : ["url"],           "default" : 50, "type": "int" },
        ],
        "resp_fields" : {
        },
        "app_version"   : version,
        "method"        : "GET",
        "help"          : u"define the endpoint to get data for : an user ",
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"    : True
      },

      ### USER INFOS
      { "field"         : "app_data_API_user_infos",
        "data_type"     : "user",
        "endpoint_type" : "user_modif",
        "content"       : u"apiviz default API endpoint for user infos",
        "root_url"      : "/usr/infos/get_one",
        "args_options"  : [
          { "app_arg" : "authToken", "arg" : "token",  "optional" : False, "in" : ["url","header"],   "default" : "", "type" : "str" },
          { "app_arg" : "userID",    "arg" : "doc_id", "optional" : True,   "in" : ["url"],           "default" : "", "type" : "str"}
        ],
        "resp_fields" : {
        },
        "app_version"   : version,
        "method"        : "GET",
        "help"          : u"define the endpoint to get data for : an user ",
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"    : True
      },

      ### USER EDIT
      { "field"         : "app_data_API_user_edit",
        "data_type"     : "user",
        "endpoint_type" : "user_modif",
        "content"       : u"apiviz default API endpoint for editing an user",
        "root_url"      : "/auth/edit/",
        "args_options"  : [
          { "app_arg" : "authToken", "arg" : "token",  "optional" : False, "in" : ["url","header"],   "default" : "", "type" : "str" },
          { "app_arg" : "userID",    "arg" : "doc_id", "optional" : True,   "in" : ["url"],           "default" : "", "type" : "str"}
        ],
        "resp_fields" : {
        },
        "app_version"   : version,
        "method"        : "PUT",
        "help"          : u"define the endpoint to get data for : an user ",
        "needs_form"    : True,
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"    : True
      },

      ### USER DELETE
      { "field"         : "app_data_API_user_delete",
        "data_type"     : "user",
        "endpoint_type" : "user_modif",
        "content"       : u"apiviz default API endpoint for deleting an user",
        "root_url"      : "/auth/edit/",
        "args_options"  : [
          { "app_arg" : "authToken", "arg" : "token",  "optional" : False, "in" : ["url","header"],   "default" : "", "type" : "str" },
          { "app_arg" : "userID",    "arg" : "doc_id", "optional" : True,   "in" : ["url"],           "default" : "", "type" : "str"}
        ],
        "resp_fields" : {
        },
        "app_version"   : version,
        "method"        : "DELETE",
        "help"          : u"define the endpoint to get data for : an user ",
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"    : True
      },

      ### USER FORGOT PWD
      { "field"         : "app_data_API_forgot_pwd",
        "data_type"     : "user",
        "endpoint_type" : "user_modif",
        "content"       : u"apiviz default API endpoint for changing password",
        "root_url"      : "/auth/password/password_forgotten",
        "args_options"  : [
          { "app_arg" : "authToken", "arg" : "token",  "optional" : False, "in" : ["url","header"],   "default" : "", "type" : "str" },
        ],
        "resp_fields" : {
        },
        "app_version"   : version,
        "method"        : "GET",
        "help"          : u"define the endpoint to get data for : an user ",
        "needs_form"    : True,
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"    : True
      },

    ### - - - - - - - - - - - - - - - ###
    ### DATA ENDPOINTS
    ### - - - - - - - - - - - - - - - ###

      ####### SONUM / CARTO #######

        ### DATA FILTERS
        { "field"         : "sonum_carto_data_API_filters",
          "is_visible"    : True,
          "is_disabled"   : False,
          "data_type"     : "data",
          "endpoint_type" : "filters",
          "dataset_uri"   : "sonum-carto",
          "available_views" : ['VIEW_LIST', 'VIEW_MAP', 'VIEW_STATS'],
          "has_shuffle"  : False,
          "has_pagination" : False,
          "has_export" : True,
          "pagination_options" : {
            "per_page" : [ 5, 10, 25, 100 ],
          },
          "has_infinite_scroll" : True,
          "has_order_by" : False,
          "order_by_options" : {
            "order_by_list" : [],
          },

          "placeholder"   : [
            {"locale" : "en", "text" : "Enter a place, a project name..."},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Tapez le nom d'un lieu" },

          ],
          "items_found"   : [
            {"locale" : "en", "text" : "places found"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "lieux trouvés" },
          ],
          "stats_text"   : [
            {"locale" : "en", "text" : "experimental"},{"locale" : "es", "text" : "experimental"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "expérimental" }
          ],
          "reset"   : [
            {"locale" : "en", "text" : "reset"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "effacer" },

          ],

          "content"       : u"apiviz default API endpoint for navbar filters",
          "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c89636d328ed70609be03ab",
          "args_options"  : [
            {  "app_arg" : "dataToken",      "arg" : "token",             "optional" : True, "in" : ["url","header"],   "default" : "",   "type": "str" },
            {  "app_arg" : "filtersList",    "arg" : "get_filters",       "optional" : False, "in" : ["url"],           "default" : True, "type": "bool" },
            {  "app_arg" : "filterChoices",  "arg" : "get_uniques",       "optional" : False, "in" : ["url"],           "default" : "tag", "type": "str" },
          ],

          "filter_options" : [
            { "name"		: u"coding services__",
              "id"      : "filter_1", 
              "col_name" : "coding services",
              "dataType" : "text",
              "filter_title" : [{"locale" : "en", "text" : "Coaching methods"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Modalités d'accompagnement" }],
              "choices"	: [
                {"name" : u"ACC", "choice_title" : [{"locale" : "en", "text" : "coaching"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "accompagnement" }]},
                {"name" : u"FOR", "choice_title" : [{"locale" : "en", "text" : "training"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "formation" }]},
                {"name" : u"ACL", "choice_title" : [{"locale" : "en", "text" : "free access"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "accès libre" }]},
                {"name" : u"NR",  "choice_title" : [{"locale" : "en", "text" : "not specified"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "non renseigné" }]},
              ]
            },
            { "name"		: u"coding jours__",
              "id"      : "filter_2", 
              "col_name" : "coding jours",
              "dataType" : "text",
              "filter_title" : [{"locale" : "en", "text" : "Opening days"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Jours d'ouverture" }],
              "choices"	: [
                {"name" : u"lu", "choice_title" : [{"locale" : "en", "text" : "monday"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "lundi" }]},
                {"name" : u"ma", "choice_title" : [{"locale" : "en", "text" : "tuesday"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "mardi" }]},
                {"name" : u"me", "choice_title" : [{"locale" : "en", "text" : "wednesday"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "mercredi" }]},
                {"name" : u"je", "choice_title" : [{"locale" : "en", "text" : "thursday"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "jeudi" }]},
                {"name" : u"ve", "choice_title" : [{"locale" : "en", "text" : "friday"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "vendredi" }]},
                {"name" : u"sa", "choice_title" : [{"locale" : "en", "text" : "saturday"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "samedi" }]},
                {"name" : u"di", "choice_title" : [{"locale" : "en", "text" : "sunday"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "dimanche" }]},
              ]
            },
            {	"name"		: u"source__",
              "id"      : "filter_3", 
              "col_name" : "source",
              "dataType" : "text",
              "filter_title" : [{"locale" : "en", "text" : "Sources"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Sources" }],
              "choices"	: [
                {"name" : u"APTIC",            "choice_title" : [{"locale" : "en", "text" : "APTIC"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "APTIC" }]},
                {"name" : u"Gironde",          "choice_title" : [{"locale" : "en", "text" : "Gironde"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Gironde" }]},
                {"name" : u"Hauts de France",  "choice_title" : [{"locale" : "en", "text" : "Hauts de France"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Hauts de France" }]},
                {"name" : u"Loire-Atlantique", "choice_title" : [{"locale" : "en", "text" : "Loire-Atlantique"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Loire-Atlantique" }]},
                {"name" : u"MSAP",             "choice_title" : [{"locale" : "en", "text" : "MSAP"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "MSAP" }]},
                {"name" : u"NetPublic",        "choice_title" : [{"locale" : "en", "text" : "NetPublic"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "NetPublic" }]},
              ], 
            },

          ],
          "app_version"    : version,
          "method"        : "GET",
          "help"          : u"define the endpoint to get data for : filters in search navbar",
          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"    : True
        },

        ### DATA LIST
        { "field"         : "sonum_carto_data_API_list",
          "is_visible"    : True,
          "is_disabled"   : False,
          "data_type"     : "data",
          "endpoint_type" : "list",
          "dataset_uri"   : "sonum-carto",
          "content"       : u"apiviz default API endpoint for list results",
          "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c89636d328ed70609be03ab",
          "args_options"  : [
            {  "app_arg" : "dataToken",  "arg" : "token",            "optional" : True, "in" : ["url","header"], "default" : "", "type": "str" },
            {  "app_arg" : "page",       "arg" : "page_n",           "optional" : True, "in" : ["url"],           "default" : 1,   "type": "int" },
            {  "app_arg" : "perPage",    "arg" : "per_page",         "optional" : True, "in" : ["url"],           "default" : 100, "type": "int" },
            {  "app_arg" : "query",      "arg" : "search_for",       "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
            {  "app_arg" : "filters",    "arg" : "search_filters",   "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
            {  "app_arg" : "shuffleSeed","arg" : "shuffle_seed",     "optional" : True, "in" : ["url"],           "default" : 0 , "type": "int" },
            # {  "app_arg" : "descending","arg" : "descending",     "optional" : True, "in" : ["url"],           "default" : False , "type": "bool" },

          ],
          "resp_fields" : {
            "projects" : { "resp_format" : "dict", "path" : "data/data_raw/f_data" },
            "total" :    { "resp_format" : "int",  "path" : "data/data_raw/f_data_count" },
          },
          "app_version"    : version,
          "method"        : "GET",
          "help"          : u"define the endpoint to get data for : a view list",
          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"    : True
        },

        ### DATA DETAIL
        { "field"         : "sonum_carto_data_API_detail",
          "is_visible"    : True,
          "is_disabled"   : False,
          "data_type"     : "data",
          "endpoint_type" : "detail",
          "dataset_uri"   : "sonum-carto",
          "content"       : u"apiviz default API endpoint for detailled results",
          "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c89636d328ed70609be03ab",
          "args_options"  : [
            {  "app_arg" : "dataToken",  "arg" : "token",     "optional" : True,  "in" : ["url","header"],   "default" : "", "type": "str" },
            {  "app_arg" : "itemId",     "arg" : "item_id",   "optional" : False, "in" : ["url"],           "default" : "", "type": "str" },
          ],
          "resp_fields" : {
            "projects" : { "resp_format" : "dict", "path" : "data/data_raw/f_data" },
            "total" :    { "resp_format" : "int",  "path" : "data/data_raw/f_data_count" },
          },
          "app_version"    : version,
          "method"        : "GET",
          "help"          : u"define the endpoint to get data for : a detailled data",
          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"    : True
        },

        ### DATA STATS
        { "field"         : "sonum_carto_data_API_stats",
          "is_visible"    : True,
          "is_disabled"   : False,
          "data_type"     : "data",
          "endpoint_type" : "stat",
          "dataset_uri"   : "sonum-carto",
          "content"       : u"apiviz default API endpoint for stats results",
          
          "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one_stats/5c89636d328ed70609be03ab",
          # "root_url"      : "http://localhost:4000/api/dso/infos/get_one_stats/5d1936d48626a07bb258d1c6",
          
          "args_options"  : [
            {  "app_arg" : "dataToken", "arg" : "token",          "optional" : True, "in" : ["url","header"], "default" : "", "type": "str" },
            {  "app_arg" : "query",     "arg" : "search_for",     "optional" : True, "in" : ["url"],          "default" : "", "type": "str" },
            {  "app_arg" : "filters",   "arg" : "search_filters", "optional" : True, "in" : ["url"],          "default" : "", "type": "str" },
          ],
          
          "payload_options" : {

            # "payload_format" : "list",

            "payload_queries" : [
              { 
                "serie_id" : "sonum-carto-stat-bar-horiz",
                "agg_fields" : [
                  { 
                    "agg_field" : "source",
                    "agg_sum_type" : "count_items", 
                    "agg_needs_unwind" : False,
                    "agg_unwind_separator" : "-"
                  },
                  { 
                    # "agg_field" : "code services",
                    "agg_field" : "coding services",
                    "agg_sum_type" : "count_items",
                    "agg_needs_unwind" : True,
                    "agg_unwind_separator" : "-" 
                  }  
                ]
              },
              { 
                "serie_id" : "sonum-carto-stat-donut",
                "agg_fields" : [
                  { 
                    "agg_field" : "source",
                    "agg_sum_type" : "count_items", 
                    "agg_needs_unwind" : False,
                    "agg_unwind_separator" : "-"
                  }
                ]
              },
            ],
          },
          "resp_fields" : {
            "stats"      : { "resp_format" : "dict", "path" : "series" },
            # "projects"   : { "resp_format" : "dict", "path" : "data" },
            # "dimensions" : { 
            #   "quantity"    : { "resp_format" : "int", "path" : "data/count", "label" : "" },
            #   "dimension_A" : { "resp_format" : "str", "path" : "data/_id",   "label" : "" },
            #   "dimension_B" : { "resp_format" : "str", "path" : "data/count", "label" : "" },
            # },
            # "total"      : { "resp_format" : "int",  "path" : "/" },
          },

          "app_version"   : version,
          "method"        : "POST",
          "help"          : u"define the endpoint to get data for : a stat about the dataset",
          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"    : True
        },

        ### DATA MAP
        { "field"         : "sonum_carto_data_API_map",
          "is_visible"    : True,
          "is_disabled"   : False,
          "data_type"     : "data",
          "endpoint_type" : "map",
          "dataset_uri"   : "sonum-carto",

          "map_options"   : {

            ### TO ADAPT TO MAPBOX-GL-JS OPTIONS
            "url"              : "https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png",
            "attribution"      : '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
            "subdomains"       : 'abcd',
            "center"           : [46.2276, 2.2137],
            "currentCenter"    : [46.2276, 2.2137],
            "zoom"             : 6,
            "maxZoom"          : 18,
            "minZoom"          : 3,
            "useMarkerCluster" : True,
            "pinIconUrl"       : "/static/icons/icon_pin_plein_violet.svg",
            "pinIconSize"      : { "highlighted" : [46, 46], "normal" : [29, 29]}

          },
          
          "content"       : u"apiviz default API endpoint for map results",
          "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c89636d328ed70609be03ab",
          # "root_url"      : "http://localhost:4000/api/dso/infos/get_one/5c89636d328ed70609be03ab",
          "args_options"  : [
            {  "app_arg" : "dataToken",  "arg" : "token",            "optional" : True, "in" : ["url","header"], "default" : "",   "type": "str" },

            {  "app_arg" : "forMap",     "arg" : "map_list",         "optional" : False, "in" : ["url"],         "default" : True, "type": "bool" },
            # {  "app_arg" : "asLatLng", "arg" : "as_latlng",        "optional" : False, "in" : ["url"],         "default" : True, "type": "bool" },
            {  "app_arg" : "onlyGeocoded", "arg" : "only_geocoded",  "optional" : False, "in" : ["url"],         "default" : True, "type": "bool" },

            # {  "app_arg" : "page",       "arg" : "page_n",           "optional" : True, "in" : ["url"],          "default" : 1,    "type": "int" },
            # {  "app_arg" : "perPage",    "arg" : "per_page", "optional" : True, "in" : ["url"],          "default" : 100,  "type": "int" },
            {  "app_arg" : "query",      "arg" : "search_for",       "optional" : True, "in" : ["url"],          "default" : "",   "type": "str" },
            {  "app_arg" : "filters",    "arg" : "search_filters",   "optional" : True, "in" : ["url"],          "default" : "",   "type": "str" },
            {  "app_arg" : "itemId",     "arg" : "item_id",          "optional" : True, "in" : ["url"],          "default" : "",   "type": "str" },

          ],
          "resp_fields" : {
            "projects" : { "resp_format" : "dict", "path" : "data/data_raw/f_data" },
            "total" :    { "resp_format" : "int",  "path" : "data/data_raw/f_data_count" },
          },
          "app_version"    : version,
          "method"        : "GET",
          "help"          : u"define the endpoint to get data for : map results",
          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"    : True
        },

        ### DATA EXPORT
        { "field"         : "sonum_carto_data_API_export",
          "is_visible"    : True,
          "is_disabled"   : False,
          "data_type"     : "data",
          "endpoint_type" : "export",
          "dataset_uri"   : "sonum-carto",
          "content"       : u"apiviz default API endpoint for export results",
          "root_url"      : "https://solidata-api.co-demos.com/api/dso/exports/as_csv/5c89636d328ed70609be03ab", ## V2
          "args_options"  : [
            {  "app_arg" : "dataToken",  "arg" : "token",            "optional" : True, "in" : ["url","header"],  "default" : "", "type": "str" },
            # {  "app_arg" : "page",       "arg" : "page_n",           "optional" : True, "in" : ["url"],           "default" : 1,  "type": "int" },
            # {  "app_arg" : "perPage",    "arg" : "per_page",         "optional" : True, "in" : ["url"],           "default" : 300, "type": "int" },
            # {  "app_arg" : "query",      "arg" : "search_for",       "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
            # {  "app_arg" : "filters",    "arg" : "search_filters",   "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
            # {  "app_arg" : "shuffleSeed","arg" : "shuffle_seed",     "optional" : True, "in" : ["url"],           "default" : 205 , "type": "int" },
          ],
          "resp_fields" : {
            # "projects" : { "resp_format" : "list", "path" : "data/data_raw/f_data" },
            # "total" :    { "resp_format" : "int",  "path" : "data/data_raw/f_data_count" },
          },
          "app_version"    : version,
          "method"        : "GET",
          "help"          : u"define the endpoint to get data for : export dataset as csv",
          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"    : True
        },

      ####### SONUM / XP #######

        ### DATA FILTERS
        { "field"         : "sonum_xp_data_API_filters",
          "is_visible"    : True,
          "is_disabled"   : False,
          "data_type"     : "data",
          "endpoint_type" : "filters",
          "dataset_uri"   : "sonum-xp",
          "available_views" : ['VIEW_LIST', 'VIEW_MAP'],
          "has_shuffle"  : False,
          "has_pagination" : False,
          "has_export" : True,
          "pagination_options" : {
            "per_page" : [ 5, 10, 25, 100 ],
          },
          "has_infinite_scroll" : True,
          "has_order_by" : False,
          "order_by_options" : {
            "order_by_list" : [],
          },

          "placeholder"   : [
            {"locale" : "en", "text" : "Enter the name of an initiative"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Tapez le nom d'une initiative" }
          ],
          "items_found"   : [
            {"locale" : "en", "text" : "initiatives found"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "initiatives trouvées" }
          ],
          "reset"   : [
            {"locale" : "en", "text" : "reset"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "effacer" }
          ],

          "content"       : u"apiviz default API endpoint for navbar filters",
          "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7ebc7d328ed724cebd7fc0",
          "args_options"  : [
            {  "app_arg" : "dataToken",      "arg" : "token",             "optional" : True, "in" : ["url","header"],   "default" : "",   "type": "str" },
            {  "app_arg" : "filtersList",    "arg" : "get_filters",       "optional" : False, "in" : ["url"],           "default" : True, "type": "bool" },
            {  "app_arg" : "filterChoices",  "arg" : "get_uniques",       "optional" : False, "in" : ["url"],           "default" : "tag", "type": "str" },
          ],

          "filter_options" : [

            { "name"		: u"type structure__", 
              "id"      : "filter_1",
              "col_name" : "type structure",
              "dataType" : "text",
              "filter_title" : [{"locale" : "en", "text" : "Structure type"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Type de structure" }],
              "choices"	: [
                {"name" : u"structure publique (CCAS, CIAS, bibliothèque, etc...)", "choice_title" : [{"locale" : "en", "text" : "public structure"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "structure publique" }]},
                {"name" : u"collectivité territoriale/EPCI",                        "choice_title" : [{"locale" : "en", "text" : "local government"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "collectivité territoriale/EPCI" }]},

              ]
            },
            { "name"		: u"thématique__", 
              "id"      : "filter_2",
              "col_name" : "thématique",
              "dataType" : "text",
              "filter_title" : [{"locale" : "en", "text" : "Topics"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Thématique" }],
              "choices"	: [
                {"name" : u"INCNUM", "choice_title" : [{"locale" : "en", "text" : "digital inclusion"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "inclusion numérique" }]},
                {"name" : u"DEMPAR", "choice_title" : [{"locale" : "en", "text" : "participative democracy"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "démocratie participative" }]},
                {"name" : u"FORNUM", "choice_title" : [{"locale" : "en", "text" : "formation to digital"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "formation aux métiers du numérique" }]},
                {"name" : u"POLOUV", "choice_title" : [{"locale" : "en", "text" : "opan data policicy"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "politique d'ouverture des données" }]},
                {"name" : u"MEDNUM", "choice_title" : [{"locale" : "en", "text" : "digital mediation"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "médiation numérique" }]},
                {"name" : u"FORAGP", "choice_title" : [{"locale" : "en", "text" : "public servannts training"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "formation d'agents publics" }]},
                {"name" : u"TERINT", "choice_title" : [{"locale" : "en", "text" : "smart territories"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "territoire intelligent" }]},
                {"name" : u"CULNUM", "choice_title" : [{"locale" : "en", "text" : "digital culture"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "culture numérique" }]},
                {"name" : u"TIELIE", "choice_title" : [{"locale" : "en", "text" : "third places"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "tiers lieux" }]},
                {"name" : u"COMMUN", "choice_title" : [{"locale" : "en", "text" : "digital commons"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "communs numériques" }]},
                {"name" : u"DATLIT", "choice_title" : [{"locale" : "en", "text" : "data literacy"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "data literacy" }]},
                {"name" : u"AUTRES", "choice_title" : [{"locale" : "en", "text" : "other"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "autre" }]},
              ]
            },


          ],
          "app_version"    : version,
          "method"        : "GET",
          "help"          : u"define the endpoint to get data for : filters in search navbar",
          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"    : True
        },

        ### DATA LIST
        { "field"         : "sonum_xp_data_API_list",
          "is_visible"    : True,
          "is_disabled"   : False,
          "data_type"     : "data",
          "endpoint_type" : "list",
          "dataset_uri"   : "sonum-xp",
          "content"       : u"apiviz default API endpoint for list results",
          "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7ebc7d328ed724cebd7fc0",
          "args_options"  : [
            {  "app_arg" : "dataToken",  "arg" : "token",            "optional" : True, "in" : ["url","header"], "default" : "", "type": "str" },
            {  "app_arg" : "page",       "arg" : "page_n",           "optional" : True, "in" : ["url"],           "default" : 1,   "type": "int" },
            {  "app_arg" : "perPage",    "arg" : "per_page",         "optional" : True, "in" : ["url"],           "default" : 100, "type": "int" },
            {  "app_arg" : "query",      "arg" : "search_for",       "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
            {  "app_arg" : "filters",    "arg" : "search_filters",   "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
            {  "app_arg" : "shuffleSeed","arg" : "shuffle_seed",     "optional" : True, "in" : ["url"],           "default" : 0 , "type": "int" },
          ],
          "resp_fields" : {
            "projects" : { "resp_format" : "dict", "path" : "data/data_raw/f_data" },
            "total" :    { "resp_format" : "int",  "path" : "data/data_raw/f_data_count" },
          },
          "app_version"   : version,
          "method"        : "GET",
          "help"          : u"define the endpoint to get data for : a view list",
          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"    : True
        },

        ### DATA DETAIL
        { "field"         : "sonum_xp_data_API_detail",
          "is_visible"    : True,
          "is_disabled"   : False,
          "data_type"     : "data",
          "endpoint_type" : "detail",
          "dataset_uri"   : "sonum-xp",
          "content"       : u"apiviz default API endpoint for detailled results",
          "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7ebc7d328ed724cebd7fc0",
          "args_options"  : [
            {  "app_arg" : "dataToken",  "arg" : "token",     "optional" : True,  "in" : ["url","header"],   "default" : "", "type": "str" },
            {  "app_arg" : "itemId",     "arg" : "item_id",   "optional" : False, "in" : ["url"],           "default" : "", "type": "str" },
          ],
          "resp_fields" : {
            "projects" : { "resp_format" : "dict", "path" : "data/data_raw/f_data" },
            "total" :    { "resp_format" : "int",  "path" : "data/data_raw/f_data_count" },
          },
          "app_version"    : version,
          "method"        : "GET",
          "help"          : u"define the endpoint to get data for : a detailled data",
          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"    : True
        },

        ### DATA STATS
        { "field"         : "sonum_xp_data_API_stats",
          "is_visible"    : False,
          "is_disabled"   : False,
          "data_type"     : "data",
          "endpoint_type" : "stat",
          "dataset_uri"    : "sonum-xp",
          "content"       : u"apiviz default API endpoint for stats results",
          "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7ebc7d328ed724cebd7fc0",
          "args_options"   : [
            {  "app_arg" : "dataToken",        "arg" : "token",              "optional" : True, "in" : ["url","header"],   "default" : "", "type": "str" },
            {  "app_arg" : "onlyCountsSimple", "arg" : "only_counts_simple", "optional" : True, "in" : ["url"],           "default" : "", "type": "bool" },
          ],
          "resp_fields" : {
            "projects" : { "resp_format" : "dict", "path" : "data/data_raw/f_data" },
            "total" :    { "resp_format" : "int",  "path" : "data/data_raw/f_data_count" },
          },
          "app_version"    : version,
          "method"        : "GET",
          "help"          : u"define the endpoint to get data for : a stat about the dataset",
          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"    : True
        },

        ### DATA MAP
        { "field"         : "sonum_xp_data_API_map",
          "is_visible"    : True,
          "is_disabled"   : False,
          "data_type"     : "data",
          "endpoint_type" : "map",
          "dataset_uri"   : "sonum-xp",
          "map_options"   : {
            "url"              : "https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png",
            "attribution"      : '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
            "subdomains"       : 'abcd',
            "center"           : [46.2276, 2.2137],
            "currentCenter"    : [46.2276, 2.2137],
            "zoom"             : 6,
            "maxZoom"          : 18,
            "minZoom"          : 5,
            "useMarkerCluster" : True,
            "pinIconUrl"       : "/static/icons/icon_pin_plein_violet.svg",
            "pinIconSize"      : { "highlighted" : [46, 46], "normal" : [29, 29]}
          },
          "content"       : u"apiviz default API endpoint for map results",
          "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7ebc7d328ed724cebd7fc0",
          "args_options"  : [
            {  "app_arg" : "dataToken",     "arg" : "token",            "optional" : True, "in" : ["url","header"], "default" : "",   "type": "str" },
            {  "app_arg" : "forMap",        "arg" : "map_list",         "optional" : False, "in" : ["url"],         "default" : True, "type": "bool" },
            {  "app_arg" : "asLatLng",      "arg" : "as_latlng",        "optional" : False, "in" : ["url"],         "default" : True, "type": "bool" },
            {  "app_arg" : "onlyGeocoded",  "arg" : "only_geocoded",    "optional" : False, "in" : ["url"],         "default" : True, "type": "bool" },
            {  "app_arg" : "page",          "arg" : "page_n",           "optional" : True, "in" : ["url"],          "default" : 1,   "type": "int" },
            {  "app_arg" : "perPage",       "arg" : "per_page",         "optional" : True, "in" : ["url"],          "default" : 100,   "type": "int" },
            {  "app_arg" : "itemId",        "arg" : "item_id",          "optional" : False, "in" : ["url"],           "default" : "", "type": "str" },

            {  "app_arg" : "query",         "arg" : "search_for",       "optional" : True, "in" : ["url"],          "default" : "",   "type": "str" },
            {  "app_arg" : "filters",       "arg" : "search_filters",   "optional" : True, "in" : ["url"],          "default" : "",   "type": "str" },
          ],
          "resp_fields" : {
            "projects" : { "resp_format" : "dict", "path" : "data/data_raw/f_data" },
            "total" :    { "resp_format" : "int",  "path" : "data/data_raw/f_data_count" },
          },
          "app_version"    : version,
          "method"        : "GET",
          "help"          : u"define the endpoint to get data for : map results",
          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"    : True
        },

        ### DATA EXPORT
        { "field"         : "sonum_xp_data_API_export",
          "is_visible"    : True,
          "is_disabled"   : False,
          "data_type"     : "data",
          "endpoint_type" : "export",
          "dataset_uri"   : "sonum-xp",
          "content"       : u"apiviz default API endpoint for export results",
          "root_url"      : "https://solidata-api.co-demos.com/api/dso/exports/as_csv/5c7ebc7d328ed724cebd7fc0", ## V2
          "args_options"  : [
            {  "app_arg" : "dataToken",  "arg" : "token",            "optional" : True, "in" : ["url","header"],  "default" : "", "type": "str" },
            # {  "app_arg" : "page",       "arg" : "page_n",           "optional" : True, "in" : ["url"],           "default" : 1,  "type": "int" },
            # {  "app_arg" : "perPage",    "arg" : "per_page",         "optional" : True, "in" : ["url"],           "default" : 300, "type": "int" },
            # {  "app_arg" : "query",      "arg" : "search_for",       "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
            # {  "app_arg" : "filters",    "arg" : "search_filters",   "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
            # {  "app_arg" : "shuffleSeed","arg" : "shuffle_seed",     "optional" : True, "in" : ["url"],           "default" : 205 , "type": "int" },
          ],
          "resp_fields" : {
            # "projects" : { "resp_format" : "list", "path" : "data/data_raw/f_data" },
            # "total" :    { "resp_format" : "int",  "path" : "data/data_raw/f_data_count" },
          },
          "app_version"    : version,
          "method"        : "GET",
          "help"          : u"define the endpoint to get data for : export dataset as csv",
          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"    : True
        },

]
