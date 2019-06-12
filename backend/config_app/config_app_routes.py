# -*- encoding: utf-8 -*-

from . import version, uuid_models

### ROUTES / PAGES

default_routes_config = [


  ### - - - - - - - - - - - - - - - - - - -  ### 
  ### CONFIG SONUM 
  ### - - - - - - - - - - - - - - - - - - -  ### 

    ### - - - - - - - - - - - - - - - - - ###
    ### PAGES : HOME --> NEED AT LEAST ONE ROUTE AS 'is_global_app_homepage = True' / TO BE ADDED VIA BACK OFFICE BY ADMIN USER
    ### - - - - - - - - - - - - - - - - - ###

      { "field"             : "app_home_fr",
        "is_global_app_homepage" : True,
        "route_title"       : u"Home",
        "route_description" : u"apiviz default home page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : True,
          "banner_uri" : "banner-sonum-carto"
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_left",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "en", "text" : "Search for a place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "en", "text" : "Search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : False,
        "link_in_logo"      : True,
        "urls"              : ["/test"],
        
        "template_urls"     : [
          { "locale" : "fr", "url" : "https://raw.githubusercontent.com/co-demos/carto-sonum/master/pages-html/test-apiviz.html" }, 
          { "locale" : "en", "url" : "https://raw.githubusercontent.com/co-demos/carto-sonum/master/pages-html/test-apiviz.html" }, 
        ],
        
        "has_ext_script"    : False,
        "ext_script_urls"   : "",
        
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main home route in french",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "sonum-tabs",
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"        : True
      },

      ### PAGE PROJECT
      { "field"             : "sonum_carto_project",
        "is_global_app_homepage" : True,
        "route_title"       : u"Home",
        "route_description" : u"apiviz default home page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "banner-sonum-carto"
        },
        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "en", "text" : "Search for a place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "en", "text" : "Search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : False,
        "link_in_logo"      : True,
        "urls"              : [ "/sonum-carto/projet"],
        
        "template_urls"     : [
          { "locale" : "fr", "url" : "https://raw.githubusercontent.com/co-demos/carto-sonum/master/pages-html/sonum-carto-projet.html" }, 
          { "locale" : "en", "url" : "https://raw.githubusercontent.com/co-demos/carto-sonum/master/pages-html/sonum-carto-projet.html" }, 
        ],
        
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main project route in french",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "sonum-tabs",
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"        : True
      },

    ### - - - - - - - - - - - - - - - - - ###
    ### PAGES : DATASETS --> TO BE ADDED VIA BACK OFFICE BY ADMIN USER
    ### - - - - - - - - - - - - - - - - - ###

      ### DATASETS CARTO SONUM

        ## PAGE - map
        { "field"             : "sonum_carto_carte",
          "is_global_app_homepage" : False,
          "route_title"       : u"Rechercher",
          "route_description" : u"Page de recherche carto LM d'Apiviz",
          "route_activated"   : True,
          "banner" : {
            "activated"  : False,
            "banner_uri" : "banner-sonum-carto"
          },
          "is_dataset_homepage" : True,

          "in_main_navbar"    : True,
          "navbar_btn_options" : {
            "only_in_navbar_for_this_dataset" : False,
            "position"   : "middle_right",
            "link_type"  : "link",
            "icon_class" : "",
            "link_text"  : [{"locale" : "en", "text" : "Search for a place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Recherher un lieu" }],
            "tooltip"    : [{"locale" : "en", "text" : "Search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Rechercher" }],
          },

          "in_footer"         : False,
          "urls"              : [ "/", "/sonum-carto/carte"],
          # "template_url"      : "/static/spa.html",
          "template_urls"     : [
          ],
          
          "help"              : u"you can specify a remote template (f.e. a github url)",
          "languages"         : ["fr"],
          "app_version"       : version,
          "comment"           : u"Main search route in french",
          "is_dynamic"        : True,
          "dataset_uri"       : "sonum-carto",
          "dynamic_template"  : 'DynamicMap',
          "endpoint_type"     : "map",

          "contents_fields"  : [

            { "field" : "sd_id",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_id",
              
              "locale" : "fr"
            },
            { "field" : "adresse structure",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_address",
              # "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "ville structure",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_city",
              # "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "intitulé structure",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_title",
              # "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_image",
              # "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "description structure",
              "field_format" : { "trim" : 150, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_abstract",
              
              "locale" : "fr"
            },
            { "field" : "source",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_src",
              
              "locale" : "fr"
            },
            # { "field" : "",
            #   "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            #   "is_visible" : True,
            #   "position" : "block_tags",
              
            #   "locale" : "fr"
            # },
            { "field" : "services",
              "field_format" : { "trim" : 30, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_tags",
              "filter_correspondance" : True,
              "is_tag_like" : True,
              "tags_separator" : "\r\n",
              "locale" : "fr"
            },
            
          ],

          "lat_long_fields" : {
            "latitude" : "lat",
            "longitude" : "lon"
          },

          "images_fields"        : {
            "card_img_main" : { "field" : "", "default" : "img_card",  "is_visible" : True  },
            "card_img_top"  : { "field" : "", "default" : None,        "is_visible" : False },
          },

          "ui_options"        : {
            "card_color"    : { "value" : None, "default" : "white", },
            "text_color"    : { "value" : None, "default" : "black", },
            "link_to_detail"   : { "is_visible" : True, "tooltip" : [{"locale" : "en", "text" : "See the document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le document" }] },
            "link_to_next"     : { "is_visible" : True, "tooltip" : [{"locale" : "en", "text" : "See the next document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir prochain document" }] },
            "link_to_previous" : { "is_visible" : True, "tooltip" : [{"locale" : "en", "text" : "See the previous document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le document précédent" }] },
          },

          "links_options"  : {

            "block_contents_links" : {
            "is_visible"  : False,
            "position"    : "block_bottom_1",
            "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
            "links"       : []
            },

            "block_data_infos" : {
            "is_visible"  : False,
            "position"    : "block_bottom_2",
            "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
            "links"       : []
            },

            "block_share" : {
            "is_visible"  : False,
            "position"    : "block_bottom_3",
            "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
            "links"       : []
            },

          },

          "has_navbar"        : True,
          "has_footer"        : True,
          "has_tabs"          : False,
          "tabs_uri"          : "sonum-tabs",
          "deactivate_btn"    : False,
          "is_visible"        : True,

          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"        : True
        },

        ## PAGE - list
        { "field"             : "sonum_carto_liste",
          "is_global_app_homepage" : False,
          "route_title"       : u"Rechercher",
          "route_description" : u"Page de recherche liste LM d'Apiviz",
          "route_activated"   : True,
          "banner" : {
            "activated"  : False,
            "banner_uri" : "banner-sonum-carto"
          },
          "is_dataset_homepage" : False,

          "in_main_navbar"    : False,
          "navbar_btn_options" : {
            "only_in_navbar_for_this_dataset" : True,
            "position"   : "middle_right",
            "link_type"  : "link",
            "icon_class" : "",
            "link_text"  : [{"locale" : "en", "text" : "Search a place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Recherher un lieu" }],
            "tooltip"    : [{"locale" : "en", "text" : "Search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Rechercher" }],
          },

          "in_footer"         : False,
          "urls"              : ["/sonum-carto/liste"],
          # "template_url"      : "/static/spa.html",
          "template_urls"     : [
          ],
          
          "help"              : u"you can specify a remote template (f.e. a github url)",
          "languages"         : ["fr"],
          "app_version"       : version,
          "comment"           : u"Main search route in french",
          "is_dynamic"        : True,
          "dataset_uri"       : "sonum-carto",
          "dynamic_template"  : 'DynamicList',
          "endpoint_type"     : "list",

          "contents_fields"  : [

            { "field" : "sd_id",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_id",
              
              "locale" : "fr"
            },
            { "field" : "adresse structure",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_address",
              # "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "ville structure",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_city",
              # "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "intitulé structure",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_title",
              # "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_image",
              # "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "description structure",
              "field_format" : { "trim" : 150, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_abstract",
              
              "locale" : "fr"
            },
            { "field" : "source",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_src",
              
              "locale" : "fr"
            },
            { "field" : "",
              "field_format" : { "trim" : 20, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_tags",
              "filter_correspondance" : True,
              "is_tag_like" : True,
              "tags_separator" : "\r\n",
              "locale" : "fr"
            },

          ],

          "images_fields"        : {
            "card_img_main" : { "field" : "", "default" : "img_card",  "is_visible" : True  },
            "card_img_top"  : { "field" : "", "default" : None,        "is_visible" : False },
          },
          "ui_options" : {
            "card_color"    : { "value" : None, "default" : "white", },
            "text_color"    : { "value" : None, "default" : "black", },
            "link_to_detail"   : { "is_visible" : True, "tooltip" : [{"locale" : "en", "text" : "see the document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le document" }] },
            "link_to_next"     : { "is_visible" : True, "tooltip" : [{"locale" : "en", "text" : "see the next document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir prochain document" }] },
            "link_to_previous" : { "is_visible" : True, "tooltip" : [{"locale" : "en", "text" : "see the previous document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le document précédent" }] },
          },

          "links_options"  : {

            "block_contents_links" : {
            "is_visible"  : False,
            "position"    : "block_bottom_1",
            "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
            "links"       : []
            },

            "block_data_infos" : {
            "is_visible"  : False,
            "position"    : "block_bottom_2",
            "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
            "links"       : []
            },

            "block_share" : {
            "is_visible"  : False,
            "position"    : "block_bottom_3",
            "title_block" : [{"locale" : "en", "text" : "share this place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Partagez ce lieu", "is_visible" : False}],
            "links"       : []
            },

          },

          "has_navbar"        : True,
          "has_footer"        : True,
          "has_tabs"          : False,
          "tabs_uri"          : "sonum-tabs",
          "deactivate_btn"    : False,
          "is_visible"        : True,
          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"        : True
        },

        ## PAGE - detail
        { "field"             : "sonum_carto_detail",
          "is_global_app_homepage" : False,
          "route_title"        : u"Rechercher",
          "route_description"  : u"Page de recherche détails LM d'Apiviz",
          "route_activated"    : True,
          "banner" : {
            "activated"  : False,
            "banner_uri" : "banner-sonum-carto"
          },
          "is_dataset_homepage" : False,

          "in_main_navbar"    : False,
          "navbar_btn_options" : {
            "only_in_navbar_for_this_dataset" : True,
            "position"   : "middle_right",
            "link_type"  : "link",
            "icon_class" : "",
            "link_text"  : [{"locale" : "en", "text" : "Search for a place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Recherher un lieu" }],
            "tooltip"    : [{"locale" : "en", "text" : "Search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Rechercher" }],
          },

          "in_footer"         : False,
          "urls"              : ["/sonum-carto/detail"],
          # "template_url"      : "/static/spa.html",
          "template_urls"     : [
          ],
          
          "help"              : u"you can specify a remote template (f.e. a github url)",
          "languages"         : ["fr"],
          "app_version"       : version,
          "comment"           : u"Main search route in french",
          "is_dynamic"        : True,
          "dataset_uri"       : "sonum-carto",
          "dynamic_template"  : 'DynamicDetail',
          "endpoint_type"     : "detail",

          "contents_fields"  : [

            { "field" : "intitulé structure",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_title",
              
              "locale" : "fr"
            },
            { "field" : "adresse structure",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_address",
              
              "locale" : "fr"
            },
          { "field" : "code postal structure",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_cp",
              
              "locale" : "fr"
            },
            { "field" : "description structure",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_abstract",
              
              "locale" : "fr"
            },
            { "field" : "source",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : False,
              "position" : "block_src",
              
              "locale" : "fr"
            },
            { "field" : "services",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_tags",
              "filter_correspondance" : True,
              "is_tag_like" : True,
              "tags_separator" : "\r\n",
              "locale" : "fr"
            },
            { "field" : "website structure",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_wesite",
              
              "locale" : "fr"
            },
            { "field" : "contact",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_contact",
              
              "locale" : "fr"
            },
            { "field" : "téléphone",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_tel",
              
              "locale" : "fr"
            },
            { "field" : "horaires structure",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_open_infos",
              
              "locale" : "fr"
            },
            { "field" : "services",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_services",
              "title_block" : [{"locale" : "en", "text" : "Services"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Services proposés", "is_visible" : False }],
            },
            { "field" : "infos pratiques",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_infos_pract",
              "title_block" : [{"locale" : "en", "text" : "Informations"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Informations pratiques", "is_visible" : False }],
            },

          ],

          "images_fields"     : {
            "card_img_main"  : { "field" : "", "default" : "img_card",  "is_visible" : True,  "position" : "block_right_top_1" },
            "card_img_top"   : { "field" : "", "default" : None,        "is_visible" : False, "position" : "block_right_middle" },
          },

          "ui_options"        : {
            "card_color"     : { "value" : None, "default" : "white", },
            "text_color"     : { "value" : None, "default" : "black", },
            "link_to_detail"   : { "is_visible" : False, "tooltip" : [{"locale" : "en", "text" : "see the document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le document" }] },
            "link_to_next"     : { "is_visible" : True,  "tooltip" : [{"locale" : "en", "text" : "see the next document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le prochain document" }] },
            "link_to_previous" : { "is_visible" : True,  "tooltip" : [{"locale" : "en", "text" : "see the previous document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le document précédent" }] },
          },

          "links_options"  : {

            "block_contents_links" : {
            "is_visible"  : True,
            "position"    : "block_left_middle_2",
            "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
            "links"       : [
              { "field" : "website",
                "is_visible" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "website" }],
                "tooltip"    : [{"locale" : "en", "text" : "check the website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le site" }]
              },
              { "field" : "contact",
                "is_visible" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "contact"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "contact" }],
                "tooltip"    : [{"locale" : "en", "text" : "contact the structure"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "contacter la structure" }]
              },
            ]
            },

            "block_share" : {
            "is_visible"  : True,
            "position"    : "block_left_bottom_2",
            "title_block" : [{"locale" : "en", "text" : "Share this place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Partagez ce lieu", "is_visible" : True}],
            "links"       : [
              {
                "is_visible" : True,
                "link_type"  : "icon",
                "icon_class" : "fas fa-link",
                "link_text"  : [{"locale" : "en", "text" : "link"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "lien" }],
                "tooltip"    : [{"locale" : "en", "text" : "share this page"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "partager cette page (copier le lien)" }]
              },
              {
                "is_visible" : True,
                "link_type"  : "icon",
                "icon_class" : "fab fa-facebook-f",
                "link_text"  : [{"locale" : "en", "text" : "facebook"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "facebook" }],
                "tooltip"    : [{"locale" : "en", "text" : "share on facebook"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "partager sur facebook" }]
              },
              {
                "is_visible" : True,
                "link_type"  : "icon",
                "icon_class" : "fab fa-twitter",
                "link_text"  : [{"locale" : "en", "text" : "twitter"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "twitter" }],
                "tooltip"    : [{"locale" : "en", "text" : "share on twitter"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "partager sur twitter" }]
              },
            ]
            },

          },

          "has_navbar"        : True,
          "has_footer"        : True,
          "has_tabs"          : False,
          "tabs_uri"          : "sonum-tabs",
          "deactivate_btn"    : False,
          "is_visible"        : True,
          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"        : True
        },

      ### DATASETS XP SONUM
        ## PAGE - map
        { "field"             : "sonum_xp_carte",
          "is_global_app_homepage" : False,
          "route_title"        : u"Rechercher",
          "route_description"  : u"Page de recherche carto XP d'Apiviz",
          "route_activated"    : True,
          "banner" : {
            "activated"  : False,
            "banner_uri" : "banner-sonum-xp"
          },
          "is_dataset_homepage" : False,

          "in_main_navbar"    : False,
          "navbar_btn_options" : {
            "only_in_navbar_for_this_dataset" : True,
            "position"   : "middle_right",
            "link_type"  : "link",
            "icon_class" : "",
            "link_text"  : [{"locale" : "en", "text" : "Search an experience"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Recherher une expérience" }],
            "tooltip"    : [{"locale" : "en", "text" : "Search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Rechercher" }],
          },

          "in_footer"         : False,
          "urls"              : ["/sonum-xp/carte"],
          # "template_url"      : "/static/spa.html",
          "template_urls"     : [
          ],
          
          "help"              : u"you can specify a remote template (f.e. a github url)",
          "languages"         : ["fr"],
          "app_version"       : version,
          "comment"           : u"Main search route in french",
          "is_dynamic"        : True,
          "dataset_uri"       : "sonum-xp",
          "dynamic_template"  : 'DynamicMap',
          "endpoint_type"     : "map",

          "contents_fields"  : [

            { "field" : "sd_id",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_id",
              
              "locale" : "fr"
            },
            { "field" : "titre initiative",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_title",
              
              "locale" : "fr"
            },
            { "field" : "adresse structure",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_address",
              # "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "city",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_city",
              # "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "présentation initiative",
              "field_format" : { "trim" : 150, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_abstract",
              
              "locale" : "fr"
            },
            { "field" : "type structure",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_tags",
              "filter_correspondance" : True,
              "is_tag_like" : True,
              "tags_separator" : "\r\n",
              "locale" : "fr"
            },
          ],

          "images_fields"        : {
            "card_img_main" : { "field" : "", "default" : "img_card",  "is_visible" : True  },
            "card_img_top"  : { "field" : "", "default" : None,        "is_visible" : False },
          },

          "ui_options"        : {
            "card_color"    : { "value" : None, "default" : "white", },
            "text_color"    : { "value" : None, "default" : "black", },
            "link_to_detail"   : { "is_visible" : True, "tooltip" : [{"locale" : "en", "text" : "see the document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le document" }] },
            "link_to_next"     : { "is_visible" : True, "tooltip" : [{"locale" : "en", "text" : "see the next document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le prochain document" }] },
            "link_to_previous" : { "is_visible" : True, "tooltip" : [{"locale" : "en", "text" : "see the previous document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le document précédent" }] },
          },

          "links_options"  : {

            "block_contents_links" : {
            "is_visible"  : False,
            "position"    : "block_bottom_1",
            "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
            "links"       : []
            },

            "block_data_infos" : {
            "is_visible"  : False,
            "position"    : "block_bottom_2",
            "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
            "links"       : []
            },

            "block_share" : {
            "is_visible"  : False,
            "position"    : "block_bottom_3",
            "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
            "links"       : []
            },

          },

          "has_navbar"        : True,
          "has_footer"        : True,
          "has_tabs"          : False,
          "tabs_uri"          : "sonum-tabs",
          "deactivate_btn"    : False,
          "is_visible"        : True,
          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"        : True
        },
        ## PAGE - list
        { "field"             : "sonum_xp_liste",
          "is_global_app_homepage" : False,
          "route_title"        : u"Rechercher",
          "route_description"  : u"Page de recherche liste XP d'Apiviz",
          "route_activated"    : True,
          "banner" : {
            "activated"  : True,
            "banner_uri" : "banner-sonum-xp"
          },
          "is_dataset_homepage" : True,

          "in_main_navbar"    : True,
          "navbar_btn_options" : {
            "only_in_navbar_for_this_dataset" : False,
            "position"   : "middle_right",
            "link_type"  : "link",
            "icon_class" : "",
            "link_text"  : [{"locale" : "en", "text" : "Search for an experience"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Recherher une expérience" }],
            "tooltip"    : [{"locale" : "en", "text" : "Search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Rechercher" }],
          },

          "in_footer"         : False,
          "urls"              : ["/sonum-xp/liste"],
          # "template_url"      : "/static/spa.html",
          "template_urls"     : [
          ],
          
          "help"              : u"you can specify a remote template (f.e. a github url)",
          "languages"         : ["fr"],
          "app_version"       : version,
          "comment"           : u"Main search route in french",
          "is_dynamic"        : True,
          "dataset_uri"       : "sonum-xp",
          "dynamic_template"  : 'DynamicList',
          "endpoint_type"     : "list",


          "contents_fields"  : [

            { "field" : "sd_id",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_id",
              
              "locale" : "fr"
            },
            { "field" : "titre initiative",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_title",
              
              "locale" : "fr"
            },
            { "field" : "adresse structure",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_address",
              # "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "city",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_city",
              # "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "présentation initiative",
              "field_format" : { "trim" : 150, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_abstract",
              
              "locale" : "fr"
            },
            { "field" : "type structure",
              "field_format" : { "trim" : 25, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_tags",
              "filter_correspondance" : True,
              "is_tag_like" : True,
              "tags_separator" : "-",
              "locale" : "fr"
            },
          ],

          "images_fields"        : {
            "card_img_main" : { "field" : "illustration initiative", "default" : "img_card",  "is_visible" : True  },
            "card_img_top"  : { "field" : "", "default" : None,        "is_visible" : False },
          },
          "ui_options" : {
            "card_color"    : { "value" : None, "default" : "white", },
            "text_color"    : { "value" : None, "default" : "black", },
            "link_to_detail"   : { "is_visible" : True, "tooltip" : [{"locale" : "en", "text" : "see the document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le document" }] },
            "link_to_next"     : { "is_visible" : True, "tooltip" : [{"locale" : "en", "text" : "see the next document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le prochain document" }] },
            "link_to_previous" : { "is_visible" : True, "tooltip" : [{"locale" : "en", "text" : "see the previous document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le document précédent" }] },
          },

          "links_options"  : {

            "block_contents_links" : {
            "is_visible"  : False,
            "position"    : "block_bottom_1",
            "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
            "links"       : []
            },

            "block_data_infos" : {
            "is_visible"  : False,
            "position"    : "block_bottom_2",
            "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
            "links"       : []
            },

            "block_share" : {
            "is_visible"  : False,
            "position"    : "block_bottom_3",
            "title_block" : [{"locale" : "en", "text" : "share this place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Partagez ce lieu", "is_visible" : False}],
            "links"       : []
            },

          },

          "has_navbar"        : True,
          "has_footer"        : True,
          "has_tabs"          : False,
          "tabs_uri"          : "sonum-tabs",
          "deactivate_btn"    : False,
          "is_visible"        : True,
          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"        : True
        },
        ## PAGE - detail
        { "field"               : "sonum_xp_detail",
          "is_global_app_homepage" : False,
          "route_title"         : u"Rechercher",
          "route_description"   : u"Page de recherche details XP d'Apiviz",
          "route_activated"     : True,
          "is_dataset_homepage" : False,
          "banner" : {
            "activated"  : False,
            "banner_uri" : "banner-sonum-xp"
          },

          "in_main_navbar"    : False,
          "navbar_btn_options" : {
            "only_in_navbar_for_this_dataset" : True,
            "position"   : "middle_right",
            "link_type"  : "link",
            "icon_class" : "",
            "link_text"  : [{"locale" : "en", "text" : "Search for an experience"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Recherher une expérience" }],
            "tooltip"    : [{"locale" : "en", "text" : "Search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Rechercher" }],
          },

          "in_footer"         : False,
          "urls"              : ["/sonum-xp/detail"],
          # "template_url"      : "/static/spa.html",
          "template_urls"     : [
          ],
          
          "help"              : u"you can specify a remote template (f.e. a github url)",
          "languages"         : ["fr"],
          "app_version"       : version,
          "comment"           : u"Main search route in french",
          "is_dynamic"        : True,
          "dataset_uri"       : "sonum-xp",
          "dynamic_template"  : 'DynamicDetail',
          "endpoint_type"     : "detail",

          "contents_fields"  : [

            { "field" : "titre initiative",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_title",
              
              "locale" : "fr"
            },
            { "field" : "public visé",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_main_tags",
              "custom_title" : "Publics visés :",
              "is_tag_like" : True,
              "tags_separator" : "-",
              # "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "échelle action initiative",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_scale_tags",
              "custom_title" : "Echelle :",
              "is_tag_like" : True,
              "tags_separator" : "-",
              # "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "nom structure porteuse",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_scale_2",
              "custom_title" : "Structure :",
              # "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "adresse structure",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_scale_address",
              # "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "city",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_city",
              # "trim" : 20,
              "locale" : "fr"
            },
            { "field" : "présentation structure",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_pre_abstract",
              "custom_title" : "Présentation de la structure",
              
              "locale" : "fr"
            },
            { "field" : "présentation initiative",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_abstract",
              "custom_title" : "Présentation de l'initiative",
              
              "locale" : "fr"
            },
            { "field" : "type structure",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_tags",
              "filter_correspondance" : True,
              "is_tag_like" : True,
              "tags_separator" : "-",
              "locale" : "fr"
            },
            { "field" : "date action initiative - début",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_period",
              
              "locale" : "fr"
            },
            { "field" : "contact - nom",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_contact_surname",
              
              "locale" : "fr"
            },
            { "field" : "contact - prénom",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_contact_name",
              
              "locale" : "fr"
            },
            { "field" : "contact - titre",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_contact_title",
              
              "locale" : "fr"
            },
            { "field" : "contact - email",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_contact_email",
              
              "locale" : "fr"
            },
            { "field" : "contact - téléphone",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_contact_tel",
              
              "locale" : "fr"
            },
            { "field" : "lien document présentation",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_file_1",
              
              "locale" : "fr"
            },
            { "field" : "website - initiative",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_wesite",
              
              "locale" : "fr"
            },
            { "field" : "retour d'expérience",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_right_bottom_1",
              
              "custom_title" : "Retour d'expérience",
              "locale" : "fr"
            },
            { "field" : "partenaires initiative",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_post_abstract_1",
              
              "custom_title" : "Partenaires de l'initiative",
              "locale" : "fr"
            },
            { "field" : "moyens humains initiative",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_post_abstract_2",
              
              "custom_title" : "Moyens",
              "locale" : "fr"
            },
            { "field" : "mesure d'impact",
              "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
              "is_visible" : True,
              "position" : "block_right_bottom_2",
              
              "custom_title" : "Mesure d'impact",
              "locale" : "fr"
            },
          ],

          "images_fields"     : {
            "card_img_main"  : { "field" : "", "default" : "img_card",  "is_visible" : True,  "position" : "block_right_top_1" },
            "card_img_top"   : { "field" : "", "default" : None,        "is_visible" : False, "position" : "block_right_middle" },
          },
          "ui_options"        : {
            "card_color"     : { "value" : None, "default" : "white", },
            "text_color"     : { "value" : None, "default" : "black", },
            "link_to_detail"   : { "is_visible" : False, "tooltip" : [{"locale" : "en", "text" : "see the document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le document" }] },
            "link_to_next"     : { "is_visible" : True,  "tooltip" : [{"locale" : "en", "text" : "see the next document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le prochain document" }] },
            "link_to_previous" : { "is_visible" : True,  "tooltip" : [{"locale" : "en", "text" : "see the previous document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le document précédent" }] },
          },

          "links_options"  : {

            "block_contents_links" : {
            "is_visible"  : True,
            "position"    : "block_left_middle_2",
            "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
            "links"       : [
              { "field" : "website",
                "is_visible" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "website" }],
                "tooltip"    : [{"locale" : "en", "text" : "check the website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le site" }]
              },
              { "field" : "contact",
                "is_visible" : True,
                "link_type"  : "text",
                "icon_class" : "",
                "link_text"  : [{"locale" : "en", "text" : "contact"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "contact" }],
                "tooltip"    : [{"locale" : "en", "text" : "contact the structure"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "contacter la structure" }]
              },
            ]
            },

            "block_share" : {
            "is_visible"  : True,
            "position"    : "block_left_bottom_2",
            "title_block" : [{"locale" : "en", "text" : "share this place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Partagez ce lieu", "is_visible" : True}],
            "links"       : [
                {
                  "is_visible" : True,
                  "link_type"  : "icon",
                  "icon_class" : "fas fa-link",
                  "link_text"  : [{"locale" : "en", "text" : "link"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "lien" }],
                  "tooltip"    : [{"locale" : "en", "text" : "share this page"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "partager cette page (copier le lien)" }]
                },
                {
                  "is_visible" : True,
                  "link_type"  : "icon",
                  "icon_class" : "fab fa-facebook-f",
                  "link_text"  : [{"locale" : "en", "text" : "facebook"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "facebook" }],
                  "tooltip"    : [{"locale" : "en", "text" : "share on facebook"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "partager sur facebook" }]
                },
                {
                  "is_visible" : True,
                  "link_type"  : "icon",
                  "icon_class" : "fab fa-twitter",
                  "link_text"  : [{"locale" : "en", "text" : "twitter"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "twitter" }],
                  "tooltip"    : [{"locale" : "en", "text" : "share on twitter"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "partager sur twitter" }]
                },
              ]
            },

          },

          "has_navbar"        : True,
          "has_footer"        : True,
          "has_tabs"          : False,
          "tabs_uri"          : "sonum-tabs",
          "deactivate_btn"    : False,
          "is_visible"        : True,
          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"        : True
        },

        ### PAGE HOME XP
        { "field"             : "sonum_xp_home",
          "is_global_app_homepage" : True,
          "route_title"       : u"Accueil XP",
          "route_description" : u"XP sonum default home page",
          "route_activated"   : True,
          "banner" : {
            "activated"  : False,
            "banner_uri" : "banner-sonum-xp"
          },
          "in_main_navbar"    : False,
          "navbar_btn_options" : {
            "position"   : "middle_right",
            "link_type"  : "link",
            "icon_class" : "",
            "link_text"  : [{"locale" : "en", "text" : "Search for a place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Recherher un lieu" }],
            "tooltip"    : [{"locale" : "en", "text" : "Search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Rechercher" }],
          },

          "in_footer"         : False,
          "link_in_logo"      : True,
          "urls"              : ["/sonum-xp/accueil"],
          
          "template_urls"     : [
            { "locale" : "fr", "url" : "https://raw.githubusercontent.com/co-demos/xp-sonum/master/pages-html/accueil-clean.html" },
            { "locale" : "en", "url" : "https://raw.githubusercontent.com/co-demos/xp-sonum/master/pages-html/accueil-clean.html" },
          ],
          
          "help"              : u"you can specify a remote template (f.e. a github url)",
          "languages"         : ["fr"],
          "app_version"       : version,
          "comment"           : u"Main project route in french",
          "is_dynamic"        : True,
          "dynamic_template"  : "DynamicStatic",
          "has_navbar"        : True,
          "has_footer"        : True,
          "has_tabs"          : False,
          "tabs_uri"          : "sonum-tabs",
          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"        : True
        },
        ### PAGE STRATEGIE
        { "field"             : "sonum_xp_strategie",
          "is_global_app_homepage" : True,
          "route_title"       : u"Stratégie XP",
          "route_description" : u"apiviz stratégie XP page",
          "route_activated"   : True,
          "banner" : {
            "activated"  : False,
            "banner_uri" : "banner-sonum-xp"
          },
          "in_main_navbar"    : False,
          "navbar_btn_options" : {
            "position"   : "middle_right",
            "link_type"  : "link",
            "icon_class" : "",
            "link_text"  : [{"locale" : "en", "text" : "Search for a place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Recherher un lieu" }],
            "tooltip"    : [{"locale" : "en", "text" : "Search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Rechercher" }],
          },

          "in_footer"         : False,
          "link_in_logo"      : True,
          "urls"              : ["/sonum-xp/strategie"],
          
          "template_urls"     : [
            { "locale" : "fr", "url" : "https://raw.githubusercontent.com/co-demos/xp-sonum/master/pages-html/strategie-clean.html" },
            { "locale" : "en", "url" : "https://raw.githubusercontent.com/co-demos/xp-sonum/master/pages-html/strategie-clean.html" },
          ],
          # "template_url"      : "https://raw.githubusercontent.com/CBalsier/test-content/master/pages-html/le-collectif.html",
          
          "help"              : u"you can specify a remote template (f.e. a github url)",
          "languages"         : ["fr"],
          "app_version"       : version,
          "comment"           : u"Main project route in french",
          "is_dynamic"        : True,
          "dynamic_template"  : "DynamicStatic",
          "has_navbar"        : True,
          "has_footer"        : True,
          "has_tabs"          : False,
          "tabs_uri"          : "sonum-tabs",
          "apiviz_front_uuid" : uuid_models["uuid_sonum"],
          "is_default"        : True
        },

    ### - - - - - - - - - - - - - - - - - ###
    ### CUSTOM ROUTES-PAGES --> TO BE ADDED VIA BACK OFFICE BY ADMIN USER
    ### - - - - - - - - - - - - - - - - - ###

      ### PAGE : QUI SOMMES-NOUS
      { "field"             : "app_who_fr",
        "is_global_app_homepage" : False,
        "route_title"        : u"Home",
        "route_description"  : u"Qui sommes-nous",
        "route_activated"    : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "default"
        },
        "is_dataset_homepage" : False,

        "in_main_navbar"    : True,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "button",
          "icon_class" : "",
          "link_text"  : [{"locale" : "en", "text" : "Search for a place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "en", "text" : "Search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/qui-sommes-nous"],
        
        "template_urls"     : [
          { "locale" : "fr", "url" : "https://github.com/co-demos/carto-sonum/blob/master/pages-html/qui-sommes-nous.html?raw=true" },
          { "locale" : "en", "url" : "https://github.com/co-demos/carto-sonum/blob/master/pages-html/qui-sommes-nous.html?raw=true" },
        ],
        
        "has_ext_script"    : False,
        "ext_script_urls"   : "",
        
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"A custom page for your ApiViz app",
        "is_dynamic"        : True,
        "dynamic_template"  : 'DynamicStatic',
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "cis-tabs",
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"        : True
      },

      ### PAGES : TOOLS
      { "field"              : "app_outils",
        "is_global_app_homepage" : False,
        "route_title"        : u"Outils",
        "route_description"  : u"Nos outils",
        "route_activated"    : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "default"
        },
        "is_dataset_homepage" : False,

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "button",
          "icon_class" : "",
          "link_text"  : [{"locale" : "en", "text" : "Search for a place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "en", "text" : "Search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : True,
        "urls"              : ["/nos-outils"],
        # "template_url"      : "/static/les-outils.html",
        "template_urls"     : [
          { "locale" : "fr", "url" : "" },
          { "locale" : "en", "url" : "" },
        ],
        
        "has_ext_script"    : False,
        "ext_script_urls"   : "",
        
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main tools route in french",
        "is_dynamic"        : False,
        "dynamic_template"  : None,
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "cis-tabs",
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"        : True
      },

      ### PAGE TOOLS - FR
      { "field"             : "app_tools",
        "is_global_app_homepage" : True,
        "route_title"       : u"Outils",
        "route_description" : u"apiviz default tools page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },
        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "" }],
          "tooltip"    : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "" }],
        },

        "in_footer"         : True,
        "link_in_logo"      : False,
        "urls"              : ["/apiviz/outils"],
        
        "template_urls"     : [
          { "locale" : "fr", "url" : "https://raw.githubusercontent.com/co-demos/structure/master/pages-html/tools-fr.html" },
          { "locale" : "en", "url" : "https://raw.githubusercontent.com/co-demos/structure/master/pages-html/tools-fr.html" },
        ],
        
        "has_ext_script"    : False,
        "ext_script_urls"   : "",
        
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main apiviz tools route in french",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "cis-tabs",
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"        : True
      },
      ### ...

    ### - - - - - - - - - - - - - - - - - ###
    ### CUSTOM ROUTES-LOGIN 
    ### - - - - - - - - - - - - - - - - - ###

      { "field"             : "app_login",
        "is_global_app_homepage" : False,
        "route_title"       : u"Login",
        "route_description" : u"apiviz default login page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/login"],
        
        "template_urls"     : [
        ],
        
        "help"              : u"default login page for Apiviz",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main login route ",
        "is_dynamic"        : True,
        "dynamic_template"  : "Login",
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "cis-tabs",
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"        : True
      },

      { "field"             : "app_register",
        "is_global_app_homepage" : False,
        "route_title"       : u"Register",
        "route_description" : u"apiviz default register page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/register"],
        
        "template_urls"     : [
        ],
        
        "help"              : u"default register page for Apiviz",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main register route ",
        "is_dynamic"        : True,
        "dynamic_template"  : "Register",
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "cis-tabs",
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"        : True
      },

      { "field"             : "app_logout",
        "is_global_app_homepage" : False,
        "route_title"       : u"logout",
        "route_description" : u"apiviz default logout page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/logout"],
        
        "template_urls"     : [
        ],
        
        "help"              : u"default logout page for Apiviz",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main logout route ",
        "is_dynamic"        : True,
        "dynamic_template"  : "Logout",
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "cis-tabs",
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"        : True
      },

      { "field"             : "app_backoffice",
        "is_global_app_homepage" : False,
        "route_title"       : u"backoffice",
        "route_description" : u"apiviz default backoffice page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/backoffice"],
        
        "template_urls"     : [
        ],
        
        "help"              : u"default backoffice page for Apiviz",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main backoffice route ",
        "is_dynamic"        : True,
        "dynamic_template"  : "BackOffice",
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "cis-tabs",
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"        : True
      },

      { "field"             : "app_preferences",
        "is_global_app_homepage" : False,
        "route_title"       : u"preferences",
        "route_description" : u"apiviz default user preferences page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/preferences"],
        
        "template_urls"     : [
        ],
        
        "help"              : u"default preferences page for Apiviz",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main user preferences route",
        "is_dynamic"        : True,
        "dynamic_template"  : "Preferences",
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "cis-tabs",
        "apiviz_front_uuid" : uuid_models["uuid_sonum"],
        "is_default"        : True
      },



  ### - - - - - - - - - - - - - - - - - - -  ### 
  ### CONFIG CIS 
  ### - - - - - - - - - - - - - - - - - - -  ###

    ### - - - - - - - - - - - - - - - - - ###
    ### PAGES : HOME --> NEED AT LEAST ONE ROUTE AS 'is_global_app_homepage = True' / TO BE ADDED VIA BACK OFFICE BY ADMIN USER
    ### - - - - - - - - - - - - - - - - - ###

      { "field"             : "app_home_fr",
        "is_global_app_homepage" : True,
        "route_title"       : u"Home",
        "route_description" : u"apiviz default home page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "banner-cis-carto"
        },
        "tabs" : {
          "activated" : False,
        },
        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_left",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "en", "text" : "Search for a place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "en", "text" : "Search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : False,
        "link_in_logo"      : True,
        "urls"              : ["/"],

        # "template_url"      : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/home.html",
        # "template_url"      : "http://localhost:8800/html/pages-html/home.html",
        "template_urls"     : [
          {"locale" : "fr", "url" : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/home.html" },
          {"locale" : "en", "url" : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/home-en.html" },
          # { "locale" : "fr", "url" : "http://localhost:8800/html/pages-html/home.html" },
          # { "locale" : "en", "url" : "http://localhost:8800/html/pages-html/home-en.html" }
        ],
        

        "has_ext_script"    : True,
        "ext_script_urls"   : [
          {"script_id" : "js-car" , "at_mount" : True,  "type" : None,              "url" : "https://cdn.jsdelivr.net/npm/bulma-carousel@4.0.4/dist/js/bulma-carousel.min.js"},

          {"script_id" : "js-home", "at_mount" : False, "type" : "text/javascript", "url" : "http://localhost:8800/statics/scripts/home.js?v7"},
          # {"script_id" : "js-home" , "at_mount" : False, "type" : "text/javascript", "url" : "https://cdn.jsdelivr.net/gh/co-demos/cis-data/scripts/home.js"}
        ],

        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main home route in french",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "",
        "dataset_uri"       : "recherche",
        "apiviz_front_uuid" : uuid_models["uuid_apcis"],
        "is_default"        : True
      },

    ### - - - - - - - - - - - - - - - - - ###
    ### PAGES : DATASETS --> TO BE ADDED VIA BACK OFFICE BY ADMIN USER
    ### - - - - - - - - - - - - - - - - - ###

      ### PAGE - map
      { "field"             : "cis_carte",
        "is_global_app_homepage" : False,
        "route_title"       : u"Rechercher",
        "route_description" : u"Page de recherche d'Apiviz",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "banner-sonum-carto" # TODO
        },
        "is_dataset_homepage" : True,

        "in_main_navbar"    : True,
        "navbar_btn_options" : {
          "only_in_navbar_for_this_dataset" : False,
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "en", "text" : "Search for a place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "en", "text" : "Search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : False,
        "urls"              : ["/recherche/carte"],
        
        "template_urls"     : [
        ],
        
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main search route in french",
        "is_dynamic"        : True,
        "dataset_uri"       : "recherche",
        "dynamic_template"  : 'DynamicMap',
        "endpoint_type"     : "map",

        "contents_fields"  : [

          { "field" : "sd_id",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_id",
            
            "custom_title" : "to do",
            "locale" : "fr"
          },
          # { "field" : "adresse structure", # SONUM
          { "field" : "adresse du projet", # CIS
            "field_format" : { "trim" : None, "type" : "list", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_address",
            # "trim" : 20,
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "ville structure",
            "field_format" : { "trim" : None, "type" : "list", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_city",
            # "trim" : 20,
            "custom_title" : "to do",
            "locale" : "fr"
          },
          # { "field" : "intitulé structure", # SONUM
          { "field" : "titre du projet", # CIS
            "field_format" : { "trim" : None, "type" : "list", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_title",
            # "trim" : 20,
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "image(s) du projet",
            "field_format" : { "trim" : None, "type" : "list", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_image",
            # "trim" : 20,
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "résumé du projet",
            "field_format" : { "trim" : None, "type" : "list", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_abstract",
            
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "link_src", # spider/sourceur
            "field_format" : { "trim" : None, "type" : "list", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_src",
            
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "",
            "field_format" : { "trim" : None, "type" : "list", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_tags",
            "filter_correspondance" : True,
            "is_tag_like" : True,
            "tags_separator" : "\r\n",
            "custom_title" : "to do",
            "locale" : "fr"
          },

        ],

        "lat_long_fields" : {
          "latitude" : "lat",
          "longitude" : "lon"
        },

        "images_fields"        : {
          "card_img_main" : { "field" : "image(s) du projet", "default" : "img_card",  "is_visible" : True  },
          "card_img_top"  : { "field" : "", "default" : None,        "is_visible" : False },
        },

        "ui_options"        : {
          "card_color"    : { "value" : None, "default" : "white", },
          "text_color"    : { "value" : None, "default" : "black", },
          "link_to_detail"   : { "is_visible" : True, "tooltip" : [{"locale" : "en", "text" : "see the document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le document" }] },
          "link_to_next"     : { "is_visible" : True, "tooltip" : [{"locale" : "en", "text" : "see the next document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le prochain document" }] },
          "link_to_previous" : { "is_visible" : True, "tooltip" : [{"locale" : "en", "text" : "see the previous document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le document précédent" }] },
        },

        "links_options"  : {

          "block_contents_links" : {
          "is_visible"  : False,
          "position"    : "block_bottom_1",
          "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
          "links"       : []
          },

          "block_data_infos" : {
          "is_visible"  : False,
          "position"    : "block_bottom_2",
          "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
          "links"       : []
          },

          "block_share" : {
          "is_visible"  : False,
          "position"    : "block_bottom_3",
          "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
          "links"       : []
          },

        },

        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "cis-tabs",
        "deactivate_btn"    : False,
        "is_visible"        : True,
        "apiviz_front_uuid" : uuid_models["uuid_apcis"],
        "is_default"      : True
      },

      ### PAGE - list
      { "field"             : "cis_liste",
        "is_global_app_homepage" : False,
        "route_title"       : u"Rechercher",
        "route_description" : u"Page de recherche du CIS",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "banner-sonum-carto"
        },
        "is_dataset_homepage" : False,

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "only_in_navbar_for_this_dataset" : True,
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "en", "text" : "Search for a place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "en", "text" : "Search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : False,
        "urls"              : ["/recherche", "/recherche/liste"],
        # "template_url"      : "/static/spa.html",
        "template_urls"     : [
        ],
        
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main search route in french",
        "is_dynamic"        : True,
        "dataset_uri"       : "recherche",
        "dynamic_template"  : 'DynamicList',
        "endpoint_type"     : "list",

        "contents_fields"  : [

          { "field" : "sd_id",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_id",
            
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "address",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_city",
            # "trim" : 20,
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "ville structure",
            "field_format" : { "trim" : None, "type" : "list", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_city",
            # "trim" : 20,
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "titre du projet",
            "field_format" : { "trim" : 50, "type" : "list", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_title",
            # "trim" : 20,
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "image(s) du projet",
            "field_format" : { "trim" : None, "type" : "list", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_image",
            # "trim" : 20,
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "résumé du projet",
            "field_format" : { "trim" : 75, "type" : "list", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_abstract",
            
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "link_src",
            "field_format" : { "trim" : 15, "type" : "object", "retrieve" : [0] },
            "is_visible" : False,
            "position" : "block_src",
            
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "tags",
            "field_format" : { "trim" : 10, "type" : "list_tags", "retrieve" : [-1] },
            "is_visible" : True,
            "position" : "block_tags",
            "filter_correspondance" : True,
            "is_tag_like" : False,
            "tags_separator" : ";",
            "custom_title" : "to do",
            "locale" : "fr"
          },

        ],

        "images_fields"        : {
          "card_img_main" : { "field" : "", "default" : "img_card",  "is_visible" : True  },
          "card_img_top"  : { "field" : "", "default" : None,        "is_visible" : False },
        },
        "ui_options" : {
          "card_color"    : { "value" : None, "default" : "white", },
          "text_color"    : { "value" : None, "default" : "black", },
          "link_to_detail"   : { "is_visible" : True, "tooltip" : [{"locale" : "en", "text" : "see the document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le document" }] },
          "link_to_next"     : { "is_visible" : True, "tooltip" : [{"locale" : "en", "text" : "see the next document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le prochain document" }] },
          "link_to_previous" : { "is_visible" : True, "tooltip" : [{"locale" : "en", "text" : "see the previous document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le document précédent" }] },
        },

        "links_options"  : {

          "block_contents_links" : {
          "is_visible"  : False,
          "position"    : "block_bottom_1",
          "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
          "links"       : []
          },

          "block_data_infos" : {
          "is_visible"  : False,
          "position"    : "block_bottom_2",
          "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
          "links"       : []
          },

          "block_share" : {
          "is_visible"  : False,
          "position"    : "block_bottom_3",
          "title_block" : [{"locale" : "en", "text" : "share this place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Partagez ce lieu", "is_visible" : False}],
          "links"       : []
          },

        },

        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "cis-tabs",
        "deactivate_btn"    : False,
        "is_visible"        : True,
        "apiviz_front_uuid" : uuid_models["uuid_apcis"],
        "is_default"        : True
      },

      ### PAGE - detail
      { "field"             : "cis_detail",
        "is_global_app_homepage" : False,
        "route_title"        : u"Rechercher",
        "route_description"  : u"Page de recherche d'Apiviz",
        "route_activated"    : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "banner-sonum-carto"
        },
        "is_dataset_homepage" : False,

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "only_in_navbar_for_this_dataset" : True,
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "en", "text" : "Search for a place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "en", "text" : "Search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : False,
        "urls"              : ["/project", "/cis/detail", "/recherche/detail"],
        # "template_url"      : "/static/spa.html",
        "template_urls"     : [
        ],
        
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main search route in french",
        "is_dynamic"        : True,
        "dataset_uri"       : "recherche",
        "dynamic_template"  : 'DynamicDetail',
        "endpoint_type"     : "detail",

        "contents_fields"  : [

          # { "field" : "intitulé structure", #SONUM
          { "field" : "titre du projet", #CIS
            "field_format" : { "trim" : None, "type" : "list", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_title",
            
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "image(s) du projet",
            "field_format" : { "trim" : None, "type" : "list", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_image",
            # "trim" : 20,
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "adresse du projet",
            "field_format" : { "trim" : None, "type" : "list", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_address",
            
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "code postal structure",
            "field_format" : { "trim" : None, "type" : "list", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_cp",
            
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "résumé du projet",
            "field_format" : { "trim" : 500, "type" : "list", "retrieve" : [-1] },
            "is_visible" : True,
            "position" : "block_abstract",
            
            "custom_title" : "Résumé du projet",
            "locale" : "fr"
          },
          { "field" : "link_src",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_src",
            
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "services",
            "field_format" : { "trim" : None, "type" : "list", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_tags",
            
            "is_tag_like" : True,
            "tags_separator" : "-",
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "link_data",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_wesite",
            
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field"       : "tags",
            "field_format" : { "trim" : 10, "type" : "list_tags", "retrieve" : [-1] },
            "is_visible"  : True,
            "position"    : "block_rb1_tags",

            "is_tag_like" : False,
            "tags_separator" : "",
            "custom_title" : "Thématiques",
            "locale" : "fr"
          },

        ],

        "images_fields"     : {
          "card_img_main"  : { "field" : "", "default" : "img_card",  "is_visible" : True,  "position" : "block_right_top_1" },
          "card_img_top"   : { "field" : "", "default" : None,        "is_visible" : False, "position" : "block_right_middle" },
        },

        "ui_options"        : {
          "card_color"     : { "value" : None, "default" : "white", },
          "text_color"     : { "value" : None, "default" : "black", },
          "link_to_detail"   : { "is_visible" : True, "tooltip" : [{"locale" : "en", "text" : "see the document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le document" }] },
          "link_to_next"     : { "is_visible" : True,  "tooltip" : [{"locale" : "en", "text" : "see the next document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le prochain document" }] },
          "link_to_previous" : { "is_visible" : True,  "tooltip" : [{"locale" : "en", "text" : "see the previous document"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le document précédent" }] },
        },

        "links_options"  : {

          "block_contents_links" : {
          "is_visible"  : True,
          "position"    : "block_left_middle_2",
          "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
          "links"       : [
            { "field" : "website",
              "is_visible" : True,
              "link_type"  : "text",
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "website" }],
              "tooltip"    : [{"locale" : "en", "text" : "check the website"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "voir le site" }]
            },
            { "field" : "contact",
              "is_visible" : True,
              "link_type"  : "text",
              "icon_class" : "",
              "link_text"  : [{"locale" : "en", "text" : "contact"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "contact" }],
              "tooltip"    : [{"locale" : "en", "text" : "contact the structure"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "contacter la structure" }]
            },
          ]
          },

          "block_share" : {
          "is_visible"  : True,
          "position"    : "block_left_bottom_2",
          "title_block" : [{"locale" : "en", "text" : "Share this place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Partagez ce lieu", "is_visible" : True}],
          "links"       : [
            {
              "is_visible" : True,
              "link_type"  : "icon",
              "icon_class" : "fas fa-link",
              "link_text"  : [{"locale" : "en", "text" : "link"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "lien" }],
              "tooltip"    : [{"locale" : "en", "text" : "share this page"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "partager cette page (copier le lien)" }]
            },
            {
              "is_visible" : True,
              "link_type"  : "icon",
              "icon_class" : "fab fa-facebook-f",
              "link_text"  : [{"locale" : "en", "text" : "facebook"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "facebook" }],
              "tooltip"    : [{"locale" : "en", "text" : "share on facebook"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "partager sur facebook" }]
            },
            {
              "is_visible" : True,
              "link_type"  : "icon",
              "icon_class" : "fab fa-twitter",
              "link_text"  : [{"locale" : "en", "text" : "twitter"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "twitter" }],
              "tooltip"    : [{"locale" : "en", "text" : "share on twitter"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "partager sur twitter" }]
            },
          ]
          },

        },

        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "cis-tabs",
        "deactivate_btn"    : False,
        "is_visible"        : True,
        "apiviz_front_uuid" : uuid_models["uuid_apcis"],
        "is_default"        : True
      },

    ### - - - - - - - - - - - - - - - - - ###
    ### CUSTOM ROUTES-PAGES --> TO BE ADDED VIA BACK OFFICE BY ADMIN USER
    ### - - - - - - - - - - - - - - - - - ###

      ### PAGE - PROJECT
      { "field"             : "cis_project",
        "is_global_app_homepage" : True,
        "route_title"       : u"Home",
        "route_description" : u"apiviz default home page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "banner-sonum-carto"
        },
        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "en", "text" : "Search for a place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "en", "text" : "Search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : False,
        "link_in_logo"      : True,
        "urls"              : ["/le-projet"],
        "dataset_uri"       : "project-cis",
        
        "template_urls"     : [
          { "locale" : "fr", "url" : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/le-projet.html" }, 
          { "locale" : "en", "url" : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/le-projet.html" }, 
          # { "locale" : "fr", "url" : "http://localhost:8800/html/pages-html/le-projet.html" }, 
          # { "locale" : "en", "url" : "http://localhost:8800/html/pages-html/le-projet.html" }, 
        ],
        

        "has_ext_script"    : True,
        "ext_script_urls"   : [
          {"script_id" : "js-car"    , "at_mount" : True,  "type" : None, "url" : "https://cdn.jsdelivr.net/npm/bulma-carousel@4.0.4/dist/js/bulma-carousel.min.js"},
          
          # {"script_id" : "js-project", "at_mount" : False, "type" : None, "url" : "http://localhost:8800/statics/scripts/le-projet.js?v4"},
          {"script_id" : "js-project", "at_mount" : False, "type" : None, "url" : "https://cdn.jsdelivr.net/gh/co-demos/cis-data/scripts/le-projet.js"},
        ],

        # "has_carousel"      : True,
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main project route in french",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,

        "has_tabs"          : True,
        "tabs_uri"          : "tabs-cis-test",

        "has_footer"        : True,
        "apiviz_front_uuid" : uuid_models["uuid_apcis"],
        "is_default"        : True
      },

      ### PAGE : QUI SOMMES-NOUS CIS
      { "field"             : "app_who_fr",
        "is_global_app_homepage" : False,
        "route_title"        : u"Collectif",
        "route_description"  : u"Le collectif",
        "route_activated"    : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "default"
        },
        "is_dataset_homepage" : False,

        "in_main_navbar"    : True,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "button",
          "icon_class" : "",
          "link_text"  : [{"locale" : "en", "text" : "Search for a place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "en", "text" : "Search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/le-collectif"],
        
        "template_urls"     : [
          { "locale" : "fr", "url" : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/le-collectif.html" }, 
          { "locale" : "en", "url" : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/le-collectif.html" }, 
          # { "locale" : "fr", "url" : "http://localhost:8800/html/pages-html/le-collectif.html" }, 
          # { "locale" : "en", "url" : "http://localhost:8800/html/pages-html/le-collectif.html" }, 
        ],
        
        "has_ext_script"    : False,
        "ext_script_urls"   : "",
        
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"A custom page for your ApiViz app",
        "is_dynamic"        : True,
        "dynamic_template"  : 'DynamicStatic',

        "has_navbar"        : True,
        "has_footer"        : True,

        "has_tabs"          : True,
        "tabs_uri"          : "tabs-cis-collective",

        "apiviz_front_uuid" : uuid_models["uuid_apcis"],
        "is_default"        : True
      },

      ### PAGE : QUI-SOMMES-NOUS/QUI-FAIT-QUOI
      { "field"             : "cis_partners",
        "is_global_app_homepage" : True,
        "route_title"       : u"Qui fait quoi",
        "route_description" : u"APCIS partners page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },
        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "" }],
          "tooltip"    : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "" }],
        },

        "in_footer"         : True,
        "link_in_logo"      : False,
        "urls"              : ["/le-collectif/qui-fait-quoi"],
        
        "template_urls"     : [
          { "locale" : "fr", "url" : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/qui-fait-quoi.html" }, 
          { "locale" : "en", "url" : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/qui-fait-quoi.html" }, 
          # { "locale" : "fr", "url" : "http://localhost:8800/html/pages-html/qui-fait-quoi.html" }, 
          # { "locale" : "en", "url" : "http://localhost:8800/html/pages-html/qui-fait-quoi.html" }, 
        ],
        
        "has_ext_script"    : True,
        "ext_script_urls"   : [
          {"script_id" : "js-sho", "at_mount" : False,  "type" : "text/javascript", "url" : "https:cdn.jsdelivr.net/gh/co-demos/cis-data/scripts/who-are-we.js?v4"},
          # {"script_id" : "js-who", "at_mount" : False,  "type" : "text/javascript", "url" : "http://localhost:8800/statics/scripts/who-are-we.js?v14"},
        ],
        
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main apiviz tools route in french",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : True,
        "tabs_uri"          : "tabs-cis-collective",
        "apiviz_front_uuid" : uuid_models["uuid_apcis"],
        "is_default"        : True
      },

      ### PAGE : JOIN US/NOUS REJOINDRE CIS
      { "field"             : "app_join_us",
        "is_global_app_homepage" : False,
        "route_title"        : u"Home",
        "route_description"  : u"Nous rejoindre",
        "route_activated"    : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "default"
        },
        "is_dataset_homepage" : False,

        "in_main_navbar"    : True,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "button",
          "icon_class" : "",
          "link_text"  : [{"locale" : "en", "text" : "Search for a place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Recherher un lieu" }],
          "tooltip"    : [{"locale" : "en", "text" : "Search"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Rechercher" }],
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/nous-rejoindre"],
        
        "template_urls"     : [
          { "locale" : "fr", "url" : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/nous-rejoindre.html" }, 
          { "locale" : "en", "url" : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/nous-rejoindre.html" }, 
          # { "locale" : "fr", "url" : "http://localhost:8800/html/pages-html/nous-rejoindre.html" }, 
          # { "locale" : "en", "url" : "http://localhost:8800/html/pages-html/nous-rejoindre.html" }, 
        ],
        
        "has_ext_script"    : False,
        "ext_script_urls"   : "",
        
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"A custom page for your ApiViz app",
        "is_dynamic"        : True,
        "dynamic_template"  : 'DynamicStatic',
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : True,
        "tabs_uri"          : "tabs-cis-test",
        "apiviz_front_uuid" : uuid_models["uuid_apcis"],
        "is_default"        : True
      },

      ### PAGE : PROJECT/TOOLS (CIS)
      { "field"             : "cis_tools",
        "is_global_app_homepage" : True,
        "route_title"       : u"Outils",
        "route_description" : u"apiviz default tools page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },
        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "" }],
          "tooltip"    : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "" }],
        },

        "in_footer"         : True,
        "link_in_logo"      : False,
        "urls"              : ["/le-projet/outils"],
        
        "template_urls"     : [
          { "locale" : "fr", "url" : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/les-outils.html" },
          { "locale" : "en", "url" : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/les-outils.html" },
          # { "locale" : "fr", "url" : "http://localhost:8800/html/pages-html/les-outils.html" }, 
          # { "locale" : "en", "url" : "http://localhost:8800/html/pages-html/les-outils.html" }, 
        ],
        
        "has_ext_script"    : False,
        "ext_script_urls"   : "",
        
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main apiviz tools route in french",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : True,
        "tabs_uri"          : "tabs-cis-test",
        "apiviz_front_uuid" : uuid_models["uuid_apcis"],
        "is_default"        : True
      },

      ### PAGE : PROJECT/PARLENT-DE-NOUS (CIS)
      { "field"             : "cis_review",
        "is_global_app_homepage" : True,
        "route_title"       : u"Outils",
        "route_description" : u"apiviz default tools page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },
        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "" }],
          "tooltip"    : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "" }],
        },

        "in_footer"         : True,
        "link_in_logo"      : False,
        "urls"              : ["/le-projet/parlent-de-nous"],
        
        "template_urls"     : [
          { "locale" : "fr", "url" : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/parlent-de-nous.html" }, 
          { "locale" : "en", "url" : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/parlent-de-nous.html" }, 
          # { "locale" : "fr", "url" : "http://localhost:8800/html/pages-html/parlent-de-nous.html" }, 
          # { "locale" : "en", "url" : "http://localhost:8800/html/pages-html/parlent-de-nous.html" }, 
        ],
        
        "has_ext_script"    : False,
        "ext_script_urls"   : "",
        
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main apiviz tools route in french",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : True,
        "tabs_uri"          : "tabs-cis-test",
        "apiviz_front_uuid" : uuid_models["uuid_apcis"],
        "is_default"        : True
      },


      ### PAGE : PROJECT/RECOMPENSES
      { "field"             : "cis_rewards",
        "is_global_app_homepage" : True,
        "route_title"       : u"Outils",
        "route_description" : u"apiviz default tools page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },
        "in_main_navbar"    : False,
        "navbar_btn_options" : {
          "position"   : "middle_right",
          "link_type"  : "link",
          "icon_class" : "",
          "link_text"  : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "" }],
          "tooltip"    : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "" }],
        },

        "in_footer"         : True,
        "link_in_logo"      : False,
        "urls"              : ["/le-projet/recompenses"],
        
        "template_urls"     : [
          { "locale" : "fr", "url" : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/recompenses.html" }, 
          { "locale" : "en", "url" : "https://raw.githubusercontent.com/co-demos/cis-data/master/pages-html/recompenses.html" }, 
          # { "locale" : "fr", "url" : "http://localhost:8800/html/pages-html/recompenses.html" }, 
          # { "locale" : "en", "url" : "http://localhost:8800/html/pages-html/recompenses.html" }, 
        ],
        
        "has_ext_script"    : False,
        "ext_script_urls"   : "",
        
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main apiviz tools route in french",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : True,
        "tabs_uri"          : "tabs-cis-test",
        "apiviz_front_uuid" : uuid_models["uuid_apcis"],
        "is_default"        : True
      },

    ### - - - - - - - - - - - - - - - - - ###
    ### CUSTOM ROUTES-LOGIN 
    ### - - - - - - - - - - - - - - - - - ###

      { "field"             : "app_login",
        "is_global_app_homepage" : False,
        "route_title"       : u"Login",
        "route_description" : u"apiviz default login page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/login"],
        
        "template_urls"     : [
        ],
        
        "help"              : u"default login page for Apiviz",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main login route ",
        "is_dynamic"        : True,
        "dynamic_template"  : "Login",
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "tabs-cis-default",
        "apiviz_front_uuid" : uuid_models["uuid_apcis"],
        "is_default"        : True
      },

      { "field"             : "app_register",
        "is_global_app_homepage" : False,
        "route_title"       : u"Register",
        "route_description" : u"apiviz default register page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/register"],
        
        "template_urls"     : [
        ],
        
        "help"              : u"default register page for Apiviz",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main register route ",
        "is_dynamic"        : True,
        "dynamic_template"  : "Register",
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "tabs-cis-default",
        "apiviz_front_uuid" : uuid_models["uuid_apcis"],
        "is_default"        : True
      },

      { "field"             : "app_logout",
        "is_global_app_homepage" : False,
        "route_title"       : u"logout",
        "route_description" : u"apiviz default logout page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/logout"],
        
        "template_urls"     : [
        ],
        
        "help"              : u"default logout page for Apiviz",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main logout route ",
        "is_dynamic"        : True,
        "dynamic_template"  : "Logout",
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "tabs-cis-default",
        "apiviz_front_uuid" : uuid_models["uuid_apcis"],
        "is_default"        : True
      },

      { "field"             : "app_backoffice",
        "is_global_app_homepage" : False,
        "route_title"       : u"backoffice",
        "route_description" : u"apiviz default backoffice page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/backoffice"],
        
        "template_urls"     : [
        ],
        
        "help"              : u"default backoffice page for Apiviz",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main backoffice route ",
        "is_dynamic"        : True,
        "dynamic_template"  : "BackOffice",
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "tabs-cis-default",
        "apiviz_front_uuid" : uuid_models["uuid_apcis"],
        "is_default"        : True
      },

      { "field"             : "app_preferences",
        "is_global_app_homepage" : False,
        "route_title"       : u"preferences",
        "route_description" : u"apiviz default user preferences page",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : ""
        },

        "in_main_navbar"    : False,
        "navbar_btn_options" : {
        },

        "in_footer"         : False,
        "link_in_logo"      : False,
        "urls"              : ["/preferences"],
        
        "template_urls"     : [
        ],
        
        "help"              : u"default preferences page for Apiviz",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main user preferences route",
        "is_dynamic"        : True,
        "dynamic_template"  : "Preferences",
        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "tabs-cis-default",
        "apiviz_front_uuid" : uuid_models["uuid_apcis"],
        "is_default"        : True
      },


]
