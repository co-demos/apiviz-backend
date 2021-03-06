# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_data_endpoints_config = [

  ### - - - - - - - - - - - - - - - ###
  ### CONFIG PING CARTO 

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
        "apiviz_front_uuid" : uuid_models["uuid_ping_carto"],
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
        "apiviz_front_uuid" : uuid_models["uuid_ping_carto"],
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
        "resp_fields" : {
        },
        "app_version"   : version,
        "method"        : "GET",
        "help"          : u"define the endpoint for a new access JWT ",
        "apiviz_front_uuid" : uuid_models["uuid_ping_carto"],
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
        "apiviz_front_uuid" : uuid_models["uuid_ping_carto"],
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
        "apiviz_front_uuid" : uuid_models["uuid_ping_carto"],
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
          { "app_arg" : "pageUser",     "arg" : "page",     "optional" : True,   "in" : ["url"],           "default" : 1,  "type": "int" },
          { "app_arg" : "perPageUser",  "arg" : "per_page", "optional" : True,   "in" : ["url"],           "default" : 50, "type": "int" },
        ],
        "resp_fields" : {
        },
        "app_version"   : version,
        "method"        : "GET",
        "help"          : u"define the endpoint to get data for : an user ",
        "apiviz_front_uuid" : uuid_models["uuid_ping_carto"],
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
        "apiviz_front_uuid" : uuid_models["uuid_ping_carto"],
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
        "apiviz_front_uuid" : uuid_models["uuid_ping_carto"],
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
        "apiviz_front_uuid" : uuid_models["uuid_ping_carto"],
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
        "apiviz_front_uuid" : uuid_models["uuid_ping_carto"],
        "is_default"    : True
      },


    ### - - - - - - - - - - - - - - - ###
    ### DATA ENDPOINTS
    ### - - - - - - - - - - - - - - - ###

      ### DATA FILTERS
      { "field"         : "tl_data_API_filters",
        "is_visible"    : True,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "filters",
        "dataset_uri"   : "recherche",
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
          {"locale" : "en", "text" : "Enter the name of a place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Tapez le nom d'un lieu" }
        ],
        "items_found"   : [
          {"locale" : "en", "text" : "places found"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "lieux trouvés" }
        ],
        "stats_text"   : [
          {"locale" : "en", "text" : "experimental"},{"locale" : "es", "text" : "experimental"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "expérimental" }
        ],
        "reset"   : [
          {"locale" : "en", "text" : "reset"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "effacer" }
        ],

        "content"       : u"apiviz default API endpoint for navbar filters",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5e4bac5d328ed74937e075b1",  
        "args_options"  : [
          {  "app_arg" : "dataToken",      "arg" : "token",             "optional" : True, "in" : ["url","header"],   "default" : "",   "type": "str" },
          {  "app_arg" : "filtersList",    "arg" : "get_filters",       "optional" : False, "in" : ["url"],           "default" : True, "type": "bool" }, # also working with dsi?
          {  "app_arg" : "filterChoices",  "arg" : "get_uniques",       "optional" : False, "in" : ["url"],           "default" : "tag", "type": "str" },
        ],

        "filter_options" : [

          {	"name"		: u"result_context__",
            "id"      : "filter_1",
            "col_name" : "result_context",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Areas"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Départements" }],
            "choices"	: [
              {'name' : u'44  Loire-Atlantique  Pays de la Loire', 'choice_title' : [{'locale' : 'en', 'text' : 'Loire-Atlantique'},{'locale' : 'es', 'text' : 'Loire-Atlantique'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : 'Loire-Atlantique'}, {'locale' : 'fr', 'text' : 'Loire-Atlantique' }]},
              {'name' : u'49  Maine-et-Loire  Pays de la Loire', 'choice_title' : [{'locale' : 'en', 'text' : 'Maine-et-Loire'},{'locale' : 'es', 'text' : 'Maine-et-Loire'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : 'Maine-et-Loire'}, {'locale' : 'fr', 'text' : 'Maine-et-Loire' }]},
              {'name' : u'53  Mayenne  Pays de la Loire', 'choice_title' : [{'locale' : 'en', 'text' : 'Mayenne'},{'locale' : 'es', 'text' : 'Mayenne'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : 'Mayenne'}, {'locale' : 'fr', 'text' : 'Mayenne' }]},
              {'name' : u'72  Sarthe  Pays de la Loire', 'choice_title' : [{'locale' : 'en', 'text' : 'Sarthe'},{'locale' : 'es', 'text' : 'Sarthe'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : 'Sarthe'}, {'locale' : 'fr', 'text' : 'Sarthe' }]},
              {'name' : u'85  Vendée  Pays de la Loire', 'choice_title' : [{'locale' : 'en', 'text' : 'Vendée'},{'locale' : 'es', 'text' : 'Vendée'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : 'Vendée'}, {'locale' : 'fr', 'text' : 'Vendée' }]},

            ],
          },
          {	"name"		: u"TYPOLOGIE__",  
            "id"      : "filter_2",
            "col_name" : "TYPOLOGIE",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Typologies"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Typologies" }],
            "choices"	: [
              {'name' : u'T', 'choice_title' : [{'locale' : 'en', 'text' : 'Renew work'},{'locale' : 'es', 'text' : 'Renovar el trabajo'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Renouveler le travail' }]},
              {'name' : u'O', 'choice_title' : [{'locale' : 'en', 'text' : 'Work together'},{'locale' : 'es', 'text' : 'Renovar el trabajo'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Œuvrer ensemble' }]},
              {'name' : u'D', 'choice_title' : [{'locale' : 'en', 'text' : 'Collectively discover'},{'locale' : 'es', 'text' : 'Renovar el trabajo'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Découvrir collectivement' }]},
              {'name' : u'C', 'choice_title' : [{'locale' : 'en', 'text' : 'Rethink our consumption'},{'locale' : 'es', 'text' : 'Renovar el trabajo'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Repenser sa consommation' }]},
            ],
          },
          {	"name"		: u"PUBLICS__",  
            "id"      : "filter_2",
            "col_name" : "PUBLICS",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Publics"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Publics" }],
            "choices"	: [
              {'name' : u'Professionnels', 'choice_title' : [{'locale' : 'en', 'text' : 'Professionals'},{'locale' : 'es', 'text' : 'Renovar el trabajo'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Professionnels' }]},
              {'name' : u'Citoyens', 'choice_title' : [{'locale' : 'en', 'text' : 'Citizens'},{'locale' : 'es', 'text' : 'Renovar el trabajo'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Citoyens' }]},
            ],
          },
          {	"name"		: u"SOURCE_codes__",
            "id"      : "filter_3",
            "col_name" : "SOURCE_codes",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Sources"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Sources" }],
            "choices"	: [
              {"name" : u"CGET", "choice_title" : [{"locale" : "en", "text" : "CGET"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "CGET" }]},
              {"name" : u"PiNG", "choice_title" : [{"locale" : "en", "text" : "PiNG"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "PiNG" }]},
              {"name" : u"CAPTL", "choice_title" : [{"locale" : "en", "text" : "CAP Tiers-lieux"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "CAP Tiers-lieux" }]},
            ],
          },
        ],
        "app_version"    : version,
        "method"        : "GET",
        "help"          : u"define the endpoint to get data for : filters in search navbar",
        "apiviz_front_uuid" : uuid_models["uuid_ping_carto"],
        "is_default"    : True
      },

      ### DATA TABLE
      { "field"         : "tl_data_API_table",
        "is_visible"    : True,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "table",
        "dataset_uri"   : "recherche",
        "content"       : u"apiviz default API endpoint for list results",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5e4bac5d328ed74937e075b1", ## V2
        "args_options"  : [
          {  "app_arg" : "dataToken",        "arg" : "token",            "optional" : True, "in" : ["url","header"],  "default" : "", "type": "str" },
          {  "app_arg" : "page",             "arg" : "page",             "optional" : True, "in" : ["url"],           "default" : 1,  "type": "int" },
          {  "app_arg" : "perPage",          "arg" : "per_page",         "optional" : True, "in" : ["url"],           "default" : 25, "type": "int", "authorized" : [10, 25, 50, 100, 200, 300] },
          {  "app_arg" : "sortBy",           "arg" : "sort_by",          "optional" : True, "in" : ["url"],           "default" : "NOM DU LIEU", "type": "str" },
          {  "app_arg" : "sortIsDescending", "arg" : "descending",       "optional" : False, "in" : ["url"],          "default" : False, "type": "bool" },
          {  "app_arg" : "query",            "arg" : "search_for",       "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
          {  "app_arg" : "filters",          "arg" : "search_filters",   "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
          {  "app_arg" : "shuffleSeed",      "arg" : "shuffle_seed",     "optional" : True, "in" : ["url"],           "default" : None , "type": "int" },
        ],
        "resp_fields" : {
          "projects" : { "resp_format" : "list", "path" : "data/data_raw/f_data" },
          "total" :    { "resp_format" : "int",  "path" : "data/data_raw/f_data_count" },
        },
        "app_version"    : version,
        "method"        : "GET",
        "help"          : u"define the endpoint to get data for : a view list",
        "apiviz_front_uuid" : uuid_models["uuid_ping_carto"],
        "is_default"    : True
      },

      ### DATA LIST
      { "field"         : "tl_data_API_list",
        "is_visible"    : True,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "list",
        "dataset_uri"   : "recherche",
        "content"       : u"apiviz default API endpoint for list results",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5e4bac5d328ed74937e075b1", ## V2
        "args_options"  : [
          {  "app_arg" : "dataToken",  "arg" : "token",            "optional" : True, "in" : ["url","header"],  "default" : "", "type": "str" },
          {  "app_arg" : "page",       "arg" : "page",             "optional" : True, "in" : ["url"],           "default" : 1,  "type": "int" },
          {  "app_arg" : "perPage",    "arg" : "per_page",         "optional" : True, "in" : ["url"],           "default" : 25, "type": "int", "authorized" : [10, 25, 50, 100, 200, 300] },
          {  "app_arg" : "query",      "arg" : "search_for",       "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
          {  "app_arg" : "filters",    "arg" : "search_filters",   "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
          {  "app_arg" : "shuffleSeed","arg" : "shuffle_seed",     "optional" : True, "in" : ["url"],           "default" : None , "type": "int" },
        ],
        "resp_fields" : {
          "projects" : { "resp_format" : "list", "path" : "data/data_raw/f_data" },
          "total" :    { "resp_format" : "int",  "path" : "data/data_raw/f_data_count" },
        },
        "app_version"    : version,
        "method"        : "GET",
        "help"          : u"define the endpoint to get data for : a view list",
        "apiviz_front_uuid" : uuid_models["uuid_ping_carto"],
        "is_default"    : True
      },

      ### DATA DETAIL
      { "field"         : "tl_data_API_detail",
        "is_visible"    : True,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "detail",
        "dataset_uri"   : "recherche",
        "content"       : u"apiviz default API endpoint for detailled results",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5e4bac5d328ed74937e075b1", ## V2
        "args_options"  : [
          {  "app_arg" : "dataToken", "arg" : "token",     "optional" : True,  "in" : ["url","header"],   "default" : "", "type": "str" },
          # {  "app_arg" : "itemId",    "arg" : "item_id",   "optional" : False, "in" : ["url"],           "default" : "", "type": "str" },
          {  "app_arg" : "itemId",     "arg" : "item_id", "optional" : False, "in" : ["url"],          "default" : "", "type": "str", "replace_arg": { "arg" : "search_filters", "sub_arg" : "INDEX", "sep" : "__" }},
        ],
        "resp_fields" : {
          "projects" : { "resp_format" : "list", "path" : "data/data_raw/f_data" },
          "total"    : { "resp_format" : "int",  "path" : "data/data_raw/f_data_count" },
        },
        "app_version"    : version,
        "method"        : "GET",
        "help"          : u"define the endpoint to get data for : a detailled data",
        "apiviz_front_uuid" : uuid_models["uuid_ping_carto"],
        "is_default"    : True
      },

      ### DATA STATS
      { "field"         : "tl_data_API_stats",
        "is_visible"    : False,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "stat",
        "dataset_uri"   : "recherche",
        "content"       : u"apiviz default API endpoint for stats results",

        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one_stats/5e4bac5d328ed74937e075b1", ## V2

        "args_options"  : [
          {  "app_arg" : "dataToken", "arg" : "token",          "optional" : True, "in" : ["url","header"], "default" : "", "type": "str" },
          {  "app_arg" : "query",     "arg" : "search_for",     "optional" : True, "in" : ["url"],          "default" : "", "type": "str" },
          {  "app_arg" : "filters",   "arg" : "search_filters", "optional" : True, "in" : ["url"],          "default" : "", "type": "str" },
        ],
        
        "payload_options" : {

          # "payload_format" : "list",

          "payload_queries" : [
            { 
              "serie_id" : "tl-stat-bar-horiz",
              "agg_fields" : [
                { 
                  "agg_field" : "TYPOLOGIE",
                  "agg_sum_type" : "count_items", 
                  "agg_needs_unwind" : True,
                  "agg_unwind_separator" : "-"
                },
                { 
                  "agg_field" : "result_context",
                  "agg_sum_type" : "count_items",
                  "agg_needs_unwind" : False,
                  "agg_unwind_separator" : "-" 
                }  
              ]
            },
            { 
              "serie_id" : "tl-stat-donut",
              "agg_fields" : [
                { 
                  "agg_field" : "TYPOLOGIE",
                  "agg_sum_type" : "count_items", 
                  "agg_needs_unwind" : True,
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

        "app_version"    : version,
        "method"        : "POST",
        "help"          : u"define the endpoint to get data for : a stat about the dataset",
        "apiviz_front_uuid" : uuid_models["uuid_ping_carto"],
        "is_default"    : True
      },

      ### DATA MAP
      { "field"         : "tl_data_API_map",
        "is_visible"    : True,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "map",
        "dataset_uri"   : "recherche",

        "content"       : u"apiviz default API endpoint for map results",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5e4bac5d328ed74937e075b1", ## V2
        "args_options"  : [
          {  "app_arg" : "dataToken",  "arg" : "token",            "optional" : True, "in" : ["url","header"], "default" : "",   "type": "str" },

          {  "app_arg" : "forMap",       "arg" : "map_list",          "optional" : False, "in" : ["url"], "default" : True,        "type": "bool" },
          # {  "app_arg" : "defaultValue", "arg" : "fields_to_return",  "optional" : False, "in" : ["url"], "default" : "INSEEDEP",  "type": "str" },
          {  "app_arg" : "defaultValue", "arg" : "fields_to_return",  "optional" : False, "in" : ["url"], "default" : "result_context,DEPARTEMENT,INDEX,NOM DU LIEU",  "type": "str" },
          # {  "app_arg" : "asLatLng", "arg" : "as_latlng",         "optional" : False, "in" : ["url"], "default" : True, "type": "bool" },
          # {  "app_arg" : "onlyGeocoded", "arg" : "only_geocoded", "optional" : False, "in" : ["url"], "default" : True, "type": "bool" },

          # {  "app_arg" : "itemId",     "arg" : "item_id",         "optional" : True, "in" : ["url"],  "default" : "",   "type": "str" },
          {  "app_arg" : "query",      "arg" : "search_for",        "optional" : True, "in" : ["url"],  "default" : "",   "type": "str" },
          {  "app_arg" : "filters",    "arg" : "search_filters",    "optional" : True, "in" : ["url"],  "default" : "",   "type": "str" },

        ],
        "resp_fields" : {
          "projects" : { "resp_format" : "list", "path" : "data/data_raw/f_data" },
          "total" :    { "resp_format" : "int",  "path" : "data/data_raw/f_data_count" },
        },
        "app_version"    : version,
        "method"        : "GET",
        "help"          : u"define the endpoint to get data for : map results",
        "apiviz_front_uuid" : uuid_models["uuid_ping_carto"],
        "is_default"    : True
      },

      ### DATA EXPORT
      { "field"         : "tl_data_API_export",
        "is_visible"    : True,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "export",
        "dataset_uri"   : "recherche",
        "content"       : u"apiviz default API endpoint for export results",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/exports/as_csv/5e4bac5d328ed74937e075b1", ## V2
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
        "apiviz_front_uuid" : uuid_models["uuid_ping_carto"],
        "is_default"    : True
      },

]
