import os

ls=["python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold0_piecewise_affine.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold1_piecewise_affine.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold2_piecewise_affine.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold3_piecewise_affine.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold4_piecewise_affine.yml",
]

for l in ls:
  os.system(l)