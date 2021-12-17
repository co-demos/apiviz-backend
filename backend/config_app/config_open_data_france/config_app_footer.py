# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_app_footer = [

  ### FOOTER

    ### CONFIG ODF 
      { "field"       : "app_footer",
        "app_version" : version,
        "help"        : u"The default footer for your ApiViz instance",

        "template_url"      : None,
        "is_dynamic"        : True,
        "dynamic_template"  : 'DynamicFooter',
        "has_credits_footer": False,
        "credits_footer_url" : "https://raw.githubusercontent.com/co-demos/ODF-carto/master/pages-html/footer-mednum.html",

        "ui_options" : {

            "card_color" : { "value" : "default_background_app", "default" : "light", },
            "card_class"  : { "value" : "", "default" : "" },

            "title_color" : { "value" : 'primary',   "default" : "white",   "custom_color" : None},
            "text_color" : { "value" : "grey-dark", "default" : "black", },

            "socials_color" : { "value" : "primary", "default" : "primary" } ,
            "socials_class" : { "value" : "", "default" : "" } ,

            "footer_logos" : [
              { "src_image" : "https://github.com/co-demos/ODF-carto/blob/master/logos/bloc-web-le-maire-darmanin.png?raw=true",
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
            "link_class"  : { "value" : 'has-text-centered', "default" : "" },

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
            "link_class"  : { "value" : 'has-text-centered', "default" : "" },

            "position"    : "block_top_center_left",
            "title_block" : [{"locale" : "en", "text" : "Partners"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Partenaires"}],
            "title_visible" : True,
            "links"       : [

              # { "is_visible" : True,
              #   "link_to"    : "https://www.etalab.gouv.fr/",
              #   "is_external_link" : True,
              #   "link_type"  : "text",
              #   "icon_class" : "",
              #   "link_text"  : [{"locale" : "en", "text" : "Etalab"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Etalab" }],
              #   "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              # },
              { "is_visible" : True,
                "link_to"    : "https://www.numerique.gouv.fr/dinum/",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "DINUM"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "DINUM" }],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },
              { "is_visible" : True,
                "link_to"    : "https://agence-cohesion-territoires.gouv.fr/",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "ANCT"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "ANCT" }],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },
              { "is_visible" : True,
                "link_to"    : "https://www.banquedesterritoires.fr/",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Banque des territoires"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Banque des territoires" }],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },
              # { "is_visible" : True,
              #   "link_to"    : "https://www.caissedesdepots.fr/",
              #   "is_external_link" : True,
              #   "link_type"  : "text",
              #   "icon_class" : "",
              #   "link_text"  : [{"locale" : "en", "text" : "Caisse des dépôts et consignations"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Caisse des dépôts et consignations" }],
              #   "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              # },
            ]
          },

          {
            # "block_center_right" : {
            "is_visible"  : True,
            "has_socials" : False,
            "block_class" : "is-3",
            "link_class"  : { "value" : 'has-text-centered', "default" : "" },

            "position"    : "block_top_center_right",
            "title_block" : [{"locale" : "en", "text" : "OpenDataFrance"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "OpenDataFrance"}],
            "title_visible" : True,
            "links"       : [

              { "is_visible" : True,
                "link_to"    : "https://www.opendatafrance.net/",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Site officiel" }],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },
              { "is_visible" : True,
                "link_to"    : "https://www.observatoire-opendata.fr/",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Observatoire open data"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Observatoire open data" }],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },

            ]
          },

          {
            # "block_right" : {
            "is_visible"  : True,
            "has_socials" : True,
            "block_class" : "is-3",
            "link_class"  : { "value" : 'has-text-centered', "default" : "" },

            "position"    : "block_top_right",
            "title_block" : [{"locale" : "en", "text" : "..."},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "En savoir plus"}],
            "title_visible" : True,
            "links"       : [
              
              { "is_visible" : True,
                "link_to"    : "/mentions-legales",
                "is_external_link" : False,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Legal"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Mentions légales" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              },
              # { "is_visible" : True,
              #   "link_to"    : "/outils",
              #   "is_external_link" : False,
              #   "link_type"  : "text",
              #   "icon_class" : "",
              #   "link_text"  : [{"locale" : "en", "text" : "Our tools"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les outils" }],
              #   "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              # },
            ]
          },

        ],

        "apiviz_front_uuid" : uuid_models["uuid_open_data_france"],
        "is_default"  : True
      },

]
