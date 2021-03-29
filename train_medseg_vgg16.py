import os

ls=["python main.py --configs configs/train_medseg_unetplusplus_vgg16_fold0.yml",
"python main.py --configs configs/train_medseg_unetplusplus_vgg16_fold1.yml",
"python main.py --configs configs/train_medseg_unetplusplus_vgg16_fold2.yml",
"python main.py --configs configs/train_medseg_unetplusplus_vgg16_fold3.yml",
"python main.py --configs configs/train_medseg_unetplusplus_vgg16_fold4.yml",
"python main.py --configs configs/train_medseg_unet_vgg16_fold0.yml",
"python main.py --configs configs/train_medseg_unet_vgg16_fold1.yml",
"python main.py --configs configs/train_medseg_unet_vgg16_fold2.yml",
"python main.py --configs configs/train_medseg_unet_vgg16_fold3.yml",
"python main.py --configs configs/train_medseg_unet_vgg16_fold4.yml",
"python main.py --configs configs/train_medseg_fpn_vgg16_fold0.yml",
"python main.py --configs configs/train_medseg_fpn_vgg16_fold1.yml",
"python main.py --configs configs/train_medseg_fpn_vgg16_fold2.yml",
"python main.py --configs configs/train_medseg_fpn_vgg16_fold3.yml",
"python main.py --configs configs/train_medseg_fpn_vgg16_fold4.yml",
"python main.py --configs configs/train_medseg_pspnet_vgg16_fold0.yml",
"python main.py --configs configs/train_medseg_pspnet_vgg16_fold1.yml",
"python main.py --configs configs/train_medseg_pspnet_vgg16_fold2.yml",
"python main.py --configs configs/train_medseg_pspnet_vgg16_fold3.yml",
"python main.py --configs configs/train_medseg_pspnet_vgg16_fold4.yml",
"python main.py --configs configs/train_medseg_linknet_vgg16_fold0.yml",
"python main.py --configs configs/train_medseg_linknet_vgg16_fold1.yml",
"python main.py --configs configs/train_medseg_linknet_vgg16_fold2.yml",
"python main.py --configs configs/train_medseg_linknet_vgg16_fold3.yml",
"python main.py --configs configs/train_medseg_linknet_vgg16_fold4.yml",
"python main.py --configs configs/train_medseg_pan_vgg16_fold0.yml",
"python main.py --configs configs/train_medseg_pan_vgg16_fold1.yml",
"python main.py --configs configs/train_medseg_pan_vgg16_fold2.yml",
"python main.py --configs configs/train_medseg_pan_vgg16_fold3.yml",
"python main.py --configs configs/train_medseg_pan_vgg16_fold4.yml",
"python main.py --configs configs/train_medseg_manet_vgg16_fold0.yml",
"python main.py --configs configs/train_medseg_manet_vgg16_fold1.yml",
"python main.py --configs configs/train_medseg_manet_vgg16_fold2.yml",
"python main.py --configs configs/train_medseg_manet_vgg16_fold3.yml",
"python main.py --configs configs/train_medseg_manet_vgg16_fold4.yml",
"python main.py --configs configs/train_medseg_deeplabv3_vgg16_fold0.yml",
"python main.py --configs configs/train_medseg_deeplabv3_vgg16_fold1.yml",
"python main.py --configs configs/train_medseg_deeplabv3_vgg16_fold2.yml",
"python main.py --configs configs/train_medseg_deeplabv3_vgg16_fold3.yml",
"python main.py --configs configs/train_medseg_deeplabv3_vgg16_fold4.yml",
"python main.py --configs configs/train_medseg_deeplabv3plus_vgg16_fold0.yml",
"python main.py --configs configs/train_medseg_deeplabv3plus_vgg16_fold1.yml",
"python main.py --configs configs/train_medseg_deeplabv3plus_vgg16_fold2.yml",
"python main.py --configs configs/train_medseg_deeplabv3plus_vgg16_fold3.yml",
"python main.py --configs configs/train_medseg_deeplabv3plus_vgg16_fold4.yml",
]

for l in ls:
  os.system(l)