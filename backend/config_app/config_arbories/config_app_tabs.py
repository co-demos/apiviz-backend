# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_app_tabs = [

  ### MAIN TABS

    ### - - - - - - - - - - - - - - - ###
    ### CONFIG PING CARTO

      { "field"       : "app_tabs_test",
        "tabs_uri"     : "tabs-tl-test",
        "content"     : u"apiviz tabs test",
        "app_version" : version,
        "help"        : u"The tabs of your ApiViz instance",
        "ui_options"  : {
          "background_color" : { "value" : "white" },
          "top_margin"       : { "value" : 2 },
          "bottom_margin"    : { "value" : 1 },
          "class"            : { "value" : "tabs" },
          "position"         : { "value" : "is-centered"},
          "size"             : { "value" : "is-small"},
        }, 
        "tabs_options" : [ 
          { "is_visible"   : True, 
            "tab_code"     : "tab-1",
            "is_activated" : True,
            "link_to"      : "/a-propos",
            "has_icon"     : False,
            "icon_class"   : "", 
            "link_text"    : [{"locale" : "en", "text" : "About"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "A propos" }],
            "tooltip"      : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir la carte" }],
          },
          { "is_visible"   : True, 
            "tab_code"     : "tab-1",
            "is_activated" : True,
            "link_to"      : "/mentions-legales",
            "has_icon"     : False,
            "icon_class"   : "", 
            "link_text"    : [{"locale" : "en", "text" : "Legal"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Mentions légales" }],
            "tooltip"      : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir la carte" }],
          },
          # { "is_visible"   : True, 
          #   "tab_code"     : "tab-2",
          #   "is_activated" : True,
          #   "link_to"      : "/outils",
          #   "has_icon"     : False,
          #   "icon_class"   : "", 
          #   "link_text"    : [{"locale" : "en", "text" : "Our tools"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les outils techniques" }],
          #   "tooltip"      : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir les outils" }],
          # },

        ],
        "apiviz_front_uuid" : uuid_models["uuid_arbories"],
        "is_default"  : True
      },


]
