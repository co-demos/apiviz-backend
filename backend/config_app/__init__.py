# -*- encoding: utf-8 -*-

from .app_metas import app_metas
version = app_metas["version"]

import os
cwd = os.getcwd()

# cf : https://www.uuidgenerator.net/

uuid_models = {
  "uuid_apcis" :          "f0a482da-28be-4929-a443-f22ecb03ee68",
  "uuid_sonum" :          "c5efafab-1733-4ad1-9eb8-d529bc87c481",
  "uuid_tiers_lieux" :    "fd9d4302-bddb-4fb1-8f13-d64dfdb66b91",
  "uuid_ping_carto" :     "0278419c-558e-43d5-a4d6-c836afd10445",
  "uuid_ocf" :            "305ab50d-c976-44d7-a8f2-a7594155c292",
  "uuid_open_archives" :  "0278419c-558e-43d5-a4d6-c836afd10445",
}

config_folders = [
  "config_apcis",
  "config_sonum",
  "config_tiers_lieux",
  # "config_ping_carto",
  # "config_ocf",
  # "config_open_archives",
]