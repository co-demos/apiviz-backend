# -*- encoding: utf-8 -*-

from . import version, uuid_models

default_app_styles_config = [

  ### CONFIG DOUBS STYLES

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
          'primary'    : '#0080c8', #'#428bca', # '#28357f',# '#00c0aa', #'#FF9300' , #'#004494', # '#592d7b',
          'info'       : '#4abcc1',
          'success'    : '#80C2BD',
          'warning'    : '#f3bd80',
          'danger'     : '#e8385b',
          'text-color' : '#3D3A39',

          # ### EXTRA COLORS
          # "dark_blue"   : "#40529d",
          # "light_pink"  : "#e89db1",
          # "light_blue"  : "#a3b1d7",
          # "deep_blue"   : "#21295e",
        },
        "app_version" : version,
        "help"        : u"Choose a set of colors (an hexa for example) for your ApiViz instance",
        "apiviz_front_uuid" : uuid_models["uuid_doubs_inclusion"],
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
      #   "apiviz_front_uuid" : uuid_models["uuid_doubs_inclusion"],
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
        "apiviz_front_uuid" : uuid_models["uuid_doubs_inclusion"],
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
        "apiviz_front_uuid" : uuid_models["uuid_doubs_inclusion"],
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
            { "dft_text" : "img_1", "src_image" : "https://raw.githubusercontent.com/multi-coop/apiviz-config-doubs-inclusion/master/logos/LOGO_CD25_colors_rect.jpeg?raw=true", "credits" : "", "licence" : "" },
          #   { "dft_text" : "img_2", "src_image" : "https://raw.githubusercontent.com/co-demos/BFC-ternum/master/illustrations/Formes_logo-4-rect-b.png?raw=true", "credits" : "", "licence" : "" },
          #   { "dft_text" : "img_3", "src_image" : "https://raw.githubusercontent.com/co-demos/BFC-ternum/master/illustrations/Formes_logo-5-rect-b.png?raw=true", "credits" : "", "licence" : "" },
          #   { "dft_text" : "img_4", "src_image" : "https://raw.githubusercontent.com/co-demos/BFC-ternum/master/illustrations/Formes_logo-6-rect-b.png?raw=true", "credits" : "", "licence" : "" },
          ]
        }
      ],

      "apiviz_front_uuid" : uuid_models["uuid_doubs_inclusion"],
      "is_default"  : True
    },



]
