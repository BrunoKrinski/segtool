import os

ls=["python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold0.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold1.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold2.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold3.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_timm-regnetx_002_fold4.yml",
]

for l in ls:
  os.system(l)