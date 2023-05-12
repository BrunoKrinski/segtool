import os

runs = ['python train_ricord1a_timm-regnetx_002_noda_0p2_stargan.py',
        'python train_ricord1a_timm-regnetx_002_noda_0p2_stylegan.py']
        

for run in runs:
  os.system(run)
