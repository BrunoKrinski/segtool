import os

ls=["python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold0_flip.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold1_flip.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold2_flip.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold3_flip.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold4_flip.yml",
]

for l in ls:
  os.system(l)