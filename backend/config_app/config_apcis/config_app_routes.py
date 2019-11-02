# -*- encoding: utf-8 -*-

from . import version, uuid_models

### ROUTES / PAGES

default_routes_config = [

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

          {"script_id" : "js-home" , "at_mount" : False, "type" : "text/javascript", "url" : "https://cdn.jsdelivr.net/gh/co-demos/cis-data/scripts/home.js?v2"}
          # {"script_id" : "js-home", "at_mount" : False, "type" : "text/javascript", "url" : "http://localhost:8800/statics/scripts/home.js?v7"},
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
          { "field" : "address", # CIS
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_address",
            # "trim" : 20,
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "ville structure",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_city",
            # "trim" : 20,
            "custom_title" : "to do",
            "locale" : "fr"
          },
          # { "field" : "intitulé structure", # SONUM
          { "field" : "titre du projet", # CIS
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_title",
            # "trim" : 20,
            "custom_title" : "to do",
            "locale" : "fr"
          },
          # { "field" : "image(s) du projet",
          #   "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
          #   "is_visible" : True,
          #   "position" : "block_image",
          #   # "trim" : 20,
          #   "custom_title" : "to do",
          #   "locale" : "fr"
          # },
          { "field" : "résumé du projet",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_abstract",
            
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "source", # spider/sourceur
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_src",
            
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field"       : "coding APCIS N1",
            "field_format" : { "trim" : 15, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_tags",
            "filter_correspondance" : True,
            "is_tag_like" : True,
            "tags_separator" : "-",
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

        "map_options"   : {
          
          ### TO ADAPT TO MAPBOX-GL-JS OPTIONS
          "url"              : "https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png",
          "attribution"      : '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
          "subdomains"       : 'abcd',
          "center"           : [46.2276, 2.2137],
          "currentCenter"    : [46.2276, 2.2137],
          "zoom"             : 5,
          "maxZoom"          : 18,
          "minZoom"          : 2,
          "useMarkerCluster" : True,
          "pinIconUrl"       : "/static/icons/icon_pin_plein_violet.svg",
          "pinIconSize"      : { "highlighted" : [46, 46], "normal" : [29, 29]},

          "mapbox_layers" : {

            "all_points_layer" : {
              "is_activated"        : True,
              "source_id"           : "allPointsSource",
              "layer_id"            : "all-points",
              "is_default_visible"  : True,
              "is_source_distant"   : False,

              "is_live_data"        : False,
              "refresh_delay"       : 3000,

              "is_clickable"        : True,

              "radius_min"          : 1,
              "radius_max"          : 10,
              "max_zoom"            : 14,
              "min_zoom"            : 4,
              "circle_color"        : "#a174ac",
              "circle_stroke_color" : "#fff",
              "circle_opacity"      : 0.8,
            },

            "cluster_circles_layer" : {
              "is_activated"        : True,
              "source_id"           : "clusterSource",
              "layer_id"            : "cluster-circles",
              "is_default_visible"  : True,

              "is_source_distant"   : False, ### clusters all points sources by default
              "is_clickable"        : True,

              "circle_color"     : "#a174ac", 
              "circle_color_100" : "#90689a", 
              "circle_color_250" : "#805c89", 
              "circle_color_500" : "#705178", 
              "circle_color_750" : "#503a56", 

              "circle_radius"     : 20, 
              "circle_radius_100" : 20, 
              "circle_radius_250" : 30, 
              "circle_radius_500" : 40, 
              "circle_radius_750" : 50, 

              "circle_stroke_color" : "#fff",
              "circle_stroke_width" : 1,
            },

            "cluster_count_layer" : {
              "is_activated"        : True,
              "source_id"           : "clusterSource",
              "layer_id"            : "cluster-counts",
              "is_default_visible"  : True,
              "is_source_distant"   : False,
              "is_clickable"        : True,

              "text_size"  : 12,
              "text_color" : "#ffffff"
            },

            "cluster_unclustered_layer" : {
              "is_activated"        : True,
              "source_id"           : "clusterSource",
              "layer_id"            : "unclustered-point",
              "is_default_visible"  : False,
              "is_source_distant"   : False,
              "is_clickable"        : True,

              "circle_color"        : "#fff", 
              "circle_troke_color"  : "#a174ac",
              "circle_radius"       : 5, 
              "circle_stroke_width" : 5, 
            },
          },
        
          "layers_visibility" :{
            "is_activated" : True,
            "is_drawer_open" : True,
            "layers_switches" : [ 
              { "label" : "projets", "layers" : [ "all-points" ], "default_visible" : True }, 
              { "label" : "clusters" , "layers" : [ "cluster-circles", "cluster-counts" ], "default_visible" : True }, 
              # { "label" : "départements" , "layers" : [ "chorolayer-departements" ], "default_visible" : True }, 
              # { "title" : "communes" ,   "layers" : [ "chorolayer-communes" ],     "default_visible" : False }, 
              # { "label" : "radar" ,        "layers" : [ "heatmap-layer" ],           "default_visible" : False }
            ],
          },


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
          "banner_uri" : "banner-apcis-carto"
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
          # { "field" : "address",
          #   "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
          #   "is_visible" : True,
          #   "position" : "block_city",
          #   # "trim" : 20,
          #   "custom_title" : "to do",
          #   "locale" : "fr"
          # },
          { "field" : "ville structure",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_city",
            # "trim" : 20,
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "titre du projet",
            "field_format" : { "trim" : 50, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_title",
            # "trim" : 20,
            "custom_title" : "to do",
            "locale" : "fr"
          },
          # { "field" : "image(s) du projet",
          #   "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
          #   "is_visible" : True,
          #   "position" : "block_image",
          #   # "trim" : 20,
          #   "custom_title" : "to do",
          #   "locale" : "fr"
          # },
          { "field" : "résumé du projet",
            "field_format" : { "trim" : 75, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_abstract",
            
            "custom_title" : "to do",
            "locale" : "fr"
          },
          { "field" : "source",
            "field_format" : { "trim" : 15, "type" : "object", "retrieve" : [0] },
            "is_visible" : False,
            "position" : "block_src",
            
            "custom_title" : "to do",
            "locale" : "fr"
          },
          # { "field" : "tags",
          #   "field_format" : { "trim" : 10, "type" : "list_tags", "retrieve" : [-1] },
          #   "is_visible" : True,
          #   "position" : "block_tags",
          #   "filter_correspondance" : True,
          #   "is_tag_like" : False,
          #   "tags_separator" : ";",
          #   "custom_title" : "to do",
          #   "locale" : "fr"
          # },
          { "field"       : "coding APCIS N1",
            "field_format" : { "trim" : 15, "type" : "object", "retrieve" : [0] },
            "is_visible"  : True,
            "position"    : "block_tags",
            "filter_correspondance" : True,
            "is_tag_like" : True,
            "tags_separator" : "-",
            "custom_title" : "Thématiques",
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
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_title",
            
            "custom_title" : "to do",
            "locale" : "fr"
          },
          # { "field" : "image(s) du projet",
          #   "field_format" : { "trim" : None, "type" : "list", "retrieve" : [0] },
          #   "is_visible" : True,
          #   "position" : "block_image",
          #   # "trim" : 20,
          #   "custom_title" : "to do",
          #   "locale" : "fr"
          # },
          { "field" : "ville structure",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
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
            "field_format" : { "trim" : 500, "type" : "object", "retrieve" : [-1] },
            "is_visible" : True,
            "position" : "block_abstract",
            
            "custom_title" : "Résumé du projet",
            "locale" : "fr"
          },
          { "field" : "source",
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
          { "field"       : "coding APCIS N1",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible"  : True,
            "position"    : "block_rb1_tags",
            "filter_correspondance" : True,
            "is_tag_like" : True,
            "tags_separator" : "-",
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

      ## PAGE - stats
      { "field"             : "cis_stats",
        "is_global_app_homepage" : False,
        "route_title"       : u"Rechercher stats",
        "route_description" : u"Page de recherche stats LM d'Apiviz",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "banner-apcis-carto"
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
        "urls"              : ["/recherche/stats"],
        "template_urls"     : [
        ],
        
        "help"              : u"helper stats...",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main search route in french",
        "is_dynamic"        : True,
        "dataset_uri"       : "recherche",
        "dynamic_template"  : 'DynamicStats',
        "endpoint_type"     : "stat",

        "contents_fields"  : [
          { "field" : "sd_id",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_id",
            "locale" : "fr"
          },
        ],

        "images_fields"   : {
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

        "charts_list" : [ 
          
          ### apexCharts configs
          ### cf : https://apexcharts.com/vue-chart-demos/

          { ### BAR HORIZ - SETTINGS EXAMPLE
            "serie_id" : "apcis-stat-bar-horiz",
            "is_activated" : True,
            "chart_type": "bar", 
            "help" : "bar horiz + stacked example",
            "position": 1,
            "col_size" : 6,
            "height": "400px",
            "width" : "100%", 

            "data_mapping" : {

              "serie_path" : "results/data",
              "serie_name_field" : "_id",
              "serie_data" : {

                "subpath" : "subcounts",

                "need_remap" : True,
                "data_value" : "count",
                "label_field" : "tag_name",

                "need_list_only" : False,

                "add_missing_values" : True,
                "missing_data_by" : {
                  "val_fields_list" : [ 
                    "EDU",
                    "EMP",
                    "ENV",
                    "SAN",
                    "SOL",
                    "TER",
                    "ART",
                    "COM",
                    "CON",
                    "DEM",
                    "GOU",
                    "NUM",
                    "SPO",
                    "TOU",
                    "FIN",
                    "PAT",
                  ],
                  # "val_field" : "tag_name",
                },

                "need_labels_remap" : True,
                "need_labels_rename" : True,
                "labels_mapping" : {
                  "chart_options_label_path" : "xaxis/categories",
                  "labels_dict" : {
                    "EDU" : "éducation",
                    "EMP" : "emploi",
                    "ENV" : "environnement",
                    "SAN" : "santé",
                    "SOL" : "solidarité",
                    "TER" : "territoires",
                    "ART" : "arts",
                    "COM" : "communication",
                    "CON" : "consommation",
                    "DEM" : "démocratie",
                    "GOU" : "gouvernance",
                    "NUM" : "numérique",
                    "SPO" : "sport",
                    "TOU" : "tourisme",
                    "FIN" : "finance",
                    "PAT" : "patrimoine",
                    "None" : "( non renseigné )",
                  }
                },

                "need_sorting" : True,
                "sorting_by" : {
                  "sort_field" : "tag_name",
                },

              },

              "serie_chart_options" : [ 
                # { 
                #   "options_field_path" : "xaxis/categories",
                #   "build_list_from" : "results/data/subcounts/tag_name"
                # },
              ],
            },  

            "chart_options": {

              "chart": {
                "stacked": True,
                # "stackType": '100%'
              },
              "plotOptions": {
                "bar": {
                  "horizontal": True,
                }
              },
              "theme" : {
                "palette" : "palette10", ### cf : https://apexcharts.com/docs/options/theme/#palette
              },
              "stroke": {
                "width": 1,
                "colors": [
                  "#fff",
                  "#fff",
                  "#fff",
                  "#fff",
                  "#fff"
                ]
              },
              "title": {
                "text": "Categories / Sources"
              },
              "xaxis": {
                # "categories": [
                #   2008,
                #   2009,
                #   2010,
                #   2011,
                #   2012,
                #   2013,
                #   2014
                # ],
                "categories": [
                  "EDUCATION",
                  "EMPLOI",
                  "ENVIRONNEMENT",
                  "SANTE",
                  "SOLIDARITE",
                  "TERRITOIRE",
                  "ARTS",
                  "COMMUNICATION",
                  "CONSOMMATION",
                  "DEMOCRATIE",
                  "GOUVERNANCE",
                  "NUMERIQUE",
                  "SPORT",
                  "TOURISME",
                  "FINANCE",
                  "PATRIMOINE",
                ],
                "labels": {}
              },
              "yaxis": {
                "title": {}
              },
              "tooltip": {
                "y": {}
              },
              "fill": {
                "opacity": 1
              },
              "legend": {
                "position": "top",
                "horizontalAlign": "left",
                "offsetX": 40
              }
            }
          },

          { ### DOUGHNUT - SETTINGS EXAMPLE
            "serie_id" : "apcis-stat-donut",
            "is_activated" : True,
            "chart_type": "donut", 
            "position": 0,
            "col_size" : 6,
            "height": "350px",
            "width" : "100%", 

            "data_mapping" : {
              
              "serie_path" : "results/data",
              "serie_name_field" : "_id",
              "serie_data" : {

                "subpath" : None,

                "need_remap" : False,
                "data_value" : "count",
                "label_field" : None,

                "need_list_only" : True,

                "add_missing_values" : False,
                "missing_data_by" : {
                  # "val_fields_list" : None,
                },

                "need_sorting" : False,
                "sorting_by" : {
                  "sort_field" : "_id",
                },

              },
              "serie_chart_options" : [ 
                { 
                  "step" : "before_list",
                  "options_field_path" : "labels",
                  "build_list_from" : "_id"
                },
              ],
            },

            "chart_options": {
              "title": {
                "text": "Sources (%)",
              },
              "theme" : {
                "palette" : "palette3", ### cf : https://apexcharts.com/docs/options/theme/#palette 
              },
              "responsive": [{
                "breakpoint": 480,
                "options": {
                  "chart": {
                    "width": 200
                  },
                  "legend": {
                    "position": 'bottom'
                  }
                }
              }]
            },

          },


        ],

        "links_options"  : {
        },

        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : None,
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
          {"script_id" : "js-sho", "at_mount" : False,  "type" : "text/javascript", "url" : "https://cdn.jsdelivr.net/gh/co-demos/cis-data/scripts/who-are-we-https.js"},
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
