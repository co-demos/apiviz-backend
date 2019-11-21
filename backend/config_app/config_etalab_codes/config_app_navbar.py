# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_app_navbar = [

  ### MAIN NAVBAR

    ### - - - - - - - - - - - - - - - ###
    ### CONFIG TIERS LIEUX
      { "field"       : "app_navbar",
        "content"     : u"EC navbar",
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
              "link_to"    : "/repos",
              "help"       : u"First menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "Softwares"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Logiciels" }],
              "tooltip"    : [{"locale" : "en", "text" : "Begin a search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Lancer une recherche" }],
              "has_dropdown" : False,
              "dropdowns"  : [
                # { "is_divider" : True,  "is_external_link" : False },
              ]
            },
            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/orgas",
              "help"       : u"Second menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "Softwares"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Organisations" }],
              "tooltip"    : [{"locale" : "en", "text" : "Begin a search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Lancer une recherche" }],
              "has_dropdown" : False,
              "dropdowns"  : [
                # { "is_divider" : True,  "is_external_link" : False },
              ]
            },
            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/a-propos",
              "help"       : u"Third menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "Project"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "A propos" }],
              "tooltip"    : [{"locale" : "en", "text" : "More infos on the topic"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations sur ce site" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/a-propos",           "link_text" : [{"locale" : "en", "text" : "The project"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "A propos"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/a-propos/glossaire", "link_text" : [{"locale" : "en", "text" : "Our tools"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Glossaire"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/a-propos/outils",    "link_text" : [{"locale" : "en", "text" : "Our tools"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Outils"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.etalab.gouv.fr/", "link_text" : [{"locale" : "en", "text" : "Our tools"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Etalab"}] },
              ]
            },

          ]
        },
        "apiviz_front_uuid" : uuid_models["uuid_etalab_codes"],
        "is_default"  : True
      },

]