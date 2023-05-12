import os

ls = ["python eval_covid19china_timm-regnetx_002_Clahe_0p35.py",
"python eval_covid19china_timm-regnetx_002_CoarseDropout_0p35.py",
"python eval_covid19china_timm-regnetx_002_ElasticTransform_0p35.py",
"python eval_covid19china_timm-regnetx_002_Emboss_0p35.py",
"python eval_covid19china_timm-regnetx_002_Flip_0p35.py",
"python eval_covid19china_timm-regnetx_002_GaussianBlur_0p35.py",
"python eval_covid19china_timm-regnetx_002_GridDistortion_0p35.py",
"python eval_covid19china_timm-regnetx_002_GridDropout_0p35.py",
"python eval_covid19china_timm-regnetx_002_ImageCompression_0p35.py",
"python eval_covid19china_timm-regnetx_002_MedianBlur_0p35.py",
"python eval_covid19china_timm-regnetx_002_noda_0p35.py",
"python eval_covid19china_timm-regnetx_002_OpticalDistortion_0p35.py",
"python eval_covid19china_timm-regnetx_002_PiecewiseAffine_0p35.py",
"python eval_covid19china_timm-regnetx_002_Posterize_0p35.py",
"python eval_covid19china_timm-regnetx_002_RandomBrightnessContrast_0p35.py",
"python eval_covid19china_timm-regnetx_002_RandomCrop_0p35.py",
"python eval_covid19china_timm-regnetx_002_RandomGamma_0p35.py",
"python eval_covid19china_timm-regnetx_002_RandomSnow_0p35.py",
"python eval_covid19china_timm-regnetx_002_Rotate_0p35.py",
"python eval_covid19china_timm-regnetx_002_Sharpen_0p35.py",
"python eval_covid19china_timm-regnetx_002_ShiftScaleRotate_0p35.py",
"python eval_covid20cases_timm-regnetx_002_Clahe_0p35.py",
"python eval_covid20cases_timm-regnetx_002_CoarseDropout_0p35.py",
"python eval_covid20cases_timm-regnetx_002_ElasticTransform_0p35.py",
"python eval_covid20cases_timm-regnetx_002_Emboss_0p35.py",
"python eval_covid20cases_timm-regnetx_002_Flip_0p35.py",
"python eval_covid20cases_timm-regnetx_002_GaussianBlur_0p35.py",
"python eval_covid20cases_timm-regnetx_002_GridDistortion_0p35.py",
"python eval_covid20cases_timm-regnetx_002_GridDropout_0p35.py",
"python eval_covid20cases_timm-regnetx_002_ImageCompression_0p35.py",
"python eval_covid20cases_timm-regnetx_002_MedianBlur_0p35.py",
"python eval_covid20cases_timm-regnetx_002_noda_0p35.py",
"python eval_covid20cases_timm-regnetx_002_OpticalDistortion_0p35.py",
"python eval_covid20cases_timm-regnetx_002_PiecewiseAffine_0p35.py",
"python eval_covid20cases_timm-regnetx_002_Posterize_0p35.py",
"python eval_covid20cases_timm-regnetx_002_RandomBrightnessContrast_0p35.py",
"python eval_covid20cases_timm-regnetx_002_RandomCrop_0p35.py",
"python eval_covid20cases_timm-regnetx_002_RandomGamma_0p35.py",
"python eval_covid20cases_timm-regnetx_002_RandomSnow_0p35.py",
"python eval_covid20cases_timm-regnetx_002_Rotate_0p35.py",
"python eval_covid20cases_timm-regnetx_002_Sharpen_0p35.py",
"python eval_covid20cases_timm-regnetx_002_ShiftScaleRotate_0p35.py",
"python eval_medseg_timm-regnetx_002_Clahe_0p35.py",
"python eval_medseg_timm-regnetx_002_CoarseDropout_0p35.py",
"python eval_medseg_timm-regnetx_002_ElasticTransform_0p35.py",
"python eval_medseg_timm-regnetx_002_Emboss_0p35.py",
"python eval_medseg_timm-regnetx_002_Flip_0p35.py",
"python eval_medseg_timm-regnetx_002_GaussianBlur_0p35.py",
"python eval_medseg_timm-regnetx_002_GridDistortion_0p35.py",
"python eval_medseg_timm-regnetx_002_GridDropout_0p35.py",
"python eval_medseg_timm-regnetx_002_ImageCompression_0p35.py",
"python eval_medseg_timm-regnetx_002_MedianBlur_0p35.py",
"python eval_medseg_timm-regnetx_002_noda_0p35.py",
"python eval_medseg_timm-regnetx_002_OpticalDistortion_0p35.py",
"python eval_medseg_timm-regnetx_002_PiecewiseAffine_0p35.py",
"python eval_medseg_timm-regnetx_002_Posterize_0p35.py",
"python eval_medseg_timm-regnetx_002_RandomBrightnessContrast_0p35.py",
"python eval_medseg_timm-regnetx_002_RandomCrop_0p35.py",
"python eval_medseg_timm-regnetx_002_RandomGamma_0p35.py",
"python eval_medseg_timm-regnetx_002_RandomSnow_0p35.py",
"python eval_medseg_timm-regnetx_002_Rotate_0p35.py",
"python eval_medseg_timm-regnetx_002_Sharpen_0p35.py",
"python eval_medseg_timm-regnetx_002_ShiftScaleRotate_0p35.py",
"python eval_mosmed_timm-regnetx_002_Clahe_0p35.py",
"python eval_mosmed_timm-regnetx_002_CoarseDropout_0p35.py",
"python eval_mosmed_timm-regnetx_002_ElasticTransform_0p35.py",
"python eval_mosmed_timm-regnetx_002_Emboss_0p35.py",
"python eval_mosmed_timm-regnetx_002_Flip_0p35.py",
"python eval_mosmed_timm-regnetx_002_GaussianBlur_0p35.py",
"python eval_mosmed_timm-regnetx_002_GridDistortion_0p35.py",
"python eval_mosmed_timm-regnetx_002_GridDropout_0p35.py",
"python eval_mosmed_timm-regnetx_002_ImageCompression_0p35.py",
"python eval_mosmed_timm-regnetx_002_MedianBlur_0p35.py",
"python eval_mosmed_timm-regnetx_002_noda_0p35.py",
"python eval_mosmed_timm-regnetx_002_OpticalDistortion_0p35.py",
"python eval_mosmed_timm-regnetx_002_PiecewiseAffine_0p35.py",
"python eval_mosmed_timm-regnetx_002_Posterize_0p35.py",
"python eval_mosmed_timm-regnetx_002_RandomBrightnessContrast_0p35.py",
"python eval_mosmed_timm-regnetx_002_RandomCrop_0p35.py",
"python eval_mosmed_timm-regnetx_002_RandomGamma_0p35.py",
"python eval_mosmed_timm-regnetx_002_RandomSnow_0p35.py",
"python eval_mosmed_timm-regnetx_002_Rotate_0p35.py",
"python eval_mosmed_timm-regnetx_002_Sharpen_0p35.py",
"python eval_mosmed_timm-regnetx_002_ShiftScaleRotate_0p35.py",
"python eval_ricord1a_timm-regnetx_002_Clahe_0p35.py",
"python eval_ricord1a_timm-regnetx_002_CoarseDropout_0p35.py",
"python eval_ricord1a_timm-regnetx_002_ElasticTransform_0p35.py",
"python eval_ricord1a_timm-regnetx_002_Emboss_0p35.py",
"python eval_ricord1a_timm-regnetx_002_Flip_0p35.py",
"python eval_ricord1a_timm-regnetx_002_GaussianBlur_0p35.py",
"python eval_ricord1a_timm-regnetx_002_GridDistortion_0p35.py",
"python eval_ricord1a_timm-regnetx_002_GridDropout_0p35.py",
"python eval_ricord1a_timm-regnetx_002_ImageCompression_0p35.py",
"python eval_ricord1a_timm-regnetx_002_MedianBlur_0p35.py",
"python eval_ricord1a_timm-regnetx_002_noda_0p35.py",
"python eval_ricord1a_timm-regnetx_002_OpticalDistortion_0p35.py",
"python eval_ricord1a_timm-regnetx_002_PiecewiseAffine_0p35.py",
"python eval_ricord1a_timm-regnetx_002_Posterize_0p35.py",
"python eval_ricord1a_timm-regnetx_002_RandomBrightnessContrast_0p35.py",
"python eval_ricord1a_timm-regnetx_002_RandomCrop_0p35.py",
"python eval_ricord1a_timm-regnetx_002_RandomGamma_0p35.py",
"python eval_ricord1a_timm-regnetx_002_RandomSnow_0p35.py",
"python eval_ricord1a_timm-regnetx_002_Rotate_0p35.py",
"python eval_ricord1a_timm-regnetx_002_Sharpen_0p35.py",
"python eval_ricord1a_timm-regnetx_002_ShiftScaleRotate_0p35.py",]

for l in ls:
    #print(l)
    os.system(l)