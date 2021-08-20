import os

ls=["python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold0_shift_scale_rotate.yml",
"python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold1_shift_scale_rotate.yml",
"python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold2_shift_scale_rotate.yml",
"python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold3_shift_scale_rotate.yml",
"python main.py --configs configs/train_medseg_unetplusplus_timm-regnetx_002_fold4_shift_scale_rotate.yml",
]

for l in ls:
  os.system(l)