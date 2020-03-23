# -*- encoding: utf-8 -*-

from .app_metas import app_metas
version = app_metas["version"]

import os
cwd = os.getcwd()

# cf : https://www.uuidgenerator.net/

uuid_models = {

  "uuid_demo_apiviz" :    "89edbf7d-8b63-4088-ad14-ae6779d7698f",

  "uuid_apcis" :          "f0a482da-28be-4929-a443-f22ecb03ee68",
  "uuid_sonum" :          "c5efafab-1733-4ad1-9eb8-d529bc87c481",
  "uuid_tiers_lieux" :    "fd9d4302-bddb-4fb1-8f13-d64dfdb66b91",

  "uuid_ping_carto" :     "0278419c-558e-43d5-a4d6-c836afd10445",
  "uuid_conumm" :         "2f658fb8-f00a-4b1a-ab73-7064433c98bc",
  "uuid_etalab_codes" :   "a44de08d-12a1-4182-a06e-78058928c1e1",

  "uuid_decider_ensemble" : "b8b52f0c-e66f-4018-bc0b-9ec7d17f8ccc",
  "uuid_ternum"           : "e8aff5a7-64b1-46b0-942a-8b16ac53aa3b",

  "uuid_covid"           : "ebd7910d-5c98-4701-883a-6003a288b37d",

  "uuid_orgues" :         "3f3fd562-5202-427f-8ba3-f58d5660aabf",

  "uuid_ocf" :            "305ab50d-c976-44d7-a8f2-a7594155c292",
  "uuid_transiscope"   :  "1c6fbb31-9953-4bc0-83a7-d71c9ffbd2c3",
  
  "uuid_open_archives" :  "07c6f4e3-c98a-4f1d-b242-f9fa95a19c1d",

}

config_folders = [
  
  "config_demo_apiviz",

  "config_apcis",
  "config_sonum",
  "config_tiers_lieux",
  "config_ping_carto",
  "config_conumm",

  "config_decider_ensemble",
  "config_ternum",
  "config_covid",

  "config_etalab_codes",
  "config_orgues",

  "config_ocf",
  # "config_transiscope",

  # "config_open_archives",

]