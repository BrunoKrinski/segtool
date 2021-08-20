import os

ls=["python main.py --configs configs/train_ricord1a_unetplusplus_timm-regnetx_002_fold0_rotate.yml",
"python main.py --configs configs/train_ricord1a_unetplusplus_timm-regnetx_002_fold1_rotate.yml",
"python main.py --configs configs/train_ricord1a_unetplusplus_timm-regnetx_002_fold2_rotate.yml",
"python main.py --configs configs/train_ricord1a_unetplusplus_timm-regnetx_002_fold3_rotate.yml",
"python main.py --configs configs/train_ricord1a_unetplusplus_timm-regnetx_002_fold4_rotate.yml",
]

for l in ls:
  os.system(l)