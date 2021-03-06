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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
        "is_default"    : True
      },


    ### - - - - - - - - - - - - - - - ###
    ### DATA ENDPOINTS
    ### - - - - - - - - - - - - - - - ###

    ## repos dsi_oid / solidata : 5dd57679328ed74add976bfe

      ### DATA FILTERS
      { "field"         : "repos_data_API_filters",
        "is_visible"    : True,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "filters",
        "dataset_uri"   : "repos",
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
          {"locale" : "en", "text" : "Enter the name of a place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Tapez le nom d'un logiciel" }
        ],
        "items_found"   : [
          {"locale" : "en", "text" : "places found"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "logiciels trouvés" }
        ],
        "stats_text"   : [
          {"locale" : "en", "text" : "experimental"},{"locale" : "es", "text" : "experimental"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "expérimental" }
        ],
        "reset"   : [
          {"locale" : "en", "text" : "reset"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "effacer" }
        ],

        "content"       : u"apiviz default API endpoint for navbar filters",
        # "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7f0438328ed72e431f338e",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5dd57679328ed74add976bfe",  
        "args_options"  : [
          {  "app_arg" : "dataToken",      "arg" : "token",             "optional" : True, "in" : ["url","header"],   "default" : "",   "type": "str" },
          {  "app_arg" : "filtersList",    "arg" : "get_filters",       "optional" : False, "in" : ["url"],           "default" : True, "type": "bool" }, # also working with dsi?
          {  "app_arg" : "filterChoices",  "arg" : "get_uniques",       "optional" : False, "in" : ["url"],           "default" : "tag", "type": "str" },
        ],

        "filter_options" : [

          {	"name"		: u"plateforme__",
            "id"      : "filter_1",
            "col_name" : "plateforme",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Organisation"},{"locale" : "es", "text" : "Organisation"},{"locale" : "tr", "text" : "Organisation"},{"locale" : "de", "text" : "Organisation"}, {"locale" : "fr", "text" : "Plateforme" }],
            "choices"	: [
              {'name' : u'Github', 'choice_title' : [{'locale' : 'en', 'text' : 'Github'},{'locale' : 'es', 'text' : 'Bordeaux Métropole'},{'locale' : 'tr', 'text' : 'Github'},{'locale' : 'de', 'text' : 'Github'}, {'locale' : 'fr', 'text' : 'Github' }]},
              {'name' : u'Gitlab', 'choice_title' : [{'locale' : 'en', 'text' : 'Gitlab'},{'locale' : 'es', 'text' : 'Bordeaux Métropole'},{'locale' : 'tr', 'text' : 'Gitlab'},{'locale' : 'de', 'text' : 'Gitlab'}, {'locale' : 'fr', 'text' : 'Gitlab' }]},
            ],
          },

          {	"name"		: u"licence__",
            "id"      : "filter_2",
            "col_name" : "licence",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Organisation"},{"locale" : "es", "text" : "Organisation"},{"locale" : "tr", "text" : "Organisation"},{"locale" : "de", "text" : "Organisation"}, {"locale" : "fr", "text" : "Licence" }],
            "choices"	: [
              {'name' : u'Apache License 2.0', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'Apache License 2.0' }]},
              {'name' : u'Eclipse Public License 1.0', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'Eclipse Public License 1.0' }]},
              {'name' : u'GNU Affero General Public License v3.0', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : ' GNU Affero General Public License v3.0 ' }]},
              {'name' : u'GNU Lesser General Public License v2.1', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'GNU Lesser General Public License v2.1 ' }]},
              {'name' : u'MIT License', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'MIT License' }]},
              {'name' : u'Other', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'Other' }]},
            ],
          },

          {	"name"		: u"langage__",
            "id"      : "filter_3",
            "col_name" : "langage",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "langage"},{"locale" : "es", "text" : "Organisation"},{"locale" : "tr", "text" : "Organisation"},{"locale" : "de", "text" : "Organisation"}, {"locale" : "fr", "text" : "Langage" }],
            "choices"	: [
              {'name' : u'Assembly', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'Assembly' }]},
              {'name' : u'C', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'C' }]},
              {'name' : u'C++', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'C++' }]},
              {'name' : u'CartoCSS', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'CartoCSS' }]},
              {'name' : u'CSS', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'CSS' }]},
              {'name' : u'Java', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'Java' }]},
              {'name' : u'Javascript', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'Javascript' }]},
              {'name' : u'Jupyter Notebook', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'Jupyter Notebook' }]},
              {'name' : u'Go', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'Go' }]},
              {'name' : u'HTML', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'HTML' }]},
              {'name' : u'OCaml', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'OCaml' }]},
              {'name' : u'PHP', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'PHP' }]},
              {'name' : u'PLpgSQL', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'PLpgSQL' }]},
              {'name' : u'PowerShell', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'PowerShell' }]},
              {'name' : u'Puppet', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'Puppet' }]},
              {'name' : u'Python', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'Python' }]},
              {'name' : u'QML', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'QML' }]},
              {'name' : u'R', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'R' }]},
              {'name' : u'Ruby', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'Ruby' }]},
              {'name' : u'Shell', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'Shell' }]},
              {'name' : u'TypeScript', 'choice_title' : [{'locale' : 'en', 'text' : ''},{'locale' : 'es', 'text' : ''},{'locale' : 'tr', 'text' : ''},{'locale' : 'de', 'text' : ''}, {'locale' : 'fr', 'text' : 'TypeScript' }]},
            ],
          },

          # {	"name"		: u"COMCLASS_CODE__",
          #   "id"      : "filter_3",
          #   "col_name" : "COMCLASS_CODE",
          #   "dataType" : "text",
          #   "filter_title" : [{"locale" : "en", "text" : "Population"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Population" }],
          #   "choices"	: [
          #     {'name' : u'pop_0', 'choice_title' : [{'locale' : 'en', 'text' : '0-5000'},{'locale' : 'es', 'text' : '0-5000'},{'locale' : 'tr', 'text' : '0-5000'},{'locale' : 'de', 'text' : '0-5000'}, {'locale' : 'fr', 'text' : '0-5000' }]},
          #     {'name' : u'pop_1', 'choice_title' : [{'locale' : 'en', 'text' : '5000-20000'},{'locale' : 'es', 'text' : '5000-20000'},{'locale' : 'tr', 'text' : '5000-20000'},{'locale' : 'de', 'text' : '5000-20000'}, {'locale' : 'fr', 'text' : '5000-20000' }]},
          #     {'name' : u'pop_2', 'choice_title' : [{'locale' : 'en', 'text' : '20000-50000'},{'locale' : 'es', 'text' : '20000-50000'},{'locale' : 'tr', 'text' : '20000-50000'},{'locale' : 'de', 'text' : '20000-50000'}, {'locale' : 'fr', 'text' : '20000-50000' }]},
          #     {'name' : u'pop_3', 'choice_title' : [{'locale' : 'en', 'text' : '50000-100000'},{'locale' : 'es', 'text' : '50000-100000'},{'locale' : 'tr', 'text' : '50000-100000'},{'locale' : 'de', 'text' : '50000-100000'}, {'locale' : 'fr', 'text' : '50000-100000' }]},
          #     {'name' : u'pop_4', 'choice_title' : [{'locale' : 'en', 'text' : '100000 et plus'},{'locale' : 'es', 'text' : '100000 et plus'},{'locale' : 'tr', 'text' : '100000 et plus'},{'locale' : 'de', 'text' : '100000 et plus'}, {'locale' : 'fr', 'text' : '100000 et plus' }]},
          #   ],
          # },
          # {	"name"		: u"TYPO_CODE__",  
          #   "id"      : "filter_4",
          #   "col_name" : "TYPO_CODE",
          #   "dataType" : "text",
          #   "filter_title" : [{"locale" : "en", "text" : "Typology"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Typologie" }],
          #   "choices"	: [
          #     {'name' : u'COWORKING', 'choice_title' : [{'locale' : 'en', 'text' : 'Tiers lieux à dominante coworking'},{'locale' : 'es', 'text' : 'Tiers lieux à dominante coworking'},{'locale' : 'tr', 'text' : 'Tiers lieux à dominante coworking'},{'locale' : 'de', 'text' : 'Tiers lieux à dominante coworking'}, {'locale' : 'fr', 'text' : 'Tiers lieux à dominante coworking' }]},
          #     {'name' : u'FABLAB', 'choice_title' : [{'locale' : 'en', 'text' : 'Tiers lieux à dominante fablab'},{'locale' : 'es', 'text' : 'Tiers lieux à dominante fablab'},{'locale' : 'tr', 'text' : 'Tiers lieux à dominante fablab'},{'locale' : 'de', 'text' : 'Tiers lieux à dominante fablab'}, {'locale' : 'fr', 'text' : 'Tiers lieux à dominante fablab' }]},
          #     {'name' : u'info manquante', 'choice_title' : [{'locale' : 'en', 'text' : 'missing info'},{'locale' : 'es', 'text' : 'Tiers lieux à dominante fablab'},{'locale' : 'tr', 'text' : 'Tiers lieux à dominante fablab'},{'locale' : 'de', 'text' : 'Tiers lieux à dominante fablab'}, {'locale' : 'fr', 'text' : 'info manquante' }]},
          #   ],
          # },
          # {	"name"		: u"SOURCE__",
          #   "id"      : "filter_1",
          #   "col_name" : "SOURCE",
          #   "dataType" : "text",
          #   "filter_title" : [{"locale" : "en", "text" : "Sources"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Sources" }],
          #   "choices"	: [
          #     {"name" : u"CGET", "choice_title" : [{"locale" : "en", "text" : "Fondation la France s’engage"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "CGET" }]},
          #   ],
          # },
        ],
        "app_version"    : version,
        "method"        : "GET",
        "help"          : u"define the endpoint to get data for : filters in search navbar",
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
        "is_default"    : True
      },

      ### DATA TABLE
      { "field"         : "repos_data_API_table",
        "is_visible"    : True,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "table",
        "dataset_uri"   : "repos",
        "content"       : u"apiviz default API endpoint for list results",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5dd57679328ed74add976bfe", 
        "args_options"  : [
          {  "app_arg" : "dataToken",        "arg" : "token",            "optional" : True, "in" : ["url","header"],  "default" : "", "type": "str" },
          {  "app_arg" : "page",             "arg" : "page",             "optional" : True, "in" : ["url"],           "default" : 1,  "type": "int" },
          {  "app_arg" : "perPage",          "arg" : "per_page",         "optional" : True, "in" : ["url"],           "default" : 25, "type": "int", "authorized" : [10, 25, 50, 100, 200, 300] },
          {  "app_arg" : "sortBy",           "arg" : "sort_by",          "optional" : True, "in" : ["url"],           "default" : "nom", "type": "str" },
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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
        "is_default"    : True
      },

      ### DATA LIST
      { "field"         : "repos_data_API_list",
        "is_visible"    : True,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "list",
        "dataset_uri"   : "repos",
        "content"       : u"apiviz default API endpoint for list results",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5dd57679328ed74add976bfe", 
        "args_options"  : [
          {  "app_arg" : "dataToken",  "arg" : "token",            "optional" : True, "in" : ["url","header"],  "default" : "", "type": "str" },
          {  "app_arg" : "page",       "arg" : "page",             "optional" : True, "in" : ["url"],           "default" : 1,  "type": "int" },
          {  "app_arg" : "perPage",    "arg" : "per_page",         "optional" : True, "in" : ["url"],           "default" : 300, "type": "int", "authorized" : [10, 25, 50, 100, 200, 300] },
          # {  "app_arg" : "sortBy",     "arg" : "sort_by",          "optional" : True, "in" : ["url"],           "default" : "nom", "type": "str" },
          # {  "app_arg" : "sortIsDescending", "arg" : "descending", "optional" : True, "in" : ["url"],           "default" : False, "type": "bool" },
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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
        "is_default"    : True
      },

      ### DATA DETAIL
      { "field"         : "repos_data_API_detail",
        "is_visible"    : True,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "detail",
        "dataset_uri"   : "repos",
        "content"       : u"apiviz default API endpoint for detailled results",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5dd57679328ed74add976bfe", 
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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
        "is_default"    : True
      },

      ### DATA STATS
      { "field"         : "repos_data_API_stats",
        "is_visible"    : False,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "stat",
        "dataset_uri"   : "repos",
        "content"       : u"apiviz default API endpoint for stats results",

        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one_stats/5dd57679328ed74add976bfe", 

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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
        "is_default"    : True
      },

      ### DATA EXPORT
      { "field"         : "repos_data_API_export",
        "is_visible"    : True,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "export",
        "dataset_uri"   : "repos",
        "content"       : u"apiviz default API endpoint for export results",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/exports/as_csv/5dd57679328ed74add976bfe", 
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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
        "is_default"    : True
      },

    ## orgas  dsi_oid / solidata : 5dd576a1328ed74add977a99

      ### DATA FILTERS
      { "field"         : "orgas_data_API_filters",
        "is_visible"    : True,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "filters",
        "dataset_uri"   : "orgas",
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
        # "root_url"      : "https://solidata-api.co-demos.com/api/dso/infos/get_one/5c7f0438328ed72e431f338e",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5dd576a1328ed74add977a99",  
        "args_options"  : [
          {  "app_arg" : "dataToken",      "arg" : "token",             "optional" : True, "in" : ["url","header"],   "default" : "",   "type": "str" },
          {  "app_arg" : "filtersList",    "arg" : "get_filters",       "optional" : False, "in" : ["url"],           "default" : True, "type": "bool" }, # also working with dsi?
          {  "app_arg" : "filterChoices",  "arg" : "get_uniques",       "optional" : False, "in" : ["url"],           "default" : "tag", "type": "str" },
        ],

        "filter_options" : [

          {	"name"		: u"plateforme__",
            "id"      : "filter_1",
            "col_name" : "plateforme",
            "dataType" : "text",
            "filter_title" : [{"locale" : "en", "text" : "Organisation"},{"locale" : "es", "text" : "Organisation"},{"locale" : "tr", "text" : "Organisation"},{"locale" : "de", "text" : "Organisation"}, {"locale" : "fr", "text" : "Plateforme" }],
            "choices"	: [
              {'name' : u'Github', 'choice_title' : [{'locale' : 'en', 'text' : 'Github'},{'locale' : 'es', 'text' : 'Bordeaux Métropole'},{'locale' : 'tr', 'text' : 'Github'},{'locale' : 'de', 'text' : 'Github'}, {'locale' : 'fr', 'text' : 'Github' }]},
              {'name' : u'Gitlab', 'choice_title' : [{'locale' : 'en', 'text' : 'Gitlab'},{'locale' : 'es', 'text' : 'Bordeaux Métropole'},{'locale' : 'tr', 'text' : 'Gitlab'},{'locale' : 'de', 'text' : 'Gitlab'}, {'locale' : 'fr', 'text' : 'Gitlab' }]},
            ],
          },
          # {	"name"		: u"COMCLASS_CODE__",
          #   "id"      : "filter_3",
          #   "col_name" : "COMCLASS_CODE",
          #   "dataType" : "text",
          #   "filter_title" : [{"locale" : "en", "text" : "Population"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Population" }],
          #   "choices"	: [
          #     {'name' : u'pop_0', 'choice_title' : [{'locale' : 'en', 'text' : '0-5000'},{'locale' : 'es', 'text' : '0-5000'},{'locale' : 'tr', 'text' : '0-5000'},{'locale' : 'de', 'text' : '0-5000'}, {'locale' : 'fr', 'text' : '0-5000' }]},
          #     {'name' : u'pop_1', 'choice_title' : [{'locale' : 'en', 'text' : '5000-20000'},{'locale' : 'es', 'text' : '5000-20000'},{'locale' : 'tr', 'text' : '5000-20000'},{'locale' : 'de', 'text' : '5000-20000'}, {'locale' : 'fr', 'text' : '5000-20000' }]},
          #     {'name' : u'pop_2', 'choice_title' : [{'locale' : 'en', 'text' : '20000-50000'},{'locale' : 'es', 'text' : '20000-50000'},{'locale' : 'tr', 'text' : '20000-50000'},{'locale' : 'de', 'text' : '20000-50000'}, {'locale' : 'fr', 'text' : '20000-50000' }]},
          #     {'name' : u'pop_3', 'choice_title' : [{'locale' : 'en', 'text' : '50000-100000'},{'locale' : 'es', 'text' : '50000-100000'},{'locale' : 'tr', 'text' : '50000-100000'},{'locale' : 'de', 'text' : '50000-100000'}, {'locale' : 'fr', 'text' : '50000-100000' }]},
          #     {'name' : u'pop_4', 'choice_title' : [{'locale' : 'en', 'text' : '100000 et plus'},{'locale' : 'es', 'text' : '100000 et plus'},{'locale' : 'tr', 'text' : '100000 et plus'},{'locale' : 'de', 'text' : '100000 et plus'}, {'locale' : 'fr', 'text' : '100000 et plus' }]},
          #   ],
          # },
          # {	"name"		: u"TYPO_CODE__",  
          #   "id"      : "filter_4",
          #   "col_name" : "TYPO_CODE",
          #   "dataType" : "text",
          #   "filter_title" : [{"locale" : "en", "text" : "Typology"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Typologie" }],
          #   "choices"	: [
          #     {'name' : u'COWORKING', 'choice_title' : [{'locale' : 'en', 'text' : 'Tiers lieux à dominante coworking'},{'locale' : 'es', 'text' : 'Tiers lieux à dominante coworking'},{'locale' : 'tr', 'text' : 'Tiers lieux à dominante coworking'},{'locale' : 'de', 'text' : 'Tiers lieux à dominante coworking'}, {'locale' : 'fr', 'text' : 'Tiers lieux à dominante coworking' }]},
          #     {'name' : u'FABLAB', 'choice_title' : [{'locale' : 'en', 'text' : 'Tiers lieux à dominante fablab'},{'locale' : 'es', 'text' : 'Tiers lieux à dominante fablab'},{'locale' : 'tr', 'text' : 'Tiers lieux à dominante fablab'},{'locale' : 'de', 'text' : 'Tiers lieux à dominante fablab'}, {'locale' : 'fr', 'text' : 'Tiers lieux à dominante fablab' }]},
          #     {'name' : u'info manquante', 'choice_title' : [{'locale' : 'en', 'text' : 'missing info'},{'locale' : 'es', 'text' : 'Tiers lieux à dominante fablab'},{'locale' : 'tr', 'text' : 'Tiers lieux à dominante fablab'},{'locale' : 'de', 'text' : 'Tiers lieux à dominante fablab'}, {'locale' : 'fr', 'text' : 'info manquante' }]},
          #   ],
          # },
          # {	"name"		: u"SOURCE__",
          #   "id"      : "filter_1",
          #   "col_name" : "SOURCE",
          #   "dataType" : "text",
          #   "filter_title" : [{"locale" : "en", "text" : "Sources"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Sources" }],
          #   "choices"	: [
          #     {"name" : u"CGET", "choice_title" : [{"locale" : "en", "text" : "Fondation la France s’engage"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "CGET" }]},
          #   ],
          # },
        ],
        "app_version"    : version,
        "method"        : "GET",
        "help"          : u"define the endpoint to get data for : filters in search navbar",
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
        "is_default"    : True
      },

      ### DATA TABLE
      { "field"         : "orgas_data_API_table",
        "is_visible"    : False,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "table",
        "dataset_uri"   : "orgas",
        "content"       : u"apiviz default API endpoint for list results",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5dd576a1328ed74add977a99", 
        "args_options"  : [
          {  "app_arg" : "dataToken",        "arg" : "token",            "optional" : True, "in" : ["url","header"],  "default" : "", "type": "str" },
          {  "app_arg" : "page",             "arg" : "page",             "optional" : True, "in" : ["url"],           "default" : 1,  "type": "int" },
          {  "app_arg" : "perPage",          "arg" : "per_page",         "optional" : True, "in" : ["url"],           "default" : 25, "type": "int", "authorized" : [10, 25, 50, 100, 200, 300] },
          {  "app_arg" : "sortBy",           "arg" : "sort_by",          "optional" : True, "in" : ["url"],           "default" : "nom", "type": "str" },
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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
        "is_default"    : True
      },

      ### DATA LIST
      { "field"         : "orgas_data_API_list",
        "is_visible"    : True,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "list",
        "dataset_uri"   : "orgas",
        "content"       : u"apiviz default API endpoint for list results",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5dd576a1328ed74add977a99", 
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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
        "is_default"    : True
      },

      ### DATA DETAIL
      { "field"         : "orgas_data_API_detail",
        "is_visible"    : True,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "detail",
        "dataset_uri"   : "orgas",
        "content"       : u"apiviz default API endpoint for detailled results",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one/5dd576a1328ed74add977a99", 
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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
        "is_default"    : True
      },

      ### DATA STATS
      { "field"         : "orgas_data_API_stats",
        "is_visible"    : False,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "stat",
        "dataset_uri"   : "orgas",
        "content"       : u"apiviz default API endpoint for stats results",

        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/infos/get_one_stats/5dd576a1328ed74add977a99", 

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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
        "is_default"    : True
      },

      ### DATA EXPORT
      { "field"         : "orgas_data_API_export",
        "is_visible"    : True,
        "is_disabled"   : False,
        "data_type"     : "data",
        "endpoint_type" : "export",
        "dataset_uri"   : "orgas",
        "content"       : u"apiviz default API endpoint for export results",
        "root_url"      : "https://solidata-api.co-demos.com/api/dsi/exports/as_csv/5dd576a1328ed74add977a99", 
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
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
        "is_default"    : True
      },


]
