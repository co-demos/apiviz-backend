# -*- encoding: utf-8 -*-

from . import version, uuid_models

### ROUTES / PAGES

default_routes_config = [

  ### - - - - - - - - - - - - - - - - - - -  ### 
  ### CONFIG RHINOCC CARTO 
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
          { "locale" : "fr", "url" : "https://raw.githubusercontent.com/co-demos/rhinocc-carto/master/pages-html/home.html" },
          { "locale" : "en", "url" : "https://raw.githubusercontent.com/co-demos/rhinocc-carto/master/pages-html/home.html" },
          # { "locale" : "fr", "url" : "http://localhost:8800/html/pages-html/home.html" },
          # { "locale" : "en", "url" : "http://localhost:8800/html/pages-html/home.html" }
        ],
        

        "has_ext_script"    : False,
        "ext_script_urls"   : [
          # {"script_id" : "js-car" , "at_mount" : True,  "type" : None,              "url" : "https://cdn.jsdelivr.net/npm/bulma-carousel@4.0.4/dist/js/bulma-carousel.min.js"},
          # {"script_id" : "js-home" , "at_mount" : False, "type" : "text/javascript", "url" : "https://cdn.jsdelivr.net/gh/co-demos/cis-data/scripts/home.js?v2"}
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
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"        : True
      },

    ### - - - - - - - - - - - - - - - - - ###
    ### PAGES : DATASETS --> TO BE ADDED VIA BACK OFFICE BY ADMIN USER
    ### - - - - - - - - - - - - - - - - - ###

      ### PAGE - map
      { "field"             : "rh_carte",
        "is_global_app_homepage" : False,
        "route_title"       : u"Rechercher",
        "route_description" : u"Page de recherche d'Apiviz",
        "route_activated"   : True,
        "banner" : {
          "activated"  : False,
          "banner_uri" : "banner-TL-carto" # TODO
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
        "urls"              : [ "/recherche", "/recherche/carte"],
        
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

          # { "field" : "sd_id",
          #   "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
          #   "is_visible" : True,
          #   "position" : "block_id",
          # },
          { "field" : "rh_id",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_id",
          },

          { "field" : "nom", 
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_title",
          },

          # location
          { "field" : "adresse_full",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_city",
          },

          # contact
          { "field" : "tel_structure",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_phone",
          },
          { "field" : "email_structure",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_email",
          },
          { "field" : "site_internet",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_url",
          },

          # tags
          { "field" : "code_label",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_tags",
            "has_tooltip" : True,
            "is_tag_like" : True,
            "tags_separator" : "-",
            # "text_color" : "white",
            "background_color" : "warning",
            "convert_from_filters" : True, # uses "field" to match with "filter_options.col_name"
          },
          { "field"       : "codes_types_mediations",
            "field_format" : { "trim" : 20, "type" : "object", "retrieve" : [0] },
            "is_visible"  : True,
            "position"    : "block_tags_bis",
            "has_tooltip" : True,
            "is_tag_like" : True,
            "tags_separator" : "-",
            "text_color" : "white",
            "background_color" : "primary",
            "convert_from_filters" : True, # uses "field" to match with "filter_options.col_name"
          },

          # technical
          { "field" : "date_maj",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_tech",
            "custom_title" : [ { "locale" : "fr", "text" : "mise à jour :" } ],
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

          ### center departements w/ 4 deps 
          "center"           : [43.281245, 1.625257],
          "currentCenter"    : [43.281245, 1.625257],
          "zoom"             : 7.3,
          ### center Occitanie 
          # "center"           : [43.5563826, 2.560496],
          # "currentCenter"    : [43.5563826, 2.560496],
          # "zoom"             : 6.5,
          ### center departements w/ data
          # "center"           : [43.487427, 2.383375],
          # "currentCenter"    : [43.487427, 2.383375],
          # "zoom"             : 6.5,
          
          "maxZoom"          : 18,
          "minZoom"          : 2,
          "useMarkerCluster" : True,

          "item_geo_fields"   : { "latitude" : "lat", "longitude": "lon"},
          "item_marker"       : "fas fa-map-marker-alt",
          "item_marker_color" : "info",
          "item_marker_offset" : [ 0, 8 ],
          "item_marker_anchor" : "bottom",

          "pinIconUrl"       : "/static/icons/icon_pin_plein_violet.svg",
          "pinIconSize"      : { "highlighted" : [46, 46], "normal" : [29, 29]},

          "mapbox_layers" : {

            ### all points source and layer
            "all_points_layer" : {
              "is_activated"        : True,
              "source_id"           : "allPointsSource",
              "layer_id"            : "all-points",
              "is_default_visible"  : False,
              "is_source_distant"   : False,

              "is_live_data"        : False,
              "refresh_delay"       : 3000,

              "is_clickable"        : True,
              "add_zoom_on_click"   : 3.5,
              "is_hoverable"        : True,
              "hover_infos"         : {},
              "direct_to_detail"    : False,
              "has_popup"           : True, 
              "popup_config"        : {
                "action" : 'mousemove',
                "fields" : [
                  { 'position' : 'field_main_title', 'field' : 'nom', 'prefix' : None, 'suffix' : None, 'class': 'is-size-6 has-text-weight-semibold' },
                  { 'position' : 'field_info', 'field' : None, 'prefix' : "(cliquez pour + d'infos)", 'suffix' : None, 'class': 'has-text-centered has-text-weight-light' },
                ],
              },

              "radius_min"          : 2,
              "radius_max"          : 15,
              "max_zoom"            : 14,
              "min_zoom"            : 4,
              "circle_color"        : "#e69c75",
              "circle_stroke_color" : "#fff",
              "circle_opacity"      : 0.7,
            },

            ### clusters source and layer
            "cluster_circles_layer" : {
              "is_activated"     : True,
              "source_id"           : "clusterSource",
              "layer_id"            : "cluster-circles",
              "is_default_visible"  : True,

              "is_source_distant"   : False, ### clusters all points sources by default
              "is_clickable"        : True,

              "circle_color"     : "#e69c75", 
              "circle_color_100" : "#e39064", 
              "circle_color_250" : "#e08453", 
              "circle_color_500" : "#c9764a", 
              "circle_color_750" : "#b36942", 

              "circle_radius"     : 15, 
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

              "text_size"    : 11,
              "text_color"   : "#ffffff"
            },

            "cluster_unclustered_layer" : {
              "is_activated"        : True,
              "source_id"           : "clusterSource",
              "layer_id"            : "unclustered-point",
              "is_default_visible"  : True,
              "is_source_distant"   : False,
              "is_clickable"        : True,
              "add_zoom_on_click"   : 3.5,
              "is_hoverable"        : True,
              "hover_infos"         : {},
              "direct_to_detail"    : False,
              "has_popup"           : True, 
              "popup_config"        : {
                "action" : 'mousemove',
                "fields" : [
                  { 'position' : 'field_main_title', 'field' : 'nom', 'prefix' : None, 'suffix' : None, 'class': 'is-size-6 has-text-weight-semibold' },
                  { 'position' : 'field_info', 'field' : None, 'prefix' : "(cliquez pour + d'infos)", 'suffix' : None, 'class': 'has-text-centered has-text-weight-light' },
                ],
              },
              "circle_color"        : "#fff", 
              "circle_stroke_color" : "#e08453",
              "circle_radius"       : 7, 
              "circle_stroke_width" : 3, 
            },

            ### choropleth source and layer
            "choropleth_layer" : {
              "is_activated"        : True,
              # "source_id"           : "choroSource",
              # "layer_id"            : "choropleth",
              "is_live_data"        : False,
              "refresh_delay"       : 3000,

              "is_drawer_open"      : False,

              "is_source_distant"   : True,
              # "distant_source_url" : "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements-version-simplifiee.geojson", 
              # "distant_source_url"  : "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/communes-avec-outre-mer.geojson", 
              
              "change_source_by_zoom" : True,
              "is_clickable"        : False,

              ### list of choropleth sources
              "sources" : [

                { ### FR - departements
                  "is_activated" : True,
                  "source_id" : "chorosource-departements",
                  "layer_id"  : "chorolayer-departements",
                  "is_default_visible" : True,
                  "max_zoom" : 9,
                  "min_zoom" : 0,

                  # "next_layer_id"  : "chorolayer-communes",
                  # "source_url" : "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements-version-simplifiee.geojson", 
                  "source_url" : "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/regions/occitanie/departements-occitanie.geojson", 
                  # "source_url" : "https://raw.githubusercontent.com/co-demos/rhinocc-carto/master/data/datasets_src/departements-occitanie.geojson", 
                  "update_src_from_previous_layer" : False,

                  "need_aggregation" : True,
                  "polygon_prop_id" : "code",
                  # "agregate_data_from_source" : "allPointsSource",
                  "join_polygon_id_to_field"  : "departement",
                  "agregated_data_field"      : "count_dep",
                  # "fill_color"          : "#888888",
                  'fill_color': [
                    'interpolate',
                    ['linear'],
                    ['get', 'count_dep' ],
                    0,  "#fbf2ed",
                    1,  '#6cc3b7',
                    10, '#42b2a3',
                    25, '#18a28f',
                    50, '#158b7b',
                    100, '#10685c',
                    150, '#106268'
                  ],
                  "fill_opacity"        : 0.5,
                  "fill_outline_color"  : "#f2f3f3",

                  "has_popup" : False, 
                  "popup_config" : {
                    "action" : 'mousemove',
                    "fields" : [
                      { 'position' : 'field_title' ,      'field' : 'nom',       'prefix' : None,       'suffix' : None },
                      { 'position' : 'field_title_post' , 'field' : 'code',      'prefix' : ' (',       'suffix' : ')' },
                      { 'position' : 'field_value' ,      'field' : 'count_dep', 'prefix' : 'total : ', 'suffix' : ' lieux' }
                    ],
                  },
                  "legend" : {
                    "position" : "bottom-right", 
                    "title" : "Tiers-lieux / département",
                    "scales" : [
                      { 'value' : '>150 lieux', 'color' : '#106268'},
                      { 'value' : '100 lieux',  'color' : '#10685c'},
                      { 'value' : '50 lieux',  'color' : '#158b7b'},
                      { 'value' : '25 lieux',  'color' : '#18a28f'},
                      { 'value' : '10 lieux',   'color' : '#42b2a3'},
                      { 'value' : '1 lieu',   'color' : '#6cc3b7'},
                      { 'value' : '0 lieu',    'color' : "#fbf2ed"},
                    ]
                  }

                },

                { ### OCCITANIE - EPCI
                  "is_activated" : True,
                  "source_id" : "chorosource-epci",
                  "layer_id"  : "chorolayer-epci",
                  "is_default_visible" : True,
                  "max_zoom" : 12,
                  "min_zoom" : 9,
                  # "next_layer_id"  : "chorolayer-communes",

                  # "properties":
                  #   {
                  #     "code_epci":200035715,
                  #     "ville":"CARCASSONNE CEDEX 9",
                  #     "code_region":76,
                  #     "nom_epci":"CA Carcassonne Agglo",
                  #     "st_perimeter_shape":217557.68644176133,
                  #     "nom_region":"OCCITANIE",
                  #     "geo_point_2d":[43.2274173661,2.42725204977],
                  #     "surface":1093.88288048,
                  #     "nom_dep":"AUDE",
                  #     "st_area_shape":1093882880.4800167,
                  #     "nb_commune":83,
                  #     "densdr":103.16643766,
                  #     "perimetre":217.55768644,
                  #     "adresse1":"1 Rue Pierre Germain",
                  #     "code_dep":11,
                  #     "cp":11890,
                  #     "id":24,
                  #     "pop_dr":112852
                  #   },

                  "source_url" : "https://raw.githubusercontent.com/co-demos/rhinocc-carto/master/data/datasets_src/EPCI_4DPT.geojson", 
                  "update_src_from_previous_layer" : False,
                  "need_aggregation" : False,
                  "polygon_prop_id" : "code_epci",
                  # "agregate_data_from_source" : "allPointsSource",
                  "join_polygon_id_to_field"  : "departement",
                  "agregated_data_field"      : "count_dep",
                  'fill_color': 'transparent',
                  "fill_opacity"        : 0.9,
                  "fill_outline_color"  : "#e69c75",
                  "has_popup" : False, 
                  "popup_config" : {
                    "action" : 'mousemove',
                    "fields" : [
                      { 'position' : 'field_title' ,      'field' : 'nom',       'prefix' : None,       'suffix' : None },
                      { 'position' : 'field_title_post' , 'field' : 'code',      'prefix' : ' (',       'suffix' : ')' },
                      { 'position' : 'field_value' ,      'field' : 'count_dep', 'prefix' : 'total : ', 'suffix' : ' lieux' }
                    ],
                  },
                  "legend" : {
                    "position" : "bottom-right", 
                    "title" : "Tiers-lieux / EPCI",
                    "scales" : [
                      { 'value' : '>150 lieux', 'color' : '#106268'},
                      { 'value' : '100 lieux',  'color' : '#10685c'},
                      { 'value' : '50 lieux',  'color' : '#158b7b'},
                      { 'value' : '25 lieux',  'color' : '#18a28f'},
                      { 'value' : '10 lieux',   'color' : '#42b2a3'},
                      { 'value' : '1 lieu',   'color' : '#6cc3b7'},
                      { 'value' : '0 lieu',    'color' : "#fbf2ed"},
                    ]
                  }
                },
                { ### OCCITANIE - QPV
                  "is_activated" : True,
                  "source_id" : "chorosource-qpv",
                  "layer_id"  : "chorolayer-qpv",
                  "is_default_visible" : True,
                  "max_zoom" : 15,
                  "min_zoom" : 0,
                  # "next_layer_id"  : "chorolayer-communes",

                  # "properties":{
                  #   "objectid":1280,
                  #   "st_length_shape":0,
                  #   "region":"OCCITANIE",
                  #   "geo_point_2d":[43.63572389851926,0.5947729269099461],
                  #   "commune_qp":"Auch",
                  #   "st_area_shape":221287.96815355896,
                  #   "dept":"GERS",
                  #   "code_insee":32013,
                  #   "nom_qp":"Grand Garros",
                  #   "code_qp":"QP032001"
                  # }

                  "source_url" : "https://raw.githubusercontent.com/co-demos/rhinocc-carto/master/data/datasets_src/QPV_4DPT.geojson", 
                  "update_src_from_previous_layer" : False,
                  "need_aggregation" : False,
                  "polygon_prop_id" : "objectid",
                  # "agregate_data_from_source" : "allPointsSource",
                  "join_polygon_id_to_field"  : "departement",
                  "agregated_data_field"      : "count_dep",
                  'fill_color': '#feb24c',
                  # 'fill_color': [
                  #   'interpolate',
                  #   ['linear'],
                  #   ['get', 'count_dep' ],
                  #   0,  "#fbf2ed",
                  #   1,  '#6cc3b7',
                  #   10, '#42b2a3',
                  #   25, '#18a28f',
                  #   50, '#158b7b',
                  #   100, '#10685c',
                  #   150, '#106268'
                  # ],
                  "fill_opacity"        : 0.8,
                  "fill_outline_color"  : "#fd8d3c",
                  "has_popup" : False, 
                  "popup_config" : {
                    "action" : 'mousemove',
                    "fields" : [
                      { 'position' : 'field_title' ,      'field' : 'nom',       'prefix' : None,       'suffix' : None },
                      { 'position' : 'field_title_post' , 'field' : 'code',      'prefix' : ' (',       'suffix' : ')' },
                      { 'position' : 'field_value' ,      'field' : 'count_dep', 'prefix' : 'total : ', 'suffix' : ' lieux' }
                    ],
                  },
                  "legend" : {
                    "position" : "bottom-right", 
                    "title" : "Tiers-lieux / EPCI",
                    "scales" : [
                      { 'value' : '>150 lieux', 'color' : '#106268'},
                      { 'value' : '100 lieux',  'color' : '#10685c'},
                      { 'value' : '50 lieux',  'color' : '#158b7b'},
                      { 'value' : '25 lieux',  'color' : '#18a28f'},
                      { 'value' : '10 lieux',   'color' : '#42b2a3'},
                      { 'value' : '1 lieu',   'color' : '#6cc3b7'},
                      { 'value' : '0 lieu',    'color' : "#fbf2ed"},
                    ]
                  }
                },
                { ### OCCITANIE - 4DPT
                  "is_activated" : False,
                  "source_id" : "chorosource-4DPT",
                  "layer_id"  : "chorolayer-4DPT",
                  "is_default_visible" : False,
                  "max_zoom" : 9,
                  "min_zoom" : 0,
                  # "next_layer_id"  : "chorolayer-communes",
                  "source_url" : "https://raw.githubusercontent.com/co-demos/rhinocc-carto/master/data/datasets_src/4DPT_RhinOcc.geojson", 
                  "update_src_from_previous_layer" : False,
                  "need_aggregation" : False,
                  "polygon_prop_id" : "code",
                  # "agregate_data_from_source" : "allPointsSource",
                  "join_polygon_id_to_field"  : "departement",
                  "agregated_data_field"      : "count_dep",
                  # "fill_color"          : "#888888",
                  'fill_color': [
                    'interpolate',
                    ['linear'],
                    ['get', 'count_dep' ],
                    0,  "#fbf2ed",
                    1,  '#6cc3b7',
                    10, '#42b2a3',
                    25, '#18a28f',
                    50, '#158b7b',
                    100, '#10685c',
                    150, '#106268'
                  ],
                  "fill_opacity"        : 0.5,
                  "fill_outline_color"  : "#f2f3f3",
                  "has_popup" : False, 
                  "popup_config" : {
                    "action" : 'mousemove',
                    "fields" : [
                      { 'position' : 'field_title' ,      'field' : 'nom',       'prefix' : None,       'suffix' : None },
                      { 'position' : 'field_title_post' , 'field' : 'code',      'prefix' : ' (',       'suffix' : ')' },
                      { 'position' : 'field_value' ,      'field' : 'count_dep', 'prefix' : 'total : ', 'suffix' : ' lieux' }
                    ],
                  },
                  "legend" : {
                    "position" : "bottom-right", 
                    "title" : "Tiers-lieux / 4DPT",
                    "scales" : [
                      { 'value' : '>150 lieux', 'color' : '#106268'},
                      { 'value' : '100 lieux',  'color' : '#10685c'},
                      { 'value' : '50 lieux',  'color' : '#158b7b'},
                      { 'value' : '25 lieux',  'color' : '#18a28f'},
                      { 'value' : '10 lieux',   'color' : '#42b2a3'},
                      { 'value' : '1 lieu',   'color' : '#6cc3b7'},
                      { 'value' : '0 lieu',    'color' : "#fbf2ed"},
                    ]
                  }
                },


                { ### FR - communes
                  "is_activated" : False,
                  "source_id" : "chorosource-communes",
                  "layer_id"  : "chorolayer-communes",
                  "is_default_visible" : True,
                  "max_zoom" : 18,
                  "min_zoom" : 8,

                  # "next_layer_id"  : "chorolayer-cadaste",
                  "source_url" : "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/communes-avec-outre-mer.geojson", 
                  "update_src_from_previous_source" : True,
                  "update_src_options" : [ 
                    { 
                      "url_base" : "https://geo.api.gouv.fr/departements/<dep_code>/communes?geometry=contour&format=geojson&type=commune-actuelle", 
                      "response_format" : "geojson",
                      "upper_load_method" : "zoom",
                      "upper_load_feat" : "only_center",
                      "upper_main_matching_prop" : "code",
                      "upper_source_id" : "chorosource-departements", 
                      "upper_layer_id" : "chorolayer-departements", 
                      "slugs_map" : [
                        {
                          "value_property" : "code", ### field in property to retrieve
                          "value_slug_code" : "dep_code" , 
                        }
                      ],
                    },
                  ],

                  "need_aggregation" : True,
                  "polygon_prop_id" : "code",
                  # "agregate_data_from_source" : "allPointsSource",
                  "join_polygon_id_to_field"  : "INSEECOM",
                  "agregated_data_field"      : "count_com",
                  # "fill_color"          : "#888888",
                  'fill_color': [
                    'interpolate',
                    ['linear'],
                    ['get', 'count_com' ],
                    0,  "#888888",
                    1,  '#EED322',
                    2,  '#DA9C20',
                    5,  '#B86B25',
                    7,  '#8B4225',
                    10, '#723122'
                  ],
                  "fill_opacity"        : 0.5,
                  "fill_outline_color"  : "rgb(256,256,256)",
                  "has_popup" : True, 
                  "popup_config" : {
                    "action" : 'mousemove',
                    "fields" : [
                      { 'position' : 'field_title' ,      'field' : 'nom',       'prefix' : None,       'suffix' : None },
                      { 'position' : 'field_title_post' , 'field' : 'code',      'prefix' : ' (',       'suffix' : ')' },
                      { 'position' : 'field_value' ,      'field' : 'count_com', 'prefix' : 'total : ', 'suffix' : ' lieux' }
                    ],
                  },
                  "legend" : {
                    "position" : "bottom-right", 
                    "title" : "Tiers-lieux / communes",
                    "scales" : [
                      { 'value' : '>10 lieux', 'color' : '#723122'},
                      { 'value' : '7 lieux',   'color' : '#8B4225'},
                      { 'value' : '5 lieux',   'color' : '#B86B25'},
                      { 'value' : '2 lieux',   'color' : '#DA9C20'},
                      { 'value' : '1 lieu',    'color' : '#EED322'},
                      { 'value' : '0 lieu',    'color' : "#888888"},
                    ]
                  }
                },

              ],

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
              "radius_min"          : 6,
              "radius_max"          : 25,
            },

          },
        
          "layers_visibility" :{
            "is_activated" : True,
            "is_drawer_open" : False,
            "layers_switches" : [ 
              { "label" : "lieux",         "layers" : [ "all-points" ], "default_visible" : False }, 
              { "label" : "ensembles" ,    "layers" : [ "cluster-circles", "cluster-counts", "unclustered-point" ], "default_visible" : True }, 
              { "label" : "départements" , "layers" : [ "chorolayer-departements" ], "default_visible" : True }, 
              { "label" : "EPCI" ,         "layers" : [ "chorolayer-epci" ], "default_visible" : True }, 
              { "label" : "QPV" ,          "layers" : [ "chorolayer-qpv" ], "default_visible" : True }, 
              { "label" : "heatmap" ,       "layers" : [ "heatmap-layer" ], "default_visible" : False }
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
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"      : True
      },

      ### PAGE - table
      { "field"             : "rh_table",
        "is_global_app_homepage" : False,
        "route_title"       : u"Rechercher",
        "route_description" : u"Page de recherche du CIS",
        "route_activated"   : True,
        "has_shuffle"       : True,
        "shuffle_minnmax"   : { "min": 0, "max":  2000 },
        "banner" : {
          "activated"  : False,
          "banner_uri" : "banner-TL-carto"
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
        "urls"              : ["/recherche/table"],
        # "template_url"      : "/static/spa.html",
        "template_urls"     : [
        ],
        
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Table search route in french",
        "is_dynamic"        : True,
        "dataset_uri"       : "recherche",
        "dynamic_template"  : 'DynamicTable',
        "endpoint_type"     : "table",
        "pagination"        : {
          "is_visible" : True,
          "position" : "top_and_bottom",
          "feedback" : "bottom"
        },

        "table_options" : {
          "has_link_col" : True,
        },

        "contents_fields"  : [

          # { "field" : "sd_id",
          #   "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
          #   "is_visible" : False,
          #   "is_id_field" : True,
          #   "position" : "col_id",
          # },
          { "field" : "rh_id",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : False,
            "is_id_field" : True,
            "position" : "col_id",
          },
          { "field" : "nom",
            "field_format" : { "trim" : 50, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "has_link_to_detail" : True,
            "is_table_head" : True,
            "position" : "col_1",
            "is_sortable" : True,
          },
          { "field" : "ville",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "col_2",
            "is_sortable" : True,
          },
          { "field" : "code_postal",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "col_3",
            "is_sortable" : True,
          },
          { "field" : "departement",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "col_3",
            "is_sortable" : True,
          },
          { "field" : "adresse",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "col_4",
            "is_sortable" : False,
          },

          # { "field"       : "code_mediations",
          #   "field_format" : { "trim" : 20, "type" : "object", "retrieve" : [0] },
          #   "is_visible"  : True,
          #   "position"    : "col_3",
          #   "is_sortable" : False,
          #   "custom_title" : [ { "locale" : "fr", "text" : "activités" }],
          #   "is_tag_like" : True,
          #   "tags_separator" : "-",
          #   "text_color" : "white",
          #   "background_color" : "primary",
          #   "convert_from_filters" : True, # uses "field" to match with "filter_options.col_name"
          # },

          # { "field"       : "SOURCE_codes",
          #   "field_format" : { "trim" : 20, "type" : "object", "retrieve" : [0] },
          #   "is_visible"  : True,
          #   "position"    : "col_4",
          #   "is_sortable" : False,
          #   "custom_title" : [ { "locale" : "fr", "text" : "SOURCE" }],
          #   "is_tag_like" : True,
          #   "tags_separator" : "-",
          #   "text_color" : "white",
          #   "background_color" : "primary",
          #   "convert_from_filters" : True, # uses "field" to match with "filter_options.col_name"
          # },

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

          # "block_contents_links" : {
          # "is_visible"  : False,
          # "position"    : "block_bottom_1",
          # "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
          # "links"       : []
          # },

          # "block_data_infos" : {
          # "is_visible"  : False,
          # "position"    : "block_bottom_2",
          # "title_block" : [{"locale" : "en", "text" : "todo"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "", "is_visible" : False}],
          # "links"       : []
          # },

          # "block_share" : {
          # "is_visible"  : False,
          # "position"    : "block_bottom_3",
          # "title_block" : [{"locale" : "en", "text" : "share this place"},{"locale" : "es", "text" : "pendiente"},{"locale" : "tr", "text" : "yapılmamış"},{"locale" : "de", "text" : "ungemacht"}, {"locale" : "fr", "text" : "Partagez ce lieu", "is_visible" : False}],
          # "links"       : []
          # },

        },

        "has_navbar"        : True,
        "has_footer"        : True,
        "has_tabs"          : False,
        "tabs_uri"          : "TL-tabs",
        "deactivate_btn"    : False,
        "is_visible"        : True,
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"        : True
      },

      ### PAGE - list
      { "field"             : "rh_liste",
        "is_global_app_homepage" : False,
        "route_title"       : u"Rechercher",
        "route_description" : u"Page de recherche du CIS",
        "route_activated"   : True,
        "has_shuffle"       : True,
        "shuffle_minnmax"   : { "min": 0, "max":  4000 },
        "banner" : {
          "activated"  : False,
          "banner_uri" : "banner-TL-carto"
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
        "urls"              : ["/recherche/liste"],
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
        "pagination"        : {
          "is_visible" : True,
          "position" : "top_and_bottom",
          "feedback" : "top_and_bottom"
        },

        "contents_fields"  : [

          # { "field" : "sd_id",
          #   "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
          #   "is_visible" : True,
          #   "position" : "block_id",
          # },
          { "field" : "rh_id",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_id",
          },
          # { "field" : "url_illustration",
          #   "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
          #   "is_visible" : True,
          #   "position" : "block_image",
          # },
          { "field" : "nom",
            "field_format" : { "trim" : 50, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_title",
          },

          # location
          { "field" : "ville",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_city",
          },

          # contact
          { "field" : "tel_structure",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_phone",
          },
          { "field" : "email_structure",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_email",
          },
          { "field" : "site_internet",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_url",
          },

          # tags
          { "field" : "code_label",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_tags",
            "has_tooltip" : True,
            "is_tag_like" : True,
            "tags_separator" : "-",
            # "text_color" : "white",
            "background_color" : "warning",
            "convert_from_filters" : True, # uses "field" to match with "filter_options.col_name"
          },
          { "field"       : "codes_types_mediations",
            "field_format" : { "trim" : 40, "type" : "object", "retrieve" : [0] },
            "is_visible"  : True,
            "position"    : "block_tags_bis",
            "has_tooltip" : True,
            "is_tag_like" : True,
            "tags_separator" : "-",
            "text_color" : "white",
            "background_color" : "primary",
            "convert_from_filters" : True, # uses "field" to match with "filter_options.col_name"
          },

          # technical
          { "field" : "date_maj",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_tech",
            "custom_title" : [ { "locale" : "fr", "text" : "mise à jour :" } ],
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
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"        : True
      },

      ### PAGE - detail
      { "field"             : "rh_detail",
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

          { "field" : "nom", 
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_title",
          },
          { "field" : "nature_juridique",
            "custom_title" : [ { "locale" : "fr", "text" : "Nature juridique :" } ],
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_abstract",
          },

          ### minimap
          { "field" : None,
            "is_visible" : True,
            "map_height" : 250,
            "item_title_field" : "nom",
            "position" : "block_map_top_right_bis",
            "item_geo_fields" : { "latitude" : "lat", "longitude": "lon"},
            "item_marker" : "fas fa-map-marker-alt",
            "item_marker_color" : "danger",
            "item_marker_offset" : [ 0, 8 ],
            "item_marker_anchor" : "bottom",
            "zoom" : 10,
            "max_zoom" : 13,
            "min_zoom" : 4,
            "interactive" : False,
            "max_bounds" : { "latitude" : "lat", "longitude": "lon"},
          },


          # { "field" : "url_illustration",
          #   "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
          #   "is_visible" : True,
          #   "position" : "block_image",
          # },
          { "field" : "adresse_full",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_address",
          },
          { "field" : "ville",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_city",
          },
          { "field" : "code_postal",
            "field_format" : { "trim" : None, "type" : "list", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_cp",
          },

          ### mediation
          { "field" : "bloc_mediations",
            "custom_title" : [ { "locale" : "fr", "text" : "Activités d'inclusion numérique" } ],
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_left_open_infos",
          },
          # { "field" : "bloc_mediation_2",
          #   # "custom_title" : [ { "locale" : "fr", "text" : "Activité 2 :" } ],
          #   "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
          #   "is_visible" : True,
          #   "position" : "block_left_open_infos_2",
          # },
          # { "field" : "bloc_mediation_3",
          #   # "custom_title" : [ { "locale" : "fr", "text" : "Activité 3 :" } ],
          #   "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
          #   "is_visible" : True,
          #   "position" : "block_left_open_infos_3",
          # },
          # { "field" : "bloc_mediation_4",
          #   # "custom_title" : [ { "locale" : "fr", "text" : "Activité 4 :" } ],
          #   "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
          #   "is_visible" : True,
          #   "position" : "block_left_open_infos_4",
          # },
          # { "field" : "bloc_mediation_5",
          #   # "custom_title" : [ { "locale" : "fr", "text" : "Activité 5 :" } ],
          #   "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
          #   "is_visible" : True,
          #   "position" : "block_left_open_infos_5",
          # },

          ### block contact
          { "field" : "tel_structure",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_contact_tel",
          },
          { "field" : "email_structure",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_contact_email",
            "text_color" : "white",
            "background_color" : "primary",
          },
          { "field" : "site_internet",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_contact_website",
          },

          { "field" : "horaires_semaine",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_open_infos",
          },

          # technical
          { "field" : "n_ref",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_right_top_tech",
            "background_color" : "link",
            "custom_title" : [ { "locale" : "fr", "text" : "numéro de référence :" } ],
          },
          { "field" : "date_maj",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_right_top_tech_2",
            "custom_title" : [ { "locale" : "fr", "text" : "mise à jour :" } ],
          },

          ### block tags
          { "field" : "code_label",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible" : True,
            "position" : "block_rb1_tags",
            "has_tooltip" : False,
            "is_tag_like" : True,
            "tags_separator" : "-",
            # "text_color" : "white",
            "background_color" : "warning",
            "custom_title" : [ { "locale" : "fr", "text" : "Label :" } ],
            "convert_from_filters" : True, # uses "field" to match with "filter_options.col_name"
          },
          { "field"       : "codes_types_mediations",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible"  : True,
            "position"    : "block_rb2_tags",
            "has_tooltip" : False,
            "is_tag_like" : True,
            "tags_separator" : "-",
            "text_color" : "white",
            "background_color" : "primary",
            "custom_title" : [ { "locale" : "fr", "text" : "Activité(s) :" } ],
            "convert_from_filters" : True, # uses "field" to match with "filter_options.col_name"
          },
          { "field"       : "codes_publics",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible"  : True,
            "position"    : "block_rb3_tags",
            "has_tooltip" : False,
            "is_tag_like" : True,
            "tags_separator" : "-",
            "text_color" : "white",
            "background_color" : "danger",
            "custom_title" : [ { "locale" : "fr", "text" : "Public(s) :" } ],
            "convert_from_filters" : True, # uses "field" to match with "filter_options.col_name"
          },
          { "field"       : "codes_thematiques",
            "field_format" : { "trim" : None, "type" : "object", "retrieve" : [0] },
            "is_visible"  : True,
            "position"    : "block_rb4_tags",
            "has_tooltip" : False,
            "is_tag_like" : True,
            "tags_separator" : "-",
            "text_color" : "white",
            "background_color" : "link-hover",
            "custom_title" : [ { "locale" : "fr", "text" : "Thématique(s) :" } ],
            "convert_from_filters" : True, # uses "field" to match with "filter_options.col_name"
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
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"        : True
      },

      ## PAGE - stats
      { "field"             : "rh_stats",
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
            "serie_id" : "tl-stat-bar-horiz",
            "is_activated" : True,
            "chart_type": "bar", 
            "help" : "bar horiz + stacked example",
            "position": 1,
            "col_size" : 12,
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

                "add_missing_values" : False,
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

                "need_labels_remap" : False,
                "need_labels_rename" : False,
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
                "toolbar" : {
                  "show" : True,
                },
                # "stackType": '100%'
              },
              "plotOptions": {
                "bar": {
                  "horizontal": True,
                }
              },
              "theme" : {
                "palette" : "palette8", ### cf : https://apexcharts.com/docs/options/theme/#palette
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
                "text": "Typologies / Régions"
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
                # "categories": [
                #   "EDUCATION",
                #   "EMPLOI",
                #   "ENVIRONNEMENT",
                #   "SANTE",
                #   "SOLIDARITE",
                #   "TERRITOIRE",
                #   "ARTS",
                #   "COMMUNICATION",
                #   "CONSOMMATION",
                #   "DEMOCRATIE",
                #   "GOUVERNANCE",
                #   "NUMERIQUE",
                #   "SPORT",
                #   "TOURISME",
                #   "FINANCE",
                #   "PATRIMOINE",
                # ],
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
            },

            "chart_texts": {
              "is_activated" : True,
              "inner_col_size" : 3,
              "placement" : "left",
              "text_title" : [
                {"locale" : "en", "text" : "Title h-chart"},
                {"locale" : "es", "text" : "pendiente"},
                {"locale" : "tr", "text" : "yapılmamış"},
                {"locale" : "de", "text" : "ungemacht"}, 
                {"locale" : "fr", "text" : "Titre h-chart" }
              ],
              "text_content_a" : [
                {"locale" : "en", "text" : "Text test h-chart"},
                {"locale" : "es", "text" : "pendiente"},
                {"locale" : "tr", "text" : "yapılmamış"},
                {"locale" : "de", "text" : "ungemacht"}, 
                {"locale" : "fr", "text" : "Test texte h-chart" }
              ]
            }
          },

          { ### DOUGHNUT - SETTINGS EXAMPLE
            "serie_id" : "tl-stat-donut",
            "is_activated" : True,
            "chart_type": "donut", 
            "position": 0,
            "col_size" : 12,
            "height": "250px",
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
                "text": "Typologies (%)",
              },
              "chart": {
                "toolbar" : {
                  "show" : True,
                },
                # "stackType": '100%'
              },
              "theme" : {
                "palette" : "palette8", ### cf : https://apexcharts.com/docs/options/theme/#palette 
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

            "chart_texts": {
              "is_activated" : True,
              "inner_col_size" : 5,
              "placement" : "right",
              "text_title" : [
                {"locale" : "en", "text" : "Title donut"},
                {"locale" : "es", "text" : "pendiente"},
                {"locale" : "tr", "text" : "yapılmamış"},
                {"locale" : "de", "text" : "ungemacht"}, 
                {"locale" : "fr", "text" : "Titre donut" }
              ],
              "text_content_a" : [
                {"locale" : "en", "text" : "Text test donut"},
                {"locale" : "es", "text" : "pendiente"},
                {"locale" : "tr", "text" : "yapılmamış"},
                {"locale" : "de", "text" : "ungemacht"}, 
                {"locale" : "fr", "text" : "Test texte donut" }
              ]
            }

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
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"        : True
      },

    ### - - - - - - - - - - - - - - - - - ###
    ### CUSTOM ROUTES-PAGES --> TO BE ADDED VIA BACK OFFICE BY ADMIN USER
    ### - - - - - - - - - - - - - - - - - ###

      ### PAGE - DEMARCHE
      { "field"             : "rh_demarche",
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
        "urls"              : ["/la-demarche"],
        "dataset_uri"       : "project-cis",
        
        "template_urls"     : [
          { "locale" : "fr", "url" : "https://raw.githubusercontent.com/co-demos/rhinocc-carto/master/pages-html/la-demarche.html" },
          { "locale" : "en", "url" : "https://raw.githubusercontent.com/co-demos/rhinocc-carto/master/pages-html/la-demarche.html" },
          # { "locale" : "fr", "url" : "http://localhost:8800/html/pages-html/la-demarche.html" },
          # { "locale" : "en", "url" : "http://localhost:8800/html/pages-html/la-demarche.html" }
        ],
        

        "has_ext_script"    : False,
        "ext_script_urls"   : [
          # {"script_id" : "js-car"    , "at_mount" : True,  "type" : None, "url" : "https://cdn.jsdelivr.net/npm/bulma-carousel@4.0.4/dist/js/bulma-carousel.min.js"},s
          # {"script_id" : "js-project", "at_mount" : False, "type" : None, "url" : "http://localhost:8800/statics/scripts/le-projet.js?v4"},
          # {"script_id" : "js-project", "at_mount" : False, "type" : None, "url" : "https://cdn.jsdelivr.net/gh/co-demos/cget-tiers-lieux/scripts/le-projet.js"},
        ],

        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main demarche route",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,

        "has_tabs"          : True,
        "tabs_uri"          : "tabs-rh-test",

        "has_footer"        : True,
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"        : True
      },

      ### PAGE - DONNEES
      { "field"             : "rh_donnees",
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
        "urls"              : ["/les-donnees"],
        "dataset_uri"       : "project-cis",
        
        "template_urls"     : [
          { "locale" : "fr", "url" : "https://raw.githubusercontent.com/co-demos/rhinocc-carto/master/pages-html/les-donnees.html" },
          { "locale" : "en", "url" : "https://raw.githubusercontent.com/co-demos/rhinocc-carto/master/pages-html/les-donnees.html" },
          # { "locale" : "fr", "url" : "http://localhost:8800/html/pages-html/les-donnees.html" },
          # { "locale" : "en", "url" : "http://localhost:8800/html/pages-html/les-donnees.html" }
        ],
        

        "has_ext_script"    : False,
        "ext_script_urls"   : [
          # {"script_id" : "js-car"    , "at_mount" : True,  "type" : None, "url" : "https://cdn.jsdelivr.net/npm/bulma-carousel@4.0.4/dist/js/bulma-carousel.min.js"},s
          # {"script_id" : "js-project", "at_mount" : False, "type" : None, "url" : "http://localhost:8800/statics/scripts/le-projet.js?v4"},
          # {"script_id" : "js-project", "at_mount" : False, "type" : None, "url" : "https://cdn.jsdelivr.net/gh/co-demos/cget-tiers-lieux/scripts/le-projet.js"},
        ],

        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main donnees route",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,

        "has_tabs"          : False,
        "tabs_uri"          : "tabs-rh-test",

        "has_footer"        : True,
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"        : True
      },

      ### PAGE - CONTRIBUER
      { "field"             : "rh_contribuer",
        "is_global_app_homepage" : True,
        "route_title"       : u"Home",
        "route_description" : u"apiviz default home page",
        "route_activated"   : False,
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
        "urls"              : ["/contribuer"],
        "dataset_uri"       : None,

        "template_urls"     : [
          { "locale" : "fr", "url" : "https://raw.githubusercontent.com/co-demos/rhinocc-carto/master/pages-html/contribuer.html" },
          { "locale" : "en", "url" : "https://raw.githubusercontent.com/co-demos/rhinocc-carto/master/pages-html/contribuer.html" },
          # { "locale" : "fr", "url" : "http://localhost:8800/html/pages-html/contribuer.html" },
          # { "locale" : "en", "url" : "http://localhost:8800/html/pages-html/contribuer.html" }
        ],

        "has_ext_script"    : True,
        "ext_script_urls"   : [
          {"script_id" : "js-car"    , "at_mount" : True,  "type" : None, "url" : "https://cdn.jsdelivr.net/npm/bulma-carousel@4.0.4/dist/js/bulma-carousel.min.js"},

          # {"script_id" : "js-project", "at_mount" : False, "type" : None, "url" : "http://localhost:8800/statics/scripts/le-projet.js?v4"},
          {"script_id" : "js-project", "at_mount" : False, "type" : None, "url" : "https://cdn.jsdelivr.net/gh/co-demos/cget-tiers-lieux/scripts/le-projet.js"},
        ],

        # "has_carousel"      : True,
        "help"              : u"you can specify a remote template (f.e. a github url)",
        "languages"         : ["fr"],
        "app_version"       : version,
        "comment"           : u"Main demarche route",
        "is_dynamic"        : True,
        "dynamic_template"  : "DynamicStatic",
        "has_navbar"        : True,

        "has_tabs"          : True,
        "tabs_uri"          : "tabs-rh-test",

        "has_footer"        : True,
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"        : True
      },

      ### PAGE : PROJECT/TOOLS
      { "field"             : "rh_tools",
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
        "urls"              : ["/outils"],
        
        "template_urls"     : [
          { "locale" : "fr", "url" : "https://raw.githubusercontent.com/co-demos/apiviz-website-demo/master/pages-html/les-outils.html" },
          { "locale" : "en", "url" : "https://raw.githubusercontent.com/co-demos/apiviz-website-demo/master/pages-html/les-outils-en.html" },
          # { "locale" : "fr", "url" : "http://localhost:8800/html/pages-html/les-outils.html" }, 
          # { "locale" : "en", "url" : "http://localhost:8800/html/pages-html/les-outils-en.html" }, 
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
        "tabs_uri"          : "tabs-rh-test",
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"        : True
      },

      ### PAGE : LEGAL 
      { "field"             : "rh_legal",
        "is_global_app_homepage" : True,
        "route_title"       : u"Mentions légales",
        "route_description" : u"apiviz default legal page",
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
        "urls"              : ["/mentions-legales"],
        
        "template_urls"     : [
          { "locale" : "fr", "url" : "https://raw.githubusercontent.com/co-demos/rhinocc-carto/master/pages-html/mentions-legales-fr.html" },
          { "locale" : "en", "url" : "https://raw.githubusercontent.com/co-demos/rhinocc-carto/master/pages-html/mentions-legales-fr.html" },
          # { "locale" : "fr", "url" : "http://localhost:8800/html/pages-html/mentions-legales-fr.html" },
          # { "locale" : "en", "url" : "http://localhost:8800/html/pages-html/mentions-legales-fr.html" }
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
        "tabs_uri"          : "tabs-rh-test",
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
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
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
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
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
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
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
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
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
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
        "apiviz_front_uuid" : uuid_models["uuid_rhinocc_carto"],
        "is_default"        : True
      },


]
