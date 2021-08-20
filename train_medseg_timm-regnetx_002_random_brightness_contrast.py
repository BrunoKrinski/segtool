import os

ls=["python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold0_random_brightness_contrast.yml",
"python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold1_random_brightness_contrast.yml",
"python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold2_random_brightness_contrast.yml",
"python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold3_random_brightness_contrast.yml",
"python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold4_random_brightness_contrast.yml",
]

for l in ls:
  os.system(l)