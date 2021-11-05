# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_socials_config = [

  ### - - - - - - - - - - - - - - - ###
  ### CONFIG PING
  
    ### SOCIAL NETWORKS
    { "field"       : "app_twitter",
      "content"     : u"twitter",
      "icon_class"  : "fab fa-twitter",
      "url"         : "https://twitter.com/opendata_fr",
      "app_version" : version,
      "help"        : u"Choose the twitter account for your ApiViz instance",
      "in_footer"   : True,
      "tooltip"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "notre page Twitter" }],
      "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
      "is_default"  : True
    },

    # { "field"       : "app_facebook",
    #   "content"     : u"facebook",
    #   "icon_class"  : "fab fa-facebook-f",
    #   "url"         : "https://www.facebook.com/AssociationPiNG/",
    #   "app_version" : version,
    #   "help"        : u"Choose the facebook account for your ApiViz instance",
    #   "in_footer"   : True,
    #   "tooltip"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "notre page sur Facebook" }],
    #   "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
    #   "is_default"  : True
    # },

    { "field"       : "app_linkedin",
      "content"     : u"linkedin",
      "icon_class"  : "fab fa-linkedin",
      "url"         : "https://www.linkedin.com/company/opendatafr/",
      "app_version" : version,
      "help"        : u"Choose the linkedin account for your ApiViz instance",
      "in_footer"   : True,
      "tooltip"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "notre page linkedin" }],
      "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
      "is_default"  : True
    },

    { "field"       : "app_github",
      "content"     : u"github",
      "icon_class"  : "fab fa-github",
      "url"         : "https://github.com/co-demos/ODF-carto",
      "app_version" : version,
      "help"        : u"Choose the github account for your ApiViz instance",
      "in_footer"   : True,
      "tooltip"     : [{"locale" : "en", "text" : "source codes"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "codes sources" }],
      "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
      "is_default"  : True
    },

  ### CUSTOM SOCIAL NETWORKS --> TO BE ADDED VIA BACK OFFICE BY ADMIN USER 
  ### ...

]
