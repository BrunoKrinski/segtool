import os

ls=["python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold0_sharpen.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold1_sharpen.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold2_sharpen.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold3_sharpen.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_timm-regnetx_002_fold4_sharpen.yml",
]

for l in ls:
  os.system(l)