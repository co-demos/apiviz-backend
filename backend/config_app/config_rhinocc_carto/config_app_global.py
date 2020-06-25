# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_global_config = [

  ### - - - - - - - - - - - - - - - ###
  ### CONFIG PING CARTO

    ### LANGUAGES
      { "field"       : "app_languages",
        "languages"   : ["fr"], # [ "fr", "en" ]
        "is_multi_lang" : False,
        "locale"      : "fr",
        "app_version" : version,
        "help"        : u"The default homepage for your ApiViz instance",
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"  : True
      },

      { "field"       : "app_basic_dict",
        "app_version" : version,
        "help"        : u"The default dict for your ApiViz instance",
        "no_data"        : [{"locale" : "en", "text" : "no data"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "non renseigné" }],
        "reinit_filters" : [{"locale" : "en", "text" : "delete filters"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Supprimer tous les filtres" }],
        "no_abstract"    : [{"locale" : "en", "text" : "no abstract"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "(Pas de résumé)" }],
        "no_address"     : [{"locale" : "en", "text" : "no address"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Pas d'adresse enregistrée" }],
        "no_info"        : [{"locale" : "en", "text" : "no info"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Pas d'information" }],
        
        "source"         : [{"locale" : "en", "text" : "Source"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Source" }],
        "back_to_results": [{"locale" : "en", "text" : "Back to results"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Retour aux résultats de recherche" }],
        "see_website"    : [{"locale" : "en", "text" : "Check the website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Aller sur le site" }],
        "see_contact"    : [{"locale" : "en", "text" : "See the contact"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Contact" }],
        "share_link"     : [{"locale" : "en", "text" : "Share this link"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Partagez ce lieu" }],
        "infos"          : [{"locale" : "en", "text" : "Infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Informations pratiques" }],
        "open_infos"     : [{"locale" : "en", "text" : "Schedule"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Horaires" }],
        "more_infos"     : [{"locale" : "en", "text" : "More infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Autres informations" }],
        # "name"           : [{"locale" : "en", "text" : "name"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "prénom" }],
        # "surname"        : [{"locale" : "en", "text" : "surname"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "nom" }],
        "tel"            : [{"locale" : "en", "text" : "Phone"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Téléphone" }],
        "period"         : [{"locale" : "en", "text" : "Period"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Période" }],
        "services"       : [{"locale" : "en", "text" : "Services"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Services proposés" }],
        "dowload_file"   : [{"locale" : "en", "text" : "Download document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Télécharger le document" }],

        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"  : True
      },

      # { "field"       : "app_screen_tabs",
      #   "app_version" : version,
      #   "help"        : u"The default homepage for your ApiViz instance",
      #   "tab_list"    : {
      #     "link_text"  : [ {"locale" : "en", "text" : "list"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "liste" }],
      #   },
      #   "tab_map"    : {
      #     "link_text"  : [ {"locale" : "en", "text" : "map"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "carte" }],
      #   },
      #   "tab_stat"    : {
      #     "link_text"  : [ {"locale" : "en", "text" : "data"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "données" }],
      #   },
      #   "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
      #   "is_default"  : True
      # },

    ### LOGO
      { "field"       : "app_logo",
        "content"     : u"apiviz default logo in navbar",
        # "url"         : "http://localhost:8800/statics/logos/logo_TLF_carré_04.png",
        "url"           : "https://raw.githubusercontent.com/co-demos/PING-carto/master/logos/logo_ping.png",
        "app_version" : version,
        "help"        : u"The official default logo for your ApiViz instance",
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"  : True
      },

    ### FAVICON
      { "field"       : "app_favicon",
        "content"     : u"apiviz default favicon in browser",
        "url"           : "https://raw.githubusercontent.com/co-demos/PING-carto/master/logos/logo_ping.png",
        "app_version" : version,
        "help"        : u"The default favicon for your ApiViz instance",
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"  : True
      },

    ### METAS
      { "field"       : "app_title",
        "app_version" : version,
        "help"        : u"Choose a title for your ApiViz instance",

        "can_be_used_as_model" : True,
        # "image_preview" : "https://raw.githubusercontent.com/co-demos/apiviz-frontend/master/documentation/screenshots/list-view-apcis-01.png",
        "image_preview" : "https://raw.githubusercontent.com/co-demos/PING-carto/master/documentation/screenshots/map-view-tiers-lieux-01.png",

        "content"      : u"Carto PiNG",
        "content_text" : [{"locale" : "en", "text" : "A lookout at third places in Loire region"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Regards sur les tiers-lieux en Pays de la Loire"}],
        "content_size" : 7,
        "is_in_navbar" : True,
        # "title_color" : "primary",

        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"  : True
      },

      { "field"       : "app_description",
        "app_version" : version,
        "help"        : u"Choose a description for your ApiViz instance",
        "content"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : ""}],
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"  : True
      },

      { "field"       : "app_keywords",
        "app_version" : version,
        "help"        : u"Choose a set of keywords for your ApiViz instance",
        "content"     : u"""dataviz,data visualisation,data visualization,SIG,commons,digital commons,API,opensource,open source,open data,opendata,MIT licence,github,sJS,javascript,python,flask,HTML,CSS,JSON,bulma,Vue.js,sEtalab,co-demos, codemos""",
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"  : True
      },

    ### GLOBAL CONTENTS / TEXTS
      { "field"       : "app_welcome",
        "app_version" : version,
        "help"        : u"Choose a welcoming phrase for your ApiViz instance",
        "content"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Bienvenue"}],
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"  : True
      },

      { "field"       : "app_pitch",
        "app_version" : version,
        "help"        : u"Choose a pitch/catchphrase for your ApiViz instance",
        "content"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : ""}],
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"  : True
      },

    ### REPO GITHUB
      { "field"       : "app_code",
        "url"         : "https://github.com/co-demos/apiviz-frontend",
        "app_version" : version,
        "help"        : u"Choose the repo for the source code of your ApiViz instance",
        "content"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Code source"}],
        "in_navbar"   : False,
        "in_footer"   : True,
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"  : True,
      },

    ### FAVORITES
      { "field"       : "app_favorites",
        "app_version" : version,
        "help"        : u"Choose is users can use favorites (cookies)",
        "content"     : u"",
        "activated"   : False,
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"  : True
      },

    ### SEO / INDEXING
      { "field"       : "app_indexing",
        "app_version" : version,
        "help"        : u"Choose a token for indexing your ApiViz instance",
        "content"     : u"",
        "activated"    : False,
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"  : True
      },

    ### ANALYTICS
      { "field"       : "app_analytics",
        "app_version" : version,
        "help"        : u"Choose the token for the analytics (ex. mix panel) of your ApiViz instance",
        "content"     : u"your_id_or_token",
        "url"         : "",
        "activated"    : False,
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"  : True
      },

    ### SUPPORT
      { "field"       : "app_support",
        "app_version" : version,
        "help"        : u"Choose the token for the support (ex. crisp) of your ApiViz instance",
        "content"     : u"your_id_or_token",
        "url"         : "",
        "activated"    : False,
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"  : True
      },


]
