import os
import cv2
import numpy as np

datasets_path = 'datasets/'
'''
datasets = ['covid19china', 'covid20cases', 'medseg', 'mosmed', 'ricord1a']
#datasets = ['ricord1a']

datasets_path = 'datasets/'

for dataset in datasets:
    dataset_path = datasets_path + dataset + '/'

    sets = ['train', 'valid']
    for s in sets:
        spath = dataset_path + s + '/'
        ids_path = spath + 'ids.txt'

        images_path = spath + 'images/'
        masks_path = spath + 'masks/'

        empty_images_path = spath + 'empty_images/'
        empty_masks_path = spath + 'empty_masks/'
        
        if os.path.isdir(empty_images_path):
            os.system('rm -r ' + empty_images_path)
        os.mkdir(empty_images_path)

        if os.path.isdir(empty_masks_path):
            os.system('rm -r ' + empty_masks_path)
        os.mkdir(empty_masks_path)
        
        with open(ids_path) as ids_file:
            lines = ids_file.readlines()

        for line in lines:
            #print(line)
            id = line.replace('\n','')

            img_path = images_path + id + '.jpg'
            msk_path = masks_path + id + '.png'

            #print(msk_path)
            mask = cv2.imread(msk_path, 0)

            if dataset == 'covid19china':
                mask = np.where(mask == 1, 0, mask)
            if dataset == 'covid20cases':
                mask = np.where(mask == 1, 0, mask)
                mask = np.where(mask == 2, 0, mask)

            uniques = np.unique(mask)

            if len(uniques) == 1:
                new_img_path = empty_images_path + id + '.jpg'
                new_msk_path = empty_masks_path + id + '.png'

                mv_img = 'mv ' + img_path + ' ' + new_img_path
                mv_msk = 'mv ' + msk_path + ' ' + new_msk_path

                print(mv_img)
                print(mv_msk)

                os.system(mv_img)
                os.system(mv_msk)

'''
datasets = ['lungseg']
for dataset in datasets:
    dataset_path = datasets_path + dataset + '/ricord1b_gan/'

    ids_path = dataset_path + 'ids.txt'

    images_path = dataset_path + 'images/'
    masks_path = dataset_path + 'predicted_masks/'
    segmented_path = dataset_path + 'segmented_images/'

    empty_images_path = dataset_path + 'empty_images/'
    empty_masks_path = dataset_path + 'empty_masks/'
    empty_segmented_path = dataset_path + 'empty_segmented_images/'

    if os.path.isdir(empty_images_path):
        os.system('rm -r ' + empty_images_path)
    os.mkdir(empty_images_path)

    if os.path.isdir(empty_masks_path):
        os.system('rm -r ' + empty_masks_path)
    os.mkdir(empty_masks_path)

    if os.path.isdir(empty_segmented_path):
        os.system('rm -r ' + empty_segmented_path)
    os.mkdir(empty_segmented_path)

    with open(ids_path) as ids_file:
        lines = ids_file.readlines()

    for line in lines:
        #print(line)
        id = line.replace('\n','').split('/')[-1]
        id = id.replace('.jpg','')
        print(id)
        
        img_path = images_path + id + '.jpg'
        msk_path = masks_path + id + '.png'
        sgm_path = segmented_path + id + '.jpg'

        #print(msk_path)
        mask = cv2.imread(msk_path, 0)
        mask = np.where(mask != 0, 1, 0)
        number_lung = np.sum(mask == 1)
        if number_lung < 15000:
            new_img_path = empty_images_path + id + '.jpg'
            new_msk_path = empty_masks_path + id + '.png'
            new_sgm_path = empty_segmented_path + id + '.jpg'

            mv_img = 'mv ' + img_path + ' ' + new_img_path
            mv_msk = 'mv ' + msk_path + ' ' + new_msk_path
            mv_sgm = 'mv ' + sgm_path + ' ' + new_sgm_path

            print(mv_img)
            print(mv_msk)
            print(mv_sgm)

            os.system(mv_img)
            os.system(mv_msk)
            os.system(mv_sgm)