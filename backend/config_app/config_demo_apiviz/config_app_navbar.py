# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_app_navbar = [

  ### MAIN NAVBAR

    ### - - - - - - - - - - - - - - - ###
    ### CONFIG 
      { "field"       : "app_navbar",
        "content"     : u"Apiviz demo navbar",
        "app_version" : version,
        "help"        : u"The navbar of your ApiViz instance",
        "logo_to"     : "/",
        "has_login"   : False,
        "ui_options"  : {
          "background_isdark" : True,
          "background_color" : { 
            "bulma_color" : "primary"
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
              "link_text"  : [{"locale" : "en", "text" : "The Apiviz project"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Le projet Apiviz" }],
              "tooltip"    : [{"locale" : "en", "text" : "More infos on the topic"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations sur ce site" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/le-projet",                 "link_text" : [{"locale" : "en", "text" : "The project"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Le projet"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/apiviz-tutorial",           "link_text" : [{"locale" : "en", "text" : "Tutorial"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Tutoriel"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/apiviz-benchmark",          "link_text" : [{"locale" : "en", "text" : "Benchmark"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Benchmark"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/ressources-opendata",       "link_text" : [{"locale" : "en", "text" : "Ressources"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Ressources"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/le-projet/outils",          "link_text" : [{"locale" : "en", "text" : "Our free tools"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les outils libres"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/le-projet/contact",          "link_text" : [{"locale" : "en", "text" : "Contact"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Contact"}] },
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/le-projet",                 "link_text" : [{"locale" : "en", "text" : "The project"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Contact"}] },
              ]
            },

            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/mediation",
              "help"       : u"Second menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "demo - Mediation"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "démo - Médiation" }],
              "tooltip"    : [{"locale" : "en", "text" : "Begin a search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Lancer une recherche" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/mediation/projet", "link_text" : [{"locale" : "en", "text" : "The mapping project"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Le projet de cartographie"}] },
                # { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/mediation/carte", "link_text" : [{"locale" : "en", "text" : "Map of places for digital mediation"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Cartographie des lieux de médiation numérique"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/mediation/liste", "link_text" : [{"locale" : "en", "text" : "List of place for digital mediation"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Liste des lieux de médiation numérique"}] },
                # { "is_divider" : True,  "is_external_link" : False },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://forum.societenumerique.gouv.fr/category/10/cartographie-des-services-de-m%C3%A9diation-et-d-inclusion-num%C3%A9rique", "link_text" : [{"locale" : "en", "text" : "Contribute to the map"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Participez à la cartographie"}] },
              ]
            },

            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/tiers-lieux",
              "help"       : u"Third menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "demo - Third places"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "démo - Tiers-lieux" }],
              "tooltip"    : [{"locale" : "en", "text" : "Begin a search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Lancer une recherche" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/tiers-lieux/carte", "link_text" : [{"locale" : "en", "text" : "Map of third places"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Cartographie des tiers-lieux"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/tiers-lieux/table", "link_text" : [{"locale" : "en", "text" : "Table of third places"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Table des tiers-lieux"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/tiers-lieux/liste", "link_text" : [{"locale" : "en", "text" : "List of third places"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Liste des tiers-lieux"}] },
              ]
            },

            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/galery",
              "help"       : u"First menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "Gallery"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Galerie" }],
              "tooltip"    : [{"locale" : "en", "text" : "More infos on the topic"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations sur ce site" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/galery/summary",               "link_text" : [{"locale" : "en", "text" : "Summary"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Sommaire"}] },
                # { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://orgues-apiviz.netlify.com/",         "link_text" : [{"locale" : "en", "text" : "Organons"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Inventaire des orgues"}] },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://tiers-lieux-dataviz.netlify.com/",   "link_text" : [{"locale" : "en", "text" : "Third places"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Tiers lieux"}] },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://apiviz-preprod-sonum.netlify.com/",  "link_text" : [{"locale" : "en", "text" : "Sonum"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Carto Sonum"}] },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://etalab-codes.netlify.com/a-propos",  "link_text" : [{"locale" : "en", "text" : "Etalab codes"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Codes Etalab"}] },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://ping-carto.netlify.com/",            "link_text" : [{"locale" : "en", "text" : "PiNG carto"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Carto Ping"}] },
              ]
            },

          ]
        },
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
        "is_default"  : True
      },

]