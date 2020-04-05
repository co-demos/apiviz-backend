# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_socials_config = [

  ### - - - - - - - - - - - - - - - ###
  ### CONFIG PING
  
    ### SOCIAL NETWORKS
    # { "field"       : "app_twitter",
    #   "content"     : u"twitter",
    #   "icon_class"  : "fab fa-twitter",
    #   "url"         : "https://twitter.com/assoping",
    #   "app_version" : version,
    #   "help"        : u"Choose the twitter account for your ApiViz instance",
    #   "in_footer"   : True,
    #   "tooltip"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "notre page Twitter" }],
    #   "apiviz_front_uuid" : uuid_models["uuid_covid"],
    #   "is_default"  : True
    # },

    # { "field"       : "app_facebook",
    #   "content"     : u"facebook",
    #   "icon_class"  : "fab fa-facebook-f",
    #   "url"         : "https://www.facebook.com/AssociationPiNG/",
    #   "app_version" : version,
    #   "help"        : u"Choose the facebook account for your ApiViz instance",
    #   "in_footer"   : True,
    #   "tooltip"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "notre page sur Facebook" }],
    #   "apiviz_front_uuid" : uuid_models["uuid_covid"],
    #   "is_default"  : True
    # },

    { "field"       : "app_email",
      "content"     : u"email",
      "icon_class"  : "far fa-envelope",
      "url"         : "mailto:covid.initiatives@gmail.com?subject=[Covid] Contact",
      "app_version" : version,
      "help"        : u"Choose the github account for your ApiViz instance",
      "in_footer"   : True,
      "tooltip"     : [{"locale" : "en", "text" : "source codes"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "codes sources" }],
      "apiviz_front_uuid" : uuid_models["uuid_covid"],
      "is_default"  : True
    },

    { "field"       : "app_github",
      "content"     : u"github",
      "icon_class"  : "fab fa-github",
      "url"         : "https://github.com/co-demos/covid-viz",
      "app_version" : version,
      "help"        : u"Choose the github account for your ApiViz instance",
      "in_footer"   : True,
      "tooltip"     : [{"locale" : "en", "text" : "source codes"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "codes sources" }],
      "apiviz_front_uuid" : uuid_models["uuid_covid"],
      "is_default"  : True
    },

    { "field"       : "app_datagouv",
      "content"     : u"github",
      "icon_class"  : "fas fa-database",
      "url"         : "https://www.data.gouv.fr/fr/organizations/covid-initiatives",
      "app_version" : version,
      "help"        : u"Choose the github account for your ApiViz instance",
      "in_footer"   : True,
      "tooltip"     : [{"locale" : "en", "text" : "open data"},{"locale" : "es", "text" : "open data"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "openn data" }],
      "apiviz_front_uuid" : uuid_models["uuid_covid"],
      "is_default"  : True
    },

  ### CUSTOM SOCIAL NETWORKS --> TO BE ADDED VIA BACK OFFICE BY ADMIN USER 
  ### ...

]