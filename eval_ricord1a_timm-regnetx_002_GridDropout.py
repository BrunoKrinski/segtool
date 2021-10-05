import os

ls=["python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_0_GridDropout.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_1_GridDropout.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_2_GridDropout.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_3_GridDropout.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_4_GridDropout.yml",
]

for l in ls:
  os.system(l)