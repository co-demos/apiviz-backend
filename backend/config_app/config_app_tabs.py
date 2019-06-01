# -*- encoding: utf-8 -*-

from . import version

default_app_tabs = [

  ### MAIN TABS

    ### - - - - - - - - - - - - - - - ###
    ### CONFIG SONUM
      { "field"       : "app_tabs_default",
        "tab_uri"     : "sonum-tabs",
        "content"     : u"apiviz default tabs",
        "app_version" : version,
        "help"        : u"The tabs of your ApiViz instance",
        "top_margin"  : 1,
        "ui_options"  : {
          "background_color" : { "value" : None, "default" : "white", },
        }, 
        "tabs_options" : [ 

          { "is_visible" : True, 
            "tab_code"   : "tab-1",
            "link_to"    : "/sonum-carto/carte",
            "has_icon"   : False,
            "icon_class" : "", 
            "link_text"  : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "carte" }],
            "tooltip"    : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir la carte" }],
          },
          { "is_visible" : True, 
            "tab_code"   : "tab-2",
            "link_to"    : "/sonum-carto/projet",
            "has_icon"   : False,
            "icon_class" : "", 
            "link_text"  : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "projet" }],
            "tooltip"    : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "le projet" }],
          },

        ],
        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"  : True
      },

    ### - - - - - - - - - - - - - - - ###
    ### CONFIG APCIS
      { "field"       : "app_tabs_default",
        "tab_uri"     : "tabs-cis-default",
        "content"     : u"apiviz default navbar",
        "app_version" : version,
        "help"        : u"The tabs of your ApiViz instance",
        "top_margin"  : 0,
        "ui_options"  : {
          "background_color" : { "value" : None, "default" : "white", },
        }, 
        "tabs_options" : [ 
          { "is_visible" : True, 
            "tab_code"   : "tab-1",
            "is_activated" : True,
            "link_to"    : "/",
            "has_icon"   : False,
            "icon_class" : "", 
            "link_text"  : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "le projet" }],
            "tooltip"    : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir la carte" }],
          },
        ],
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"  : True
      },

]