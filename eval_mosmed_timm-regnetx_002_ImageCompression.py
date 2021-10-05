import os

ls=["python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_0_ImageCompression.yml",
"python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_1_ImageCompression.yml",
"python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_2_ImageCompression.yml",
"python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_3_ImageCompression.yml",
"python main.py --configs configs/eval_mosmed_unetplusplus_timm-regnetx_002_4_ImageCompression.yml",
]

for l in ls:
  os.system(l)