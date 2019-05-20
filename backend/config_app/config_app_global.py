# -*- encoding: utf-8 -*-

from . import version

default_global_config = [

  ### - - - - - - - - - - - - - - - ###
  ### CONFIG SONUM 

    ### LANGUAGES
      { "field"       : "app_languages",
        "languages"   : ["fr"],
        "locale"      : "fr",
        "app_version" : version,
        "help"        : u"The default homepage for your ApiViz instance",
        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"  : True
      },

      { "field"       : "app_basic_dict",
        "app_version" : version,
        "help"        : u"The default dict for your ApiViz instance",

        "no_data"        : [{"locale" : "fr", "text" : "non renseigné" }],
        "reinit_filters" : [{"locale" : "fr", "text" : "Supprimer tous les filtrees" }],
        "no_abstract"    : [{"locale" : "fr", "text" : "(Pas de résumé)" }],
        "no_address"     : [{"locale" : "fr", "text" : "Pas d'adresse enregistrée" }],
        "no_info"        : [{"locale" : "fr", "text" : "Pas d'information" }],
        
        "source"         : [{"locale" : "fr", "text" : "Source" }],
        "back_to_results": [{"locale" : "fr", "text" : "Retour aux résultats de recherche" }],
        "see_website"    : [{"locale" : "fr", "text" : "Aller sur le site" }],
        "see_contact"    : [{"locale" : "fr", "text" : "Contact" }],
        "share_link"     : [{"locale" : "fr", "text" : "Partagez ce lieu" }],
        "infos"          : [{"locale" : "fr", "text" : "Informations pratiques" }],
        "open_infos"     : [{"locale" : "fr", "text" : "Horaires" }],
        "more_infos"     : [{"locale" : "fr", "text" : "Autres informations" }],
        "name"           : [{"locale" : "fr", "text" : "prénom" }],
        "surname"        : [{"locale" : "fr", "text" : "nom" }],
        "tel"            : [{"locale" : "fr", "text" : "Téléphone" }],
        "period"         : [{"locale" : "fr", "text" : "Période" }],
        "services"       : [{"locale" : "fr", "text" : "Services proposés" }],
        "dowload_file"   : [{"locale" : "fr", "text" : "Télécharger le document" }],

        "hello"          : [{"locale" : "fr", "text" : "Bonjour" }],
        "pref_user"      : [{"locale" : "fr", "text" : "Préférences" }],
        "backoffice"     : [{"locale" : "fr", "text" : "Back-office" }],
        "email"          : [{"locale" : "fr", "text" : "email" }],

        "login"          : [{"locale" : "fr", "text" : "Login" }],
        "connect"        : [{"locale" : "fr", "text" : "Se connecter" }],
        "connected"      : [{"locale" : "fr", "text" : "déjà connecté" }],
        "reconnect"      : [{"locale" : "fr", "text" : "Se reconnecter" }],
        "disconnect"     : [{"locale" : "fr", "text" : "Se déconnecter" }],
        "disconnect_msg" : [{"locale" : "fr", "text" : "Vous avez été déconnecté.e avec succès" }],
        "want_disconnect": [{"locale" : "fr", "text" : "Voulez-vous vous déconnecter ?" }],
        "is_account"     : [{"locale" : "fr", "text" : "Vous avez déjà un compte ?" }],
        "no_account"     : [{"locale" : "fr", "text" : "Vous n'avez pas encore de compte ?" }],
        "register"       : [{"locale" : "fr", "text" : "S'inscrire" }],
        "is_registered"  : [{"locale" : "fr", "text" : "Vous êtes déjà inscrit.e" }],
        "logout"         : [{"locale" : "fr", "text" : "Se déconnecter" }],
        "name"           : [{"locale" : "fr", "text" : "prénom" }],
        "surname"        : [{"locale" : "fr", "text" : "nom" }],
        "password"       : [{"locale" : "fr", "text" : "mot de passe" }],
        "password_bis"   : [{"locale" : "fr", "text" : "répéter le mot de passe" }],
        "remember_me"    : [{"locale" : "fr", "text" : "se souvenir de moi" }],
        "forgot_password": [{"locale" : "fr", "text" : "Mot de passe oublié ?" }],
        "create_account" : [{"locale" : "fr", "text" : "Créer un compte" }],
        "accept_cgu"     : [{"locale" : "fr", "text" : "J'accepte les CGU" }],

        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"  : True
      },

      { "field"       : "app_screen_tabs",
        "app_version" : version,
        "help"        : u"The default homepage for your ApiViz instance",
        "tab_list"    : { 
          "link_text"  : [ {"locale" : "fr", "text" : "liste" }],
        },
        "tab_map"    : { 
          "link_text"  : [ {"locale" : "fr", "text" : "carte" }],
        },
        "tab_stat"    : { 
          "link_text"  : [ {"locale" : "fr", "text" : "données" }],
        },
        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"  : True
      },

    ### LOGO
      { "field"       : "app_logo",
        "content"     : u"apiviz default logo in navbar",
        "url"          : "https://github.com/co-demos/carto-sonum/blob/master/logos/logo%2Bmarianne_typo%20sombre%404x.png?raw=true",
        "app_version" : version,
        "help"        : u"The official default logo for your ApiViz instance",
        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"  : True
      },

    ### FAVICON
      { "field"       : "app_favicon",
        "content"     : u"apiviz default favicon in browser",
        "url"          : "/",
        "app_version" : version,
        "help"        : u"The default favicon for your ApiViz instance",

        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"  : True
      },

    ### METAS
      { "field"       : "app_title",
        "app_version" : version,
        "help"        : u"Choose a title for your ApiViz instance",
        "content"     : u"SoNum",

        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"  : True
      },

      { "field"       : "app_description",
        "app_version" : version,
        "help"        : u"Choose a description for your ApiViz instance",
        "content"     : [{ "locale" : "fr", "text" : ""}],

        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"  : True
      },

      { "field"       : "app_keywords",
        "app_version" : version,
        "help"        : u"Choose a set of keywords for your ApiViz instance",
        "content"     : u"""dataviz,data visualisation,data visualization,SIG,commons,digital commons,API,opensource,open source,open data,opendata,MIT licence,github,sJS,javascript,python,flask,HTML,CSS,JSON,bulma,Vue.js,sEtalab,co-demos, codemos""",

        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"  : True
      },

    ### GLOBAL CONTENTS / TEXTS
      { "field"       : "app_welcome",
        "app_version" : version,
        "help"        : u"Choose a welcoming phrase for your ApiViz instance",
        "content"     : [{ "locale" : "fr", "text" : "Bienvenue"}],

        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"  : True
      },

      { "field"       : "app_pitch",
        "app_version" : version,
        "help"        : u"Choose a pitch/catchphrase for your ApiViz instance",
        "content"     : [{ "locale" : "fr", "text" : ""}],

        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"  : True
      },

    ### REPO GITHUB
      { "field"       : "app_code",
        "url"         : "https://github.com/co-demos/ApiViz",
        "app_version" : version,
        "help"        : u"Choose the repo for the source code of your ApiViz instance",
        "content"     : [{ "locale" : "fr", "text" : "Code source"}],
        "in_navbar"   : False,
        "in_footer"   : True,

        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"  : True,
      },
    
    ### SEO / INDEXING
      { "field"       : "app_indexing",
        "app_version" : version,
        "help"        : u"Choose a token for indexing your ApiViz instance",
        "content"     : u"", 
        "activated"    : False,

        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"  : True
      },

    ### ANALYTICS
      { "field"       : "app_analytics",
        "app_version" : version,
        "help"        : u"Choose the token for the analytics (ex. mix panel) of your ApiViz instance",
        "content"     : u"your_id_or_token",
        "url"         : "",
        "activated"    : False,

        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"  : True
      },

    ### SUPPORT 
      { "field"       : "app_support",
        "app_version" : version,
        "help"        : u"Choose the token for the support (ex. crisp) of your ApiViz instance",
        "content"     : u"your_id_or_token",
        "url"         : "",
        "activated"    : False,

        "apiviz_front_uuid" : "c5efafab-1733-4ad1-9eb8-d529bc87c481",
        "is_default"  : True
      },


  ### - - - - - - - - - - - - - - - ###
  ### CONFIG APCIS

    ### LANGUAGES
      { "field"       : "app_languages",
        "languages"   : ["fr"],
        "locale"      : "fr",
        "app_version" : version,
        "help"        : u"The default homepage for your ApiViz instance",
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"  : True
      },

      { "field"       : "app_basic_dict",
        "app_version" : version,
        "help"        : u"The default dict for your ApiViz instance",

        "no_data"        : [{"locale" : "fr", "text" : "non renseigné" }],
        "reinit_filters" : [{"locale" : "fr", "text" : "Supprimer tous les filtrees" }],
        "no_abstract"    : [{"locale" : "fr", "text" : "(Pas de résumé)" }],
        "no_address"     : [{"locale" : "fr", "text" : "Pas d'adresse enregistrée" }],
        "no_info"        : [{"locale" : "fr", "text" : "Pas d'information" }],

        "source"         : [{"locale" : "fr", "text" : "Source" }],
        "back_to_results": [{"locale" : "fr", "text" : "Retour aux résultats de recherche" }],
        "see_website"    : [{"locale" : "fr", "text" : "Aller sur le site" }],
        "see_contact"    : [{"locale" : "fr", "text" : "Contact" }],
        "share_link"     : [{"locale" : "fr", "text" : "Partagez ce lien" }],
        "infos"          : [{"locale" : "fr", "text" : "Informations pratiques" }],
        "open_infos"     : [{"locale" : "fr", "text" : "Horaires" }],
        "more_infos"     : [{"locale" : "fr", "text" : "Autres informations" }],
        "name"           : [{"locale" : "fr", "text" : "Prénom" }],
        "surname"        : [{"locale" : "fr", "text" : "Nom" }],
        "tel"            : [{"locale" : "fr", "text" : "Téléphone" }],
        "period"         : [{"locale" : "fr", "text" : "Période" }],
        "services"       : [{"locale" : "fr", "text" : "Services proposés" }],
        "dowload_file"   : [{"locale" : "fr", "text" : "Télécharger le document" }],

        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"  : True
      },

      { "field"       : "app_screen_tabs",
        "app_version" : version,
        "help"        : u"The default homepage for your ApiViz instance",
        "tab_list"    : {
          "link_text"  : [ {"locale" : "fr", "text" : "liste" }],
        },
        "tab_map"    : {
          "link_text"  : [ {"locale" : "fr", "text" : "carte" }],
        },
        "tab_stat"    : {
          "link_text"  : [ {"locale" : "fr", "text" : "données" }],
        },
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"  : True
      },

    ### LOGO
      { "field"       : "app_logo",
        "content"     : u"apiviz default logo in navbar",
        "url"         : "https://raw.githubusercontent.com/co-demos/cis-data/master/logos/CIS/CIS_logo.png",
        "app_version" : version,
        "help"        : u"The official default logo for your ApiViz instance",
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"  : True
      },

    ### FAVICON
      { "field"       : "app_favicon",
        "content"     : u"apiviz default favicon in browser",
        "url"          : "/",
        "app_version" : version,
        "help"        : u"The default favicon for your ApiViz instance",
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"  : True
      },

    ### METAS
      { "field"       : "app_title",
        "app_version" : version,
        "help"        : u"Choose a title for your ApiViz instance",
        "content"     : u"CIS - ApiBêta",
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"  : True
      },

      { "field"       : "app_description",
        "app_version" : version,
        "help"        : u"Choose a description for your ApiViz instance",
        "content"     : [{ "locale" : "fr", "text" : ""}],
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"  : True
      },

      { "field"       : "app_keywords",
        "app_version" : version,
        "help"        : u"Choose a set of keywords for your ApiViz instance",
        "content"     : u"""dataviz,data visualisation,data visualization,SIG,commons,digital commons,API,opensource,open source,open data,opendata,MIT licence,github,sJS,javascript,python,flask,HTML,CSS,JSON,bulma,Vue.js,sEtalab,co-demos, codemos""",
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"  : True
      },

    ### GLOBAL CONTENTS / TEXTS
      { "field"       : "app_welcome",
        "app_version" : version,
        "help"        : u"Choose a welcoming phrase for your ApiViz instance",
        "content"     : [{ "locale" : "fr", "text" : "Bienvenue"}],
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"  : True
      },

      { "field"       : "app_pitch",
        "app_version" : version,
        "help"        : u"Choose a pitch/catchphrase for your ApiViz instance",
        "content"     : [{ "locale" : "fr", "text" : ""}],
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"  : True
      },

    ### REPO GITHUB
      { "field"       : "app_code",
        "url"         : "https://github.com/co-demos/ApiViz",
        "app_version" : version,
        "help"        : u"Choose the repo for the source code of your ApiViz instance",
        "content"     : [{ "locale" : "fr", "text" : "Code source"}],
        "in_navbar"   : False,
        "in_footer"   : True,
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"  : True,
      },

    ### SEO / INDEXING
      { "field"       : "app_indexing",
        "app_version" : version,
        "help"        : u"Choose a token for indexing your ApiViz instance",
        "content"     : u"",
        "activated"    : False,
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"  : True
      },

    ### ANALYTICS
      { "field"       : "app_analytics",
        "app_version" : version,
        "help"        : u"Choose the token for the analytics (ex. mix panel) of your ApiViz instance",
        "content"     : u"your_id_or_token",
        "url"         : "",
        "activated"    : False,
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"  : True
      },

    ### SUPPORT
      { "field"       : "app_support",
        "app_version" : version,
        "help"        : u"Choose the token for the support (ex. crisp) of your ApiViz instance",
        "content"     : u"your_id_or_token",
        "url"         : "",
        "activated"    : False,
        "apiviz_front_uuid" : "f0a482da-28be-4929-a443-f22ecb03ee68",
        "is_default"  : True
      },


]