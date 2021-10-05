import os

ls=["python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_0_OpticalDistortion.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_1_OpticalDistortion.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_2_OpticalDistortion.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_3_OpticalDistortion.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_4_OpticalDistortion.yml",
]

for l in ls:
  os.system(l)