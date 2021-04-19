import os

ls=["python main.py --configs configs/eval_ricord1a_unetplusplus_densenet201_0.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_densenet201_1.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_densenet201_2.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_densenet201_3.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_densenet201_4.yml",
"python main.py --configs configs/eval_ricord1a_unet_densenet201_0.yml",
"python main.py --configs configs/eval_ricord1a_unet_densenet201_1.yml",
"python main.py --configs configs/eval_ricord1a_unet_densenet201_2.yml",
"python main.py --configs configs/eval_ricord1a_unet_densenet201_3.yml",
"python main.py --configs configs/eval_ricord1a_unet_densenet201_4.yml",
"python main.py --configs configs/eval_ricord1a_fpn_densenet201_0.yml",
"python main.py --configs configs/eval_ricord1a_fpn_densenet201_1.yml",
"python main.py --configs configs/eval_ricord1a_fpn_densenet201_2.yml",
"python main.py --configs configs/eval_ricord1a_fpn_densenet201_3.yml",
"python main.py --configs configs/eval_ricord1a_fpn_densenet201_4.yml",
]

for l in ls:
  os.system(l)