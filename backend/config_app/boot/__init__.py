from .. import version, uuid_models, config_folders

default_global_config = []
default_app_navbar = []
default_app_tabs = []
default_data_endpoints_config = []
default_app_styles_config = []
default_routes_config = []
default_app_footer = []
default_socials_config = []

list_config_files = [
  {
    "file_name" :  "config_app_data_endpoints",
    "class_name" :  "default_data_endpoints_config",
  },
  {
    "file_name" :  "config_app_footer",
    "class_name" :  "default_app_footer",
  },
  {
    "file_name" :  "config_app_global",
    "class_name" :  "default_global_config",
  },
  {
    "file_name" :  "config_app_navbar",
    "class_name" :  "default_app_navbar",
  },
  {
    "file_name" :  "config_app_routes",
    "class_name" :  "default_routes_config",
  },
  {
    "file_name" :  "config_app_socials",
    "class_name" :  "default_socials_config",
  },
  {
    "file_name" :  "config_app_styles",
    "class_name" :  "default_app_styles_config",
  },
  {
    "file_name" :  "config_app_tabs",
    "class_name" :  "default_app_tabs",
  },
]

for config_file in list_config_files : 

  file_name  = config_file["file_name"]
  class_name = config_file["class_name"]

  default_app_vars = []

  for folder in config_folders : 
    folder_module = "..{}.{}".format(folder, file_name)
    print ("... -> folder_module : ", folder_module)
    exec( 'from {} import {} as temp_config_list'.format(folder_module, class_name) )
    # print ("... -> temp_config_list : ", temp_config_list)
    default_app_vars = default_app_vars + temp_config_list
    print

    # print ("... -> default_app_vars : ", default_app_vars)

    if class_name == "default_global_config" : 
      default_global_config = default_app_vars

    if class_name == "default_app_navbar" : 
      default_app_navbar = default_app_vars

    if class_name == "default_app_tabs" : 
      default_app_tabs = default_app_vars

    if class_name == "default_data_endpoints_config" : 
      default_data_endpoints_config = default_app_vars

    if class_name == "default_app_styles_config" : 
      default_app_styles_config = default_app_vars

    if class_name == "default_routes_config" : 
      default_routes_config = default_app_vars

    if class_name == "default_app_footer" : 
      default_app_footer = default_app_vars

    if class_name == "default_socials_config" : 
      default_socials_config = default_app_vars
    
