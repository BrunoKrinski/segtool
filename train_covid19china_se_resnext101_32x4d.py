import os

ls=["python main.py --configs configs/train_covid19china_unetplusplus_se_resnext101_32x4d_fold0.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_se_resnext101_32x4d_fold1.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_se_resnext101_32x4d_fold2.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_se_resnext101_32x4d_fold3.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_se_resnext101_32x4d_fold4.yml",
"python main.py --configs configs/train_covid19china_unet_se_resnext101_32x4d_fold0.yml",
"python main.py --configs configs/train_covid19china_unet_se_resnext101_32x4d_fold1.yml",
"python main.py --configs configs/train_covid19china_unet_se_resnext101_32x4d_fold2.yml",
"python main.py --configs configs/train_covid19china_unet_se_resnext101_32x4d_fold3.yml",
"python main.py --configs configs/train_covid19china_unet_se_resnext101_32x4d_fold4.yml",
"python main.py --configs configs/train_covid19china_fpn_se_resnext101_32x4d_fold0.yml",
"python main.py --configs configs/train_covid19china_fpn_se_resnext101_32x4d_fold1.yml",
"python main.py --configs configs/train_covid19china_fpn_se_resnext101_32x4d_fold2.yml",
"python main.py --configs configs/train_covid19china_fpn_se_resnext101_32x4d_fold3.yml",
"python main.py --configs configs/train_covid19china_fpn_se_resnext101_32x4d_fold4.yml",
"python main.py --configs configs/train_covid19china_pspnet_se_resnext101_32x4d_fold0.yml",
"python main.py --configs configs/train_covid19china_pspnet_se_resnext101_32x4d_fold1.yml",
"python main.py --configs configs/train_covid19china_pspnet_se_resnext101_32x4d_fold2.yml",
"python main.py --configs configs/train_covid19china_pspnet_se_resnext101_32x4d_fold3.yml",
"python main.py --configs configs/train_covid19china_pspnet_se_resnext101_32x4d_fold4.yml",
"python main.py --configs configs/train_covid19china_linknet_se_resnext101_32x4d_fold0.yml",
"python main.py --configs configs/train_covid19china_linknet_se_resnext101_32x4d_fold1.yml",
"python main.py --configs configs/train_covid19china_linknet_se_resnext101_32x4d_fold2.yml",
"python main.py --configs configs/train_covid19china_linknet_se_resnext101_32x4d_fold3.yml",
"python main.py --configs configs/train_covid19china_linknet_se_resnext101_32x4d_fold4.yml",
"python main.py --configs configs/train_covid19china_manet_se_resnext101_32x4d_fold0.yml",
"python main.py --configs configs/train_covid19china_manet_se_resnext101_32x4d_fold1.yml",
"python main.py --configs configs/train_covid19china_manet_se_resnext101_32x4d_fold2.yml",
"python main.py --configs configs/train_covid19china_manet_se_resnext101_32x4d_fold3.yml",
"python main.py --configs configs/train_covid19china_manet_se_resnext101_32x4d_fold4.yml",
]

for l in ls:
  os.system(l)