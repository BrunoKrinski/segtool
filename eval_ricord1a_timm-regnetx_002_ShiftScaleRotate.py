import os

ls=["python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_0_ShiftScaleRotate.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_1_ShiftScaleRotate.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_2_ShiftScaleRotate.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_3_ShiftScaleRotate.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_4_ShiftScaleRotate.yml",
]

for l in ls:
  os.system(l)