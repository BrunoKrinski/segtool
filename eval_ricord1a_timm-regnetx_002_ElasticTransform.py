import os

ls=["python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_0_ElasticTransform.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_1_ElasticTransform.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_2_ElasticTransform.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_3_ElasticTransform.yml",
"python main.py --configs configs/eval_ricord1a_unetplusplus_timm-regnetx_002_4_ElasticTransform.yml",
]

for l in ls:
  os.system(l)