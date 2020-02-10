# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_app_footer = [

  ### FOOTER

    ### CONFIG CONUMM
      { "field"       : "app_footer",
        "app_version" : version,
        "help"        : u"The default footer for your ApiViz instance",

        "template_url"      : None,
        "is_dynamic"        : True,
        "dynamic_template"  : 'DynamicFooter',
        "has_credits_footer": False,
        "credits_footer_url" : "https://raw.githubusercontent.com/co-demos/carto-sonum/master/pages-html/footer-mednum.html",

        "ui_options" : {

            "card_color" : { "value" : None, "default" : "grey", },
            "text_color" : { "value" : None, "default" : "white", },

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
            "is_visible"  : True,
            "has_socials" : False,
            "position"    : "block_top_left",
            "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Ils soutiennent le projet"}],
            "title_visible" : True,
            "links"       : [

              { "is_visible" : True,
                "link_to"    : "https://societenumerique.gouv.fr/",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Mission digital society"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Mission Société Numérique "}],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },
              { "is_visible" : True,
                "link_to"    : "https://www.banquedesterritoires.fr",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Banque des Territoires"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Banque des Territoires" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              },

            ]
          },

          {
            # "block_center_left" : {
            "is_visible"  : True,
            "has_socials" : False,
            "position"    : "block_top_center_left",
            "title_block" : [{"locale" : "en", "text" : "Others maps"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Autres cartographies"}],
            "title_visible" : True,
            "links"       : [


              { "is_visible" : True,
                "link_to"    : "https://formations-benevoles-paysdelaloire.org/",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Formation des bénévoles le Portail Régional"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Formation des bénévoles le Portail Régional"}],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },
              { "is_visible" : True,
                "link_to"    : "https://ping-carto.netlify.com/",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Cartographie des tiers lieux en Pays de la Loire"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Cartographie des tiers lieux en Pays de la Loire" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              },
              { "is_visible" : True,
                "link_to"    : "https://www.helloasso.com/pana/",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Point d'Appui au Numérique Associatif"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Point d'Appui au Numérique Associatif" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              },
              { "is_visible" : True,
                "link_to"    : "https://www.lesbonsclics.fr/fr/cartographie",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Les Bons Clics"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les Bons Clics" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              },
            ]
          },

          {
            # "block_center_right" : {
            "is_visible"  : True,
            "has_socials" : False,
            
            "position"    : "block_top_center_right",
            "title_block" : [{"locale" : "en", "text" : "CONNUMM"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "CONUMM"}],
            "title_visible" : True,
            "links"       : [
              { "is_visible" : True,
                "link_to"    : "https://conumm.fr/",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "CONUMM website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Le site de CONUMM" }],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },
              { "is_visible" : True,
                "link_to"    : "https://conumm.fr/actions",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Our actions"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Nos actions" }],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },
              { "is_visible" : True,
                "link_to"    : "https://conumm.fr/qui-sommes-nous",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Who are we ?"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Qui sommes-nous ?" }],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },
              # { "is_visible" : True,
              #   "link_to"    : "/le-projet/outils",
              #   "is_external_link" : False,
              #   "link_type"  : "text",
              #   "icon_class" : "",
              #   "link_text"  : [{"locale" : "en", "text" : "Dataviz tools"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Les outils de valorisation des données" }],
              #   "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              # },
              # { "is_visible" : True,
              #   "link_to"    : "https://github.com/co-demos/PING-carto",
              #   "is_external_link" : True,
              #   "link_type"  : "text",
              #   "icon_class" : "",
              #   "link_text"  : [{"locale" : "en", "text" : "Source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Code source" }],
              #   "tooltip"    : [{"locale" : "en", "text" : "Login"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Login" }]
              # },
              { "is_visible" : True,
                "link_to"    : "/mentions-legales",
                "is_external_link" : False,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Legal"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Mentions légales" }],
                "tooltip"    : [{"locale" : "en", "text" : "Login"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Login" }]
              },
              # { "is_visible" : True,
              #   "link_to"    : "/login",
              #   "is_external_link" : False,
              #   "link_type"  : "text",
              #   "icon_class" : "",
              #   "link_text"  : [{"locale" : "en", "text" : "Login back-office"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Login back-office" }],
              #   "tooltip"    : [{"locale" : "en", "text" : "Login"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Login" }]
              # },
            ]
          },

          # {
          #   # "block_right" : {
          #   "is_visible"  : False,
          #   "has_socials" : True,
            
          #   "position"    : "block_top_right",
          #   "title_block" : [{"locale" : "en", "text" : "Participate"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Participer"}],
          #   "title_visible" : True,
          #   "links"       : [
          #     { "is_visible" : True,
          #       "link_to"    : "https://github.com/cget-carto/mission_coworking",
          #       "is_external_link" : True,
          #       "link_type"  : "text",
          #       "icon_class" : "",
          #       "link_text"  : [{"locale" : "en", "text" : "Improve the data"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Améliorer les données sur les tiers-lieux" }],
          #       "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
          #     },
          #     { "is_visible" : True,
          #       "link_to"    : "https://github.com/co-demos/apiviz-frontend",
          #       "is_external_link" : True,
          #       "link_type"  : "text",
          #       "icon_class" : "",
          #       "link_text"  : [{"locale" : "en", "text" : "Apps' source codes"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Code source des applications" }],
          #       "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
          #     },
          #     # { "is_visible" : True,
          #     #   "link_to"    : "/nous-rejoindre",
          #     #   "is_external_link" : True,
          #     #   "link_type"  : "text",
          #     #   "icon_class" : "",
          #     #   "link_text"  : [{"locale" : "en", "text" : "Social innovations crossroad's newsletter"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Newsletter du Carrefour des Innovations Sociales" }],
          #     #   "tooltip"    : [{"locale" : "en", "text" : "Newsletter"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Newsletter" }]
          #     # },
          #   ]
          # },

        ],

        "apiviz_front_uuid" : uuid_models["uuid_conumm"],
        "is_default"  : True
      },

]