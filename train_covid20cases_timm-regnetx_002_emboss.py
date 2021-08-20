import os

ls=["python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold0_emboss.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold1_emboss.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold2_emboss.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold3_emboss.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold4_emboss.yml",
]

for l in ls:
  os.system(l)