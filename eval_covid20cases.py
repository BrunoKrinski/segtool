import os

ls=["python main.py --configs configs/eval_covid20cases_unet_resnet50_0.yml",
"python main.py --configs configs/eval_covid20cases_unet_resnet50_1.yml",
"python main.py --configs configs/eval_covid20cases_unet_resnet50_2.yml",
"python main.py --configs configs/eval_covid20cases_unet_resnet50_3.yml",
"python main.py --configs configs/eval_covid20cases_unet_resnet50_4.yml",
"python main.py --configs configs/eval_covid20cases_fpn_resnet50_0.yml",
"python main.py --configs configs/eval_covid20cases_fpn_resnet50_1.yml",
"python main.py --configs configs/eval_covid20cases_fpn_resnet50_2.yml",
"python main.py --configs configs/eval_covid20cases_fpn_resnet50_3.yml",
"python main.py --configs configs/eval_covid20cases_fpn_resnet50_4.yml",
"python main.py --configs configs/eval_covid20cases_pspnet_resnet50_0.yml",
"python main.py --configs configs/eval_covid20cases_pspnet_resnet50_1.yml",
"python main.py --configs configs/eval_covid20cases_pspnet_resnet50_2.yml",
"python main.py --configs configs/eval_covid20cases_pspnet_resnet50_3.yml",
"python main.py --configs configs/eval_covid20cases_pspnet_resnet50_4.yml",
"python main.py --configs configs/eval_covid20cases_linknet_resnet50_0.yml",
"python main.py --configs configs/eval_covid20cases_linknet_resnet50_1.yml",
"python main.py --configs configs/eval_covid20cases_linknet_resnet50_2.yml",
"python main.py --configs configs/eval_covid20cases_linknet_resnet50_3.yml",
"python main.py --configs configs/eval_covid20cases_linknet_resnet50_4.yml",
]

for l in ls:
  os.system(l)