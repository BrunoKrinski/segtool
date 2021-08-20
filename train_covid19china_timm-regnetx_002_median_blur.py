import os

ls=["python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold0_median_blur.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold1_median_blur.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold2_median_blur.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold3_median_blur.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold4_median_blur.yml",
]

for l in ls:
  os.system(l)