import os

ls=["python main.py --configs configs/train_ricord1a_unetplusplus_densenet201_fold0.yml",
"python main.py --configs configs/train_ricord1a_unetplusplus_densenet201_fold1.yml",
"python main.py --configs configs/train_ricord1a_unetplusplus_densenet201_fold2.yml",
"python main.py --configs configs/train_ricord1a_unetplusplus_densenet201_fold3.yml",
"python main.py --configs configs/train_ricord1a_unetplusplus_densenet201_fold4.yml",
"python main.py --configs configs/train_ricord1a_unet_densenet201_fold0.yml",
"python main.py --configs configs/train_ricord1a_unet_densenet201_fold1.yml",
"python main.py --configs configs/train_ricord1a_unet_densenet201_fold2.yml",
"python main.py --configs configs/train_ricord1a_unet_densenet201_fold3.yml",
"python main.py --configs configs/train_ricord1a_unet_densenet201_fold4.yml",
"python main.py --configs configs/train_ricord1a_fpn_densenet201_fold0.yml",
"python main.py --configs configs/train_ricord1a_fpn_densenet201_fold1.yml",
"python main.py --configs configs/train_ricord1a_fpn_densenet201_fold2.yml",
"python main.py --configs configs/train_ricord1a_fpn_densenet201_fold3.yml",
"python main.py --configs configs/train_ricord1a_fpn_densenet201_fold4.yml",
"python main.py --configs configs/train_ricord1a_pspnet_densenet201_fold0.yml",
"python main.py --configs configs/train_ricord1a_pspnet_densenet201_fold1.yml",
"python main.py --configs configs/train_ricord1a_pspnet_densenet201_fold2.yml",
"python main.py --configs configs/train_ricord1a_pspnet_densenet201_fold3.yml",
"python main.py --configs configs/train_ricord1a_pspnet_densenet201_fold4.yml",
"python main.py --configs configs/train_ricord1a_linknet_densenet201_fold0.yml",
"python main.py --configs configs/train_ricord1a_linknet_densenet201_fold1.yml",
"python main.py --configs configs/train_ricord1a_linknet_densenet201_fold2.yml",
"python main.py --configs configs/train_ricord1a_linknet_densenet201_fold3.yml",
"python main.py --configs configs/train_ricord1a_linknet_densenet201_fold4.yml",
"python main.py --configs configs/train_ricord1a_manet_densenet201_fold0.yml",
"python main.py --configs configs/train_ricord1a_manet_densenet201_fold1.yml",
"python main.py --configs configs/train_ricord1a_manet_densenet201_fold2.yml",
"python main.py --configs configs/train_ricord1a_manet_densenet201_fold3.yml",
"python main.py --configs configs/train_ricord1a_manet_densenet201_fold4.yml",
]

for l in ls:
  os.system(l)