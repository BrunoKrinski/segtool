import os

ls=["python main.py --configs configs/eval_medseg_unetplusplus_resnet101_0.yml",
"python main.py --configs configs/eval_medseg_unetplusplus_resnet101_1.yml",
"python main.py --configs configs/eval_medseg_unetplusplus_resnet101_2.yml",
"python main.py --configs configs/eval_medseg_unetplusplus_resnet101_3.yml",
"python main.py --configs configs/eval_medseg_unetplusplus_resnet101_4.yml",
"python main.py --configs configs/eval_medseg_unet_resnet101_0.yml",
"python main.py --configs configs/eval_medseg_unet_resnet101_1.yml",
"python main.py --configs configs/eval_medseg_unet_resnet101_2.yml",
"python main.py --configs configs/eval_medseg_unet_resnet101_3.yml",
"python main.py --configs configs/eval_medseg_unet_resnet101_4.yml",
"python main.py --configs configs/eval_medseg_fpn_resnet101_0.yml",
"python main.py --configs configs/eval_medseg_fpn_resnet101_1.yml",
"python main.py --configs configs/eval_medseg_fpn_resnet101_2.yml",
"python main.py --configs configs/eval_medseg_fpn_resnet101_3.yml",
"python main.py --configs configs/eval_medseg_fpn_resnet101_4.yml",
"python main.py --configs configs/eval_medseg_pspnet_resnet101_0.yml",
"python main.py --configs configs/eval_medseg_pspnet_resnet101_1.yml",
"python main.py --configs configs/eval_medseg_pspnet_resnet101_2.yml",
"python main.py --configs configs/eval_medseg_pspnet_resnet101_3.yml",
"python main.py --configs configs/eval_medseg_pspnet_resnet101_4.yml",
"python main.py --configs configs/eval_medseg_linknet_resnet101_0.yml",
"python main.py --configs configs/eval_medseg_linknet_resnet101_1.yml",
"python main.py --configs configs/eval_medseg_linknet_resnet101_2.yml",
"python main.py --configs configs/eval_medseg_linknet_resnet101_3.yml",
"python main.py --configs configs/eval_medseg_linknet_resnet101_4.yml",
"python main.py --configs configs/eval_medseg_pan_resnet101_0.yml",
"python main.py --configs configs/eval_medseg_pan_resnet101_1.yml",
"python main.py --configs configs/eval_medseg_pan_resnet101_2.yml",
"python main.py --configs configs/eval_medseg_pan_resnet101_3.yml",
"python main.py --configs configs/eval_medseg_pan_resnet101_4.yml",
"python main.py --configs configs/eval_medseg_manet_resnet101_0.yml",
"python main.py --configs configs/eval_medseg_manet_resnet101_1.yml",
"python main.py --configs configs/eval_medseg_manet_resnet101_2.yml",
"python main.py --configs configs/eval_medseg_manet_resnet101_3.yml",
"python main.py --configs configs/eval_medseg_manet_resnet101_4.yml",
"python main.py --configs configs/eval_medseg_deeplabv3_resnet101_0.yml",
"python main.py --configs configs/eval_medseg_deeplabv3_resnet101_1.yml",
"python main.py --configs configs/eval_medseg_deeplabv3_resnet101_2.yml",
"python main.py --configs configs/eval_medseg_deeplabv3_resnet101_3.yml",
"python main.py --configs configs/eval_medseg_deeplabv3_resnet101_4.yml",
"python main.py --configs configs/eval_medseg_deeplabv3plus_resnet101_0.yml",
"python main.py --configs configs/eval_medseg_deeplabv3plus_resnet101_1.yml",
"python main.py --configs configs/eval_medseg_deeplabv3plus_resnet101_2.yml",
"python main.py --configs configs/eval_medseg_deeplabv3plus_resnet101_3.yml",
"python main.py --configs configs/eval_medseg_deeplabv3plus_resnet101_4.yml",
]

for l in ls:
  os.system(l)