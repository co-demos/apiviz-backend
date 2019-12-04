# -*- encoding: utf-8 -*-

from . import version, uuid_models, config_folders

file_name = "config_app_tabs"
class_name = "default_app_tabs"

default_app_tabs = []

for folder in config_folders : 
  folder_module = ".{}.{}".format(folder, file_name)
  print ("... -> folder_module : ", folder_module)
  exec( 'from {} import {} as temp_config_list'.format(folder_module, class_name) )
  # print ("... -> temp_config_list : ", temp_config_list)
  default_app_tabs = default_app_tabs + temp_config_list
  print

print ("... -> default_app_tabs : ", default_app_tabs)

default_app_tabs_ = [

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

    ### - - - - - - - - - - - - - - - ###
    ### CONFIG APCIS

      { "field"       : "app_tabs_test",
        "tabs_uri"     : "tabs-cis-test",
        "content"     : u"apiviz tabs test",
        "app_version" : version,
        "help"        : u"The tabs of your ApiViz instance",
        "ui_options"  : {
          "background_color" : { "value" : "white" },
          "top_margin"       : { "value" : 2 },
          "bottom_margin"    : { "value" : 1 },
          "class"            : { "value" : "cis-tabs" },
          "position"         : { "value" : "is-centered"},
          "size"             : { "value" : "is-small"},
        }, 
        "tabs_options" : [ 
          { "is_visible"   : True, 
            "tab_code"     : "tab-1",
            "is_activated" : True,
            "link_to"      : "/le-projet",
            "has_icon"     : False,
            "icon_class"   : "", 
            "link_text"    : [{"locale" : "en", "text" : "The project"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "A propos" }],
            "tooltip"      : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir la carte" }],
          },
          { "is_visible"   : True, 
            "tab_code"     : "tab-2",
            "is_activated" : True,
            "link_to"      : "/le-projet/outils",
            "has_icon"     : False,
            "icon_class"   : "", 
            "link_text"    : [{"locale" : "en", "text" : "Our tools"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les outils techniques" }],
            "tooltip"      : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir les outils" }],
          },
          { "is_visible"   : True, 
            "tab_code"     : "tab-3",
            "is_activated" : True,
            "link_to"      : "/le-projet/parlent-de-nous",
            "has_icon"     : False,
            "icon_class"   : "", 
            "link_text"    : [{"locale" : "en", "text" : "Press"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Ils parlent de nous" }],
            "tooltip"      : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir la carte" }],
          },
          { "is_visible"   : True, 
            "tab_code"     : "tab-4",
            "is_activated" : True,
            "link_to"      : "/le-projet/recompenses",
            "has_icon"     : False,
            "icon_class"   : "", 
            "link_text"    : [{"locale" : "en", "text" : "Awards"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Récompenses" }],
            "tooltip"      : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir la carte" }],
          },
        ],
        "apiviz_front_uuid" : uuid_models["uuid_apcis"],
        "is_default"  : True
      },

      { "field"       : "app_tabs_collective",
        "tabs_uri"     : "tabs-cis-collective",
        "content"     : u"apiviz tabs collective",
        "app_version" : version,
        "help"        : u"The tabs of your ApiViz instance",
        "ui_options"  : {
          "background_color" : { "value" : "white" },
          "top_margin"       : { "value" : 2 },
          "bottom_margin"    : { "value" : 1 },
          "class"            : { "value" : "cis-tabs" },
          "position"         : { "value" : "is-centered"},
          "size"             : { "value" : "is-small"},
        }, 
        "tabs_options" : [ 
          { "is_visible"   : True, 
            "tab_code"     : "tab-1",
            "is_activated" : True,
            "link_to"      : "/le-collectif",
            "has_icon"     : False,
            "icon_class"   : "", 
            "link_text"    : [{"locale" : "en", "text" : "The collective"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Le collectif" }],
            "tooltip"      : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir la carte" }],
          },
          { "is_visible"   : True, 
            "tab_code"     : "tab-2",
            "is_activated" : True,
            "link_to"      : "/le-collectif/qui-fait-quoi",
            "has_icon"     : False,
            "icon_class"   : "", 
            "link_text"    : [{"locale" : "en", "text" : "Who are we ?"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Qui sommes-nous ?" }],
            "tooltip"      : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir les outils" }],
          },
        ],
        "apiviz_front_uuid" : uuid_models["uuid_apcis"],
        "is_default"  : True
      },
]