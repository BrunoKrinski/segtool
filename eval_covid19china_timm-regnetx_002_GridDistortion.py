import os

ls=["python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_0_GridDistortion.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_1_GridDistortion.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_2_GridDistortion.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_3_GridDistortion.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_4_GridDistortion.yml",
]

for l in ls:
  os.system(l)