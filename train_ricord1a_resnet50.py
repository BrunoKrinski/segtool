import os

ls=["python main.py --configs configs/train_ricord1a_pan_resnet50_fold0.yml",
"python main.py --configs configs/train_ricord1a_pan_resnet50_fold1.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3_resnet50_fold0.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3_resnet50_fold1.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3plus_resnet50_fold0.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3plus_resnet50_fold1.yml",
]

for l in ls:
  os.system(l)