import os

ls=["python main.py --configs configs/eval_covid19china_unetplusplus_resnet101_0.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_resnet101_1.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_resnet101_2.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_resnet101_3.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_resnet101_4.yml",
"python main.py --configs configs/eval_covid19china_unet_resnet101_0.yml",
"python main.py --configs configs/eval_covid19china_unet_resnet101_1.yml",
"python main.py --configs configs/eval_covid19china_unet_resnet101_2.yml",
"python main.py --configs configs/eval_covid19china_unet_resnet101_3.yml",
"python main.py --configs configs/eval_covid19china_unet_resnet101_4.yml",
"python main.py --configs configs/eval_covid19china_fpn_resnet101_0.yml",
"python main.py --configs configs/eval_covid19china_fpn_resnet101_1.yml",
"python main.py --configs configs/eval_covid19china_fpn_resnet101_2.yml",
"python main.py --configs configs/eval_covid19china_fpn_resnet101_3.yml",
"python main.py --configs configs/eval_covid19china_fpn_resnet101_4.yml",
"python main.py --configs configs/eval_covid19china_pspnet_resnet101_0.yml",
"python main.py --configs configs/eval_covid19china_pspnet_resnet101_1.yml",
"python main.py --configs configs/eval_covid19china_pspnet_resnet101_2.yml",
"python main.py --configs configs/eval_covid19china_pspnet_resnet101_3.yml",
"python main.py --configs configs/eval_covid19china_pspnet_resnet101_4.yml",
"python main.py --configs configs/eval_covid19china_linknet_resnet101_0.yml",
"python main.py --configs configs/eval_covid19china_linknet_resnet101_1.yml",
"python main.py --configs configs/eval_covid19china_linknet_resnet101_2.yml",
"python main.py --configs configs/eval_covid19china_linknet_resnet101_3.yml",
"python main.py --configs configs/eval_covid19china_linknet_resnet101_4.yml",
"python main.py --configs configs/eval_covid19china_manet_resnet101_0.yml",
"python main.py --configs configs/eval_covid19china_manet_resnet101_1.yml",
"python main.py --configs configs/eval_covid19china_manet_resnet101_2.yml",
"python main.py --configs configs/eval_covid19china_manet_resnet101_3.yml",
"python main.py --configs configs/eval_covid19china_manet_resnet101_4.yml",
]

for l in ls:
  os.system(l)