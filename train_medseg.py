import os

ls=["python main.py --configs configs/train_medseg_unetplusplus_resnet50_fold0.yml",
"python main.py --configs configs/train_medseg_unetplusplus_resnet50_fold1.yml",
"python main.py --configs configs/train_medseg_unetplusplus_resnet50_fold2.yml",
"python main.py --configs configs/train_medseg_unetplusplus_resnet50_fold3.yml",
"python main.py --configs configs/train_medseg_unetplusplus_resnet50_fold4.yml",
"python main.py --configs configs/train_medseg_pan_resnet50_fold0.yml",
"python main.py --configs configs/train_medseg_pan_resnet50_fold1.yml",
"python main.py --configs configs/train_medseg_pan_resnet50_fold2.yml",
"python main.py --configs configs/train_medseg_pan_resnet50_fold3.yml",
"python main.py --configs configs/train_medseg_pan_resnet50_fold4.yml",
"python main.py --configs configs/train_medseg_manet_resnet50_fold0.yml",
"python main.py --configs configs/train_medseg_manet_resnet50_fold1.yml",
"python main.py --configs configs/train_medseg_manet_resnet50_fold2.yml",
"python main.py --configs configs/train_medseg_manet_resnet50_fold3.yml",
"python main.py --configs configs/train_medseg_manet_resnet50_fold4.yml",
"python main.py --configs configs/train_medseg_deeplabv3_resnet50_fold0.yml",
"python main.py --configs configs/train_medseg_deeplabv3_resnet50_fold1.yml",
"python main.py --configs configs/train_medseg_deeplabv3_resnet50_fold2.yml",
"python main.py --configs configs/train_medseg_deeplabv3_resnet50_fold3.yml",
"python main.py --configs configs/train_medseg_deeplabv3_resnet50_fold4.yml",
"python main.py --configs configs/train_medseg_deeplabv3plus_resnet50_fold0.yml",
"python main.py --configs configs/train_medseg_deeplabv3plus_resnet50_fold1.yml",
"python main.py --configs configs/train_medseg_deeplabv3plus_resnet50_fold2.yml",
"python main.py --configs configs/train_medseg_deeplabv3plus_resnet50_fold3.yml",
"python main.py --configs configs/train_medseg_deeplabv3plus_resnet50_fold4.yml",
]

for l in ls:
  os.system(l)