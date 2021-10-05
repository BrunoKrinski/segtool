import os

ls=["python main.py --configs configs/train_lungseg_unetplusplus_resnet50_fold0_noda.yml",
"python main.py --configs configs/train_lungseg_unetplusplus_resnet50_fold1_noda.yml",
"python main.py --configs configs/train_lungseg_unetplusplus_resnet50_fold2_noda.yml",
"python main.py --configs configs/train_lungseg_unetplusplus_resnet50_fold3_noda.yml",
"python main.py --configs configs/train_lungseg_unetplusplus_resnet50_fold4_noda.yml",
]

for l in ls:
  os.system(l)