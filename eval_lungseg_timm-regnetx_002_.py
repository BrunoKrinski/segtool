import os

ls=["python main.py --configs configs/eval_lungseg_unetplusplus_timm-regnetx_002_0_.yml",
"python main.py --configs configs/eval_lungseg_unetplusplus_timm-regnetx_002_1_.yml",
"python main.py --configs configs/eval_lungseg_unetplusplus_timm-regnetx_002_2_.yml",
"python main.py --configs configs/eval_lungseg_unetplusplus_timm-regnetx_002_3_.yml",
"python main.py --configs configs/eval_lungseg_unetplusplus_timm-regnetx_002_4_.yml",
]

for l in ls:
  os.system(l)