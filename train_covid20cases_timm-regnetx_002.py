import os

ls=["python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold0.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold1.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold2.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold3.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_timm-regnetx_002_fold4.yml",
"python main.py --configs configs/train_covid20cases_unet_timm-regnetx_002_fold0.yml",
"python main.py --configs configs/train_covid20cases_unet_timm-regnetx_002_fold1.yml",
"python main.py --configs configs/train_covid20cases_unet_timm-regnetx_002_fold2.yml",
"python main.py --configs configs/train_covid20cases_unet_timm-regnetx_002_fold3.yml",
"python main.py --configs configs/train_covid20cases_unet_timm-regnetx_002_fold4.yml",
"python main.py --configs configs/train_covid20cases_fpn_timm-regnetx_002_fold0.yml",
"python main.py --configs configs/train_covid20cases_fpn_timm-regnetx_002_fold1.yml",
"python main.py --configs configs/train_covid20cases_fpn_timm-regnetx_002_fold2.yml",
"python main.py --configs configs/train_covid20cases_fpn_timm-regnetx_002_fold3.yml",
"python main.py --configs configs/train_covid20cases_fpn_timm-regnetx_002_fold4.yml",
"python main.py --configs configs/train_covid20cases_pspnet_timm-regnetx_002_fold0.yml",
"python main.py --configs configs/train_covid20cases_pspnet_timm-regnetx_002_fold1.yml",
"python main.py --configs configs/train_covid20cases_pspnet_timm-regnetx_002_fold2.yml",
"python main.py --configs configs/train_covid20cases_pspnet_timm-regnetx_002_fold3.yml",
"python main.py --configs configs/train_covid20cases_pspnet_timm-regnetx_002_fold4.yml",
"python main.py --configs configs/train_covid20cases_linknet_timm-regnetx_002_fold0.yml",
"python main.py --configs configs/train_covid20cases_linknet_timm-regnetx_002_fold1.yml",
"python main.py --configs configs/train_covid20cases_linknet_timm-regnetx_002_fold2.yml",
"python main.py --configs configs/train_covid20cases_linknet_timm-regnetx_002_fold3.yml",
"python main.py --configs configs/train_covid20cases_linknet_timm-regnetx_002_fold4.yml",
"python main.py --configs configs/train_covid20cases_manet_timm-regnetx_002_fold0.yml",
"python main.py --configs configs/train_covid20cases_manet_timm-regnetx_002_fold1.yml",
"python main.py --configs configs/train_covid20cases_manet_timm-regnetx_002_fold2.yml",
"python main.py --configs configs/train_covid20cases_manet_timm-regnetx_002_fold3.yml",
"python main.py --configs configs/train_covid20cases_manet_timm-regnetx_002_fold4.yml",
]

for l in ls:
  os.system(l)