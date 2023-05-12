import os

runs = ['python train_covid20cases_timm-regnetx_002_noda.py',
        'python train_covid20cases_timm-regnetx_002_clahe.py',
        'python train_covid20cases_timm-regnetx_002_emboss.py',
        'python train_covid20cases_timm-regnetx_002_gaussian_blur.py',
        'python train_covid20cases_timm-regnetx_002_image_compression.py',
        'python train_covid20cases_timm-regnetx_002_median_blur.py',
        'python train_covid20cases_timm-regnetx_002_posterize.py',
        'python train_covid20cases_timm-regnetx_002_random_brightness_contrast.py',
        'python train_covid20cases_timm-regnetx_002_random_gamma.py',
        'python train_covid20cases_timm-regnetx_002_random_snow.py',
        'python train_covid20cases_timm-regnetx_002_sharpen.py',
        'python train_covid20cases_timm-regnetx_002_coarse_dropout.py',
        'python train_covid20cases_timm-regnetx_002_elastic_transform.py',
        'python train_covid20cases_timm-regnetx_002_flip.py',
        'python train_covid20cases_timm-regnetx_002_grid_distortion.py',
        'python train_covid20cases_timm-regnetx_002_grid_dropout.py',
        'python train_covid20cases_timm-regnetx_002_optical_distortion.py',
        'python train_covid20cases_timm-regnetx_002_piecewise_affine.py',
        'python train_covid20cases_timm-regnetx_002_random_crop.py',
        'python train_covid20cases_timm-regnetx_002_rotate.py',
        'python train_covid20cases_timm-regnetx_002_shift_scale_rotate.py']

for run in runs:
  os.system(run)
