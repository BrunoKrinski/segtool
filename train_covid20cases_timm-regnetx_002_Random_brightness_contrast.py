import os

ls=["python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold0_Random_brightness_contrast.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold1_Random_brightness_contrast.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold2_Random_brightness_contrast.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold3_Random_brightness_contrast.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold4_Random_brightness_contrast.yml",
]

for l in ls:
  os.system(l)