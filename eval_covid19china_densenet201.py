import os

ls=["python main.py --configs configs/eval_covid19china_unetplusplus_densenet201_0.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_densenet201_1.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_densenet201_2.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_densenet201_3.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_densenet201_4.yml",
"python main.py --configs configs/eval_covid19china_unet_densenet201_0.yml",
"python main.py --configs configs/eval_covid19china_unet_densenet201_1.yml",
"python main.py --configs configs/eval_covid19china_unet_densenet201_2.yml",
"python main.py --configs configs/eval_covid19china_unet_densenet201_3.yml",
"python main.py --configs configs/eval_covid19china_unet_densenet201_4.yml",
"python main.py --configs configs/eval_covid19china_fpn_densenet201_0.yml",
"python main.py --configs configs/eval_covid19china_fpn_densenet201_1.yml",
"python main.py --configs configs/eval_covid19china_fpn_densenet201_2.yml",
"python main.py --configs configs/eval_covid19china_fpn_densenet201_3.yml",
"python main.py --configs configs/eval_covid19china_fpn_densenet201_4.yml",
"python main.py --configs configs/eval_covid19china_pspnet_densenet201_0.yml",
"python main.py --configs configs/eval_covid19china_pspnet_densenet201_1.yml",
"python main.py --configs configs/eval_covid19china_pspnet_densenet201_2.yml",
"python main.py --configs configs/eval_covid19china_pspnet_densenet201_3.yml",
"python main.py --configs configs/eval_covid19china_pspnet_densenet201_4.yml",
"python main.py --configs configs/eval_covid19china_linknet_densenet201_0.yml",
"python main.py --configs configs/eval_covid19china_linknet_densenet201_1.yml",
"python main.py --configs configs/eval_covid19china_linknet_densenet201_2.yml",
"python main.py --configs configs/eval_covid19china_linknet_densenet201_3.yml",
"python main.py --configs configs/eval_covid19china_linknet_densenet201_4.yml",
"python main.py --configs configs/eval_covid19china_manet_densenet201_0.yml",
"python main.py --configs configs/eval_covid19china_manet_densenet201_1.yml",
"python main.py --configs configs/eval_covid19china_manet_densenet201_2.yml",
"python main.py --configs configs/eval_covid19china_manet_densenet201_3.yml",
"python main.py --configs configs/eval_covid19china_manet_densenet201_4.yml",
]

for l in ls:
  os.system(l)