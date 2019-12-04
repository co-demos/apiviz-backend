# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_app_navbar = [

  ### MAIN NAVBAR

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