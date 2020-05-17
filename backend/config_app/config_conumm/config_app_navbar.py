# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_app_navbar = [

  ### MAIN NAVBAR

    ### - - - - - - - - - - - - - - - ###
    ### CONFIG CONUMM
      { "field"       : "app_navbar",
        "content"     : u"TL navbar",
        "app_version" : version,
        "help"        : u"The navbar of your ApiViz instance",
        "logo_to"     : "/",
        "has_login"   : False,
        "ui_options"  : {
          "background_isdark" : False,
          "background_color" : { 
            "bulma_color" : "white"
          },

        },
        "links_options" : {
          "extra_buttons" : [ ### for buttons not declared in routes/pages

            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/le-projet",
              "help"       : u"First menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "The project"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Le projet de cartographie" }],
              "tooltip"    : [{"locale" : "en", "text" : "Begin a search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Lancer une recherche" }],
              "has_dropdown" : False,
              "dropdowns"  : [
                # { "is_divider" : True,  "is_external_link" : False },
              ]
            },
            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/recherche",
              "help"       : u"First menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "The map"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "La carte" }],
              "tooltip"    : [{"locale" : "en", "text" : "Begin a search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Lancer une recherche" }],
              "has_dropdown" : False,
              "dropdowns"  : [
                # { "is_divider" : True,  "is_external_link" : False },
              ]
            },
            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/qui-sommes-nous",
              "help"       : u"Second menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link",
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "Who are we ?"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Qui sommes-nous ?" }],
              "tooltip"    : [{"locale" : "en", "text" : "More infos on the topic"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations sur ce site" }],
              "has_dropdown" : False,
              "dropdowns"  : [
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/le-projet",                 "link_text" : [{"locale" : "en", "text" : "The project"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Le projet"}] },
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/le-projet/outils",          "link_text" : [{"locale" : "en", "text" : "Our tools"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les outils"}] },
                # { "is_divider" : True,  "is_external_link" : False },
              ]
            },
            { "is_visible" : False,
              "position"   : "exterior_right",
              "link_to"    : "/partenaires",
              "help"       : u"Third menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link",
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "Project"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Partenaires" }],
              "tooltip"    : [{"locale" : "en", "text" : "More infos on the topic"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations sur ce site" }],
              "has_dropdown" : False,
              "dropdowns"  : [
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/le-projet",                 "link_text" : [{"locale" : "en", "text" : "The project"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Le projet"}] },
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/le-projet/outils",          "link_text" : [{"locale" : "en", "text" : "Our tools"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les outils"}] },
                # { "is_divider" : True,  "is_external_link" : False },
              ]
            },
            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "https://conumm.fr/",
              "help"       : u"Fourth menu in navbar",
              "is_external_link" : True,
              "link_type"  : "button", ### link | text | button --- show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "CONUMM"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "retour vers CONNUMM" }],
              "tooltip"    : [{"locale" : "en", "text" : "More infos on the topic"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations sur ce site" }],
              "has_dropdown" : False,
              "dropdowns"  : [
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/la-demarche",        "link_text" : [{"locale" : "en", "text" : "The approach"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "La démarche"}] },
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/mentions-legales",   "link_text" : [{"locale" : "en", "text" : "Legal"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Mentions légales"}] },
                # { "is_divider" : True,  "is_external_link" : False },
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/outils",   "link_text" : [{"locale" : "en", "text" : "Our tools"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les outils"}] },
              ]
            },
          ]
        },
        "apiviz_front_uuid" : uuid_models["uuid_conumm"],
        "is_default"  : True
      },

]
