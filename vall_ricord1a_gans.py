import os

runs = ['python eval_ricord1a_timm-regnetx_002_Stargan_0p05.py',
        'python eval_ricord1a_timm-regnetx_002_Stargan_0p1.py',
        'python eval_ricord1a_timm-regnetx_002_Stargan_0p15.py',
        'python eval_ricord1a_timm-regnetx_002_Stargan_0p2.py',
        'python eval_ricord1a_timm-regnetx_002_Stylegan_0p05.py',
        'python eval_ricord1a_timm-regnetx_002_Stylegan_0p1.py',
        'python eval_ricord1a_timm-regnetx_002_Stylegan_0p15.py',
        'python eval_ricord1a_timm-regnetx_002_Stylegan_0p2.py',]
        

for run in runs:
  os.system(run)
