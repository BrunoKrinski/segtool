import os

ls=["python main.py --configs configs/mosmed_resnet50_unet_fold0.yml",
"python main.py --configs configs/mosmed_resnet50_fpn_fold0.yml",
"python main.py --configs configs/mosmed_resnet50_pspnet_fold0.yml",
"python main.py --configs configs/mosmed_resnet50_linknet_fold0.yml",
"python main.py --configs configs/mosmed_resnet50_unet_fold1.yml",
"python main.py --configs configs/mosmed_resnet50_fpn_fold1.yml",
"python main.py --configs configs/mosmed_resnet50_pspnet_fold1.yml",
"python main.py --configs configs/mosmed_resnet50_linknet_fold1.yml",
"python main.py --configs configs/mosmed_resnet50_unet_fold2.yml",
"python main.py --configs configs/mosmed_resnet50_fpn_fold2.yml",
"python main.py --configs configs/mosmed_resnet50_pspnet_fold2.yml",
"python main.py --configs configs/mosmed_resnet50_linknet_fold2.yml",
"python main.py --configs configs/mosmed_resnet50_unet_fold3.yml",
"python main.py --configs configs/mosmed_resnet50_fpn_fold3.yml",
"python main.py --configs configs/mosmed_resnet50_pspnet_fold3.yml",
"python main.py --configs configs/mosmed_resnet50_linknet_fold3.yml",
"python main.py --configs configs/mosmed_resnet50_unet_fold4.yml",
"python main.py --configs configs/mosmed_resnet50_fpn_fold4.yml",
"python main.py --configs configs/mosmed_resnet50_pspnet_fold4.yml",
"python main.py --configs configs/mosmed_resnet50_linknet_fold4.yml",
]

for l in ls:
  os.system(l)