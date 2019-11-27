# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_global_config = [

  ### - - - - - - - - - - - - - - - ###
  ### CONFIG TIERS LIEUX

    ### LANGUAGES
      { "field"       : "app_languages",
        "languages"   : ["fr", "en"],
        "is_multi_lang" : True,
        "locale"      : "fr",
        "app_version" : version,
        "help"        : u"The default homepage for your ApiViz instance",
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
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

        # "hello"          : [{"locale" : "en", "text" : "Hello"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Bonjour" }],

        # "home"           : [{"locale" : "en", "text" : "Welcome page"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Page d'accueil" }],
        # "documentation"  : [{"locale" : "en", "text" : "Documentation"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Documentation" }],
        # "preferences"    : [{"locale" : "en", "text" : "Preferences"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Préférences" }],
        # "backoffice"     : [{"locale" : "en", "text" : "Back office"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Back-office" }],
        # "back"           : [{"locale" : "en", "text" : "Back to the previous page"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Retourner à la page précédente" }],

        # "email"          : [{"locale" : "en", "text" : "email"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "email" }],
        # "login"          : [{"locale" : "en", "text" : "Login"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Login" }],
        # "connect"        : [{"locale" : "en", "text" : "Connect"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Se connecter" }],
        # "connected"      : [{"locale" : "en", "text" : "already connected"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "déjà connecté" }],
        # "reconnect"      : [{"locale" : "en", "text" : "Reconnect"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Se reconnecter" }],
        # "disconnect"     : [{"locale" : "en", "text" : "Disconnect"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Se déconnecter" }],
        # "disconnect_msg" : [{"locale" : "en", "text" : "successfully disconnected"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Vous avez été déconnecté.e avec succès" }],
        # "want_disconnect": [{"locale" : "en", "text" : "Do you want to disconnect"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Voulez-vous vous déconnecter ?" }],
        # "is_account"     : [{"locale" : "en", "text" : "You already have an account ?"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Vous avez déjà un compte ?" }],
        # "no_account"     : [{"locale" : "en", "text" : "You don't have an account yet ?"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Vous n'avez pas encore de compte ?" }],
        # "register"       : [{"locale" : "en", "text" : "Register"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "S'inscrire" }],
        # "is_registered"  : [{"locale" : "en", "text" : "You are already registred"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Vous êtes déjà inscrit.e" }],
        # "logout"         : [{"locale" : "en", "text" : "Logout"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Se déconnecter" }],
        # "password"       : [{"locale" : "en", "text" : "password"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "mot de passe" }],
        # "password_confirm" : [{"locale" : "en", "text" : "confirm the password"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "confirmer le mot de passe" }],
        # "password_bis"   : [{"locale" : "en", "text" : "rrepeat the password"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "répéter le mot de passe" }],
        # "remember_me"    : [{"locale" : "en", "text" : "remember me"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "se souvenir de moi" }],
        # "forgot_password": [{"locale" : "en", "text" : "Forgot your password ?"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Mot de passe oublié ?" }],
        # "create_account" : [{"locale" : "en", "text" : "Create an account"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Créer un compte" }],
        # "accept_cgu"     : [{"locale" : "en", "text" : "Accept CGU"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "J'accepte les CGU" }],

        # ### for back office
        # "menu_app_settings"   : [{"locale" : "en", "text" : "CONFIGURATION"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "CONFIGURATION" }],
        # "menu_preferences"    : [{"locale" : "en", "text" : "PREFERENCES"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "PREFERENCES" }],

        # # menus
        # "bo_global"          : [{"locale" : "en", "text" : "global"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "global" }],
        # "bo_navbar"          : [{"locale" : "en", "text" : "navigation"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "navigation" }],
        # "bo_routes"          : [{"locale" : "en", "text" : "routes"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "routes" }],
        # "bo_endpoints"       : [{"locale" : "en", "text" : "data"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "données" }],
        # "bo_tabs"            : [{"locale" : "en", "text" : "tabs"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "tabs" }],
        # "bo_footer"          : [{"locale" : "en", "text" : "footer"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "footer" }],
        # "bo_socials"         : [{"locale" : "en", "text" : "socials"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "réseaux sociaux" }],
        # "bo_styles"          : [{"locale" : "en", "text" : "styles"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "styles" }],
        # "bo_users"           : [{"locale" : "en", "text" : "users"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "utilisateurs" }],

        # # tabs
        # "gl_general"          : [{"locale" : "en", "text" : "general"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "général" }],
        # "gl_identity"         : [{"locale" : "en", "text" : "identity"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "identité du site" }],
        # "gl_meta"             : [{"locale" : "en", "text" : "meta"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "meta" }],
        # "gl_seo"              : [{"locale" : "en", "text" : "SEO"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "SEO" }],
        # "gl_lang"             : [{"locale" : "en", "text" : "international"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "international" }],
        # "na_global"           : [{"locale" : "en", "text" : "navbar"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "navbar" }],
        # "na_links"            : [{"locale" : "en", "text" : "navbar links"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "liens navbar" }],
        # "ro_data"             : [{"locale" : "en", "text" : "data routes"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "routes data" }],
        # "ro_statics"          : [{"locale" : "en", "text" : "pages routes"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "routes pages" }],
        # "ro_user"             : [{"locale" : "en", "text" : "user routes"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "routes utilisateur" }],
        # "ep_data_filters"     : [{"locale" : "en", "text" : "filters"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "filtres" }],
        # "ep_data"             : [{"locale" : "en", "text" : "data"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "données" }],
        # "ep_auth"             : [{"locale" : "en", "text" : "authentication"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "authentification" }],
        # "ep_user"             : [{"locale" : "en", "text" : "users"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "utilisateurs" }],
        # "ta_tabs"             : [{"locale" : "en", "text" : "tabs"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "tabs" }],
        # "fo_settings"         : [{"locale" : "en", "text" : "footer"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "footer" }],
        # "fo_links"            : [{"locale" : "en", "text" : "footer links"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "liens footer" }],
        # "so_settings"         : [{"locale" : "en", "text" : "socials"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "réseaux sociaux" }],
        # "st_colors"           : [{"locale" : "en", "text" : "colors"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "couleurs" }],
        # "st_typo"             : [{"locale" : "en", "text" : "typos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "typos" }],
        # "st_typocolors"       : [{"locale" : "en", "text" : "typo colors"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "couleurs typo" }],
        # "st_banners"          : [{"locale" : "en", "text" : "banners"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "bannières" }],
        # "st_images"           : [{"locale" : "en", "text" : "images"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "images" }],
        # "us_users"            : [{"locale" : "en", "text" : "users list"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "liste utilisateurs" }],
        # "us_teams"            : [{"locale" : "en", "text" : "teams list"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "liste équipes" }],
        
        # # preferences
        # "u_infos"             : [{"locale" : "en", "text" : "infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "infos" }],
        # "u_password"          : [{"locale" : "en", "text" : "security"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "sécurité" }],
        # "u_logout"            : [{"locale" : "en", "text" : "logout"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "logout" }],
        # "u_contact"           : [{"locale" : "en", "text" : "contact"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "contact" }],
        # "u_profile"           : [{"locale" : "en", "text" : "profile"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "profil" }],
        # "u_about"             : [{"locale" : "en", "text" : "message"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "message" }],
        # "u_about_more"        : [{"locale" : "en", "text" : "How can we help ?"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "comment pourrions-nous vous aider ?" }],
        # "u_infos_send"        : [{"locale" : "en", "text" : "update my infos"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "mettre à jour les informations" }],
        # "password_new"        : [{"locale" : "en", "text" : "your new password"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "votre nouveau mot de passe" }],
        # "password_send"       : [{"locale" : "en", "text" : "update my password"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "enregister le nouveau mot de passe" }],

        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
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
      #   "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
      #   "is_default"  : True
      # },

    ### LOGO
      { "field"       : "app_logo",
        "content"     : u"apiviz default logo in navbar",
        # "url"         : "http://localhost:8800/statics/logos/logo_TLF_carré_04.png",
        "url"           : "https://raw.githubusercontent.com/co-demos/apiviz-website-demo/master/logos/logo_apiviz_15_white.png",
        # "url"           : "https://raw.githubusercontent.com/co-demos/apiviz-website-demo/master/logos/logo_apiviz_15.png",
        "app_version" : version,
        "help"        : u"The official default logo for your ApiViz instance",
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
        "is_default"  : True
      },

    ### FAVICON
      { "field"       : "app_favicon",
        "content"     : u"apiviz default favicon in browser",
        # "url"         : "https://raw.githubusercontent.com/co-demos/apiviz-website-demo/master/logos/favicon/favicon.ico",
        "url"         : "https://raw.githubusercontent.com/co-demos/apiviz-website-demo/master/logos/logo_apiviz_icon_15.png",
        "app_version" : version,
        "help"        : u"The default favicon for your ApiViz instance",
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
        "is_default"  : True
      },

    ### METAS
      { "field"       : "app_title",
        "app_version" : version,
        "help"        : u"Choose a title for your ApiViz instance",

        "can_be_used_as_model" : True,
        # "image_preview" : "https://raw.githubusercontent.com/co-demos/apiviz-frontend/master/documentation/screenshots/list-view-apcis-01.png",
        "image_preview" : "https://raw.githubusercontent.com/co-demos/apiviz-website-demo/master/documentation/screenshots/map-view-tiers-lieux-01.png",

        "content"      : u"Apiviz - Solidata",
        "content_text" : [{"locale" : "en", "text" : "Apiviz - Solidata"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Apiviz - Solidata"}],
        "is_in_navbar" : False,
        # "title_color" : "primary",

        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
        "is_default"  : True
      },

      { "field"       : "app_description",
        "app_version" : version,
        "help"        : u"Choose a description for your ApiViz instance",
        "content"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : ""}],
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
        "is_default"  : True
      },

      { "field"       : "app_keywords",
        "app_version" : version,
        "help"        : u"Choose a set of keywords for your ApiViz instance",
        "content"     : u"""dataviz,data visualisation,data visualization,SIG,commons,digital commons,API,opensource,open source,open data,opendata,MIT licence,github,sJS,javascript,python,flask,HTML,CSS,JSON,bulma,Vue.js,sEtalab,co-demos, codemos""",
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
        "is_default"  : True
      },

    ### GLOBAL CONTENTS / TEXTS
      { "field"       : "app_welcome",
        "app_version" : version,
        "help"        : u"Choose a welcoming phrase for your ApiViz instance",
        "content"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Bienvenue"}],
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
        "is_default"  : True
      },

      { "field"       : "app_pitch",
        "app_version" : version,
        "help"        : u"Choose a pitch/catchphrase for your ApiViz instance",
        "content"     : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : ""}],
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
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
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
        "is_default"  : True,
      },

    ### SEO / INDEXING
      { "field"       : "app_indexing",
        "app_version" : version,
        "help"        : u"Choose a token for indexing your ApiViz instance",
        "content"     : u"",
        "activated"    : False,
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
        "is_default"  : True
      },

    ### ANALYTICS
      { "field"       : "app_analytics",
        "app_version" : version,
        "help"        : u"Choose the token for the analytics (ex. mix panel) of your ApiViz instance",
        "content"     : u"your_id_or_token",
        "url"         : "",
        "activated"    : False,
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
        "is_default"  : True
      },

    ### SUPPORT
      { "field"       : "app_support",
        "app_version" : version,
        "help"        : u"Choose the token for the support (ex. crisp) of your ApiViz instance",
        "content"     : u"your_id_or_token",
        "url"         : "",
        "activated"    : False,
        "apiviz_front_uuid" : uuid_models["uuid_demo_apiviz"],
        "is_default"  : True
      },


]