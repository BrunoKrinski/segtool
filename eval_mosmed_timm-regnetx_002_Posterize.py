import os

ls=["python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_0_Posterize.yml",
"python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_1_Posterize.yml",
"python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_2_Posterize.yml",
"python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_3_Posterize.yml",
"python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_4_Posterize.yml",
]

for l in ls:
  os.system(l)