# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_socials_config = [

  ### - - - - - - - - - - - - - - - ###
  ### CONFIG SONUM 

    ### SOCIAL NETWORKS
    { "field"       : "app_twitter",
      "content"     : u"twitter",
      "icon_class"  : "fab fa-twitter",
      "url"         : "https://twitter.com/co-demos",
      "app_version" : version,
      "help"        : u"Choose the twitter account for your ApiViz instance",
      "in_footer"   : True,
      "tooltip"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "notre page Twitter" }],
      "apiviz_front_uuid" : uuid_models["uuid_sonum"],
      "is_default"  : True
    },

    { "field"       : "app_facebook",
      "content"     : u"facebook",
      "icon_class"  : "fab fa-facebook-f",
      "url"         : "https://www.facebook.com/co-demos/",
      "app_version" : version,
      "help"        : u"Choose the facebook account for your ApiViz instance",
      "in_footer"   : True,
      "tooltip"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "notre page sur Facebook" }],
      "apiviz_front_uuid" : uuid_models["uuid_sonum"],
      "is_default"  : True
    },

    { "field"       : "app_github",
      "content"     : u"github",
      "icon_class"  : "fab fa-github",
      "url"         : "https://www.github.com/co-demos/",
      "app_version" : version,
      "help"        : u"Choose the github account for your ApiViz instance",
      "in_footer"   : True,
      "tooltip"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "notre page Github" }],
      "apiviz_front_uuid" : uuid_models["uuid_sonum"],
      "is_default"  : True
    },


  ### - - - - - - - - - - - - - - - ###
  ### CONFIG CIS 
  
    ### SOCIAL NETWORKS
    { "field"       : "app_twitter",
      "content"     : u"twitter",
      "icon_class"  : "fab fa-twitter",
      "url"         : "https://twitter.com/touteslesinnoso",
      "app_version" : version,
      "help"        : u"Choose the twitter account for your ApiViz instance",
      "in_footer"   : True,
      "tooltip"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "notre page Twitter" }],
      "apiviz_front_uuid" : uuid_models["uuid_apcis"],
      "is_default"  : True
    },

    { "field"       : "app_facebook",
      "content"     : u"facebook",
      "icon_class"  : "fab fa-facebook-f",
      "url"         : "https://www.facebook.com/ToutesLesInnoSo/",
      "app_version" : version,
      "help"        : u"Choose the facebook account for your ApiViz instance",
      "in_footer"   : True,
      "tooltip"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "notre page sur Facebook" }],
      "apiviz_front_uuid" : uuid_models["uuid_apcis"],
      "is_default"  : True
    },

    { "field"       : "app_github",
      "content"     : u"github",
      "icon_class"  : "fab fa-github",
      "url"         : "https://www.github.com/co-demos/",
      "app_version" : version,
      "help"        : u"Choose the github account for your ApiViz instance",
      "in_footer"   : True,
      "tooltip"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "notre page Github" }],
      "apiviz_front_uuid" : uuid_models["uuid_apcis"],
      "is_default"  : True
    },

  ### CUSTOM SOCIAL NETWORKS --> TO BE ADDED VIA BACK OFFICE BY ADMIN USER 
  ### ...

]