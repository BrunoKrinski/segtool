import os

ls=["python main.py --configs configs/train_lungseg_unetplusplus_vgg16_fold0_noda.yml",
"python main.py --configs configs/train_lungseg_unetplusplus_vgg16_fold1_noda.yml",
"python main.py --configs configs/train_lungseg_unetplusplus_vgg16_fold2_noda.yml",
"python main.py --configs configs/train_lungseg_unetplusplus_vgg16_fold3_noda.yml",
"python main.py --configs configs/train_lungseg_unetplusplus_vgg16_fold4_noda.yml",
]

for l in ls:
  os.system(l)