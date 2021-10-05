import os

ls=["python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_0_Sharpen.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_1_Sharpen.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_2_Sharpen.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_3_Sharpen.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_4_Sharpen.yml",
]

for l in ls:
  os.system(l)