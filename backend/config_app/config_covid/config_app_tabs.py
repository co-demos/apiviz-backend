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
            "link_to"      : "/la-demarche",
            "has_icon"     : False,
            "icon_class"   : "", 
            "link_text"    : [{"locale" : "en", "text" : "Our approach"},{"locale" : "es", "text" : "Nuestro enfoque"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Notre démarche" }],
            "tooltip"      : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir la carte" }],
          },
          { "is_visible"   : True, 
            "tab_code"     : "tab-1",
            "is_activated" : True,
            "link_to"      : "/contact",
            "has_icon"     : False,
            "icon_class"   : "", 
            "link_text"    : [{"locale" : "en", "text" : "Contact us"},{"locale" : "es", "text" : "Contactarnos"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Nous contacter" }],
            "tooltip"      : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir la carte" }],
          },
          { "is_visible"   : True, 
            "tab_code"     : "tab-1",
            "is_activated" : True,
            "link_to"      : "/mentions-legales",
            "has_icon"     : False,
            "icon_class"   : "", 
            "link_text"    : [{"locale" : "en", "text" : "Legal mentions"},{"locale" : "es", "text" : "Menciones legales"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Mentions légales" }],
            "tooltip"      : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir la carte" }],
          },
          { "is_visible"   : True, 
            "tab_code"     : "tab-2",
            "is_activated" : True,
            "link_to"      : "/outils",
            "has_icon"     : False,
            "icon_class"   : "", 
            "link_text"    : [{"locale" : "en", "text" : "Our tools"},{"locale" : "es", "text" : "Nuestras herramientas"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Nos outils " }],
            "tooltip"      : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir les outils" }],
          },

        ],
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
        "is_default"  : True
      },


]