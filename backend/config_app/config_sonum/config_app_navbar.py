# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_app_navbar = [

  ### MAIN NAVBAR

    ### - - - - - - - - - - - - - - - ###
    ### CONFIG SONUM
      { "field"       : "app_navbar",
        "content"     : u"apiviz default navbar",
        "app_version" : version,
        "help"        : u"The navbar of your ApiViz instance",
        "logo_to"     : "/sonum-carto/carte",
        "has_login"   : False,
        "ui_options"  : {
          "background_isdark" : False,
          "background_color" : { 
            "bulma_color" : "white"
          },
        }, 
        "links_options" : {

          "extra_buttons" : [ ### for buttons not declared in routes/pages

            # NAVBAR ITEM - LINK WITH DROPDOWNS
            { "is_visible" : True, 
              "position"   : "exterior_right",
              "link_to"    : "/sonum-xp/accueil",
              "help"       : u"First menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show as link
              "icon_class" : "", 
              "link_text"  : [{"locale" : "en", "text" : "territories"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "territoires" }],
              "tooltip"    : [{"locale" : "en", "text" : "see the list"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir la liste" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-xp/accueil",   "link_text" : [{"locale" : "en", "text" : "Home page"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Accueil"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-xp/strategie", "link_text" : [{"locale" : "en", "text" : "Design a local strategy for digital inclusion"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Elaborer une stratégie locale d'inclusion numérique"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-xp/liste", "link_text" : [{"locale" : "en", "text" : "Documentation on inspiring initatives"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Documentation des initiatives inspirantes"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-xp/carte", "link_text" : [{"locale" : "en", "text" : "Map of initiatives"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Cartographie des initiatives"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://societenumerique.gouv.fr/territoires/", "link_text" : [{"locale" : "en", "text" : "Benefit from toolkits"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Bénéficier des outils à ma disposition"}] },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://societenumerique.gouv.fr/hubs/", "link_text" : [{"locale" : "en", "text" : "Mobilize your counterparts"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Mobiliser les interlocuteurs"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://framaforms.org/documentation-dinitiatives-et-politiques-publiques-numeriques-innovantes-1540547339", "link_text" : [{"locale" : "en", "text" : "Documentation form"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Formulaire de documentation"}] },
              ]
            },

            # NAVBAR ITEM - LINK WITH DROPDOWNS
            { "is_visible" : True, 
              "position"   : "exterior_right",
              "link_to"    : "/sonum-carto/carte",
              "help"       : u"Second menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show as link
              "icon_class" : "", 
              "link_text"  : [{"locale" : "en", "text" : "places of digital mediation"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "lieux de médiation numérique" }],
              "tooltip"    : [{"locale" : "en", "text" : "see the map"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir la carte" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-carto/projet", "link_text" : [{"locale" : "en", "text" : "The mapping project"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Le projet de cartographie"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-carto/carte", "link_text" : [{"locale" : "en", "text" : "Map of places for digital mediation"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Cartographie des lieux de médiation numérique"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-carto/liste", "link_text" : [{"locale" : "en", "text" : "List of place for digital mediation"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Liste des lieux de médiation numérique"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://forum.societenumerique.gouv.fr/category/10/cartographie-des-services-de-m%C3%A9diation-et-d-inclusion-num%C3%A9rique", "link_text" : [{"locale" : "en", "text" : "Contribute to the map"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Participez à la cartographie"}] },
              ]
            },

            # NAVBAR ITEM - SIMPLE LINK-LIKE
            # { "is_visible" : True, 
            #   "position"   : "exterior_right",
            #   "link_to"    : "/sonum-carto/projet",
            #   "is_external_link" : False,
            #   "link_type"  : "link", ### show as link
            #   "icon_class" : "", 
            #   "link_text"  : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "le projet" }],
            #   "tooltip"    : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir la carte" }],
            #   "has_dropdown" : False,
            #   "dropdowns"  : [],
            # },

            # NAVBAR ITEM - BUTTON-LIKE
            { "is_visible" : True, 
              "position"   : "exterior_right",
              "link_to"    : "https://forum.societenumerique.gouv.fr/category/10/cartographie-des-services-de-médiation-et-d-inclusion-numérique",
              "help"       : u"Third menu in navbar",
              "is_external_link" : True,
              "link_type"  : "button", ### show btn border
              "icon_class" : "", 
              "link_text"  : [{"locale" : "en", "text" : "Version beta | contribute"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Version bêta | Participez" }],
              "tooltip"    : [{"locale" : "en", "text" : "check the website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le site" }],
              "has_dropdown" : False,
              "dropdowns"  : [],
            },
          ]
        },
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"  : True
      },

]