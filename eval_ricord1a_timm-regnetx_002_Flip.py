import os

ls=["python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_0_Flip.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_1_Flip.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_2_Flip.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_3_Flip.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_4_Flip.yml",
]

for l in ls:
  os.system(l)