import os

ls=["python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_0_Clahe.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_1_Clahe.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_2_Clahe.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_3_Clahe.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_4_Clahe.yml",
]

for l in ls:
  os.system(l)