import os

ls=["python main.py --configs configs/train_ricord1a_unetplusplus_timm-regnetx_002_fold0_image_compression.yml",
"python main.py --configs configs/train_ricord1a_unetplusplus_timm-regnetx_002_fold1_image_compression.yml",
"python main.py --configs configs/train_ricord1a_unetplusplus_timm-regnetx_002_fold2_image_compression.yml",
"python main.py --configs configs/train_ricord1a_unetplusplus_timm-regnetx_002_fold3_image_compression.yml",
"python main.py --configs configs/train_ricord1a_unetplusplus_timm-regnetx_002_fold4_image_compression.yml",
]

for l in ls:
  os.system(l)