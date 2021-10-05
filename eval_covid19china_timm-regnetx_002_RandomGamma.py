import os

ls=["python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_0_RandomGamma.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_1_RandomGamma.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_2_RandomGamma.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_3_RandomGamma.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_4_RandomGamma.yml",
]

for l in ls:
  os.system(l)