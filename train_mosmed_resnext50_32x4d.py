import os

ls=["python main.py --configs configs/train_mosmed_unetplusplus_resnext50_32x4d_fold0.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_resnext50_32x4d_fold1.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_resnext50_32x4d_fold2.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_resnext50_32x4d_fold3.yml",
"python main.py --configs configs/train_mosmed_unetplusplus_resnext50_32x4d_fold4.yml",
"python main.py --configs configs/train_mosmed_unet_resnext50_32x4d_fold0.yml",
"python main.py --configs configs/train_mosmed_unet_resnext50_32x4d_fold1.yml",
"python main.py --configs configs/train_mosmed_unet_resnext50_32x4d_fold2.yml",
"python main.py --configs configs/train_mosmed_unet_resnext50_32x4d_fold3.yml",
"python main.py --configs configs/train_mosmed_unet_resnext50_32x4d_fold4.yml",
"python main.py --configs configs/train_mosmed_fpn_resnext50_32x4d_fold0.yml",
"python main.py --configs configs/train_mosmed_fpn_resnext50_32x4d_fold1.yml",
"python main.py --configs configs/train_mosmed_fpn_resnext50_32x4d_fold2.yml",
"python main.py --configs configs/train_mosmed_fpn_resnext50_32x4d_fold3.yml",
"python main.py --configs configs/train_mosmed_fpn_resnext50_32x4d_fold4.yml",
"python main.py --configs configs/train_mosmed_pspnet_resnext50_32x4d_fold0.yml",
"python main.py --configs configs/train_mosmed_pspnet_resnext50_32x4d_fold1.yml",
"python main.py --configs configs/train_mosmed_pspnet_resnext50_32x4d_fold2.yml",
"python main.py --configs configs/train_mosmed_pspnet_resnext50_32x4d_fold3.yml",
"python main.py --configs configs/train_mosmed_pspnet_resnext50_32x4d_fold4.yml",
"python main.py --configs configs/train_mosmed_linknet_resnext50_32x4d_fold0.yml",
"python main.py --configs configs/train_mosmed_linknet_resnext50_32x4d_fold1.yml",
"python main.py --configs configs/train_mosmed_linknet_resnext50_32x4d_fold2.yml",
"python main.py --configs configs/train_mosmed_linknet_resnext50_32x4d_fold3.yml",
"python main.py --configs configs/train_mosmed_linknet_resnext50_32x4d_fold4.yml",
"python main.py --configs configs/train_mosmed_pan_resnext50_32x4d_fold0.yml",
"python main.py --configs configs/train_mosmed_pan_resnext50_32x4d_fold1.yml",
"python main.py --configs configs/train_mosmed_pan_resnext50_32x4d_fold2.yml",
"python main.py --configs configs/train_mosmed_pan_resnext50_32x4d_fold3.yml",
"python main.py --configs configs/train_mosmed_pan_resnext50_32x4d_fold4.yml",
"python main.py --configs configs/train_mosmed_manet_resnext50_32x4d_fold0.yml",
"python main.py --configs configs/train_mosmed_manet_resnext50_32x4d_fold1.yml",
"python main.py --configs configs/train_mosmed_manet_resnext50_32x4d_fold2.yml",
"python main.py --configs configs/train_mosmed_manet_resnext50_32x4d_fold3.yml",
"python main.py --configs configs/train_mosmed_manet_resnext50_32x4d_fold4.yml",
"python main.py --configs configs/train_mosmed_deeplabv3_resnext50_32x4d_fold0.yml",
"python main.py --configs configs/train_mosmed_deeplabv3_resnext50_32x4d_fold1.yml",
"python main.py --configs configs/train_mosmed_deeplabv3_resnext50_32x4d_fold2.yml",
"python main.py --configs configs/train_mosmed_deeplabv3_resnext50_32x4d_fold3.yml",
"python main.py --configs configs/train_mosmed_deeplabv3_resnext50_32x4d_fold4.yml",
"python main.py --configs configs/train_mosmed_deeplabv3plus_resnext50_32x4d_fold0.yml",
"python main.py --configs configs/train_mosmed_deeplabv3plus_resnext50_32x4d_fold1.yml",
"python main.py --configs configs/train_mosmed_deeplabv3plus_resnext50_32x4d_fold2.yml",
"python main.py --configs configs/train_mosmed_deeplabv3plus_resnext50_32x4d_fold3.yml",
"python main.py --configs configs/train_mosmed_deeplabv3plus_resnext50_32x4d_fold4.yml",
]

for l in ls:
  os.system(l)