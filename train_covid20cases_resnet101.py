import os

ls=["python main.py --configs configs/train_covid20cases_unetplusplus_resnet101_fold0.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_resnet101_fold1.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_resnet101_fold2.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_resnet101_fold3.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_resnet101_fold4.yml",
"python main.py --configs configs/train_covid20cases_unet_resnet101_fold0.yml",
"python main.py --configs configs/train_covid20cases_unet_resnet101_fold1.yml",
"python main.py --configs configs/train_covid20cases_unet_resnet101_fold2.yml",
"python main.py --configs configs/train_covid20cases_unet_resnet101_fold3.yml",
"python main.py --configs configs/train_covid20cases_unet_resnet101_fold4.yml",
"python main.py --configs configs/train_covid20cases_fpn_resnet101_fold0.yml",
"python main.py --configs configs/train_covid20cases_fpn_resnet101_fold1.yml",
"python main.py --configs configs/train_covid20cases_fpn_resnet101_fold2.yml",
"python main.py --configs configs/train_covid20cases_fpn_resnet101_fold3.yml",
"python main.py --configs configs/train_covid20cases_fpn_resnet101_fold4.yml",
"python main.py --configs configs/train_covid20cases_pspnet_resnet101_fold0.yml",
"python main.py --configs configs/train_covid20cases_pspnet_resnet101_fold1.yml",
"python main.py --configs configs/train_covid20cases_pspnet_resnet101_fold2.yml",
"python main.py --configs configs/train_covid20cases_pspnet_resnet101_fold3.yml",
"python main.py --configs configs/train_covid20cases_pspnet_resnet101_fold4.yml",
"python main.py --configs configs/train_covid20cases_linknet_resnet101_fold0.yml",
"python main.py --configs configs/train_covid20cases_linknet_resnet101_fold1.yml",
"python main.py --configs configs/train_covid20cases_linknet_resnet101_fold2.yml",
"python main.py --configs configs/train_covid20cases_linknet_resnet101_fold3.yml",
"python main.py --configs configs/train_covid20cases_linknet_resnet101_fold4.yml",
"python main.py --configs configs/train_covid20cases_pan_resnet101_fold0.yml",
"python main.py --configs configs/train_covid20cases_pan_resnet101_fold1.yml",
"python main.py --configs configs/train_covid20cases_pan_resnet101_fold2.yml",
"python main.py --configs configs/train_covid20cases_pan_resnet101_fold3.yml",
"python main.py --configs configs/train_covid20cases_pan_resnet101_fold4.yml",
"python main.py --configs configs/train_covid20cases_manet_resnet101_fold0.yml",
"python main.py --configs configs/train_covid20cases_manet_resnet101_fold1.yml",
"python main.py --configs configs/train_covid20cases_manet_resnet101_fold2.yml",
"python main.py --configs configs/train_covid20cases_manet_resnet101_fold3.yml",
"python main.py --configs configs/train_covid20cases_manet_resnet101_fold4.yml",
"python main.py --configs configs/train_covid20cases_deeplabv3_resnet101_fold0.yml",
"python main.py --configs configs/train_covid20cases_deeplabv3_resnet101_fold1.yml",
"python main.py --configs configs/train_covid20cases_deeplabv3_resnet101_fold2.yml",
"python main.py --configs configs/train_covid20cases_deeplabv3_resnet101_fold3.yml",
"python main.py --configs configs/train_covid20cases_deeplabv3_resnet101_fold4.yml",
"python main.py --configs configs/train_covid20cases_deeplabv3plus_resnet101_fold0.yml",
"python main.py --configs configs/train_covid20cases_deeplabv3plus_resnet101_fold1.yml",
"python main.py --configs configs/train_covid20cases_deeplabv3plus_resnet101_fold2.yml",
"python main.py --configs configs/train_covid20cases_deeplabv3plus_resnet101_fold3.yml",
"python main.py --configs configs/train_covid20cases_deeplabv3plus_resnet101_fold4.yml",
]

for l in ls:
  os.system(l)