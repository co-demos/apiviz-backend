# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_socials_config = [

  ### - - - - - - - - - - - - - - - ###
  ### CONFIG DOUBS
  
    ### SOCIAL NETWORKS

    { "field"       : "app_site",
      "content"     : u"site",
      "icon_class"  : "fas fa-external-link-alt",
      "url"         : "https://www.mednum-bfc.fr/",
      "app_version" : version,
      "help"        : u"Choose the official website for your ApiViz instance",
      "in_footer"   : True,
      "tooltip"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "notre page Twitter" }],
      "apiviz_front_uuid" : uuid_models["uuid_doubs_inclusion"],
      "is_default"  : True
    },

    { "field"       : "app_twitter",
      "content"     : u"twitter",
      "icon_class"  : "fab fa-twitter",
      "url"         : "https://twitter.com/BfcMed",
      "app_version" : version,
      "help"        : u"Choose the twitter account for your ApiViz instance",
      "in_footer"   : True,
      "tooltip"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "notre page Twitter" }],
      "apiviz_front_uuid" : uuid_models["uuid_doubs_inclusion"],
      "is_default"  : True
    },

    { "field"       : "app_facebook",
      "content"     : u"facebook",
      "icon_class"  : "fab fa-facebook-f",
      "url"         : "https://www.facebook.com/MedNumBFC-111287107014098",
      "app_version" : version,
      "help"        : u"Choose the facebook account for your ApiViz instance",
      "in_footer"   : True,
      "tooltip"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "notre page sur Facebook" }],
      "apiviz_front_uuid" : uuid_models["uuid_doubs_inclusion"],
      "is_default"  : True
    },

    { "field"       : "app_github",
      "content"     : u"github",
      "icon_class"  : "fab fa-github",
      "url"         : "https://github.com/co-demos/BFC-ternum",
      "app_version" : version,
      "help"        : u"Choose the github account for your ApiViz instance",
      "in_footer"   : True,
      "tooltip"     : [{"locale" : "en", "text" : "source codes"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "codes sources" }],
      "apiviz_front_uuid" : uuid_models["uuid_doubs_inclusion"],
      "is_default"  : True
    },

  ### CUSTOM SOCIAL NETWORKS --> TO BE ADDED VIA BACK OFFICE BY ADMIN USER 
  ### ...

]