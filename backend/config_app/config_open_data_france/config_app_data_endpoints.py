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
        "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
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
        "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
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
        "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
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
        "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
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
        "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
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
        "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
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
        "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
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
        "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
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
        "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
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
        "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
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
        "has_shuffle"  : True,
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
          {"locale" : "en", "text" : "Enter the name of a place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Tapez le nom d'une organisation" }
        ],
        "items_found"   : [
          {"locale" : "en", "text" : "places found"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "organisations trouvées" }
        ],
        "stats_text"   : [
          {"locale" : "en", "text" : "experimental"},{"locale" : "es", "text" : "experimental"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "expérimental" }
        ],
        "reset"   : [
          {"locale" : "en", "text" : "reset"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "effacer" }
        ],

        "content"       : u"apiviz default API endpoint for navbar filters",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/61b8eedc328ed773d00efa16",  
        "args_options"  : [
          {  "app_arg" : "dataToken",      "arg" : "token",             "optional" : True, "in" : ["url","header"],   "default" : "",   "type": "str" },
          {  "app_arg" : "filtersList",    "arg" : "get_filters",       "optional" : False, "in" : ["url"],           "default" : True, "type": "bool" }, # also working with dsi?
          {  "app_arg" : "filterChoices",  "arg" : "get_uniques",       "optional" : False, "in" : ["url"],           "default" : "tag", "type": "str" },
        ],

        "filter_options" : [

          {	"name"		: u"tranche_pop__",
            "id"      : "filter_1",
            "col_name" : "tranche_pop",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Orga"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Population" }],
            "choices"	: [
              {'name' : u'p_0_1', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'moins de 1 000 habitants' }]},
              {'name' : u'p_1_5', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'entre 1 000 et 5 000 habitants' }]},
              {'name' : u'p_5_10', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'entre 5 000 et 10 000 habitants' }]},
              {'name' : u'p_10_25', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'entre 1 000 et 25 000 habitants' }]},
              {'name' : u'p_25_50', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'entre 25 000 et 50 000 habitants' }]},
              {'name' : u'p_50_100', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'entre 50 000 et 100 000 habitants' }]},
              {'name' : u'p_100_250', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'entre 100 000 et 250 000 habitants' }]},
              {'name' : u'p_250_500', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'entre 250 000 et 500 000 habitants' }]},
              {'name' : u'p_500_1000', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'entre 500 000 et 1 000 000 habitants' }]},
              {'name' : u'p_1000_5000', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'plus de 1 000 000 habitants' }]},
              {'name' : u'p_na', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'Non renseigné' }]},
            ],
          },

          {	"name"		: u"tranche_ptf__",
            "id"      : "filter_2",
            "col_name" : "tranche_ptf",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Orga"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Jeux de données publiés" }],
            "choices"	: [
              {'name' : u'd_1_5', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'entre 1 et 5 jeux de données' }]},
              {'name' : u'd_6_10', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'entre 6 et 10 jeux de données' }]},
              {'name' : u'd_11_25', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'entre 11 et 25 jeux de données' }]},
              {'name' : u'd_26_50', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'entre 26 et 50 jeux de données' }]},
              {'name' : u'd_51_100', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'entre 51 et 100 jeux de données' }]},
              {'name' : u'd_101_250', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'entre 101 et 250 jeux de données' }]},
              {'name' : u'd_251_500', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'entre 251 et 500 jeux de données' }]},
              {'name' : u'd_501_5000', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'plus de 500 jeux de données' }]},
              {'name' : u'd_na', 'choice_title' : [{'locale' : 'en', 'text' : '_'},{'locale' : 'es', 'text' : '_'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '_'}, {'locale' : 'fr', 'text' : 'Non renseigné' }]},
            ],
          },

          {	"name"		: u"type__",  
            "id"      : "filter_3",
            "col_name" : "type",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Type"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Types d'organisation" }],
            "choices"	: [
              {'name' : u'COM', 'choice_title' : [{'locale' : 'en', 'text' : 'COM'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : "Commune" }]},
              {'name' : u'CC', 'choice_title' : [{'locale' : 'en', 'text' : 'CC'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : "Communauté de Communes" }]},
              {'name' : u'CA', 'choice_title' : [{'locale' : 'en', 'text' : 'CA'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : "Communauté d'Agglomération" }]},
              {'name' : u'CU', 'choice_title' : [{'locale' : 'en', 'text' : 'CU'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : "Communauté Urbaine" }]},
              {'name' : u'EPT', 'choice_title' : [{'locale' : 'en', 'text' : 'CEPT'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : "Etab. Public Territorial, rattaché à la Métropole du Grand Paris" }]},
              {'name' : u'MET', 'choice_title' : [{'locale' : 'en', 'text' : 'CMET'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : "Métropole" }]},
              {'name' : u'DEP', 'choice_title' : [{'locale' : 'en', 'text' : 'DEP'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : "Département" }]},
              {'name' : u'REG', 'choice_title' : [{'locale' : 'en', 'text' : 'REG'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : "Région" }]},
              {'name' : u'AGCT', 'choice_title' : [{'locale' : 'en', 'text' : 'AGCT'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : "Autre Groupement de Coll. Terr : SMI, GIP, ..." }]},
              {'name' : u'OACT', 'choice_title' : [{'locale' : 'en', 'text' : 'OACT'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : "Organisme Associé de Coll. Terr. : Office de Tourisme, Régie de transport, ..." }]},
              {'name' : u'DSPT', 'choice_title' : [{'locale' : 'en', 'text' : 'CDSPT'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : "Délégataire de Serivce Public Territoriaux : opérateurs privés, Soc. d'Economie Mixte,..." }]},
            ],
          },


          {	"name"		: u"regcode__",  
            "id"      : "filter_4",
            "col_name" : "reg_code_short",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Region"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Régions" }],
            "choices"	: [
              {'name' : u'ARA-84', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Auvergne-Rhône-Alpes' }]},
              {'name' : u'BFC-27', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Bourgogne-Franche-Comté' }]},
              {'name' : u'BRE-53', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Bretagne' }]},
              {'name' : u'COR-94', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Corse' }]},
              {'name' : u'CVL-24', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Centre-Val de Loire' }]},
              {'name' : u'GES-44', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Grand-Est' }]},
              {'name' : u'HDF-32', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Hauts-de-France' }]},
              {'name' : u'IDF-11', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Île-de-France' }]},
              {'name' : u'NAQ-75', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Nouvelle-Aquitaine' }]},
              {'name' : u'NOR-28', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Normandie' }]},
              {'name' : u'OCC-76', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Occitanie' }]},
              {'name' : u'PAC-93', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Provence-Alpes-Côte-d’Azur' }]},
              {'name' : u'PDL-52', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Pays-de-la-Loire' }]},
              {'name' : u'GP-01', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Guadeloupe' }]},
              {'name' : u'GF-03', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Guyane' }]},
              {'name' : u'MQ-02', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Martinique' }]},
              {'name' : u'YT-06', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Mayotte' }]},
              {'name' : u'RE-04', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'La Réunion' }]},
              {'name' : u'PF', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Polynésie française' }]},
              {'name' : u'NC', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Nouvelle-Calédonie' }]},
            ],
          },

          {	"name"		: u"platform_clean__",  
            "id"      : "filter_5",
            "col_name" : "platform_clean",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Platform"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plateformes" }],
            "choices"	: [
              {'name' : u'OpenDataSoft', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'OpenDataSoft' }]},
              {'name' : u'CKAN', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'CKAN' }]},
              {'name' : u'DataGouv', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'DataGouv' }]},
              # {'name' : u'ArcGis', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'ArcGis' }]},
              {'name' : u'GeoNetwork', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'GeoNetwork' }]},
              # {'name' : u'DataGouv-CKAN', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'DataGouv-CKAN' }]},
              {'name' : u'Spécifique', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Spécifique' }]},
              {'name' : u'ArcGIS', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'ArcGIS' }]},
              # {'name' : u'CKAN-CKAN', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'CKAN-CKAN' }]},
              {'name' : u'OpenDataGazette', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'OpenDataGazette' }]},
              {'name' : u'MGDIS Open Data', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'MGDIS Open Data' }]},
              {'name' : u'DATA4CITIZEN', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'DATA4CITIZEN' }]},
              {'name' : u'TYPO3 In Cite', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'TYPO3 In Cite' }]},
              {'name' : u'Isogéo', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Isogéo' }]},
            ],
          },

          {	"name"		: u"tags__",  
            "id"      : "filter_5",
            "col_name" : "tags",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Tags"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Etiquettes" }],
            "choices"	: [
              {'name' : u'Administratif', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Administratif' }]},
              {'name' : u'Citoyenneté', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Citoyenneté' }]},
              {'name' : u'Culture', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Culture' }]},
              {'name' : u'Economie', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Economie' }]},
              {'name' : u'Education', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Education' }]},
              {'name' : u'Energie', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Energie' }]},
              {'name' : u'Enfance', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Enfance' }]},
              {'name' : u'Environnement', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Environnement' }]},
              {'name' : u'Equipements', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Equipements' }]},
              {'name' : u'Finance', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Finance' }]},
              {'name' : u'Santé', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Santé' }]},
              {'name' : u'Sécurité', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Sécurité' }]},
              {'name' : u'Social', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Social' }]},
              {'name' : u'Sports', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Sports' }]},
              {'name' : u'Télécom', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Télécom' }]},
              {'name' : u'Tourisme', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Tourisme' }]},
              {'name' : u'Transport', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Transport' }]},
              {'name' : u'Urbanisme', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Urbanisme' }]},
            ],
          },

          # {	"name"		: u"MODELE_JURIDIQUE__",  
          #   "id"      : "filter_3",
          #   "col_name" : "MODELE_JURIDIQUE",
          #   "dataType" : "text",
          #   "filter_title" : [{"locale" : "en", "text" : "Publics"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Modèle juridique" }],
          #   "choices"	: [
          #     {'name' : u'Association', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Association' }]},
          #     {'name' : u'SCIC ou SCOP', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'SCIC ou SCOP' }]},
          #     {'name' : u'Collectivité', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Collectivité' }]},
          #     {'name' : u'SARL/SAS/SA', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'SARL/SAS/SA' }]},
          #     {'name' : u'Autre', 'choice_title' : [{'locale' : 'en', 'text' : 'to do'},{'locale' : 'es', 'text' : 'to do'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Autre' }]},
          #   ],
          # },

          # {	"name"		: u"FABRIQUE_DE_TERRITOIRE__",  
          #   "id"      : "filter_4",
          #   "col_name" : "FABRIQUE_DE_TERRITOIRE",
          #   "dataType" : "text",
          #   "filter_title" : [{"locale" : "en", "text" : "to do"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Fabrique de territoire" }],
          #   "choices"	: [
          #     {'name' : u'OUI', 'choice_title' : [{'locale' : 'en', 'text' : 'TO DO'},{'locale' : 'es', 'text' : 'TO DO'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Oui' }]},
          #     {'name' : u'NON', 'choice_title' : [{'locale' : 'en', 'text' : 'TO DO'},{'locale' : 'es', 'text' : 'TO DO'},{'locale' : 'tr', 'text' : 'to do'},{'locale' : 'de', 'text' : 'to do'}, {'locale' : 'fr', 'text' : 'Non' }]},
          #   ],
          # },

          # {	"name"		: u"SOURCE_codes_temp__",
          #   "id"      : "filter_5",
          #   "col_name" : "SOURCE_codes",
          #   "dataType" : "text",
          #   "filter_title" : [{"locale" : "en", "text" : "Sources"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Sources" }],
          #   "choices"	: [
          #     # {"name" : u"CGET", "choice_title" : [{"locale" : "en", "text" : "CGET"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "CGET" }]},
          #     # {"name" : u"CGET", "choice_title" : [{"locale" : "en", "text" : "France Tiers-Lieux"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "France Tiers-Lieux" }]},
          #     {"name" : u"FTL", "choice_title" : [{"locale" : "en", "text" : "France Tiers-Lieux"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "France Tiers-Lieux" }]},
          #     {"name" : u"PiNG", "choice_title" : [{"locale" : "en", "text" : "PiNG"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "PiNG" }]},
          #     {"name" : u"CAPTL", "choice_title" : [{"locale" : "en", "text" : "CAP Tiers-lieux"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "CAP Tiers-lieux" }]},
          #   ],
          # },
        ],
        "app_version"    : version,
        "method"        : "GET",
        "help"          : u"define the endpoint to get data for : filters in search navbar",
        "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
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
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/61b8eedc328ed773d00efa16", ## V2
        "args_options"  : [
          {  "app_arg" : "dataToken",        "arg" : "token",            "optional" : True, "in" : ["url","header"],  "default" : "", "type": "str" },
          {  "app_arg" : "page",             "arg" : "page",             "optional" : True, "in" : ["url"],           "default" : 1,  "type": "int" },
          {  "app_arg" : "perPage",          "arg" : "per_page",         "optional" : True, "in" : ["url"],           "default" : 25, "type": "int", "authorized" : [10, 25, 50, 100, 200, 300] },
          {  "app_arg" : "sortBy",           "arg" : "sort_by",          "optional" : True, "in" : ["url"],           "default" : "nom", "type": "str" },
          {  "app_arg" : "sortIsDescending", "arg" : "descending",       "optional" : False, "in" : ["url"],          "default" : False, "type": "bool" },
          {  "app_arg" : "query",            "arg" : "search_for",       "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
          {  "app_arg" : "filters",          "arg" : "search_filters",   "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
          {  "app_arg" : "shuffleSeed",      "arg" : "shuffle_seed",     "optional" : True, "in" : ["url"],           "default" : None , "type": "int", "init": True },
        ],
        "resp_fields" : {
          "projects" : { "resp_format" : "list", "path" : "data/data_raw/f_data" },
          "total" :    { "resp_format" : "int",  "path" : "data/data_raw/f_data_count" },
        },
        "app_version"    : version,
        "method"        : "GET",
        "help"          : u"define the endpoint to get data for : a view list",
        "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
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
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/61b8eedc328ed773d00efa16", ## V2
        "args_options"  : [
          {  "app_arg" : "dataToken",  "arg" : "token",            "optional" : True, "in" : ["url","header"],  "default" : "", "type": "str" },
          {  "app_arg" : "page",       "arg" : "page",             "optional" : True, "in" : ["url"],           "default" : 1,  "type": "int" },
          {  "app_arg" : "perPage",    "arg" : "per_page",         "optional" : True, "in" : ["url"],           "default" : 25, "type": "int", "authorized" : [10, 25, 50, 100, 200, 300] },
          {  "app_arg" : "query",      "arg" : "search_for",       "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
          {  "app_arg" : "filters",    "arg" : "search_filters",   "optional" : True, "in" : ["url"],           "default" : "", "type": "str" },
          {  "app_arg" : "shuffleSeed","arg" : "shuffle_seed",     "optional" : True, "in" : ["url"],           "default" : None , "type": "int", "init": True },
        ],
        "resp_fields" : {
          "projects" : { "resp_format" : "list", "path" : "data/data_raw/f_data" },
          "total" :    { "resp_format" : "int",  "path" : "data/data_raw/f_data_count" },
        },
        "app_version"    : version,
        "method"        : "GET",
        "help"          : u"define the endpoint to get data for : a view list",
        "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
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
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/61b8eedc328ed773d00efa16", ## V2
        "args_options"  : [
          {  "app_arg" : "dataToken", "arg" : "token",     "optional" : True,  "in" : ["url","header"],   "default" : "", "type": "str" },
          # {  "app_arg" : "itemId",    "arg" : "item_id",   "optional" : False, "in" : ["url"],           "default" : "", "type": "str" },
          {  "app_arg" : "itemId",     "arg" : "item_id",   "optional" : False, "in" : ["url"],           "default" : "", "type": "str", "replace_arg": { "arg" : "search_filters", "sub_arg" : "id_odf", "sep" : "__" } },
          # {  "app_arg" : "itemId",     "arg" : "item_id",   "optional" : False, "in" : ["url"],           "default" : "", "type": "str", "replace_arg": { "arg" : "search_filters", "sub_arg" : "conum_id", "sep" : "__" } },
          # {  "app_arg" : "itemId",     "arg" : "item_id", "optional" : False, "in" : ["url"],          "default" : "", "type": "str", "replace_arg": { "arg" : "search_filters", "sub_arg" : "INDEX", "sep" : "__" }},
          # {  "app_arg" : "itemId",     "arg" : "item_id", "optional" : False, "in" : ["url"],          "default" : "", "type": "str", "replace_arg": { "arg" : "search_filters", "sub_arg" : "sd_id", "sep" : "__" }},
        ],
        "resp_fields" : {
          "projects" : { "resp_format" : "list", "path" : "data/data_raw/f_data" },
          "total"    : { "resp_format" : "int",  "path" : "data/data_raw/f_data_count" },
        },
        "app_version"    : version,
        "method"        : "GET",
        "help"          : u"define the endpoint to get data for : a detailled data",
        "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
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

        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one_stats/61b8eedc328ed773d00efa16", ## V2

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
        "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
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
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/61b8eedc328ed773d00efa16", ## V2
        "args_options"  : [
          {  "app_arg" : "dataToken",  "arg" : "token",            "optional" : True, "in" : ["url","header"], "default" : "",   "type": "str" },

          {  "app_arg" : "forMap",       "arg" : "map_list",          "optional" : False, "in" : ["url"], "default" : True,        "type": "bool" },
          # {  "app_arg" : "defaultValue", "arg" : "fields_to_return",  "optional" : False, "in" : ["url"], "default" : "INSEEDEP",  "type": "str" },
          # {  "app_arg" : "defaultValue", "arg" : "fields_to_return",  "optional" : False, "in" : ["url"], "default" : "result_context,DEPARTEMENT,INDEX,NOM DU LIEU",  "type": "str" },
          {  "app_arg" : "defaultValue", "arg" : "fields_to_return",  "optional" : False, "in" : ["url"], "default" : "nom,id_odf,type,platform_clean,depcode,tags,reg_code_geo",  "type": "str" },
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
        "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
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
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/exports/as_csv/61b8eedc328ed773d00efa16", ## V2
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
        "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
        "is_default"    : True
      },

]
