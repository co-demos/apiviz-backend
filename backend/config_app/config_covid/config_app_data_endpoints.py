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
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
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
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
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
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
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
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
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
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
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
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
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
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
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
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
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
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
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
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
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
          {"locale" : "en", "text" : "Enter the name of an initiative"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Tapez le nom d'une initiative" }
        ],
        "items_found"   : [
          {"locale" : "en", "text" : "initiatives found"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "initiatives trouvés" }
        ],
        "stats_text"   : [
          {"locale" : "en", "text" : "experimental"},{"locale" : "es", "text" : "experimental"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "expérimental" }
        ],
        "reset"   : [
          {"locale" : "en", "text" : "reset"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "effacer" }
        ],

        "content"       : u"apiviz default API endpoint for navbar filters",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5e7a3778328ed76a89d25794",  
        "args_options"  : [
          {  "app_arg" : "dataToken",      "arg" : "token",             "optional" : True, "in" : ["url","header"],   "default" : "",   "type": "str" },
          {  "app_arg" : "filtersList",    "arg" : "get_filters",       "optional" : False, "in" : ["url"],           "default" : True, "type": "bool" }, # also working with dsi?
          {  "app_arg" : "filterChoices",  "arg" : "get_uniques",       "optional" : False, "in" : ["url"],           "default" : "tag", "type": "str" },
        ],

        "filter_options" : [

          {	"name"		: u"tag_besoin_niv1_code__",
            "id"      : "filter_1",
            "col_name" : "tag_besoin_niv1_code",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Needs"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Besoins" }],
            "choices"	: [
              {'name' : u'NA', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'NA' }]},
              # ADMINISTRATIF
              # ALIMENTAIRE
              # DATA
              # EDUCATION
              # FINANCE
              # HELP
              # INFOS
              # LOISIRS
              # SANTE
              # SOCIAL
              {'name' : u'ADMINISTRATIF', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'ADMINISTRATIF' }]},
              {'name' : u'ALIMENTAIRE', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'ALIMENTAIRE' }]},
              {'name' : u'DATA', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'DATA' }]},
              {'name' : u'EDUCATION', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'EDUCATION' }]},
              {'name' : u'FINANCE', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'FINANCE' }]},
              {'name' : u'HELP', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'HElP' }]},
              {'name' : u'INFOS', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'INFOS' }]},
              {'name' : u'LOISIRS', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'LOISIRS' }]},
              {'name' : u'SANTE', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'SANTE' }]},
              {'name' : u'SOCIAL', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'SOCIAL' }]},

            ],
          },
          {	"name"		: u"tag_besoin_niv2_code__",
            "id"      : "filter_2",
            "col_name" : "tag_besoin_niv2_code",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Needs 2"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Besoins 2" }],
            "choices"	: [
              {'name' : u'NA', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'NA' }]},
              # CARTO
              # HELP
              # HOPITAL
              # HYGIENE
              # REA
              # TEST
              # DEV
              # PROTECTION
              # SCIENCE
              {'name' : u'CARTO', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'CARTO' }]},
              {'name' : u'HELP', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'HELP' }]},
              {'name' : u'HOPITAL', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'HOPITAL' }]},
              {'name' : u'HYGIENE', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'HYGIENE' }]},
              {'name' : u'REA', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'REA' }]},
              {'name' : u'TEST', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'TEST' }]},
              {'name' : u'DEV', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'DEV' }]},
              {'name' : u'PROTECTION', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'PROTECTION' }]},
              {'name' : u'SCIENCE', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'SCIENCE' }]},

            ],
          },
          {	"name"		: u"tag_produit_niv1_code__",  
            "id"      : "filter_3",
            "col_name" : "tag_produit_niv1_code",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Products"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Produits" }],
            "choices"	: [
              {'name' : u'NA', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'NA' }]},
              # APP
              # COURS
              # DATA
              # DIY
              # GROUPE
              # INDUSTRIEL
              # LISTE
              # MEDIA
              # PRO
              # REPO
              {'name' : u'APP', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'APP' }]},
              {'name' : u'COURS', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'COURS' }]},
              {'name' : u'DATA', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'DATA' }]},
              {'name' : u'DIY', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'DIY' }]},
              {'name' : u'GROUPE', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'GROUPE' }]},
              {'name' : u'INDUSTRIEL', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'INDUSTRIEL' }]},
              {'name' : u'LISTE', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'LISTE' }]},
              {'name' : u'MEDIA', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'MEDIA' }]},
              {'name' : u'PRO', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'PRO' }]},
              {'name' : u'REPO', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'REPO' }]},

            ],
          },
          {	"name"		: u"tag_produit_niv2_code__",  
            "id"      : "filter_4",
            "col_name" : "tag_produit_niv2_code",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Products 2"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Produits 2" }],
            "choices"	: [
              {'name' : u'NA', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'NA' }]},
              # CARTO
              # DIY
              # GEL
              # HYGIENE
              # LUNETTES
              # MASQUE
              # MASQUE_TISSU
              # POUSSE_SERINGUE
              # PROTECTION
              # RESPIRATEUR
              # TEST
              # TESTKIT
              # VENTILATOR
              # VISIERE
              {'name' : u'CARTO', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'CARTO' }]},
              {'name' : u'DIY', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'DIY' }]},
              {'name' : u'GEL', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'GEL' }]},
              {'name' : u'HYGIENE', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'HYGIENE' }]},
              {'name' : u'LUNETTES', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'LUNETTES' }]},
              {'name' : u'MASQUE', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'MASQUE' }]},
              {'name' : u'MASQUE_TISSU', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'MASQUE_TISSU' }]},
              {'name' : u'POUSSE_SERINGUE', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'POUSSE_SERINGUE' }]},
              {'name' : u'PROTECTION', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'PROTECTION' }]},
              {'name' : u'RESPIRATEUR', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'RESPIRATEUR' }]},
              {'name' : u'TEST', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'TEST' }]},
              {'name' : u'TESTKIT', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'TESTKIT' }]},
              {'name' : u'VENTILATOR', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'VENTILATOR' }]},
              {'name' : u'VISIERE', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'VISIERE' }]},
            ],
          },
          {	"name"		: u"validation__",  
            "id"      : "filter_4",
            "col_name" : "validation",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Validation"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Validation" }],
            "choices"	: [
              # OUI
              # NON
              # PARTIELLE
              # NR
              # ?
              {'name' : u'OUI', 'choice_title' : [{'locale' : 'en', 'text' : 'Yes'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'Oui' }]},
              {'name' : u'NON', 'choice_title' : [{'locale' : 'en', 'text' : 'No'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'Non' }]},
              {'name' : u'PARTIELLE', 'choice_title' : [{'locale' : 'en', 'text' : 'Partially'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'Partielle' }]},
              {'name' : u'NR', 'choice_title' : [{'locale' : 'en', 'text' : 'NR'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'Non renseigné' }]},
              {'name' : u'?', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : '?' }]},
            ],
          },
          {	"name"		: u"tag_structure_niv1_code__",  
            "id"      : "filter_5",
            "col_name" : "tag_structure_niv1_code",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Structures"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Structures" }],
            "choices"	: [
              # ANONYME
              # ASSO
              # GROUPE
              # INDIVIDU
              # INSTITUTION
              # NR
              # ?
              {'name' : u'ANONYME', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'ANONYME' }]},
              {'name' : u'ASSO', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'ASSO' }]},
              {'name' : u'GROUPE', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'GROUPE' }]},
              {'name' : u'INDIVIDU', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'INDIVIDU' }]},
              {'name' : u'INSTITUTION', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'INSTITUTION' }]},
              {'name' : u'NR', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : 'NR' }]},
              {'name' : u'?', 'choice_title' : [{'locale' : 'en', 'text' : 'HEALTH'},{'locale' : 'es', 'text' : '-'},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : '-'}, {'locale' : 'fr', 'text' : '?' }]},

            ],
          },

        ],
        "app_version"    : version,
        "method"        : "GET",
        "help"          : u"define the endpoint to get data for : filters in search navbar",
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
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
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5e7a3778328ed76a89d25794", ## V2
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
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
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
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5e7a3778328ed76a89d25794", ## V2
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
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
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
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5e7a3778328ed76a89d25794", ## V2
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
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
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

        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one_stats/5e7a3778328ed76a89d25794", ## V2

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
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
        "is_default"    : True
      },

      ### DATA MAP
      { "field"         : "tl_data_API_map",
        "is_visible"    : False,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "map",
        "dataset_uri"   : "recherche",

        # "map_options"   : {
          
        #   ### TO ADAPT TO MAPBOX-GL-JS OPTIONS
        #   "url"              : "https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png",
        #   "attribution"      : '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        #   "subdomains"       : 'abcd',
        #   "center"           : [46.2276, 2.2137],
        #   "currentCenter"    : [46.2276, 2.2137],
        #   "zoom"             : 5,
        #   "maxZoom"          : 18,
        #   "minZoom"          : 2,
        #   "useMarkerCluster" : True,
        #   "pinIconUrl"       : "/static/icons/icon_pin_plein_violet.svg",
        #   "pinIconSize"      : { "highlighted" : [46, 46], "normal" : [29, 29]}
        
        # },

        "content"       : u"apiviz default API endpoint for map results",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5e7a3778328ed76a89d25794", ## V2
        "args_options"  : [
          {  "app_arg" : "dataToken",  "arg" : "token",            "optional" : True, "in" : ["url","header"], "default" : "",   "type": "str" },

          {  "app_arg" : "forMap",       "arg" : "map_list",          "optional" : False, "in" : ["url"], "default" : True,        "type": "bool" },
          # {  "app_arg" : "defaultValue", "arg" : "fields_to_return",  "optional" : False, "in" : ["url"], "default" : "INSEEDEP",  "type": "str" },
          {  "app_arg" : "defaultValue", "arg" : "fields_to_return",  "optional" : False, "in" : ["url"], "default" : "result_context,DEPARTEMENT",  "type": "str" },
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
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
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
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/exports/as_csv/5e7a3778328ed76a89d25794", ## V2
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
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
        "is_default"    : True
      },

]
