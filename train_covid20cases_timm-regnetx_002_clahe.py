import os

ls=["python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold0_clahe.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold1_clahe.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold2_clahe.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold3_clahe.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold4_clahe.yml",
]

for l in ls:
  os.system(l)