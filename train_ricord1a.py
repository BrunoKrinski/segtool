import os

ls=["python main.py --configs configs/train_ricord1a_unet_resnet50_fold0.yml",
"python main.py --configs configs/train_ricord1a_unet_resnet50_fold1.yml",
"python main.py --configs configs/train_ricord1a_unet_resnet50_fold2.yml",
"python main.py --configs configs/train_ricord1a_unet_resnet50_fold3.yml",
"python main.py --configs configs/train_ricord1a_unet_resnet50_fold4.yml",
"python main.py --configs configs/train_ricord1a_fpn_resnet50_fold0.yml",
"python main.py --configs configs/train_ricord1a_fpn_resnet50_fold1.yml",
"python main.py --configs configs/train_ricord1a_fpn_resnet50_fold2.yml",
"python main.py --configs configs/train_ricord1a_fpn_resnet50_fold3.yml",
"python main.py --configs configs/train_ricord1a_fpn_resnet50_fold4.yml",
"python main.py --configs configs/train_ricord1a_pspnet_resnet50_fold0.yml",
"python main.py --configs configs/train_ricord1a_pspnet_resnet50_fold1.yml",
"python main.py --configs configs/train_ricord1a_pspnet_resnet50_fold2.yml",
"python main.py --configs configs/train_ricord1a_pspnet_resnet50_fold3.yml",
"python main.py --configs configs/train_ricord1a_pspnet_resnet50_fold4.yml",
"python main.py --configs configs/train_ricord1a_linknet_resnet50_fold0.yml",
"python main.py --configs configs/train_ricord1a_linknet_resnet50_fold1.yml",
"python main.py --configs configs/train_ricord1a_linknet_resnet50_fold2.yml",
"python main.py --configs configs/train_ricord1a_linknet_resnet50_fold3.yml",
"python main.py --configs configs/train_ricord1a_linknet_resnet50_fold4.yml",
"python main.py --configs configs/train_ricord1a_unetplusplus_resnet50_fold0.yml",
"python main.py --configs configs/train_ricord1a_unetplusplus_resnet50_fold1.yml",
"python main.py --configs configs/train_ricord1a_unetplusplus_resnet50_fold2.yml",
"python main.py --configs configs/train_ricord1a_unetplusplus_resnet50_fold3.yml",
"python main.py --configs configs/train_ricord1a_unetplusplus_resnet50_fold4.yml",
"python main.py --configs configs/train_ricord1a_pan_resnet50_fold0.yml",
"python main.py --configs configs/train_ricord1a_pan_resnet50_fold1.yml",
"python main.py --configs configs/train_ricord1a_pan_resnet50_fold2.yml",
"python main.py --configs configs/train_ricord1a_pan_resnet50_fold3.yml",
"python main.py --configs configs/train_ricord1a_pan_resnet50_fold4.yml",
"python main.py --configs configs/train_ricord1a_manet_resnet50_fold0.yml",
"python main.py --configs configs/train_ricord1a_manet_resnet50_fold1.yml",
"python main.py --configs configs/train_ricord1a_manet_resnet50_fold2.yml",
"python main.py --configs configs/train_ricord1a_manet_resnet50_fold3.yml",
"python main.py --configs configs/train_ricord1a_manet_resnet50_fold4.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3_resnet50_fold0.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3_resnet50_fold1.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3_resnet50_fold2.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3_resnet50_fold3.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3_resnet50_fold4.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3plus_resnet50_fold0.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3plus_resnet50_fold1.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3plus_resnet50_fold2.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3plus_resnet50_fold3.yml",
"python main.py --configs configs/train_ricord1a_deeplabv3plus_resnet50_fold4.yml",
]

for l in ls:
  os.system(l)