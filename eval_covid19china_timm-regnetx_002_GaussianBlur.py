import os

ls=["python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_0_GaussianBlur.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_1_GaussianBlur.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_2_GaussianBlur.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_3_GaussianBlur.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_4_GaussianBlur.yml",
]

for l in ls:
  os.system(l)