import os

ls=["python main.py --configs configs/eval_mosmed_resnet50_unet.yml",
"python main.py --configs configs/eval_mosmed_resnet50_unet.yml",
"python main.py --configs configs/eval_mosmed_resnet50_unet.yml",
"python main.py --configs configs/eval_mosmed_resnet50_unet.yml",
"python main.py --configs configs/eval_mosmed_resnet50_unet.yml",
"python main.py --configs configs/eval_mosmed_resnet50_fpn.yml",
"python main.py --configs configs/eval_mosmed_resnet50_fpn.yml",
"python main.py --configs configs/eval_mosmed_resnet50_fpn.yml",
"python main.py --configs configs/eval_mosmed_resnet50_fpn.yml",
"python main.py --configs configs/eval_mosmed_resnet50_fpn.yml",
"python main.py --configs configs/eval_mosmed_resnet50_pspnet.yml",
"python main.py --configs configs/eval_mosmed_resnet50_pspnet.yml",
"python main.py --configs configs/eval_mosmed_resnet50_pspnet.yml",
"python main.py --configs configs/eval_mosmed_resnet50_pspnet.yml",
"python main.py --configs configs/eval_mosmed_resnet50_pspnet.yml",
"python main.py --configs configs/eval_mosmed_resnet50_linknet.yml",
"python main.py --configs configs/eval_mosmed_resnet50_linknet.yml",
"python main.py --configs configs/eval_mosmed_resnet50_linknet.yml",
"python main.py --configs configs/eval_mosmed_resnet50_linknet.yml",
"python main.py --configs configs/eval_mosmed_resnet50_linknet.yml",
]

for l in ls:
  os.system(l)