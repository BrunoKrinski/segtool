import os

ls=["python main.py --configs configs/train_ricord1a_deeplabv3_resnext101_32x8d_fold0.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3_resnext101_32x8d_fold1.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3_resnext101_32x8d_fold2.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3_resnext101_32x8d_fold3.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3_resnext101_32x8d_fold4.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3plus_resnext101_32x8d_fold0.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3plus_resnext101_32x8d_fold1.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3plus_resnext101_32x8d_fold2.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3plus_resnext101_32x8d_fold3.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3plus_resnext101_32x8d_fold4.yml",
]

for l in ls:
  os.system(l)