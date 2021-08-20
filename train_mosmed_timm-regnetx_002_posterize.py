import os

ls=["python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold0_posterize.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold1_posterize.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold2_posterize.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold3_posterize.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold4_posterize.yml",
]

for l in ls:
  os.system(l)