import os

ls=["python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_0_RandomSnow.yml",
"python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_1_RandomSnow.yml",
"python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_2_RandomSnow.yml",
"python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_3_RandomSnow.yml",
"python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_4_RandomSnow.yml",
]

for l in ls:
  os.system(l)