# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_app_footer = [

  ### FOOTER

    ### CONFIG 
      { "field"       : "app_footer",
        "app_version" : version,
        "help"        : u"The default footer for your ApiViz instance",

        "template_url"      : None,
        "is_dynamic"        : True,
        "dynamic_template"  : 'DynamicFooter',
        "has_credits_footer": False,
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
            # "block_class" : "is-3",
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
            # "block_class" : "is-3",
            # "link_class"  : { "value" : 'has-text-centered', "default" : "" },
            
            "position"    : "block_top_center_left",
            "title_block" : [{"locale" : "en", "text" : "Mission co-working"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les données de l'inventaire"}],
            "title_visible" : True,
            "links"       : [

              { "is_visible" : True,
                "link_to"    : "/le-projet",
                "is_external_link" : False,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "The project"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Le projet d'inventaire des orgues" }],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },
              { "is_visible" : True,
                "link_to"    : "/le-projet/outils",
                "is_external_link" : False,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "The tools"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les outils de valorisation des données" }],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },
              { "is_visible" : True,
                "link_to"    : "https://github.com/inventaire-des-orgues/indexes",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Raw data"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les données brutes" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              },
              # { "is_visible" : True,
              #   "link_to"    : "https://www.cget.gouv.fr/actualites/l-etat-s-engage-pour-soutenir-et-accelerer-la-dynamique-des-tiers-lieux-dans-les-territoires",
              #   "is_external_link" : True,
              #   "link_type"  : "text",
              #   "icon_class" : "",
              #   "link_text"  : [{"locale" : "en", "text" : "To know more"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "En savoir plus sur la mission co-working" }],
              #   "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              # },
            ]
          },

          {
            # "block_center_right" : {
            "is_visible"  : False,
            "has_socials" : False,
            # "block_class" : "is-3",
            # "link_class"  : { "value" : 'has-text-centered', "default" : "" },
            
            "position"    : "block_top_center_right",
            "title_block" : [{"locale" : "en", "text" : "Digital society"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Société numérique"}],
            "title_visible" : True,
            "links"       : [
              { "is_visible" : True,
                "link_to"    : "/login",
                "is_external_link" : False,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Login back-office"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Login back-office" }],
                "tooltip"    : [{"locale" : "en", "text" : "Login"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Login" }]
              },
            ]
          },

          {
            # "block_right" : {
            "is_visible"  : True,
            "has_socials" : True,
            # "block_class" : "is-3",
            # "link_class"  : { "value" : 'has-text-centered', "default" : "" },
            
            "position"    : "block_top_right",
            "title_block" : [{"locale" : "en", "text" : "Participate"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Participer"}],
            "title_visible" : True,
            "links"       : [
              { "is_visible" : True,
                "link_to"    : "https://www.orgue-en-france.org/",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Orgue en France"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Association Orgue en France" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "" }]
              },
              { "is_visible" : True,
                "link_to"    : "https://www.inventaire-des-orgues.fr/",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Official website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Site officiel de l'inventaire des orgues" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "" }]
              },
              { "is_visible" : True,
                "link_to"    : "https://docs.inventaire-des-orgues.fr/",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Documentation"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Documentation" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              },
              # { "is_visible" : True,
              #   "link_to"    : "/nous-rejoindre",
              #   "is_external_link" : True,
              #   "link_type"  : "text",
              #   "icon_class" : "",
              #   "link_text"  : [{"locale" : "en", "text" : "Social innovations crossroad's newsletter"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Newsletter du Carrefour des Innovations Sociales" }],
              #   "tooltip"    : [{"locale" : "en", "text" : "Newsletter"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Newsletter" }]
              # },
            ]
          },

        ],

        "apiviz_front_uuid" : uuid_models["uuid_orgues"],
        "is_default"  : True
      },

]