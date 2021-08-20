import os

ls=["python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold0_grid_dropout.yml",
"python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold1_grid_dropout.yml",
"python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold2_grid_dropout.yml",
"python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold3_grid_dropout.yml",
"python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold4_grid_dropout.yml",
]

for l in ls:
  os.system(l)