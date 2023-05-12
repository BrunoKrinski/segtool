import os

ls = ["python eval_covid19china_timm-regnetx_002_ElasticTransform_0p3.py",
"python eval_covid20cases_timm-regnetx_002_ElasticTransform_0p3.py",
"python eval_medseg_timm-regnetx_002_ElasticTransform_0p3.py",
"python eval_mosmed_timm-regnetx_002_ElasticTransform_0p3.py",
"python eval_ricord1a_timm-regnetx_002_ElasticTransform_0p3.py",]

for l in ls:
    #print(l)
    os.system(l)