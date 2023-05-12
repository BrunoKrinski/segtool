import os

runs = ['python train_covid19china_timm-regnetx_002_clahe__025.py',
        'python train_covid19china_timm-regnetx_002_emboss__025.py',
        'python train_covid19china_timm-regnetx_002_gaussian_blur__025.py',
        'python train_covid19china_timm-regnetx_002_image_compression__025.py',
        'python train_covid19china_timm-regnetx_002_median_blur__025.py',
        'python train_covid19china_timm-regnetx_002_posterize__025.py',
        'python train_covid19china_timm-regnetx_002_random_brightness_contrast__025.py',
        'python train_covid19china_timm-regnetx_002_random_gamma__025.py',
        'python train_covid19china_timm-regnetx_002_random_snow__025.py',
        'python train_covid19china_timm-regnetx_002_sharpen__025.py',
        'python train_covid19china_timm-regnetx_002_coarse_dropout__025.py',
        'python train_covid19china_timm-regnetx_002_elastic_transform__025.py',
        'python train_covid19china_timm-regnetx_002_flip__025.py',
        'python train_covid19china_timm-regnetx_002_grid_distortion__025.py',
        'python train_covid19china_timm-regnetx_002_grid_dropout__025.py',
        'python train_covid19china_timm-regnetx_002_optical_distortion__025.py',
        'python train_covid19china_timm-regnetx_002_piecewise_affine__025.py',
        'python train_covid19china_timm-regnetx_002_random_crop__025.py',
        'python train_covid19china_timm-regnetx_002_rotate__025.py',
        'python train_covid19china_timm-regnetx_002_shift_scale_rotate__025.py']

for run in runs:
  os.system(run)
