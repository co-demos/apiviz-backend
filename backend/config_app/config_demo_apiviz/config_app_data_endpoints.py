# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_data_endpoints_config = [

  ### - - - - - - - - - - - - - - - ###
  ### CONFIG TIERS LIEUX 

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
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
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
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
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
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
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
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
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
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
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
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
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
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
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
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
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
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
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
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
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
        # "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7f0438328ed72e431f338e",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5d5fca92328ed71684ce1785",  ## V2
        "args_options"  : [
          {  "app_arg" : "dataToken",      "arg" : "token",             "optional" : True, "in" : ["url","header"],   "default" : "",   "type": "str" },
          {  "app_arg" : "filtersList",    "arg" : "get_filters",       "optional" : False, "in" : ["url"],           "default" : True, "type": "bool" }, # also working with dsi?
          {  "app_arg" : "filterChoices",  "arg" : "get_uniques",       "optional" : False, "in" : ["url"],           "default" : "tag", "type": "str" },
        ],

        "filter_options" : [

          {	"name"		: u"NOMMETRO_CODE__",
            "id"      : "filter_2",
            "col_name" : "NOMMETRO_CODE",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Metropolis"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Métropole" }],
            "choices"	: [
              {'name' : u'BDX', 'choice_title' : [{'locale' : 'en', 'text' : 'Bordeaux Métropole'},{'locale' : 'es', 'text' : 'Bordeaux Métropole'},{'locale' : 'tr', 'text' : 'Bordeaux Métropole'},{'locale' : 'de', 'text' : 'Bordeaux Métropole'}, {'locale' : 'fr', 'text' : 'Bordeaux Métropole' }]},
              {'name' : u'BRS', 'choice_title' : [{'locale' : 'en', 'text' : 'Brest Métropole'},{'locale' : 'es', 'text' : 'Brest Métropole'},{'locale' : 'tr', 'text' : 'Brest Métropole'},{'locale' : 'de', 'text' : 'Brest Métropole'}, {'locale' : 'fr', 'text' : 'Brest Métropole' }]},
              {'name' : u'CLT', 'choice_title' : [{'locale' : 'en', 'text' : 'Clermont Auvergne Métropole'},{'locale' : 'es', 'text' : 'Clermont Auvergne Métropole'},{'locale' : 'tr', 'text' : 'Clermont Auvergne Métropole'},{'locale' : 'de', 'text' : 'Clermont Auvergne Métropole'}, {'locale' : 'fr', 'text' : 'Clermont Auvergne Métropole' }]},
              {'name' : u'DJN', 'choice_title' : [{'locale' : 'en', 'text' : 'Dijon Métropole'},{'locale' : 'es', 'text' : 'Dijon Métropole'},{'locale' : 'tr', 'text' : 'Dijon Métropole'},{'locale' : 'de', 'text' : 'Dijon Métropole'}, {'locale' : 'fr', 'text' : 'Dijon Métropole' }]},
              {'name' : u'STR', 'choice_title' : [{'locale' : 'en', 'text' : 'Eurométropole de Strasbourg'},{'locale' : 'es', 'text' : 'Eurométropole de Strasbourg'},{'locale' : 'tr', 'text' : 'Eurométropole de Strasbourg'},{'locale' : 'de', 'text' : 'Eurométropole de Strasbourg'}, {'locale' : 'fr', 'text' : 'Eurométropole de Strasbourg' }]},
              {'name' : u'AIX', 'choice_title' : [{'locale' : 'en', 'text' : "Métropole d'Aix-Marseille-Provence"},{'locale' : 'es', 'text' : "Métropole d'Aix-Marseille-Provence"},{'locale' : 'tr', 'text' : "Métropole d'Aix-Marseille-Provence"},{'locale' : 'de', 'text' : "Métropole d'Aix-Marseille-Provence"}, {'locale' : 'fr', 'text' : "Métropole d'Aix-Marseille-Provence" }]},
              {'name' : u'LYO', 'choice_title' : [{'locale' : 'en', 'text' : 'Métropole de Lyon'},{'locale' : 'es', 'text' : 'Métropole de Lyon'},{'locale' : 'tr', 'text' : 'Métropole de Lyon'},{'locale' : 'de', 'text' : 'Métropole de Lyon'}, {'locale' : 'fr', 'text' : 'Métropole de Lyon' }]},
              {'name' : u'NCY', 'choice_title' : [{'locale' : 'en', 'text' : 'Métropole du Grand Nancy'},{'locale' : 'es', 'text' : 'Métropole du Grand Nancy'},{'locale' : 'tr', 'text' : 'Métropole du Grand Nancy'},{'locale' : 'de', 'text' : 'Métropole du Grand Nancy'}, {'locale' : 'fr', 'text' : 'Métropole du Grand Nancy' }]},
              {'name' : u'PAR', 'choice_title' : [{'locale' : 'en', 'text' : 'Métropole du Grand Paris'},{'locale' : 'es', 'text' : 'Métropole du Grand Paris'},{'locale' : 'tr', 'text' : 'Métropole du Grand Paris'},{'locale' : 'de', 'text' : 'Métropole du Grand Paris'}, {'locale' : 'fr', 'text' : 'Métropole du Grand Paris' }]},
              {'name' : u'LIL', 'choice_title' : [{'locale' : 'en', 'text' : 'Métropole Européenne de Lille'},{'locale' : 'es', 'text' : 'Métropole Européenne de Lille'},{'locale' : 'tr', 'text' : 'Métropole Européenne de Lille'},{'locale' : 'de', 'text' : 'Métropole Européenne de Lille'}, {'locale' : 'fr', 'text' : 'Métropole Européenne de Lille' }]},
              {'name' : u'GRE', 'choice_title' : [{'locale' : 'en', 'text' : 'Métropole Grenoble-Alpes-Métropole'},{'locale' : 'es', 'text' : 'Métropole Grenoble-Alpes-Métropole'},{'locale' : 'tr', 'text' : 'Métropole Grenoble-Alpes-Métropole'},{'locale' : 'de', 'text' : 'Métropole Grenoble-Alpes-Métropole'}, {'locale' : 'fr', 'text' : 'Métropole Grenoble-Alpes-Métropole' }]},
              {'name' : u'NIC', 'choice_title' : [{'locale' : 'en', 'text' : "Métropole Nice Côte d'Azur"},{'locale' : 'es', 'text' : "Métropole Nice Côte d'Azur"},{'locale' : 'tr', 'text' : "Métropole Nice Côte d'Azur"},{'locale' : 'de', 'text' : "Métropole Nice Côte d'Azur"}, {'locale' : 'fr', 'text' : "Métropole Nice Côte d'Azur" }]},
              {'name' : u'NRM', 'choice_title' : [{'locale' : 'en', 'text' : 'Métropole Rouen Normandie'},{'locale' : 'es', 'text' : 'Métropole Rouen Normandie'},{'locale' : 'tr', 'text' : 'Métropole Rouen Normandie'},{'locale' : 'de', 'text' : 'Métropole Rouen Normandie'}, {'locale' : 'fr', 'text' : 'Métropole Rouen Normandie' }]},
              {'name' : u'PRV', 'choice_title' : [{'locale' : 'en', 'text' : 'Métropole Toulon-Provence-Méditerranée'},{'locale' : 'es', 'text' : 'Métropole Toulon-Provence-Méditerranée'},{'locale' : 'tr', 'text' : 'Métropole Toulon-Provence-Méditerranée'},{'locale' : 'de', 'text' : 'Métropole Toulon-Provence-Méditerranée'}, {'locale' : 'fr', 'text' : 'Métropole Toulon-Provence-Méditerranée' }]},
              {'name' : u'MTZ', 'choice_title' : [{'locale' : 'en', 'text' : 'Metz Métropole'},{'locale' : 'es', 'text' : 'Metz Métropole'},{'locale' : 'tr', 'text' : 'Metz Métropole'},{'locale' : 'de', 'text' : 'Metz Métropole'}, {'locale' : 'fr', 'text' : 'Metz Métropole' }]},
              {'name' : u'MPT', 'choice_title' : [{'locale' : 'en', 'text' : 'Montpellier Méditerranée Métropole'},{'locale' : 'es', 'text' : 'Montpellier Méditerranée Métropole'},{'locale' : 'tr', 'text' : 'Montpellier Méditerranée Métropole'},{'locale' : 'de', 'text' : 'Montpellier Méditerranée Métropole'}, {'locale' : 'fr', 'text' : 'Montpellier Méditerranée Métropole' }]},
              {'name' : u'NTS', 'choice_title' : [{'locale' : 'en', 'text' : 'Nantes Métropole'},{'locale' : 'es', 'text' : 'Nantes Métropole'},{'locale' : 'tr', 'text' : 'Nantes Métropole'},{'locale' : 'de', 'text' : 'Nantes Métropole'}, {'locale' : 'fr', 'text' : 'Nantes Métropole' }]},
              {'name' : u'ORL', 'choice_title' : [{'locale' : 'en', 'text' : 'Orléans Métropole'},{'locale' : 'es', 'text' : 'Orléans Métropole'},{'locale' : 'tr', 'text' : 'Orléans Métropole'},{'locale' : 'de', 'text' : 'Orléans Métropole'}, {'locale' : 'fr', 'text' : 'Orléans Métropole' }]},
              {'name' : u'REN', 'choice_title' : [{'locale' : 'en', 'text' : 'Rennes Métropole'},{'locale' : 'es', 'text' : 'Rennes Métropole'},{'locale' : 'tr', 'text' : 'Rennes Métropole'},{'locale' : 'de', 'text' : 'Rennes Métropole'}, {'locale' : 'fr', 'text' : 'Rennes Métropole' }]},
              {'name' : u'SET', 'choice_title' : [{'locale' : 'en', 'text' : 'Saint-Etienne Métropole'},{'locale' : 'es', 'text' : 'Saint-Etienne Métropole'},{'locale' : 'tr', 'text' : 'Saint-Etienne Métropole'},{'locale' : 'de', 'text' : 'Saint-Etienne Métropole'}, {'locale' : 'fr', 'text' : 'Saint-Etienne Métropole' }]},
              {'name' : u'TLS', 'choice_title' : [{'locale' : 'en', 'text' : 'Toulouse Métropole'},{'locale' : 'es', 'text' : 'Toulouse Métropole'},{'locale' : 'tr', 'text' : 'Toulouse Métropole'},{'locale' : 'de', 'text' : 'Toulouse Métropole'}, {'locale' : 'fr', 'text' : 'Toulouse Métropole' }]},
              {'name' : u'TRS', 'choice_title' : [{'locale' : 'en', 'text' : 'Tours Métropole Val de Loire'},{'locale' : 'es', 'text' : 'Tours Métropole Val de Loire'},{'locale' : 'tr', 'text' : 'Tours Métropole Val de Loire'},{'locale' : 'de', 'text' : 'Tours Métropole Val de Loire'}, {'locale' : 'fr', 'text' : 'Tours Métropole Val de Loire' }]},
              {'name' : u'-', 'choice_title' : [{'locale' : 'en', 'text' : 'hors aire métropolitaine'},{'locale' : 'es', 'text' : 'hors aire métropolitaine'},{'locale' : 'tr', 'text' : 'hors aire métropolitaine'},{'locale' : 'de', 'text' : 'hors aire métropolitaine'}, {'locale' : 'fr', 'text' : 'hors aire métropolitaine' }]},
            ],
          },
          {	"name"		: u"COMCLASS_CODE__",
            "id"      : "filter_3",
            "col_name" : "COMCLASS_CODE",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Population"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Population" }],
            "choices"	: [
              {'name' : u'pop_0', 'choice_title' : [{'locale' : 'en', 'text' : '0-5000'},{'locale' : 'es', 'text' : '0-5000'},{'locale' : 'tr', 'text' : '0-5000'},{'locale' : 'de', 'text' : '0-5000'}, {'locale' : 'fr', 'text' : '0-5000' }]},
              {'name' : u'pop_1', 'choice_title' : [{'locale' : 'en', 'text' : '5000-20000'},{'locale' : 'es', 'text' : '5000-20000'},{'locale' : 'tr', 'text' : '5000-20000'},{'locale' : 'de', 'text' : '5000-20000'}, {'locale' : 'fr', 'text' : '5000-20000' }]},
              {'name' : u'pop_2', 'choice_title' : [{'locale' : 'en', 'text' : '20000-50000'},{'locale' : 'es', 'text' : '20000-50000'},{'locale' : 'tr', 'text' : '20000-50000'},{'locale' : 'de', 'text' : '20000-50000'}, {'locale' : 'fr', 'text' : '20000-50000' }]},
              {'name' : u'pop_3', 'choice_title' : [{'locale' : 'en', 'text' : '50000-100000'},{'locale' : 'es', 'text' : '50000-100000'},{'locale' : 'tr', 'text' : '50000-100000'},{'locale' : 'de', 'text' : '50000-100000'}, {'locale' : 'fr', 'text' : '50000-100000' }]},
              {'name' : u'pop_4', 'choice_title' : [{'locale' : 'en', 'text' : '100000 et plus'},{'locale' : 'es', 'text' : '100000 et plus'},{'locale' : 'tr', 'text' : '100000 et plus'},{'locale' : 'de', 'text' : '100000 et plus'}, {'locale' : 'fr', 'text' : '100000 et plus' }]},
            ],
          },
          {	"name"		: u"TYPO_CODE__",  
            "id"      : "filter_4",
            "col_name" : "TYPO_CODE",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Typology"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Typologie" }],
            "choices"	: [
              {'name' : u'COWORKING', 'choice_title' : [{'locale' : 'en', 'text' : 'Tiers lieux à dominante coworking'},{'locale' : 'es', 'text' : 'Tiers lieux à dominante coworking'},{'locale' : 'tr', 'text' : 'Tiers lieux à dominante coworking'},{'locale' : 'de', 'text' : 'Tiers lieux à dominante coworking'}, {'locale' : 'fr', 'text' : 'Tiers lieux à dominante coworking' }]},
              {'name' : u'FABLAB', 'choice_title' : [{'locale' : 'en', 'text' : 'Tiers lieux à dominante fablab'},{'locale' : 'es', 'text' : 'Tiers lieux à dominante fablab'},{'locale' : 'tr', 'text' : 'Tiers lieux à dominante fablab'},{'locale' : 'de', 'text' : 'Tiers lieux à dominante fablab'}, {'locale' : 'fr', 'text' : 'Tiers lieux à dominante fablab' }]},
              {'name' : u'info manquante', 'choice_title' : [{'locale' : 'en', 'text' : 'missing info'},{'locale' : 'es', 'text' : 'Tiers lieux à dominante fablab'},{'locale' : 'tr', 'text' : 'Tiers lieux à dominante fablab'},{'locale' : 'de', 'text' : 'Tiers lieux à dominante fablab'}, {'locale' : 'fr', 'text' : 'info manquante' }]},
            ],
          },
          {	"name"		: u"SOURCE__",
            "id"      : "filter_1",
            "col_name" : "SOURCE",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Sources"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Sources" }],
            "choices"	: [
              {"name" : u"CGET", "choice_title" : [{"locale" : "en", "text" : "Fondation la France s’engage"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "CGET" }]},
            ],
          },
        ],
        "app_version"    : version,
        "method"        : "GET",
        "help"          : u"define the endpoint to get data for : filters in search navbar",
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
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
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5d63b8d1328ed71684ce24b9", ## V2
        "args_options"  : [
          {  "app_arg" : "dataToken",        "arg" : "token",            "optional" : True, "in" : ["url","header"],  "default" : "", "type": "str" },
          {  "app_arg" : "page",             "arg" : "page",             "optional" : True, "in" : ["url"],           "default" : 1,  "type": "int" },
          {  "app_arg" : "perPage",          "arg" : "per_page",         "optional" : True, "in" : ["url"],           "default" : 25, "type": "int", "authorized" : [10, 25, 50, 100, 200, 300] },
          {  "app_arg" : "sortBy",           "arg" : "sort_by",          "optional" : True, "in" : ["url"],           "default" : "NOM_TL", "type": "str" },
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
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
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
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5d63b8d1328ed71684ce24b9", ## V2
        "args_options"  : [
          {  "app_arg" : "dataToken",  "arg" : "token",            "optional" : True, "in" : ["url","header"],  "default" : "", "type": "str" },
          {  "app_arg" : "page",       "arg" : "page",             "optional" : True, "in" : ["url"],           "default" : 1,  "type": "int" },
          {  "app_arg" : "perPage",    "arg" : "per_page",         "optional" : True, "in" : ["url"],           "default" : 300, "type": "int", "authorized" : [10, 25, 50, 100, 200, 300] },
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
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
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
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5d63b8d1328ed71684ce24b9", ## V2
        "args_options"  : [
          {  "app_arg" : "dataToken",  "arg" : "token",     "optional" : True,  "in" : ["url","header"],   "default" : "", "type": "str" },
          {  "app_arg" : "itemId",     "arg" : "item_id",   "optional" : False, "in" : ["url"],           "default" : "", "type": "str" },
        ],
        "resp_fields" : {
          "projects" : { "resp_format" : "list", "path" : "data/data_raw/f_data" },
          "total"    : { "resp_format" : "int",  "path" : "data/data_raw/f_data_count" },
        },
        "app_version"    : version,
        "method"        : "GET",
        "help"          : u"define the endpoint to get data for : a detailled data",
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
        "is_default"    : True
      },

      ### DATA STATS
      { "field"         : "tl_data_API_stats",
        "is_visible"    : True,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "stat",
        "dataset_uri"   : "recherche",
        "content"       : u"apiviz default API endpoint for stats results",

        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one_stats/5d63b8d1328ed71684ce24b9", ## V2

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
                  "agg_field" : "TYPO_CODE",
                  "agg_sum_type" : "count_items", 
                  "agg_needs_unwind" : False,
                  "agg_unwind_separator" : "-"
                },
                { 
                  "agg_field" : "NOMREG",
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
                  "agg_field" : "TYPO_CODE",
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

        "app_version"    : version,
        "method"        : "POST",
        "help"          : u"define the endpoint to get data for : a stat about the dataset",
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
        "is_default"    : True
      },

      ### DATA MAP
      { "field"         : "tl_data_API_map",
        "is_visible"    : True,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "map",
        "dataset_uri"   : "recherche",

        "map_options"   : {
          
          ### TO ADAPT TO MAPBOX-GL-JS OPTIONS
          "url"              : "https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png",
          "attribution"      : '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
          "subdomains"       : 'abcd',
          "center"           : [46.2276, 2.2137],
          "currentCenter"    : [46.2276, 2.2137],
          "zoom"             : 5,
          "maxZoom"          : 18,
          "minZoom"          : 2,
          "useMarkerCluster" : True,
          "pinIconUrl"       : "/static/icons/icon_pin_plein_violet.svg",
          "pinIconSize"      : { "highlighted" : [46, 46], "normal" : [29, 29]}
        
        },

        "content"       : u"apiviz default API endpoint for map results",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5d63b8d1328ed71684ce24b9", ## V2
        "args_options"  : [
          {  "app_arg" : "dataToken",  "arg" : "token",            "optional" : True, "in" : ["url","header"], "default" : "",   "type": "str" },

          {  "app_arg" : "forMap",       "arg" : "map_list",          "optional" : False, "in" : ["url"], "default" : True,        "type": "bool" },
          # {  "app_arg" : "defaultValue", "arg" : "fields_to_return",  "optional" : False, "in" : ["url"], "default" : "INSEEDEP",  "type": "str" },
          {  "app_arg" : "defaultValue", "arg" : "fields_to_return",  "optional" : False, "in" : ["url"], "default" : "INSEEDEP,INSEECOM",  "type": "str" },
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
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
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
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/exports/as_csv/5d63b8d1328ed71684ce24b9", ## V2
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
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
        "is_default"    : True
      },

]
