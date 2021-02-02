import os

ls = ['python main.py --configs configs/resnet50_fpn_camvid_fold0.yml',
      'python main.py --configs configs/resnet50_fpn_camvid_fold1.yml',
      'python main.py --configs configs/resnet50_fpn_camvid_fold2.yml',
      'python main.py --configs configs/resnet50_fpn_camvid_fold3.yml',
      'python main.py --configs configs/resnet50_fpn_camvid_fold4.yml']

for l in ls:
    os.system(l)
