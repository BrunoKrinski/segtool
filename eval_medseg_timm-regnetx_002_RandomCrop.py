import os

ls=["python main.py --configs configs/eval_medseg_unetplusplus_timm-regnetx_002_0_RandomCrop.yml",
"python main.py --configs configs/eval_medseg_unetplusplus_timm-regnetx_002_1_RandomCrop.yml",
"python main.py --configs configs/eval_medseg_unetplusplus_timm-regnetx_002_2_RandomCrop.yml",
"python main.py --configs configs/eval_medseg_unetplusplus_timm-regnetx_002_3_RandomCrop.yml",
"python main.py --configs configs/eval_medseg_unetplusplus_timm-regnetx_002_4_RandomCrop.yml",
]

for l in ls:
  os.system(l)