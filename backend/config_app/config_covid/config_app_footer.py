# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_app_footer = [

  ### FOOTER

    ### CONFIG PING CARTO 
      { "field"       : "app_footer",
        "app_version" : version,
        "help"        : u"The default footer for your ApiViz instance",

        "template_url"      : None,
        "is_dynamic"        : True,
        "dynamic_template"  : 'DynamicFooter',
        "has_credits_footer": False,
        "credits_footer_url" : "https://raw.githubusercontent.com/co-demos/carto-sonum/master/pages-html/footer-mednum.html",

        "ui_options" : {


            "card_color"  : { "value" : 'dark', "default" : "default_background_app",    "custom_color" : None},
            "card_class"  : { "value" : "", "default" : "" },

            "title_color" : { "value" : 'primary',   "default" : "white",   "custom_color" : None},
            "text_color"  : { "value" : 'white-bis',   "default" : "white",   "custom_color" : None},

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
            "position"    : "block_top_left",
            "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : ""}],
            "title_visible" : True,
            "links"       : []
          },

          {
            # "block_center_left" : {
            "is_visible"  : True,
            "has_socials" : False,
            # "block_class" : "is-2 is-offset-1",
            "link_class"  : { "value" : 'has-text-centered', "default" : "" },

            "position"    : "block_top_center_left",
            "title_block" : [{"locale" : "en", "text" : "Medias & data"},{"locale" : "es", "text" : "Medias"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Médias & données"}],
            "title_visible" : True,
            "links"       : [

              { "is_visible" : True,
                "link_to"    : "https://www.lemonde.fr/les-decodeurs/article/2020/02/27/en-carte-visualisez-la-propagation-mondiale-de-l-epidemie-de-coronavirus_6031092_4355770.html",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Le Monde / decoders"},{"locale" : "es", "text" : "Le Monde / les décodeurs"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Le Monde / les décodeurs" }],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },

              { "is_visible" : True,
                "link_to"    : "https://www.gouvernement.fr/info-coronavirus/carte-et-donnees",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Data infections France"},{"locale" : "es", "text" : "Datos oficiales sobre el Covid-19 Francia"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Carte officielle Covid France" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              },

              { "is_visible" : True,
                "link_to"    : "https://www.data.gouv.fr/es/datasets/5e689ada634f4177317e4820/",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Data infections France by region"},{"locale" : "es", "text" : "Datos Covid-19 Francia por regiones"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Cas confirmés France / région" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              },

              { "is_visible" : True,
                "link_to"    : "https://mapthenews.maps.arcgis.com/apps/opsdashboard/index.html#/5df19abcf8714bc590a3b143e14a548c",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "ESRI / suivi des patients"},{"locale" : "es", "text" : "ESRI / mapa"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "ESRI / suivi des patients" }],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },

              { "is_visible" : True,
                "link_to"    : "https://github.com/CSSEGISandData/COVID-19",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Johns Hopkins CSSE"},{"locale" : "es", "text" : "Johns Hopkins CSSE"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Johns Hopkins CSSE" }],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },

            ]
          },

          {
            # "block_center_right" : {
            "is_visible"  : True,
            "has_socials" : False,
            "link_class"  : { "value" : 'has-text-centered', "default" : "" },

            "position"    : "block_top_center_right",
            "title_block" : [{"locale" : "en", "text" : "Institutions"},{"locale" : "es", "text" : "Instituciones"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Institutions"}],
            "title_visible" : True,
            "links"       : [

              { "is_visible" : True,
                "link_to"    : "https://www.gouvernement.fr/info-coronavirus",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Informations officielles Covid"},{"locale" : "es", "text" : "Informaciones oficiales Francia"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Informations officielles Covid" }],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },

              { "is_visible" : True,
                "link_to"    : "https://www.santepubliquefrance.fr/maladies-et-traumatismes/maladies-et-infections-respiratoires/infection-a-coronavirus/articles/infection-au-nouveau-coronavirus-sars-cov-2-covid-19-france-et-monde",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Santé Publique France"},{"locale" : "es", "text" : "Santé Publique France"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Santé Publique France" }],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },

              { "is_visible" : True,
                "link_to"    : "https://www.who.int/fr/emergencies/diseases/novel-coronavirus-2019",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "World Health Organization"},{"locale" : "es", "text" : "World Health Organization"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Organisation Mondiale de la Santé" }],
                "tooltip"    : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations" }]
              },

            ]
          },

          {
            # "block_right" : {
            "is_visible"  : True,
            "has_socials" : True,
            "link_class"  : { "value" : 'has-text-centered', "default" : "" },

            "position"    : "block_top_right",
            "title_block" : [{"locale" : "en", "text" : "Covid-initiatives"},{"locale" : "es", "text" : "Covid-initiatives"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Covid-initiatives"}],
            "title_visible" : True,
            "links"       : [

              { "is_visible" : True,
                "link_to"    : "/la-demarche",
                "is_external_link" : False,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Our approach"},{"locale" : "es", "text" : "Nuestro enfoque"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Notre démarche" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              },
              { "is_visible" : True,
                "link_to"    : "/contact",
                "is_external_link" : False,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Contact us"},{"locale" : "es", "text" : "Contactarnos"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Nous contacter" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              },
              # { "is_visible" : True,
              #   "link_to"    : "https://etherpad.wikimedia.org/p/covid19resources",
              #   "is_external_link" : True,
              #   "link_type"  : "text",
              #   "icon_class" : "",
              #   "link_text"  : [{"locale" : "en", "text" : "Listing"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Listing" }],
              #   "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              # },


              # { "is_visible" : True,
              #   "link_to"    : "/printers/carte",
              #   "is_external_link" : False,
              #   "link_type"  : "text",
              #   "icon_class" : "",
              #   "link_text"  : [{"locale" : "en", "text" : "3D printers map"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Carte des imprimeurs 3D" }],
              #   "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              # },

              { "is_visible" : True,
                "link_to"    : "/mentions-legales",
                "is_external_link" : False,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Legal mentions"},{"locale" : "es", "text" : "Meciones legales"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Mentions légales" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              },
              { "is_visible" : True,
                "link_to"    : "https://www.data.gouv.fr/fr/organizations/covid-initiatives/#datasets",
                "is_external_link" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Open data"},{"locale" : "es", "text" : "Open data"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Open data" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
              },
              { "is_visible" : True,
                "link_to"    : "/outils",
                "is_external_link" : False,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "Our tools"},{"locale" : "es", "text" : "Nuestras herramientas"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Nos outils" }],
                "tooltip"    : [{"locale" : "en", "text" : "See the source code"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voir le code" }]
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

        ],

        "apiviz_front_uuid" : uuid_models["uuid_covid"],
        "is_default"  : True
      },

]