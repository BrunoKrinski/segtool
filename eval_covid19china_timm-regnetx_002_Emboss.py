import os

ls=["python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_0_Emboss.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_1_Emboss.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_2_Emboss.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_3_Emboss.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_4_Emboss.yml",
]

for l in ls:
  os.system(l)