import os

ls=["python main.py --configs configs/eval_covid19china_unetplusplus_vgg16_0.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_vgg16_1.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_vgg16_2.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_vgg16_3.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_vgg16_4.yml",
"python main.py --configs configs/eval_covid19china_unet_vgg16_0.yml",
"python main.py --configs configs/eval_covid19china_unet_vgg16_1.yml",
"python main.py --configs configs/eval_covid19china_unet_vgg16_2.yml",
"python main.py --configs configs/eval_covid19china_unet_vgg16_3.yml",
"python main.py --configs configs/eval_covid19china_unet_vgg16_4.yml",
"python main.py --configs configs/eval_covid19china_fpn_vgg16_0.yml",
"python main.py --configs configs/eval_covid19china_fpn_vgg16_1.yml",
"python main.py --configs configs/eval_covid19china_fpn_vgg16_2.yml",
"python main.py --configs configs/eval_covid19china_fpn_vgg16_3.yml",
"python main.py --configs configs/eval_covid19china_fpn_vgg16_4.yml",
"python main.py --configs configs/eval_covid19china_pspnet_vgg16_0.yml",
"python main.py --configs configs/eval_covid19china_pspnet_vgg16_1.yml",
"python main.py --configs configs/eval_covid19china_pspnet_vgg16_2.yml",
"python main.py --configs configs/eval_covid19china_pspnet_vgg16_3.yml",
"python main.py --configs configs/eval_covid19china_pspnet_vgg16_4.yml",
"python main.py --configs configs/eval_covid19china_linknet_vgg16_0.yml",
"python main.py --configs configs/eval_covid19china_linknet_vgg16_1.yml",
"python main.py --configs configs/eval_covid19china_linknet_vgg16_2.yml",
"python main.py --configs configs/eval_covid19china_linknet_vgg16_3.yml",
"python main.py --configs configs/eval_covid19china_linknet_vgg16_4.yml",
"python main.py --configs configs/eval_covid19china_manet_vgg16_0.yml",
"python main.py --configs configs/eval_covid19china_manet_vgg16_1.yml",
"python main.py --configs configs/eval_covid19china_manet_vgg16_2.yml",
"python main.py --configs configs/eval_covid19china_manet_vgg16_3.yml",
"python main.py --configs configs/eval_covid19china_manet_vgg16_4.yml",
]

for l in ls:
  os.system(l)