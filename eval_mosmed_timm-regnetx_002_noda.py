import os

ls=["python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_0_noda.yml",
"python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_1_noda.yml",
"python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_2_noda.yml",
"python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_3_noda.yml",
"python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_4_noda.yml",
]

for l in ls:
  os.system(l)