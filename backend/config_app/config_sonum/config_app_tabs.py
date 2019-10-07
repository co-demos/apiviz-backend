# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_app_tabs = [

  ### MAIN TABS

    ### - - - - - - - - - - - - - - - ###
    ### CONFIG SONUM
      { "field"       : "app_tabs_default",
        "tabs_uri"     : "sonum-tabs",
        "content"     : u"apiviz default tabs",
        "app_version" : version,
        "help"        : u"The tabs of your ApiViz instance",
        "ui_options"  : {
          "background_color" : { "value" : "white" },
          "top_margin"       : { "value" : 2 },
          "bottom_margin"    : { "value" : 2 },
          "class"            : { "value" : "" },
          "position"         : { "value" : "is-centered"},
          "size"             : { "value" : "is-large"},
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
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"  : True
      },

]