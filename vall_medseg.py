import os

ls = ["python eval_medseg_timm-regnetx_002_RandomBrightnessContrast_0p15.py",
"python eval_medseg_timm-regnetx_002_RandomCrop_0p15.py",
"python eval_medseg_timm-regnetx_002_RandomGamma_0p15.py",
"python eval_medseg_timm-regnetx_002_RandomSnow_0p15.py",
"python eval_medseg_timm-regnetx_002_Rotate_0p15.py",
"python eval_medseg_timm-regnetx_002_Sharpen_0p15.py",
"python eval_medseg_timm-regnetx_002_ShiftScaleRotate_0p15.py",]

for l in ls:
    #print(l)
    os.system(l)