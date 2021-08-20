import os

ls=["python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold0_optical_distortion.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold1_optical_distortion.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold2_optical_distortion.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold3_optical_distortion.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold4_optical_distortion.yml",
]

for l in ls:
  os.system(l)