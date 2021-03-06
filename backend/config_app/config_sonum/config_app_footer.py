# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_app_footer = [

  ### FOOTER

    ### CONFIG SONUM 
      { "field"       : "app_footer",
        "app_version" : version,
        "help"        : u"The default footer for your ApiViz instance",

        "template_url"      : None,
        "is_dynamic"        : True,
        "dynamic_template"  : 'DynamicFooter',

        "has_credits_footer": True,
        "credits_footer_url" : "https://raw.githubusercontent.com/co-demos/carto-sonum/master/pages-html/footer-mednum.html",

        "ui_options" : {

            "card_color" : { "value" : "default_background_app", "default" : "light", },
            "card_class"  : { "value" : "", "default" : "" },

            "title_color" : { "value" : 'primary',   "default" : "white",   "custom_color" : None},
            "text_color" : { "value" : "grey-dark", "default" : "black", },

            "socials_color" : { "value" : "primary", "default" : "primary" } ,
            "socials_class" : { "value" : "", "default" : "" } ,

            "footer_logos" : [
              { "src_image" : "https://github.com/co-demos/carto-sonum/blob/master/logos/bloc-web-le-maire-darmanin.png?raw=true", 
                "has_link"  : False,
                "link_to"   : "/" , 
                "position"  : "block_top_left" 
              }
            ],

        },

        "links_options" : [

          {
            # "block_left" : {
            "is_visible"  : False,
            "has_socials" : False,
            "block_class" : "is-3",
            # "link_class"  : { "value" : 'has-text-centered', "default" : "" },

            "position"    : "block_top_left",
            "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : ""}],
            "title_visible" : True,
            "links"       : []
          },

          {
            # "block_center_left" : {
            "is_visible"  : True,
            "has_socials" : False,
            "block_class" : "is-3",
            # "link_class"  : { "value" : 'has-text-centered', "default" : "" },

            "position"    : "block_top_center_left",
            "title_block" : [{"locale" : "en", "text" : "French Digital Agency"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "L'Agence du numérique"}],
            "title_visible" : True,
            "links"       : [

              { "is_visible" : True, 
                "link_to"    : "https://www.agencedunumerique.gouv.fr/",
                "is_external_link" : True,
                "link_type"  : "text", 
                "icon_class" : "", 
                "link_text"  : [{"locale" : "en", "text" : "French Digital Agency"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "L'Agence du numérique" }],
                "tooltip"    : [{"locale" : "en", "text" : "see the website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le site" }] 
              },
              { "is_visible" : True, 
                "link_to"    : "https://www.francethd.fr/",
                "is_external_link" : True,
                "link_type"  : "text", 
                "icon_class" : "", 
                "link_text"  : [{"locale" : "en", "text" : "Mission France Très Haut Débit"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Mission France Très Haut Débit" }],
                "tooltip"    : [{"locale" : "en", "text" : "see the website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le site" }] 
              },
              { "is_visible" : True, 
                "link_to"    : "https://www.lafrenchtech.com/",
                "is_external_link" : True,
                "link_type"  : "text", 
                "icon_class" : "", 
                "link_text"  : [{"locale" : "en", "text" : "Mission French Tech"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Mission French Tech" }],
                "tooltip"    : [{"locale" : "en", "text" : "see the website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le site" }] 
              },
            ]
          },

          {
            # "block_center_right" : {
            "is_visible"  : True,
            "has_socials" : False,
            "block_class" : "is-3",
            # "link_class"  : { "value" : 'has-text-centered', "default" : "" },

            "position"    : "block_top_center_right",
            "title_block" : [{"locale" : "en", "text" : "Digital Society"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Société numérique"}],
            "title_visible" : True,
            "links"       : [

              { "is_visible" : True, 
                "link_to"    : "https://societenumerique.gouv.fr/en-savoir-plus/",
                "is_external_link" : True,
                "link_type"  : "text", 
                "icon_class" : "", 
                "link_text"  : [{"locale" : "en", "text" : "To know more"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "En savoir plus" }],
                "tooltip"    : [{"locale" : "en", "text" : "see the website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le site" }] 
              },
              { "is_visible" : True, 
                "link_to"    : "https://societenumerique.gouv.fr/presse/",
                "is_external_link" : True,
                "link_type"  : "text", 
                "icon_class" : "", 
                "link_text"  : [{"locale" : "en", "text" : "Press"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Presse" }],
                "tooltip"    : [{"locale" : "en", "text" : "see the website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le site" }] 
              },
              { "is_visible" : True, 
                "link_to"    : "/",
                "is_external_link" : True,
                "link_type"  : "text", 
                "icon_class" : "", 
                "link_text"  : [{"locale" : "en", "text" : "Quick intervention toolkit"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Kit d'intervention rapide" }],
                "tooltip"    : [{"locale" : "en", "text" : "see the website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le site" }] 
              },
              { "is_visible" : True, 
                "link_to"    : "/",
                "is_external_link" : True,
                "link_type"  : "text", 
                "icon_class" : "", 
                "link_text"  : [{"locale" : "en", "text" : "Plateforme des Territoires"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plateforme des territoires" }],
                "tooltip"    : [{"locale" : "en", "text" : "see the website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le site" }] 
              },
              { "is_visible" : True, 
                "link_to"    : "https://societenumerique.gouv.fr/mentions-legales/",
                "is_external_link" : True,
                "link_type"  : "text", 
                "icon_class" : "", 
                "link_text"  : [{"locale" : "en", "text" : "Legal mentions"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Mentions légales" }],
                "tooltip"    : [{"locale" : "en", "text" : "see the website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le site" }] 
              },
              { "is_visible" : True, 
                "link_to"    : "https://societenumerique.gouv.fr/accessibilite/",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "", 
                "link_text"  : [{"locale" : "en", "text" : "Accessibility"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Accessibilité" }],
                "tooltip"    : [{"locale" : "en", "text" : "see the website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le site" }] 
              },
              { "is_visible" : True, 
                "link_to"    : "",
                "is_external_link" : False,
                "link_type"  : "divider",
                "icon_class" : "", 
                "link_text"  : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "todo" }],
                "tooltip"    : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "todo" }] 
              },
              { "is_visible" : True, 
                "link_to"    : "https://github.com/co-demos/apiviz-frontend",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "", 
                "link_text"  : [{"locale" : "en", "text" : "Source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Code source" }],
                "tooltip"    : [{"locale" : "en", "text" : "check the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "accéder au code source" }] 
              },
              # { "is_visible" : True, 
              #   "link_to"    : "/apiviz/outils",
              #   "is_external_link" : False,
              #   "link_type"  : "text",
              #   "icon_class" : "", 
              #   "link_text"  : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "outils open source" }],
              #   "tooltip"    : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "accéder au code source" }] 
              # },
              { "is_visible" : True, 
                "link_to"    : "/login",
                "is_external_link" : False,
                "link_type"  : "text",
                "icon_class" : "", 
                "link_text"  : [{"locale" : "en", "text" : "Login - admin"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Login - admin" }],
                "tooltip"    : [{"locale" : "en", "text" : "connect to back office"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "se connecter au back-office" }] 
              },
              # { "is_visible" : False, 
              #   "link_to"    : "/register",
              #   "is_external_link" : False,
              #   "link_type"  : "text",
              #   "icon_class" : "", 
              #   "link_text"  : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "register" }],
              #   "tooltip"    : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "se créer un compte" }] 
              # },
            ]
          },

          {
            # "block_right" : {
            "is_visible"  : True,
            "has_socials" : True,
            "block_class" : "is-3",
            # "link_class"  : { "value" : 'has-text-centered', "default" : "" },

            "position"    : "block_top_right",
            "title_block" : [{"locale" : "en", "text" : "Public websites"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les sites publics"}],
            "title_visible" : True,
            "links"       : [

              { "is_visible" : True, 
                "link_to"    : "https://www.gouvernement.fr/",
                "is_external_link" : True,
                "link_type"  : "text", 
                "icon_class" : "", 
                "link_text"  : [{"locale" : "en", "text" : "gouvernement.fr"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "gouvernement.fr" }],
                "tooltip"    : [{"locale" : "en", "text" : "see the website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le site" }] 
              },
              { "is_visible" : True, 
                "link_to"    : "https://www.service-public.fr/",
                "is_external_link" : True,
                "link_type"  : "text", 
                "icon_class" : "", 
                "link_text"  : [{"locale" : "en", "text" : "service-public.fr"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "service-public.fr" }],
                "tooltip"    : [{"locale" : "en", "text" : "see the website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le site" }] 
              },
              { "is_visible" : True, 
                "link_to"    : "https://www.legifrance.fr/",
                "is_external_link" : True,
                "link_type"  : "text", 
                "icon_class" : "", 
                "link_text"  : [{"locale" : "en", "text" : "legifrance.fr"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "legifrance.fr" }],
                "tooltip"    : [{"locale" : "en", "text" : "see the website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le site" }] 
              },
              { "is_visible" : True, 
                "link_to"    : "https://www.elysee.fr",
                "is_external_link" : True,
                "link_type"  : "text", 
                "icon_class" : "", 
                "link_text"  : [{"locale" : "en", "text" : "elysee.fr"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "elysee.fr" }],
                "tooltip"    : [{"locale" : "en", "text" : "see the website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le site" }] 
              },
              { "is_visible" : True, 
                "link_to"    : "https://www.data.gouv.fr/",
                "is_external_link" : True,
                "link_type"  : "text", 
                "icon_class" : "", 
                "link_text"  : [{"locale" : "en", "text" : "data.gouv.fr"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "data.gouv.fr" }],
                "tooltip"    : [{"locale" : "en", "text" : "see the website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le site" }] 
              },
            ]
          },

        ],

        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"  : True
      },

]