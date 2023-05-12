import os
import cv2
import glob
import numpy as np

conjs = ['train', 'valid']
datasets = ['covid19china', 'covid20cases', 'medseg']

for dataset in datasets:
    dataset_path = 'datasets2/' + dataset + '/'

    for conj in conjs:

        new_masks_path = dataset_path + conj + '/umasks/'
        if os.path.isdir(new_masks_path):
            os.system('rm -rf {}'.format(new_masks_path))
        os.mkdir(new_masks_path)

        masks_path = dataset_path + conj + '/masks/'
        masks = glob.glob(masks_path + '*.png')
        for mask_path in masks:
            mask = cv2.imread(mask_path, 0)
            if dataset == 'covid20cases':
                mask = np.where(mask == 1, 0, mask)
                mask = np.where(mask == 2, 0, mask)
            if dataset == 'covid19china':
                mask = np.where(mask == 1, 0, mask)
            mask = np.where(mask != 0, 1, 0)
            new_mask_path = new_masks_path + mask_path.split('/')[-1]
            print(new_mask_path)
            cv2.imwrite(new_mask_path, mask)
            
        print('mv ' + masks_path + ' ' + masks_path.replace('/masks/','/cmasks/'))
        print('mv ' + new_masks_path + ' ' + new_masks_path.replace('/umasks/','/masks/'))
        os.system('mv ' + masks_path + ' ' + masks_path.replace('/masks/','/cmasks/'))
        os.system('mv ' + new_masks_path + ' ' + new_masks_path.replace('/umasks/','/masks/'))


