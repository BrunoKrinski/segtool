import os

ls=["python main.py --configs configs/train_covid20cases_unet_resnet50_fold0.yml",
"python main.py --configs configs/train_covid20cases_unet_resnet50_fold1.yml",
"python main.py --configs configs/train_covid20cases_unet_resnet50_fold2.yml",
"python main.py --configs configs/train_covid20cases_unet_resnet50_fold3.yml",
"python main.py --configs configs/train_covid20cases_unet_resnet50_fold4.yml",
"python main.py --configs configs/train_covid20cases_fpn_resnet50_fold0.yml",
"python main.py --configs configs/train_covid20cases_fpn_resnet50_fold1.yml",
"python main.py --configs configs/train_covid20cases_fpn_resnet50_fold2.yml",
"python main.py --configs configs/train_covid20cases_fpn_resnet50_fold3.yml",
"python main.py --configs configs/train_covid20cases_fpn_resnet50_fold4.yml",
"python main.py --configs configs/train_covid20cases_pspnet_resnet50_fold0.yml",
"python main.py --configs configs/train_covid20cases_pspnet_resnet50_fold1.yml",
"python main.py --configs configs/train_covid20cases_pspnet_resnet50_fold2.yml",
"python main.py --configs configs/train_covid20cases_pspnet_resnet50_fold3.yml",
"python main.py --configs configs/train_covid20cases_pspnet_resnet50_fold4.yml",
"python main.py --configs configs/train_covid20cases_linknet_resnet50_fold0.yml",
"python main.py --configs configs/train_covid20cases_linknet_resnet50_fold1.yml",
"python main.py --configs configs/train_covid20cases_linknet_resnet50_fold2.yml",
"python main.py --configs configs/train_covid20cases_linknet_resnet50_fold3.yml",
"python main.py --configs configs/train_covid20cases_linknet_resnet50_fold4.yml",
]

for l in ls:
  os.system(l)