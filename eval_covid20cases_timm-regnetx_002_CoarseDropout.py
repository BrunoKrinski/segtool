import os

ls=["python main.py --configs configs/eval_covid20cases_unetplusplus_timm-regnetx_002_0_CoarseDropout.yml",
"python main.py --configs configs/eval_covid20cases_unetplusplus_timm-regnetx_002_1_CoarseDropout.yml",
"python main.py --configs configs/eval_covid20cases_unetplusplus_timm-regnetx_002_2_CoarseDropout.yml",
"python main.py --configs configs/eval_covid20cases_unetplusplus_timm-regnetx_002_3_CoarseDropout.yml",
"python main.py --configs configs/eval_covid20cases_unetplusplus_timm-regnetx_002_4_CoarseDropout.yml",
]

for l in ls:
  os.system(l)