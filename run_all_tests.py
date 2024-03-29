import os

runs = ['python eval_covid19china_resnet50.py',
        'python eval_covid19china_resnet101.py',
        'python eval_covid19china_resnext50_32x4d.py',
        'python eval_covid19china_resnext101_32x8d.py',
        'python eval_covid19china_timm-res2net50_26w_4s.py',
        'python eval_covid19china_timm-res2net101_26w_4s.py',
        'python eval_covid19china_vgg16.py',
        'python eval_covid19china_densenet121.py',
        'python eval_covid19china_densenet169.py',
        'python eval_covid19china_densenet201.py',
        'python eval_covid19china_se_resnet50.py',
        'python eval_covid19china_se_resnet101.py',
        'python eval_covid19china_se_resnext50_32x4d.py',
        'python eval_covid19china_se_resnext101_32x4d.py',
        'python eval_covid19china_timm-regnetx_002.py',
        'python eval_covid19china_timm-regnetx_004.py',
        'python eval_covid19china_timm-regnetx_006.py',
        'python eval_covid19china_timm-regnety_002.py',
        'python eval_covid19china_timm-regnety_004.py',
        'python eval_covid19china_timm-regnety_006.py',
        'python eval_covid20cases_resnet50.py',
        'python eval_covid20cases_resnet101.py',
        'python eval_covid20cases_resnext50_32x4d.py',
        'python eval_covid20cases_resnext101_32x8d.py',
        'python eval_covid20cases_timm-res2net50_26w_4s.py',
        'python eval_covid20cases_timm-res2net101_26w_4s.py',
        'python eval_covid20cases_vgg16.py',
        'python eval_covid20cases_densenet121.py',
        'python eval_covid20cases_densenet169.py',
        'python eval_covid20cases_densenet201.py',
        'python eval_covid20cases_se_resnet50.py',
        'python eval_covid20cases_se_resnet101.py',
        'python eval_covid20cases_se_resnext50_32x4d.py',
        'python eval_covid20cases_se_resnext101_32x4d.py',
        'python eval_covid20cases_timm-regnetx_002.py',
        'python eval_covid20cases_timm-regnetx_004.py',
        'python eval_covid20cases_timm-regnetx_006.py',
        'python eval_covid20cases_timm-regnety_002.py',
        'python eval_covid20cases_timm-regnety_004.py',
        'python eval_covid20cases_timm-regnety_006.py',
        'python eval_medseg_resnet50.py',
        'python eval_medseg_resnet101.py',
        'python eval_medseg_resnext50_32x4d.py',
        'python eval_medseg_resnext101_32x8d.py',
        'python eval_medseg_timm-res2net50_26w_4s.py',
        'python eval_medseg_timm-res2net101_26w_4s.py',
        'python eval_medseg_vgg16.py',
        'python eval_medseg_densenet121.py',
        'python eval_medseg_densenet169.py',
        'python eval_medseg_densenet201.py',
        'python eval_medseg_se_resnet50.py',
        'python eval_medseg_se_resnet101.py',
        'python eval_medseg_se_resnext50_32x4d.py',
        'python eval_medseg_se_resnext101_32x4d.py',
        'python eval_medseg_timm-regnetx_002.py',
        'python eval_medseg_timm-regnetx_004.py',
        'python eval_medseg_timm-regnetx_006.py',
        'python eval_medseg_timm-regnety_002.py',
        'python eval_medseg_timm-regnety_004.py',
        'python eval_medseg_timm-regnety_006.py',
        'python eval_mosmed_resnet50.py',
        'python eval_mosmed_resnet101.py',
        'python eval_mosmed_resnext50_32x4d.py',
        'python eval_mosmed_resnext101_32x8d.py',
        'python eval_mosmed_timm-res2net50_26w_4s.py',
        'python eval_mosmed_timm-res2net101_26w_4s.py',
        'python eval_mosmed_vgg16.py',
        'python eval_mosmed_densenet121.py',
        'python eval_mosmed_densenet169.py',
        'python eval_mosmed_densenet201.py',
        'python eval_mosmed_se_resnet50.py',
        'python eval_mosmed_se_resnet101.py',
        'python eval_mosmed_se_resnext50_32x4d.py',
        'python eval_mosmed_se_resnext101_32x4d.py',
        'python eval_mosmed_timm-regnetx_002.py',
        'python eval_mosmed_timm-regnetx_004.py',
        'python eval_mosmed_timm-regnetx_006.py',
        'python eval_mosmed_timm-regnety_002.py',
        'python eval_mosmed_timm-regnety_004.py',
        'python eval_mosmed_timm-regnety_006.py',
        'python eval_ricord1a_resnet50.py',
        'python eval_ricord1a_resnet101.py',
        'python eval_ricord1a_resnext50_32x4d.py',
        'python eval_ricord1a_resnext101_32x8d.py',
        'python eval_ricord1a_timm-res2net50_26w_4s.py',
        'python eval_ricord1a_timm-res2net101_26w_4s.py',
        'python eval_ricord1a_vgg16.py',
        'python eval_ricord1a_densenet121.py',
        'python eval_ricord1a_densenet169.py',
        'python eval_ricord1a_densenet201.py',
        'python eval_ricord1a_se_resnet50.py',
        'python eval_ricord1a_se_resnet101.py',
        'python eval_ricord1a_se_resnext50_32x4d.py',
        'python eval_ricord1a_se_resnext101_32x4d.py',
        'python eval_ricord1a_timm-regnetx_002.py',
        'python eval_ricord1a_timm-regnetx_004.py',
        'python eval_ricord1a_timm-regnetx_006.py',
        'python eval_ricord1a_timm-regnety_002.py',
        'python eval_ricord1a_timm-regnety_004.py',
        'python eval_ricord1a_timm-regnety_006.py']

for run in runs:
  os.system(run)
