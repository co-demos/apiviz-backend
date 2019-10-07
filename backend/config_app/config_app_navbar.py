# -*- encoding: utf-8 -*-

from . import version, uuid_models, config_folders

file_name = "config_app_navbar"
class_name = "default_app_navbar"

default_app_navbar = []

for folder in config_folders : 
  folder_module = ".{}.{}".format(folder, file_name)
  print ("... -> folder_module : ", folder_module)
  exec( 'from {} import {} as temp_config_list'.format(folder_module, class_name) )
  # print ("... -> temp_config_list : ", temp_config_list)
  default_app_navbar = default_app_navbar + temp_config_list
  print

print ("... -> default_app_navbar : ", default_app_navbar)

default_app_navbar_ = [

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

    ### - - - - - - - - - - - - - - - ###
    ### CONFIG APCIS
      { "field"       : "app_navbar",
        "content"     : u"CIS navbar",
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
              "link_to"    : "/recherche",
              "help"       : u"First menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "Search engine"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Moteur de recherche" }],
              "tooltip"    : [{"locale" : "en", "text" : "Begin a search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Lancer une recherche" }],
              "has_dropdown" : False,
              "dropdowns"  : [
              ]
            },
            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/le-projet",
              "help"       : u"Second menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "Project"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Projet" }],
              "tooltip"    : [{"locale" : "en", "text" : "More infos on the topic"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations sur ce site" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/le-projet",                 "link_text" : [{"locale" : "en", "text" : "The project"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Le projet"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/le-projet/outils",          "link_text" : [{"locale" : "en", "text" : "Our tools"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les outils"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/le-projet/parlent-de-nous", "link_text" : [{"locale" : "en", "text" : "Press"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Ils parlent de nous"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/le-projet/recompenses",     "link_text" : [{"locale" : "en", "text" : "Awards"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Récompenses"}] },
                # { "is_divider" : True,  "is_external_link" : False },
              ]
            },
            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/le-collectif",
              "help"       : u"Third menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "Who are we ?"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Qui sommes-nous ?" }],
              "tooltip"    : [{"locale" : "en", "text" : "More infos on the initiative"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations sur l’initiative" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/le-collectif",   "link_text" : [{"locale" : "en", "text" : "The collective"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Le collectif"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/le-collectif/qui-fait-quoi",     "link_text" : [{"locale" : "en", "text" : "Who does what"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Qui fait quoi"}] },
                # { "is_divider" : True,  "is_external_link" : False },
              ]
            },
            # { "is_visible" : True,
            #   "position"   : "exterior_right",
            #   "link_to"    : "",
            #   "help"       : u"Fourth menu in navbar",
            #   "is_external_link" : False,
            #   "link_type"  : "link", ### show btn border
            #   "icon_class" : "",
            #   "link_text"  : [{"locale" : "en", "text" : "FR"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "FR" }],
            #   "tooltip"    : [{"locale" : "en", "text" : "in french"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "En français" }],
            #   "has_dropdown" : False,
            #   "dropdowns"  : [
            #     { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-xp/accueil",   "link_text" : [{"locale" : "en", "text" : "Home page"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Accueil"}] },
            #     { "is_divider" : True,  "is_external_link" : False },
            #   ]
            # },
            # { "is_visible" : True,
            #   "position"   : "exterior_right",
            #   "link_to"    : "",
            #   "help"       : u"Fifth menu in navbar",
            #   "is_external_link" : False,
            #   "link_type"  : "link", ### show btn border
            #   "icon_class" : "",
            #   "link_text"  : [{"locale" : "en", "text" : "EN"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "EN" }],
            #   "tooltip"    : [{"locale" : "en", "text" : "in english"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "En anglais" }],
            #   "has_dropdown" : False,
            #   "dropdowns"  : [
            #     { "is_divider" : False, "is_external_link" : False, "link_to" : "/sonum-xp/accueil",   "link_text" : [{"locale" : "en", "text" : "Home page"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Accueil"}] },
            #     { "is_divider" : True,  "is_external_link" : False },
            #   ]
            # },
          ]
        },
        "apiviz_front_uuid" : uuid_models["uuid_apcis"],
        "is_default"  : True
      },

]