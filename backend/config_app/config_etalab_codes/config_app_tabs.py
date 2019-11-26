# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_app_tabs = [

  ### MAIN TABS

    ### - - - - - - - - - - - - - - - ###
    ### CONFIG TIERS LIEUX

      { "field"       : "app_tabs_test",
        "tabs_uri"     : "tabs-ec-test",
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
            "link_text"    : [{"locale" : "en", "text" : "The project"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "à propos" }],
            "tooltip"      : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir la carte" }],
          },
          { "is_visible"   : True, 
            "tab_code"     : "tab-2",
            "is_activated" : True,
            "link_to"      : "/a-propos/glossaire",
            "has_icon"     : False,
            "icon_class"   : "", 
            "link_text"    : [{"locale" : "en", "text" : "Our tools"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "glossaire" }],
            "tooltip"      : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir les outils" }],
          },
          { "is_visible"   : True, 
            "tab_code"     : "tab-3",
            "is_activated" : True,
            "link_to"      : "/a-propos/outils",
            "has_icon"     : False,
            "icon_class"   : "", 
            "link_text"    : [{"locale" : "en", "text" : "Our tools"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "outils" }],
            "tooltip"      : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir les outils" }],
          },

        ],
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
        "is_default"  : True
      },


]