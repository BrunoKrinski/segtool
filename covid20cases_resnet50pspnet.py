import os

ls = ['python main.py --configs configs/resnet50_pspnet_covid20cases_fold0.yml',
      'python main.py --configs configs/resnet50_pspnet_covid20cases_fold1.yml',
      'python main.py --configs configs/resnet50_pspnet_covid20cases_fold2.yml',
      'python main.py --configs configs/resnet50_pspnet_covid20cases_fold3.yml',
      'python main.py --configs configs/resnet50_pspnet_covid20cases_fold4.yml']

for l in ls:
    os.system(l)
