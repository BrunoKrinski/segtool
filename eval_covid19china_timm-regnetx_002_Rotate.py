import os

ls=["python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_0_Rotate.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_1_Rotate.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_2_Rotate.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_3_Rotate.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_4_Rotate.yml",
]

for l in ls:
  os.system(l)