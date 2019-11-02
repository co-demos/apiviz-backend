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

              ### all points source and layer
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

              ### clusters source and layer
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
                "is_default_visible"  : True,
                "is_source_distant"   : False,
                "is_clickable"        : True,

                "circle_color"        : "#fff", 
                "circle_troke_color"  : "#a174ac",
                "circle_radius"       : 5, 
                "circle_stroke_width" : 5, 
              },

              ### heatmap source and layer
              "heatmap_layer" : {
                "is_activated"        : True,
                "is_default_visible"  : False,
                "source_id"           : "allPointsSource",
                "layer_id"            : "heatmap-layer",
                "source"              : "all-points",
                "prop_weight"         : "weight",
                "max_zoom"            : 18,
                "radius_min"          : 5,
                "radius_max"          : 15,
              },

            },
          

            "layers_visibility" :{
              "is_activated" : True,
              "is_drawer_open" : True,
              "layers_switches" : [ 
                { "label" : "lieux",         "layers" : [ "all-points" ], "default_visible" : True }, 
                { "label" : "clusters" ,     "layers" : [ "cluster-circles", "cluster-counts" ], "default_visible" : True }, 
                # { "label" : "départements" , "layers" : [ "chorolayer-departements" ], "default_visible" : True }, 
                # { "title" : "communes" ,   "layers" : [ "chorolayer-communes" ], "default_visible" : False }, 
                { "label" : "radar" ,        "layers" : [ "heatmap-layer" ], "default_visible" : False }
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

        ## PAGE - stats
        { "field"             : "sonum_carto_stats",
          "is_global_app_homepage" : False,
          "route_title"       : u"Rechercher stats",
          "route_description" : u"Page de recherche stats LM d'Apiviz",
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
          "urls"              : ["/sonum-carto/stats"],
          "template_urls"     : [
          ],
          
          "help"              : u"helper stats...",
          "languages"         : ["fr"],
          "app_version"       : version,
          "comment"           : u"Main search route in french",
          "is_dynamic"        : True,
          "dataset_uri"       : "sonum-carto",
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
              "serie_id" : "sonum-carto-stat-bar-horiz",
              "is_activated" : True,
              "chart_type": "bar", 
              "help" : "bar horiz + stacked example",
              "position": 0,
              "col_size" : 6,
              "height": "350px",
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
                      "ACC", 
                      "FOR", 
                      "ACL", 
                      "NR" 
                    ],
                    # "val_field" : "tag_name",
                  },

                  "need_labels_remap" : False,
                  "need_labels_rename" : False,
                  "labels_mapping" : {
                    "chart_options_label_path" : "xaxis/categories",
                    "labels_dict" : {
                      "ACC" : "accompagnement",
                      "FOR" : "formation",
                      "ACL" : "aclimmatation",
                      "NR"  : "non renseigné",
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
                  "text": "categories / sources"
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
                    "ACC",
                    "ACL",
                    "FOR",
                    "NR"
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
              "serie_id" : "sonum-carto-stat-donut",
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
                  "text": "sources (%)",
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
          "route_activated"    : False,
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

              ### all points source and layer
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

              ### clusters source and layer
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
                "is_default_visible"  : True,
                "is_source_distant"   : False,
                "is_clickable"        : True,

                "circle_color"        : "#fff", 
                "circle_troke_color"  : "#a174ac",
                "circle_radius"       : 5, 
                "circle_stroke_width" : 5, 
              },

              ### heatmap source and layer
              "heatmap_layer" : {
                "is_activated"        : True,
                "is_default_visible"  : False,
                "source_id"           : "allPointsSource",
                "layer_id"            : "heatmap-layer",
                "source"              : "all-points",
                "prop_weight"         : "weight",
                "max_zoom"            : 18,
                "radius_min"          : 5,
                "radius_max"          : 15,
              },

            },
          

            "layers_visibility" :{
              "is_activated" : True,
              "is_drawer_open" : True,
              "layers_switches" : [ 
                { "label" : "lieux",         "layers" : [ "all-points" ], "default_visible" : True }, 
                { "label" : "clusters" ,     "layers" : [ "cluster-circles", "cluster-counts" ], "default_visible" : True }, 
                # { "label" : "départements" , "layers" : [ "chorolayer-departements" ], "default_visible" : True }, 
                # { "title" : "communes" ,   "layers" : [ "chorolayer-communes" ], "default_visible" : False }, 
                { "label" : "radar" ,        "layers" : [ "heatmap-layer" ], "default_visible" : False }
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
        { "field"             : "sonum_xp_detail",
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


]
