import os

ls=["python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold0_gaussian_blur.yml",
"python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold1_gaussian_blur.yml",
"python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold2_gaussian_blur.yml",
"python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold3_gaussian_blur.yml",
"python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold4_gaussian_blur.yml",
]

for l in ls:
  os.system(l)