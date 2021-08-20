import os

ls=["python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold0_noda.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold1_noda.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold2_noda.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold3_noda.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold4_noda.yml",
]

for l in ls:
  os.system(l)