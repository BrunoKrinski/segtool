import os

ls=["python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold0_elastic_transform.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold1_elastic_transform.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold2_elastic_transform.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold3_elastic_transform.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold4_elastic_transform.yml",
]

for l in ls:
  os.system(l)