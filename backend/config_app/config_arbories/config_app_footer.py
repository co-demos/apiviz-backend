# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_app_footer = [

  ### FOOTER

    ### CONFIG DECIDER ENSEMBLE CARTO 
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
            "block_class" : "is-3",
            # "link_class"  : { "value" : 'has-text-centered', "default" : "" },

            "position"    : "block_top_left",
            "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : ""}],
            "title_visible" : True,
            "links"       : []
          },

          {
            # "block_center_left" : {
            "is_visible"  : False,
            "has_socials" : False,
            "block_class" : "is-3",
            # "link_class"  : { "value" : 'has-text-centered', "default" : "" },

            "position"    : "block_top_center_left",
            "title_block" : [{"locale" : "en", "text" : "Partners"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Partenaires"}],
            "title_visible" : True,
            "links"       : [

              { "is_visible" : True,
                "link_to"    : "http://arbories.free.fr/",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Arbories"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Arbories" }],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },
              # { "is_visible" : True,
              #   "link_to"    : "https://www.cget.gouv.fr/",
              #   "is_external_link" : True,
              #   "link_type"  : "text",
              #   "icon_class" : "",
              #   "link_text"  : [{"locale" : "en", "text" : "CGET / ANCT"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "CGET / ANCT" }],
              #   "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              # },
              # { "is_visible" : True,
              #   "link_to"    : "http://www.cress-pdl.org/",
              #   "is_external_link" : True,
              #   "link_type"  : "text",
              #   "icon_class" : "",
              #   "link_text"  : [{"locale" : "en", "text" : "CRESS"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "CRESS" }],
              #   "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              # },
            ]
          },

          {
            # "block_center_right" : {
            "is_visible"  : False,
            "has_socials" : False,
            "block_class" : "is-3",
            # "link_class"  : { "value" : 'has-text-centered', "default" : "" },
            
            "position"    : "block_top_center_right",
            "title_block" : [{"locale" : "en", "text" : "To know more"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Pour aller plus loin"}],
            "title_visible" : True,
            "links"       : [

              { "is_visible" : True,
                "link_to"    : "https://movilab.org/index.php?title=Accueil",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Movilab"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Movilab" }],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },
              { "is_visible" : True,
                "link_to"    : "https://francetierslieux.fr/",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "FTL association"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Association France Tiers-Lieux" }],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },
              { "is_visible" : True,
                "link_to"    : "https://www.cget.gouv.fr/actualites/l-etat-s-engage-pour-soutenir-et-accelerer-la-dynamique-des-tiers-lieux-dans-les-territoires",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "CGET's mission on co-working"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Mission co-working du CGET" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              },

            ]
          },

          {
            # "block_right" : {
            "is_visible"  : True,
            "has_socials" : True,
            "block_class" : "is-4",
            "link_class"  : { "value" : 'has-text-centered', "default" : "" },
            
            "position"    : "block_top_right",
            "title_block" : [{"locale" : "en", "text" : "Les Arbories"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les Arbories"}],
            "title_visible" : True,
            "links"       : [
              
              # { "is_visible" : True,
              #   "link_to"    : "https://www.deciderensemble.com",
              #   "is_external_link" : True,
              #   "link_type"  : "text",
              #   "icon_class" : "",
              #   "link_text"  : [{"locale" : "en", "text" : "Official website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Site officiel" }],
              #   "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              # },
              { "is_visible" : True,
                "link_to"    : "http://arbories.free.fr/",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Who are we ?"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Qui sommes-nous ?" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              },
              # { "is_visible" : True,
              #   "link_to"    : "https://www.deciderensemble.com/page/724845-actuss",
              #   "is_external_link" : True,
              #   "link_type"  : "text",
              #   "icon_class" : "",
              #   "link_text"  : [{"locale" : "en", "text" : "Our news"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Actualités" }],
              #   "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              # },
              { "is_visible" : True,
                "link_to"    : "/mentions-legales",
                "is_external_link" : False,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Legal"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Mentions légales" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              },
              { "is_visible" : True,
                "link_to"    : "/outils",
                "is_external_link" : False,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Our tools"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les outils" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              },
              { "is_visible" : True,
                "link_to"    : "mailto:lesarbories@gmail.com",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Who are we ?"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Nous contacter : lesarbories@gmail.com" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              },

            ]
          },

        ],

        "apiviz_front_uuid" : uuid_models["uuid_arbories"],
        "is_default"  : True
      },

]