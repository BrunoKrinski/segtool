import os

ls=["python main.py --configs configs/train_medseg_unetplusplus_se_resnet101_fold0.yml",
"python main.py --configs configs/train_medseg_unetplusplus_se_resnet101_fold1.yml",
"python main.py --configs configs/train_medseg_unetplusplus_se_resnet101_fold2.yml",
"python main.py --configs configs/train_medseg_unetplusplus_se_resnet101_fold3.yml",
"python main.py --configs configs/train_medseg_unetplusplus_se_resnet101_fold4.yml",
"python main.py --configs configs/train_medseg_unet_se_resnet101_fold0.yml",
"python main.py --configs configs/train_medseg_unet_se_resnet101_fold1.yml",
"python main.py --configs configs/train_medseg_unet_se_resnet101_fold2.yml",
"python main.py --configs configs/train_medseg_unet_se_resnet101_fold3.yml",
"python main.py --configs configs/train_medseg_unet_se_resnet101_fold4.yml",
"python main.py --configs configs/train_medseg_fpn_se_resnet101_fold0.yml",
"python main.py --configs configs/train_medseg_fpn_se_resnet101_fold1.yml",
"python main.py --configs configs/train_medseg_fpn_se_resnet101_fold2.yml",
"python main.py --configs configs/train_medseg_fpn_se_resnet101_fold3.yml",
"python main.py --configs configs/train_medseg_fpn_se_resnet101_fold4.yml",
"python main.py --configs configs/train_medseg_pspnet_se_resnet101_fold0.yml",
"python main.py --configs configs/train_medseg_pspnet_se_resnet101_fold1.yml",
"python main.py --configs configs/train_medseg_pspnet_se_resnet101_fold2.yml",
"python main.py --configs configs/train_medseg_pspnet_se_resnet101_fold3.yml",
"python main.py --configs configs/train_medseg_pspnet_se_resnet101_fold4.yml",
"python main.py --configs configs/train_medseg_linknet_se_resnet101_fold0.yml",
"python main.py --configs configs/train_medseg_linknet_se_resnet101_fold1.yml",
"python main.py --configs configs/train_medseg_linknet_se_resnet101_fold2.yml",
"python main.py --configs configs/train_medseg_linknet_se_resnet101_fold3.yml",
"python main.py --configs configs/train_medseg_linknet_se_resnet101_fold4.yml",
"python main.py --configs configs/train_medseg_manet_se_resnet101_fold0.yml",
"python main.py --configs configs/train_medseg_manet_se_resnet101_fold1.yml",
"python main.py --configs configs/train_medseg_manet_se_resnet101_fold2.yml",
"python main.py --configs configs/train_medseg_manet_se_resnet101_fold3.yml",
"python main.py --configs configs/train_medseg_manet_se_resnet101_fold4.yml",
]

for l in ls:
  os.system(l)