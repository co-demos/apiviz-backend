# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_app_navbar = [

  ### MAIN NAVBAR

    ### - - - - - - - - - - - - - - - ###
    ### CONFIG DOUBS CARTO
      { "field"       : "app_navbar",
        "content"     : u"TL navbar",
        "app_version" : version,
        "help"        : u"The navbar of your ApiViz instance",
        # "logo_to"     : "/",
        "logo_to"     : "/", #"https://apiviz-carto-doubs-staging.netlify.app",
        "logo_to_external" : True,
        "title_to"    : "/",
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
              "link_to"    : "/",
              "help"       : u"First menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "La cartographie"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "La cartographie" }],
              "tooltip"    : [{"locale" : "en", "text" : "Begin a search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Lancer une recherche" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/recherche",        "link_text" : [{"locale" : "en", "text" : "The map"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "La carte"}] },
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/mednum-bfc",       "link_text" : [{"locale" : "en", "text" : "The approach"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "La MedNum BFC"}] },
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/les-données",      "link_text" : [{"locale" : "en", "text" : "Legal"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les données"}] },
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/aide",             "link_text" : [{"locale" : "en", "text" : "Legal"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Aide"}] },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://opendata.doubs.fr/pages/accueil/", "link_text" : [{"locale" : "en", "text" : "Legal"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Données ouvertes"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/mentions-legales", "link_text" : [{"locale" : "en", "text" : "Legal"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Mentions légales"}] },
              ]
            },
            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "https://doubs.fr",
              "help"       : u"Second menu in navbar",
              "is_external_link" : True,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "About"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Doubs.fr" }],
              "tooltip"    : [{"locale" : "en", "text" : "More infos on the topic"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations sur ce site" }],
              "has_dropdown" : False,
              "dropdowns"  : [
                # { "is_divider" : True,  "is_external_link" : False },
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/outils",   "link_text" : [{"locale" : "en", "text" : "Our tools"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les outils"}] },
              ]
            },

          ]
        },
        "apiviz_front_uuid" : uuid_models["uuid_doubs_inclusion"],
        "is_default"  : True
      },

]
