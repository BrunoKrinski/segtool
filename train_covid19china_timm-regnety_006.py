import os

ls=["python main.py --configs configs/train_covid19china_unetplusplus_timm-regnety_006_fold0.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_timm-regnety_006_fold1.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_timm-regnety_006_fold2.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_timm-regnety_006_fold3.yml",
"python main.py --configs configs/train_covid19china_unetplusplus_timm-regnety_006_fold4.yml",
"python main.py --configs configs/train_covid19china_unet_timm-regnety_006_fold0.yml",
"python main.py --configs configs/train_covid19china_unet_timm-regnety_006_fold1.yml",
"python main.py --configs configs/train_covid19china_unet_timm-regnety_006_fold2.yml",
"python main.py --configs configs/train_covid19china_unet_timm-regnety_006_fold3.yml",
"python main.py --configs configs/train_covid19china_unet_timm-regnety_006_fold4.yml",
"python main.py --configs configs/train_covid19china_fpn_timm-regnety_006_fold0.yml",
"python main.py --configs configs/train_covid19china_fpn_timm-regnety_006_fold1.yml",
"python main.py --configs configs/train_covid19china_fpn_timm-regnety_006_fold2.yml",
"python main.py --configs configs/train_covid19china_fpn_timm-regnety_006_fold3.yml",
"python main.py --configs configs/train_covid19china_fpn_timm-regnety_006_fold4.yml",
"python main.py --configs configs/train_covid19china_pspnet_timm-regnety_006_fold0.yml",
"python main.py --configs configs/train_covid19china_pspnet_timm-regnety_006_fold1.yml",
"python main.py --configs configs/train_covid19china_pspnet_timm-regnety_006_fold2.yml",
"python main.py --configs configs/train_covid19china_pspnet_timm-regnety_006_fold3.yml",
"python main.py --configs configs/train_covid19china_pspnet_timm-regnety_006_fold4.yml",
"python main.py --configs configs/train_covid19china_linknet_timm-regnety_006_fold0.yml",
"python main.py --configs configs/train_covid19china_linknet_timm-regnety_006_fold1.yml",
"python main.py --configs configs/train_covid19china_linknet_timm-regnety_006_fold2.yml",
"python main.py --configs configs/train_covid19china_linknet_timm-regnety_006_fold3.yml",
"python main.py --configs configs/train_covid19china_linknet_timm-regnety_006_fold4.yml",
"python main.py --configs configs/train_covid19china_manet_timm-regnety_006_fold0.yml",
"python main.py --configs configs/train_covid19china_manet_timm-regnety_006_fold1.yml",
"python main.py --configs configs/train_covid19china_manet_timm-regnety_006_fold2.yml",
"python main.py --configs configs/train_covid19china_manet_timm-regnety_006_fold3.yml",
"python main.py --configs configs/train_covid19china_manet_timm-regnety_006_fold4.yml",
]

for l in ls:
  os.system(l)