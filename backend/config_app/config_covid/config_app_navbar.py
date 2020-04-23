# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_app_navbar = [

  ### MAIN NAVBAR

    ### - - - - - - - - - - - - - - - ###
    ### CONFIG COVID 
      { "field"       : "app_navbar",
        "content"     : u"TL navbar",
        "app_version" : version,
        "help"        : u"The navbar of your ApiViz instance",
        "logo_to"     : "/",
        "has_login"   : False,
        "ui_options"  : {
          "background_isdark" : True,
          "background_color" : { 
            "bulma_color" : "primary"
          },

        },
        "links_options" : {
          "extra_buttons" : [ ### for buttons not declared in routes/pages


            { "is_visible" : True,
              "position"   : "exterior_right",
              # "link_to"    : "/printers/carte",
              "link_to"    : "/map-ext",
              "help"       : u"First menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "Maps"},{"locale" : "es", "text" : "Mapas"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Cartes" }],
              "tooltip"    : [{"locale" : "en", "text" : "Begin a search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Lancer une recherche" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/map-ext", "link_text" : [{"locale" : "en", "text" : "Makers' map"},{"locale" : "es", "text" : "Mapa de los makers"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Carte des makers"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/printers", "link_text" : [{"locale" : "en", "text" : "3D printers map"},{"locale" : "es", "text" : "Mapa de impresores 3D"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Carte des imprimeurs 3D - démo apiviz"}] },
                # { "is_divider" : True,  "is_external_link" : False },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.makery.info/labs-map/", "link_text" : [{"locale" : "en", "text" : "-->   Map Makery"},{"locale" : "es", "text" : "--> Mapa Makery"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Carte Makery"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://antoineh1.carto.com/builder/ee0ce4e3-847d-4c7b-beb0-24972dc154c3/embed", "link_text" : [{"locale" : "en", "text" : "-->   Map 3D printers Carto"},{"locale" : "es", "text" : "--> Mapa impresion 3D Carto"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Carte impression 3D Carto"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.google.com/maps/d/u/0/viewer?mid=1RMGwwBX6djxep-8XqWhAWtTWr30tNECE&ll=46.72403044880883%2C2.5414200499999424&z=6", "link_text" : [{"locale" : "en", "text" : "-->   Groupes Facebook Visières Solidaires"},{"locale" : "es", "text" : "--> Groupes Facebook Visières Solidaires"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Groupes Facebook Visières Solidaires"}] },
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/map-printers", "link_text" : [{"locale" : "en", "text" : "-->   Handdle Map 3D printers"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Carte Handdle impression 3D"}] },
              ]
            },

            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/diy/liste",
              "help"       : u"First menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "DIY designs"},{"locale" : "es", "text" : "Diseños DIY"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Designs DIY" }],
              "tooltip"    : [{"locale" : "en", "text" : "Begin a search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Lancer une recherche" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/diy/liste", "link_text" : [{"locale" : "en", "text" : "DIY materials inventory"},{"locale" : "es", "text" : "Materiales DIY"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Liste de matériels DIY"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/selection-diy", "link_text" : [{"locale" : "en", "text" : "Our DIY materials selection"},{"locale" : "es", "text" : "Nuestra seleccion de materiales DIY"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Notre sélection de matériels DIY"}] },
                # { "is_divider" : True,  "is_external_link" : False },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://fablabs-vs-covid.netlify.com/", "link_text" : [{"locale" : "en", "text" : "-->  Fablabs vs Covid"},{"locale" : "es", "text" : "-->  Fablabs vs Covid"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Fablabs vs Covid"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "http://covid3d.org/", "link_text" : [{"locale" : "en", "text" : "-->   3D Covid APHP"},{"locale" : "es", "text" : "-->  3D Covid APHP"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   3D Covid APHP"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.mur-project.org/", "link_text" : [{"locale" : "en", "text" : "-->   Minimal Universal Respirator"},{"locale" : "es", "text" : "-->  Minimal Universal Respirator"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Minimal Universal Respirator"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://e-vent.mit.edu/", "link_text" : [{"locale" : "en", "text" : "-->   MIT Emergency Ventilator (E-Vent)"},{"locale" : "es", "text" : "--> MIT Emergency Ventilator (E-Vent)"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   MIT Emergency Ventilator (E-Vent)"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://app.jogl.io/project/118#about", "link_text" : [{"locale" : "en", "text" : "-->   Low-cost & Open-Source Covid19 Detection kits"},{"locale" : "es", "text" : "-->  Low-cost & Open-Source Covid19 Detection kits"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Low-cost & Open-Source Covid19 Detection kits"}] },
                # { "is_divider" : True,  "is_external_link" : False },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://discordapp.com/channels/689048131253698563/689048131697901592", "link_text" : [{"locale" : "en", "text" : "-->   Discord Makers"},{"locale" : "es", "text" : "-->   Discord Maker"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Discord Entraide entre Makers – Mr Bidouille"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://app.jogl.io/project/130", "link_text" : [{"locale" : "en", "text" : "-->   Makers for health and hospitals"},{"locale" : "es", "text" : "-->   Makers for health and hospitals"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Makers pour aider hôpitaux et soignants – JOGL"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "http://www.fablab.fr/coronavirus/prototypage-et-projets/", "link_text" : [{"locale" : "en", "text" : "-->   Recommandations RFF labs"},{"locale" : "es", "text" : "-->   Recommandations RFF labs"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Recommandations du RFFLabs pour les Makers"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://fr.utopiamaker.com/", "link_text" : [{"locale" : "en", "text" : "-->   Utopia Maker"},{"locale" : "es", "text" : "-->   Utopia Make"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Utopia Maker – Relais makers près de chez vous"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://sosequipements.fr/", "link_text" : [{"locale" : "en", "text" : "-->   SOS equipments"},{"locale" : "es", "text" : "-->   SOS equipments"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   SOS équipements"}] },
                # # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://app.sraswars.org/", "link_text" : [{"locale" : "en", "text" : "-->   FabriCommuns : liens Makers – Hôpitaux"},{"locale" : "es", "text" : "-->   FabriCommuns : liens Makers – Hôpitaux"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   FabriCommuns : liens Makers – Hôpitaux"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://3d.freerider-factory.fr/", "link_text" : [{"locale" : "en", "text" : "-->   3D printings– Freerider Factory"},{"locale" : "es", "text" : "-->   3D printings– Freerider Factory"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Réserve d’impression 3D – Freerider Factory"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.avosmasques.fr/", "link_text" : [{"locale" : "en", "text" : "-->   A vos masques"},{"locale" : "es", "text" : "-->   A vos masques"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   A vos masques"}] },
              ]
            },

            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/kifekoi/liste",
              "help"       : u"Other menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "Productions"},{"locale" : "es", "text" : "Producciones"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Productions" }],
              "tooltip"    : [{"locale" : "en", "text" : "Begin a search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Lancer une recherche" }],
              "has_dropdown" : False,
              "dropdowns"  : [

              ]
            },

            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/recherche/liste",
              "help"       : u"First menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "Initiatives"},{"locale" : "es", "text" : "Iniciativas"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Initiatives solidaires" }],
              "tooltip"    : [{"locale" : "en", "text" : "Begin a search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Lancer une recherche" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/recherche", "link_text" : [{"locale" : "en", "text" : "Initiatives inventory"},{"locale" : "es", "text" : "Lista de iniciativas"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Liste des initiatives"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/selection-initiatives", "link_text" : [{"locale" : "en", "text" : "Our selection of initiatives"},{"locale" : "es", "text" : "Nuestra seleccion de iniciativas"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Notre sélection d'initiatives"}] },
                # { "is_divider" : True,  "is_external_link" : False },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.continuitepedagogique.org/", "link_text" : [{"locale" : "en", "text" : "-->   Continuité pédagogique"},{"locale" : "es", "text" : "-->   Continuité pédagogique"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Continuité pédagogique"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.latitudes.cc/covid19", "link_text" : [{"locale" : "en", "text" : "-->   Latitudes"},{"locale" : "es", "text" : "-->   Latitudes"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Latitudes contre le Covid"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://covid19.reserve-civique.gouv.fr/", "link_text" : [{"locale" : "en", "text" : "-->   Réserve civique"},{"locale" : "es", "text" : "-->   Réserve civique"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Réserve civique"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://bzg.fr/covid19-developpeurs-datascientistes-comment-aider/", "link_text" : [{"locale" : "en", "text" : "-->   Devs/data-scientists..."},{"locale" : "es", "text" : "-->   Devs/data-scientists..."},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Développeurs/data-scientists..."}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://enpremiereligne.fr/", "link_text" : [{"locale" : "en", "text" : "-->   En première ligne"},{"locale" : "es", "text" : "-->   En première ligne"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   En première ligne"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://gscn.eu.org/", "link_text" : [{"locale" : "en", "text" : "-->   Digital help group"},{"locale" : "es", "text" : "-->   Digital help group"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Groupe de Soutien en cas de Crise Numérique"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.le-frenchimpact.fr/nos-actualites/entraide", "link_text" : [{"locale" : "en", "text" : "-->   French Impact"},{"locale" : "es", "text" : "->   French Impact"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   French Impact contre le Covid"}] },
                # { "is_divider" : True,  "is_external_link" : False },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.handddle.com/covid19/", "link_text" : [{"locale" : "en", "text" : "Map 3D printers"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Carte impression 3D"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.latitudes.cc/covid19", "link_text" : [{"locale" : "en", "text" : "Latitudes"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Latitudes contre le Covid"}] },
              ]
            },


            # { "is_visible" : True,
            #   "position"   : "exterior_right",
            #   "link_to"    : "/la-demarche",
            #   "help"       : u"Second menu in navbar",
            #   "is_external_link" : False,
            #   "link_type"  : "link", ### show btn border
            #   "icon_class" : "",
            #   "link_text"  : [{"locale" : "en", "text" : "Our selection"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Notre sélection" }],
            #   "tooltip"    : [{"locale" : "en", "text" : "More infos on the topic"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations sur ce site" }],
            #   "has_dropdown" : True,
            #   "dropdowns"  : [
            #   ]
            # },


            # { "is_visible" : True,
            #   "position"   : "exterior_right",
            #   "link_to"    : "/charts-europe",
            #   "help"       : u"Second menu in navbar",
            #   "is_external_link" : False,
            #   "link_type"  : "link", ### show btn border
            #   "icon_class" : "",
            #   "link_text"  : [{"locale" : "en", "text" : "Charts Covid-19"},{"locale" : "es", "text" : "Datos sobre el Covid"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Graphiques" }],
            #   "tooltip"    : [{"locale" : "en", "text" : "More infos on the topic"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations sur ce site" }],
            #   "has_dropdown" : True,
            #   "dropdowns"  : [

            #   ]
            # },
            

            { "is_visible" : True,
              "position"   : "exterior_right",
              "link_to"    : "/la-demarche",
              "help"       : u"Second menu in navbar",
              "is_external_link" : False,
              "link_type"  : "link", ### show btn border
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "Our approach"},{"locale" : "es", "text" : "Nuestro enfoque"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Notre démarche" }],
              "tooltip"    : [{"locale" : "en", "text" : "More infos on the topic"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Plus d’informations sur ce site" }],
              "has_dropdown" : True,
              "dropdowns"  : [
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/la-demarche", "link_text" : [{"locale" : "en", "text" : "Our approach"},{"locale" : "es", "text" : "Nuestro enfoque"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Notre démarche"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/qui-sommes-nous", "link_text" : [{"locale" : "en", "text" : "Who are we ?"},{"locale" : "es", "text" : "¿Quienes somos ?"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Qui sommes-nous ?"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/contact", "link_text" : [{"locale" : "en", "text" : "Contact us"},{"locale" : "es", "text" : "Contactarnos"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Nous contacter"}] },
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/utiliser-le-site", "link_text" : [{"locale" : "en", "text" : "charts France"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Utiliser le site"}] },
                { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.data.gouv.fr/fr/organizations/covid-initiatives/#datasets", "link_text" : [{"locale" : "en", "text" : "Our data"},{"locale" : "es", "text" : "Nuestros datos"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Nos données"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/revue-presse", "link_text" : [{"locale" : "en", "text" : "Press review"},{"locale" : "es", "text" : "Revista de prensa"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Revue de presse"}] },
                { "is_divider" : True,  "is_external_link" : False },
                # { "is_divider" : True,  "is_external_link" : False },
                # { "is_divider" : True,  "is_external_link" : False },
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/ressources-officielles", "link_text" : [{"locale" : "en", "text" : "Ressources - official"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Ressources officielles"}] },
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/ressources-makers", "link_text" : [{"locale" : "en", "text" : "Ressources - makers"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Ressources makers"}] },
                # { "is_divider" : False, "is_external_link" : False, "link_to" : "/ressources-données", "link_text" : [{"locale" : "en", "text" : "Ressources - datasets"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Ressources données"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/charts-france", "link_text" : [{"locale" : "en", "text" : "Covid-19 data France"},{"locale" : "es", "text" : "Datos Francia"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Données covid-19 France"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/charts-europe", "link_text" : [{"locale" : "en", "text" : "Covid-19 data Europe"},{"locale" : "es", "text" : "Datos Europa"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Données covid-19 Europe"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/charts-world",  "link_text" : [{"locale" : "en", "text" : "Covid-19 data World"},{"locale" : "es", "text" : "Datos mundo"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Données covid-19 Monde"}] },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/charts-sources",   "link_text" : [{"locale" : "en", "text" : "Sources"},{"locale" : "es", "text" : "Fuentes de los datos"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Sources"}] },
                { "is_divider" : True,  "is_external_link" : False },
                { "is_divider" : False, "is_external_link" : False, "link_to" : "/mentions-legales", "link_text" : [{"locale" : "en", "text" : "Legal mentions"},{"locale" : "es", "text" : "Menciones legales"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Mentions légales"}] },
                # { "is_divider" : True,  "is_external_link" : False },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.gouvernement.fr/info-coronavirus/", "link_text" : [{"locale" : "en", "text" : "-->   French government official website"},{"locale" : "es", "text" : "-->   French government official website"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Site officiel du gouvernement sur le Covid19"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.gouvernement.fr/info-coronavirus/carte-et-donnees", "link_text" : [{"locale" : "en", "text" : "-->   Covid map for France"},{"locale" : "es", "text" : "-->   Covid map for France"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Carte et données officielles"}] },
                # { "is_divider" : True,  "is_external_link" : False },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.lemonde.fr/les-decodeurs/article/2020/02/27/en-carte-visualisez-la-propagation-mondiale-de-l-epidemie-de-coronavirus_6031092_4355770.html", "link_text" : [{"locale" : "en", "text" : "-->   Le Monde - Covid charts"},{"locale" : "es", "text" : "-->   Le Monde - Covid charts"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Le Monde - évolution du Covid"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.nytimes.com/interactive/2020/world/coronavirus-maps.html", "link_text" : [{"locale" : "en", "text" : "-->   NY Times Covid maps"},{"locale" : "es", "text" : "-->   NY Times Covid maps"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   New York Times - cartes et données "}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.nytimes.com/interactive/2020/03/22/world/coronavirus-spread.html", "link_text" : [{"locale" : "en", "text" : "-->   NY Times - how the virus got out"},{"locale" : "es", "text" : "-->   NY Times - how the virus got ou"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   New York Times - how the virus got out"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://mapthenews.maps.arcgis.com/apps/opsdashboard/index.html#/5df19abcf8714bc590a3b143e14a548c", "link_text" : [{"locale" : "en", "text" : "-->   ESRI - suivi des patients"},{"locale" : "es", "text" : "-->   ESRI - suivi des patients"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   ESRI - suivi des patients"}] },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://veille-coronavirus.fr/",   "link_text" : [{"locale" : "en", "text" : "-->   Dataviz France"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Veille Coronavirus France"}] },
                # { "is_divider" : True,  "is_external_link" : False },
                # { "is_divider" : False, "is_external_link" : True, "link_to" : "https://www.covid19-que-lire.fr/", "link_text" : [{"locale" : "en", "text" : "-->   What to read ? "},{"locale" : "es", "text" : "-->   What to read ? "},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "-->   Que lire ?"}] },
              ]
            },

          ]
        },
        "apiviz_front_uuid" : uuid_models["uuid_covid"],
        "is_default"  : True
      },

]