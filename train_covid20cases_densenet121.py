import os

ls=["python main.py --configs configs/train_covid20cases_unetplusplus_densenet121_fold0.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_densenet121_fold1.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_densenet121_fold2.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_densenet121_fold3.yml",
"python main.py --configs configs/train_covid20cases_unetplusplus_densenet121_fold4.yml",
"python main.py --configs configs/train_covid20cases_unet_densenet121_fold0.yml",
"python main.py --configs configs/train_covid20cases_unet_densenet121_fold1.yml",
"python main.py --configs configs/train_covid20cases_unet_densenet121_fold2.yml",
"python main.py --configs configs/train_covid20cases_unet_densenet121_fold3.yml",
"python main.py --configs configs/train_covid20cases_unet_densenet121_fold4.yml",
"python main.py --configs configs/train_covid20cases_fpn_densenet121_fold0.yml",
"python main.py --configs configs/train_covid20cases_fpn_densenet121_fold1.yml",
"python main.py --configs configs/train_covid20cases_fpn_densenet121_fold2.yml",
"python main.py --configs configs/train_covid20cases_fpn_densenet121_fold3.yml",
"python main.py --configs configs/train_covid20cases_fpn_densenet121_fold4.yml",
"python main.py --configs configs/train_covid20cases_pspnet_densenet121_fold0.yml",
"python main.py --configs configs/train_covid20cases_pspnet_densenet121_fold1.yml",
"python main.py --configs configs/train_covid20cases_pspnet_densenet121_fold2.yml",
"python main.py --configs configs/train_covid20cases_pspnet_densenet121_fold3.yml",
"python main.py --configs configs/train_covid20cases_pspnet_densenet121_fold4.yml",
"python main.py --configs configs/train_covid20cases_linknet_densenet121_fold0.yml",
"python main.py --configs configs/train_covid20cases_linknet_densenet121_fold1.yml",
"python main.py --configs configs/train_covid20cases_linknet_densenet121_fold2.yml",
"python main.py --configs configs/train_covid20cases_linknet_densenet121_fold3.yml",
"python main.py --configs configs/train_covid20cases_linknet_densenet121_fold4.yml",
"python main.py --configs configs/train_covid20cases_manet_densenet121_fold0.yml",
"python main.py --configs configs/train_covid20cases_manet_densenet121_fold1.yml",
"python main.py --configs configs/train_covid20cases_manet_densenet121_fold2.yml",
"python main.py --configs configs/train_covid20cases_manet_densenet121_fold3.yml",
"python main.py --configs configs/train_covid20cases_manet_densenet121_fold4.yml",
]

for l in ls:
  os.system(l)