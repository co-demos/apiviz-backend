# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_app_styles_config = [

  ### CONFIG PING CARTO STYLES

    ### GLOBAL STYLES
      { "field"       : "app_colors",

        ### COLOR INPUTS AS HEXA
        "content"     : {

          ### DEFAULTS
          "navbar-border-color"       : '#3D3A39' , #'#004494', # '#592d7b',
          "default_background_app"    : "#fafafa",
          "default_background_navbar" : "#ffffff",

          ### SIMILI - BULMA
          'light'      : '#40529d',
          'dark'       : '#1b1b1b',
          'link'       : '#4b4d58',
          'link-hover' : '#FF9300' , #'#004494', # '#592d7b',
          'primary'    : '#400' , # '#00c0aa', #'#FF9300' , #'#004494', # '#592d7b',
          'info'       : '#40529d',
          'success'    : '#80C2BD',
          'warning'    : '#f3bd80',
          'danger'     : '#d24745',
          'text-color' : '#3D3A39',

          # ### EXTRA COLORS
          # "dark_blue"   : "#40529d",
          # "light_pink"  : "#e89db1",
          # "light_blue"  : "#a3b1d7",
          # "deep_blue"   : "#21295e",
        },
        "app_version" : version,
        "help"        : u"Choose a set of colors (an hexa for example) for your ApiViz instance",
        "apiviz_front_uuid" : uuid_models["uuid_ocf"],
        "is_default"  : True
      },

      # { "field"       : "app_typo_colors",
      #   "content"     : {

      #     "default_dark"       : "#000000",
      #     "default_light_dark" : "#3D3A39",
      #     "default_invert"     : "#ffffff",

      #     ### SIMILI - BULMA
      #     'light'      : '#40529d',
      #     'dark'       : '#1b1b1b',
      #     'link'       : '#21295e',
      #     'link-hover' : '#592d7b',
      #     'primary'    : '#592d7b',
      #     'info'       : '#40529d',
      #     'success'    : '#80C2BD',
      #     'warning'    : '#f3bd80',
      #     'danger'     : '#d24745',
      #     'text-color' : '#3D3A39',
      #     ### EXTRA COLORS
      #     "dark_blue"   : "#40529d",
      #     "light_pink"  : "#e89db1",
      #     "light_blue"  : "#a3b1d7",
      #     "deep_blue"   : "#21295e",
      #   },
      #   "app_version" : version,
      #   "help"        : u"Choose a set of colors for your typo for your ApiViz instance",
      #   "apiviz_front_uuid" : uuid_models["uuid_ocf"],
      #   "is_default"  : True
      # },

      { "field"       : "app_typo",
        "content"     : {
          "titles" : u"BonvenoCF-Light", # TODO: replace with Barow
          "textes" : u"NEXA SANS",
        },
        "url"         : "",
        "app_version" : version,
        "help"        : u"Choose a typo for your ApiViz instance",
        "apiviz_front_uuid" : uuid_models["uuid_ocf"],
        "is_default"  : True
      },

    ### BANNERS SET
      { "field"       : "app_banners",
        "locale"      : "fr",
        "app_version" : version,
        "help"        : u"The dataset banners for your ApiViz instance (between navbar and filter)",
        "banners_set" : [
          {
            "banner_uri"       : "apiviz_default",
            "dataset_uri"      : None,
            "template_url"     : "",
            "is_dynamic"       : False,
            "dynamic_template" : 'DynamicBanner',
            "is_visible"          : False,
            "is_dismisible"       : True,
            "is_disapearing"      : False,
            "disapearing_timeout" : 5, ## in seconds
          },
          {
            "banner_uri"       : "banner-cis-carto",
            "dataset_uri"      : "cis-carto",
            "template_url"     : "",
            "is_dynamic"       : False,
            "dynamic_template" : 'DynamicBanner',
            "is_visible"          : False,
            "is_dismisible"       : True,
            "is_disapearing"      : False,
            "disapearing_timeout" : 5, ## in seconds
          },
          {
            "banner_uri"       : "banner-cis-xp",
            "dataset_uri"      : "cis-xp",
            "template_url"     : "",
            "is_dynamic"       : False,
            "dynamic_template" : 'DynamicBanner',
            "is_visible"          : False,
            "is_dismisible"       : True,
            "is_disapearing"      : False,
            "disapearing_timeout" : 5, ## in seconds
          },
        ],
        "apiviz_front_uuid" : uuid_models["uuid_ocf"],
        "is_default"     : True
      },


    ### DEFAULT IMAGES FOR DATASETS SEARCH
    { "field"       : "app_search_default_images_sets",
      "app_version" : version,
      "help"        : u"The default images sets for the cards for each dataset",

      "images_sets" : [
        {
          "dataset_uri" : "recherche",
          "images_set"  : [
            { "dft_text" : "img_1", "src_image" : "https://raw.githubusercontent.com/co-demos/cis-data/master/illustrations/textures/medium_fiche_1.png?raw=true", "credits" : "Élise Lalique", "licence" : "" },
            { "dft_text" : "img_2", "src_image" : "https://raw.githubusercontent.com/co-demos/cis-data/master/illustrations/textures/medium_fiche_2.png?r:aw=true", "credits" : "Élise Lalique", "licence" : "" },
            { "dft_text" : "img_3", "src_image" : "https://raw.githubusercontent.com/co-demos/cis-data/master/illustrations/textures/medium_fiche_3.png?raw=true", "credits" : "Élise Lalique", "licence" : "" },
            { "dft_text" : "img_4", "src_image" : "https://raw.githubusercontent.com/co-demos/cis-data/master/illustrations/textures/medium_fiche_4.png?raw=true", "credits" : "Élise Lalique", "licence" : "" },
            { "dft_text" : "img_5", "src_image" : "https://raw.githubusercontent.com/co-demos/cis-data/master/illustrations/textures/medium_fiche_5.png?raw=true", "credits" : "Élise Lalique", "licence" : "" },
            { "dft_text" : "img_6", "src_image" : "https://raw.githubusercontent.com/co-demos/cis-data/master/illustrations/textures/medium_fiche_6.png?raw=true", "credits" : "Élise Lalique", "licence" : "" },
            { "dft_text" : "img_7", "src_image" : "https://raw.githubusercontent.com/co-demos/cis-data/master/illustrations/textures/medium_fiche_7.png?raw=true", "credits" : "Élise Lalique", "licence" : "" },
            { "dft_text" : "img_8", "src_image" : "https://raw.githubusercontent.com/co-demos/cis-data/master/illustrations/textures/medium_fiche_8.png?raw=true", "credits" : "Élise Lalique", "licence" : "" },
            { "dft_text" : "img_9", "src_image" : "https://raw.githubusercontent.com/co-demos/cis-data/master/illustrations/textures/medium_fiche_9.png?raw=true", "credits" : "Élise Lalique", "licence" : "" },
            { "dft_text" : "img_10", "src_image" : "https://raw.githubusercontent.com/co-demos/cis-data/master/illustrations/textures/medium_fiche_10.png?raw=true", "credits" : "Élise Lalique", "licence" : "" },
            { "dft_text" : "img_11", "src_image" : "https://raw.githubusercontent.com/co-demos/cis-data/master/illustrations/textures/medium_fiche_11.png?raw=true", "credits" : "Élise Lalique", "licence" : "" },
            { "dft_text" : "img_12", "src_image" : "https://raw.githubusercontent.com/co-demos/cis-data/master/illustrations/textures/medium_fiche_12.png?raw=true", "credits" : "Élise Lalique", "licence" : "" },
            { "dft_text" : "img_13", "src_image" : "https://raw.githubusercontent.com/co-demos/cis-data/master/illustrations/textures/medium_fiche_13.png?raw=true", "credits" : "Élise Lalique", "licence" : "" },
            { "dft_text" : "img_14", "src_image" : "https://raw.githubusercontent.com/co-demos/cis-data/master/illustrations/textures/medium_fiche_14.png?raw=true", "credits" : "Élise Lalique", "licence" : "" },
            { "dft_text" : "img_15", "src_image" : "https://raw.githubusercontent.com/co-demos/cis-data/master/illustrations/textures/medium_fiche_15.png?raw=true", "credits" : "Élise Lalique", "licence" : "" },
            { "dft_text" : "img_16", "src_image" : "https://raw.githubusercontent.com/co-demos/cis-data/master/illustrations/textures/medium_fiche_16.png?raw=true", "credits" : "Élise Lalique", "licence" : "" },
          ]
        }
      ],

      "apiviz_front_uuid" : uuid_models["uuid_ocf"],
      "is_default"  : True
    },



]
