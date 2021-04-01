import os

ls=["python main.py --configs configs/eval_covid20cases_unetplusplus_resnext101_32x8d_0.yml",
"python main.py --configs configs/eval_covid20cases_unetplusplus_resnext101_32x8d_1.yml",
"python main.py --configs configs/eval_covid20cases_unetplusplus_resnext101_32x8d_2.yml",
"python main.py --configs configs/eval_covid20cases_unetplusplus_resnext101_32x8d_3.yml",
"python main.py --configs configs/eval_covid20cases_unetplusplus_resnext101_32x8d_4.yml",
"python main.py --configs configs/eval_covid20cases_unet_resnext101_32x8d_0.yml",
"python main.py --configs configs/eval_covid20cases_unet_resnext101_32x8d_1.yml",
"python main.py --configs configs/eval_covid20cases_unet_resnext101_32x8d_2.yml",
"python main.py --configs configs/eval_covid20cases_unet_resnext101_32x8d_3.yml",
"python main.py --configs configs/eval_covid20cases_unet_resnext101_32x8d_4.yml",
"python main.py --configs configs/eval_covid20cases_fpn_resnext101_32x8d_0.yml",
"python main.py --configs configs/eval_covid20cases_fpn_resnext101_32x8d_1.yml",
"python main.py --configs configs/eval_covid20cases_fpn_resnext101_32x8d_2.yml",
"python main.py --configs configs/eval_covid20cases_fpn_resnext101_32x8d_3.yml",
"python main.py --configs configs/eval_covid20cases_fpn_resnext101_32x8d_4.yml",
"python main.py --configs configs/eval_covid20cases_pspnet_resnext101_32x8d_0.yml",
"python main.py --configs configs/eval_covid20cases_pspnet_resnext101_32x8d_1.yml",
"python main.py --configs configs/eval_covid20cases_pspnet_resnext101_32x8d_2.yml",
"python main.py --configs configs/eval_covid20cases_pspnet_resnext101_32x8d_3.yml",
"python main.py --configs configs/eval_covid20cases_pspnet_resnext101_32x8d_4.yml",
"python main.py --configs configs/eval_covid20cases_linknet_resnext101_32x8d_0.yml",
"python main.py --configs configs/eval_covid20cases_linknet_resnext101_32x8d_1.yml",
"python main.py --configs configs/eval_covid20cases_linknet_resnext101_32x8d_2.yml",
"python main.py --configs configs/eval_covid20cases_linknet_resnext101_32x8d_3.yml",
"python main.py --configs configs/eval_covid20cases_linknet_resnext101_32x8d_4.yml",
"python main.py --configs configs/eval_covid20cases_pan_resnext101_32x8d_0.yml",
"python main.py --configs configs/eval_covid20cases_pan_resnext101_32x8d_1.yml",
"python main.py --configs configs/eval_covid20cases_pan_resnext101_32x8d_2.yml",
"python main.py --configs configs/eval_covid20cases_pan_resnext101_32x8d_3.yml",
"python main.py --configs configs/eval_covid20cases_pan_resnext101_32x8d_4.yml",
"python main.py --configs configs/eval_covid20cases_manet_resnext101_32x8d_0.yml",
"python main.py --configs configs/eval_covid20cases_manet_resnext101_32x8d_1.yml",
"python main.py --configs configs/eval_covid20cases_manet_resnext101_32x8d_2.yml",
"python main.py --configs configs/eval_covid20cases_manet_resnext101_32x8d_3.yml",
"python main.py --configs configs/eval_covid20cases_manet_resnext101_32x8d_4.yml",
"python main.py --configs configs/eval_covid20cases_deeplabv3_resnext101_32x8d_0.yml",
"python main.py --configs configs/eval_covid20cases_deeplabv3_resnext101_32x8d_1.yml",
"python main.py --configs configs/eval_covid20cases_deeplabv3_resnext101_32x8d_2.yml",
"python main.py --configs configs/eval_covid20cases_deeplabv3_resnext101_32x8d_3.yml",
"python main.py --configs configs/eval_covid20cases_deeplabv3_resnext101_32x8d_4.yml",
"python main.py --configs configs/eval_covid20cases_deeplabv3plus_resnext101_32x8d_0.yml",
"python main.py --configs configs/eval_covid20cases_deeplabv3plus_resnext101_32x8d_1.yml",
"python main.py --configs configs/eval_covid20cases_deeplabv3plus_resnext101_32x8d_2.yml",
"python main.py --configs configs/eval_covid20cases_deeplabv3plus_resnext101_32x8d_3.yml",
"python main.py --configs configs/eval_covid20cases_deeplabv3plus_resnext101_32x8d_4.yml",
]

for l in ls:
  os.system(l)