import os

ls=["python main.py --configs configs/train_medseg_unet_resnet101_fold0.yml",
"python main.py --configs configs/train_medseg_unet_resnet101_fold1.yml",
"python main.py --configs configs/train_medseg_unet_resnet101_fold2.yml",
"python main.py --configs configs/train_medseg_unet_resnet101_fold3.yml",
"python main.py --configs configs/train_medseg_unet_resnet101_fold4.yml",
"python main.py --configs configs/train_medseg_fpn_resnet101_fold0.yml",
"python main.py --configs configs/train_medseg_fpn_resnet101_fold1.yml",
"python main.py --configs configs/train_medseg_fpn_resnet101_fold2.yml",
"python main.py --configs configs/train_medseg_fpn_resnet101_fold3.yml",
"python main.py --configs configs/train_medseg_fpn_resnet101_fold4.yml",
"python main.py --configs configs/train_medseg_pspnet_resnet101_fold0.yml",
"python main.py --configs configs/train_medseg_pspnet_resnet101_fold1.yml",
"python main.py --configs configs/train_medseg_pspnet_resnet101_fold2.yml",
"python main.py --configs configs/train_medseg_pspnet_resnet101_fold3.yml",
"python main.py --configs configs/train_medseg_pspnet_resnet101_fold4.yml",
"python main.py --configs configs/train_medseg_linknet_resnet101_fold0.yml",
"python main.py --configs configs/train_medseg_linknet_resnet101_fold1.yml",
"python main.py --configs configs/train_medseg_linknet_resnet101_fold2.yml",
"python main.py --configs configs/train_medseg_linknet_resnet101_fold3.yml",
"python main.py --configs configs/train_medseg_linknet_resnet101_fold4.yml",
"python main.py --configs configs/train_medseg_unetplusplus_resnet101_fold0.yml",
"python main.py --configs configs/train_medseg_unetplusplus_resnet101_fold1.yml",
"python main.py --configs configs/train_medseg_unetplusplus_resnet101_fold2.yml",
"python main.py --configs configs/train_medseg_unetplusplus_resnet101_fold3.yml",
"python main.py --configs configs/train_medseg_unetplusplus_resnet101_fold4.yml",
"python main.py --configs configs/train_medseg_pan_resnet101_fold0.yml",
"python main.py --configs configs/train_medseg_pan_resnet101_fold1.yml",
"python main.py --configs configs/train_medseg_pan_resnet101_fold2.yml",
"python main.py --configs configs/train_medseg_pan_resnet101_fold3.yml",
"python main.py --configs configs/train_medseg_pan_resnet101_fold4.yml",
"python main.py --configs configs/train_medseg_manet_resnet101_fold0.yml",
"python main.py --configs configs/train_medseg_manet_resnet101_fold1.yml",
"python main.py --configs configs/train_medseg_manet_resnet101_fold2.yml",
"python main.py --configs configs/train_medseg_manet_resnet101_fold3.yml",
"python main.py --configs configs/train_medseg_manet_resnet101_fold4.yml",
"python main.py --configs configs/train_medseg_deeplabv3_resnet101_fold0.yml",
"python main.py --configs configs/train_medseg_deeplabv3_resnet101_fold1.yml",
"python main.py --configs configs/train_medseg_deeplabv3_resnet101_fold2.yml",
"python main.py --configs configs/train_medseg_deeplabv3_resnet101_fold3.yml",
"python main.py --configs configs/train_medseg_deeplabv3_resnet101_fold4.yml",
"python main.py --configs configs/train_medseg_deeplabv3plus_resnet101_fold0.yml",
"python main.py --configs configs/train_medseg_deeplabv3plus_resnet101_fold1.yml",
"python main.py --configs configs/train_medseg_deeplabv3plus_resnet101_fold2.yml",
"python main.py --configs configs/train_medseg_deeplabv3plus_resnet101_fold3.yml",
"python main.py --configs configs/train_medseg_deeplabv3plus_resnet101_fold4.yml",
]

for l in ls:
  os.system(l)