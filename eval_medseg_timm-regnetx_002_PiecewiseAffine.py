import os

ls=["python main.py --configs configs/eval_medseg_unetplusplus_timm-regnetx_002_0_PiecewiseAffine.yml",
"python main.py --configs configs/eval_medseg_unetplusplus_timm-regnetx_002_1_PiecewiseAffine.yml",
"python main.py --configs configs/eval_medseg_unetplusplus_timm-regnetx_002_2_PiecewiseAffine.yml",
"python main.py --configs configs/eval_medseg_unetplusplus_timm-regnetx_002_3_PiecewiseAffine.yml",
"python main.py --configs configs/eval_medseg_unetplusplus_timm-regnetx_002_4_PiecewiseAffine.yml",
]

for l in ls:
  os.system(l)