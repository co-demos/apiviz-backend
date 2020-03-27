# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_app_navbar = [

  ### MAIN NAVBAR

    ### - - - - - - - - - - - - - - - ###
    ### CONFIG COVID 
      { "field"       : "app_navbar",
        "content"     : u"TL navbar",
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
              "link_to"    : "/diy/liste",
              "help"       : u"First menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "DIY"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Matériels DIY" }],
              "tooltip"    : [{"locale" : "en", "text" : "Begin a search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Lancer une recherche" }],
              "has_dropdown" : False,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/diy", "link_text" : [{"locale" : "en", "text" : "DIY materials"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Liste de matériels DIY"}] },
                { "is_divider" : True,  "is_external_link" : False },
              ]
            },

            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/recherche/liste",
              "help"       : u"First menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "Initiatives"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les initiatives" }],
              "tooltip"    : [{"locale" : "en", "text" : "Begin a search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Lancer une recherche" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/recherche", "link_text" : [{"locale" : "en", "text" : "Initiatives"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Liste des initiatives"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.handddle.com/covid19/", "link_text" : [{"locale" : "en", "text" : "Map 3D printers"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Carte impression 3D"}] },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.latitudes.cc/covid19", "link_text" : [{"locale" : "en", "text" : "Latitudes"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Latitudes contre le Covid"}] },
              ]
            },

            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/charts-europe",
              "help"       : u"Second menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "Charts covid19"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Graphiques" }],
              "tooltip"    : [{"locale" : "en", "text" : "More infos on the topic"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations sur ce site" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/charts-france", "link_text" : [{"locale" : "en", "text" : "Data France"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Données France"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/charts-europe", "link_text" : [{"locale" : "en", "text" : "Data Europe"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "v Europe"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/charts-world",  "link_text" : [{"locale" : "en", "text" : "Data World"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Données World"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/charts-sources",   "link_text" : [{"locale" : "en", "text" : "Sources"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Sources"}] },
              ]
            },
            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/la-demarche",
              "help"       : u"Second menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "Our goals"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Notre démarche" }],
              "tooltip"    : [{"locale" : "en", "text" : "More infos on the topic"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations sur ce site" }],
              "has_dropdown" : False,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/la-demarche", "link_text" : [{"locale" : "en", "text" : "Our goals"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Notre démarche"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/utiliser-le-site", "link_text" : [{"locale" : "en", "text" : "Use our website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Utiliser le site"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/nous-contacter", "link_text" : [{"locale" : "en", "text" : "Contact us"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Nous contacter"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/utiliser-le-site", "link_text" : [{"locale" : "en", "text" : "charts France"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Utiliser le site"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/ressources-officielles", "link_text" : [{"locale" : "en", "text" : "Ressources - official"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Ressources officielles"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/ressources-makers", "link_text" : [{"locale" : "en", "text" : "Ressources - makers"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Ressources makers"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/ressources-données", "link_text" : [{"locale" : "en", "text" : "Ressources - datasets"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Ressources données"}] },
              ]
            },
          ]
        },
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
        "is_default"  : True
      },

]