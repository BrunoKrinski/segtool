import os

ls=["python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_0_MedianBlur.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_1_MedianBlur.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_2_MedianBlur.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_3_MedianBlur.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_4_MedianBlur.yml",
]

for l in ls:
  os.system(l)