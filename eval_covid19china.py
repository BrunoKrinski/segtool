import os

ls=["python main.py --configs configs/eval_covid19china_unet_resnet50_0.yml",
"python main.py --configs configs/eval_covid19china_unet_resnet50_1.yml",
"python main.py --configs configs/eval_covid19china_unet_resnet50_2.yml",
"python main.py --configs configs/eval_covid19china_unet_resnet50_3.yml",
"python main.py --configs configs/eval_covid19china_unet_resnet50_4.yml",
"python main.py --configs configs/eval_covid19china_fpn_resnet50_0.yml",
"python main.py --configs configs/eval_covid19china_fpn_resnet50_1.yml",
"python main.py --configs configs/eval_covid19china_fpn_resnet50_2.yml",
"python main.py --configs configs/eval_covid19china_fpn_resnet50_3.yml",
"python main.py --configs configs/eval_covid19china_fpn_resnet50_4.yml",
"python main.py --configs configs/eval_covid19china_pspnet_resnet50_0.yml",
"python main.py --configs configs/eval_covid19china_pspnet_resnet50_1.yml",
"python main.py --configs configs/eval_covid19china_pspnet_resnet50_2.yml",
"python main.py --configs configs/eval_covid19china_pspnet_resnet50_3.yml",
"python main.py --configs configs/eval_covid19china_pspnet_resnet50_4.yml",
"python main.py --configs configs/eval_covid19china_linknet_resnet50_0.yml",
"python main.py --configs configs/eval_covid19china_linknet_resnet50_1.yml",
"python main.py --configs configs/eval_covid19china_linknet_resnet50_2.yml",
"python main.py --configs configs/eval_covid19china_linknet_resnet50_3.yml",
"python main.py --configs configs/eval_covid19china_linknet_resnet50_4.yml",
]

for l in ls:
  os.system(l)