import os

ls=["python main.py --configs configs/eval_covid19china_unetplusplus_resnext101_32x8d_0.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_resnext101_32x8d_1.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_resnext101_32x8d_2.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_resnext101_32x8d_3.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_resnext101_32x8d_4.yml",
"python main.py --configs configs/eval_covid19china_unet_resnext101_32x8d_0.yml",
"python main.py --configs configs/eval_covid19china_unet_resnext101_32x8d_1.yml",
"python main.py --configs configs/eval_covid19china_unet_resnext101_32x8d_2.yml",
"python main.py --configs configs/eval_covid19china_unet_resnext101_32x8d_3.yml",
"python main.py --configs configs/eval_covid19china_unet_resnext101_32x8d_4.yml",
"python main.py --configs configs/eval_covid19china_fpn_resnext101_32x8d_0.yml",
"python main.py --configs configs/eval_covid19china_fpn_resnext101_32x8d_1.yml",
"python main.py --configs configs/eval_covid19china_fpn_resnext101_32x8d_2.yml",
"python main.py --configs configs/eval_covid19china_fpn_resnext101_32x8d_3.yml",
"python main.py --configs configs/eval_covid19china_fpn_resnext101_32x8d_4.yml",
"python main.py --configs configs/eval_covid19china_pspnet_resnext101_32x8d_0.yml",
"python main.py --configs configs/eval_covid19china_pspnet_resnext101_32x8d_1.yml",
"python main.py --configs configs/eval_covid19china_pspnet_resnext101_32x8d_2.yml",
"python main.py --configs configs/eval_covid19china_pspnet_resnext101_32x8d_3.yml",
"python main.py --configs configs/eval_covid19china_pspnet_resnext101_32x8d_4.yml",
"python main.py --configs configs/eval_covid19china_linknet_resnext101_32x8d_0.yml",
"python main.py --configs configs/eval_covid19china_linknet_resnext101_32x8d_1.yml",
"python main.py --configs configs/eval_covid19china_linknet_resnext101_32x8d_2.yml",
"python main.py --configs configs/eval_covid19china_linknet_resnext101_32x8d_3.yml",
"python main.py --configs configs/eval_covid19china_linknet_resnext101_32x8d_4.yml",
"python main.py --configs configs/eval_covid19china_manet_resnext101_32x8d_0.yml",
"python main.py --configs configs/eval_covid19china_manet_resnext101_32x8d_1.yml",
"python main.py --configs configs/eval_covid19china_manet_resnext101_32x8d_2.yml",
"python main.py --configs configs/eval_covid19china_manet_resnext101_32x8d_3.yml",
"python main.py --configs configs/eval_covid19china_manet_resnext101_32x8d_4.yml",
]

for l in ls:
  os.system(l)