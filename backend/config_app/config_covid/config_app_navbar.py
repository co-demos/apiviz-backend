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
              "link_to"    : "/printers/carte",
              "help"       : u"First menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "3D Printers map"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Carte des imprimeurs 3D" }],
              "tooltip"    : [{"locale" : "en", "text" : "Begin a search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Lancer une recherche" }],
              "has_dropdown" : False,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/printers", "link_text" : [{"locale" : "en", "text" : "DIY materials"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Liste de matériels DIY"}] },
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
              "link_text"  : [{"locale" : "en", "text" : "Initiatives"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les initiatives solidaires" }],
              "tooltip"    : [{"locale" : "en", "text" : "Begin a search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Lancer une recherche" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/recherche", "link_text" : [{"locale" : "en", "text" : "Initiatives"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Liste des initiatives"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/map-printers", "link_text" : [{"locale" : "en", "text" : "Map 3D printers"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Carte impression 3D"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.handddle.com/covid19/", "link_text" : [{"locale" : "en", "text" : "Map 3D printers"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Carte impression 3D"}] },
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
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/charts-europe", "link_text" : [{"locale" : "en", "text" : "Data Europe"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Données Europe"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/charts-world",  "link_text" : [{"locale" : "en", "text" : "Data World"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Données Monde"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/charts-sources",   "link_text" : [{"locale" : "en", "text" : "Sources"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Sources"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://veille-coronavirus.fr/",   "link_text" : [{"locale" : "en", "text" : "Dataviz France"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Veille Coronavirus France"}] },
              ]
            },
            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/la-demarche",
              "help"       : u"Second menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "Our selection"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Notre sélection" }],
              "tooltip"    : [{"locale" : "en", "text" : "More infos on the topic"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations sur ce site" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.gouvernement.fr/info-coronavirus/", "link_text" : [{"locale" : "en", "text" : "French government official website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Site officiel du gouvernement sur le Covid19"}] },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.gouvernement.fr/info-coronavirus/carte-et-donnees", "link_text" : [{"locale" : "en", "text" : "Covid map for France"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Carte et données officielles"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.mur-project.org/", "link_text" : [{"locale" : "en", "text" : "Minimal Universal Respirator"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Minimal Universal Respirator"}] },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.avosmasques.fr/", "link_text" : [{"locale" : "en", "text" : "A vos masques"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "A vos masques"}] },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://app.jogl.io/project/118#about", "link_text" : [{"locale" : "en", "text" : "Low-cost & Open-Source Covid19 Detection kits"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Low-cost & Open-Source Covid19 Detection kits"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.latitudes.cc/covid19", "link_text" : [{"locale" : "en", "text" : "Latitudes"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Latitudes contre le Covid"}] },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://bzg.fr/covid19-developpeurs-datascientistes-comment-aider/", "link_text" : [{"locale" : "en", "text" : "Devs/data-scientists..."},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Développeurs/data-scientists..."}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://enpremiereligne.fr/", "link_text" : [{"locale" : "en", "text" : "En première ligne"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "En première ligne"}] },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.continuitepedagogique.org/", "link_text" : [{"locale" : "en", "text" : "Continuité pédagogique"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Continuité pédagogique"}] },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://covid19.reserve-civique.gouv.fr/", "link_text" : [{"locale" : "en", "text" : "Réserve civique"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Réserve civique"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.covid19-que-lire.fr/", "link_text" : [{"locale" : "en", "text" : "What to read ? "},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Que lire ?"}] },

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
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/la-demarche", "link_text" : [{"locale" : "en", "text" : "Our goals"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Notre démarche"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/contact", "link_text" : [{"locale" : "en", "text" : "Contact us"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Nous contacter"}] },
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/utiliser-le-site", "link_text" : [{"locale" : "en", "text" : "charts France"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Utiliser le site"}] },
                # { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/mentions-legales", "link_text" : [{"locale" : "en", "text" : "Legal"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Mentions légales"}] },
                # { "is_divider" : True,  "is_external_link" : False },
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/ressources-officielles", "link_text" : [{"locale" : "en", "text" : "Ressources - official"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Ressources officielles"}] },
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/ressources-makers", "link_text" : [{"locale" : "en", "text" : "Ressources - makers"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Ressources makers"}] },
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/ressources-données", "link_text" : [{"locale" : "en", "text" : "Ressources - datasets"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Ressources données"}] },
              ]
            },
          ]
        },
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
        "is_default"  : True
      },

]