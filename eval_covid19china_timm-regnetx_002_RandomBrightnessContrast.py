import os

ls=["python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_0_RandomBrightnessContrast.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_1_RandomBrightnessContrast.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_2_RandomBrightnessContrast.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_3_RandomBrightnessContrast.yml",
"python main.py --configs configs/eval_covid19china_unetplusplus_timm-regnetx_002_4_RandomBrightnessContrast.yml",
]

for l in ls:
  os.system(l)