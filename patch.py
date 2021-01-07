import os
import cv2
import argparse
import numpy as np
from skimage.util import view_as_blocks

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, required='true')
    args = parser.parse_args()

    sets = ['train', 'valid']

    dataset_patched = 'datasets/{}_patched/'.format(args.dataset)
    if os.path.isdir(dataset_patched):
        os.system('rm -rf {}'.format(dataset_patched))
    
    os.mkdir(dataset_patched)

    for s3t in sets:
        if s3t == 'train':
            dataset_ids = 'datasets/{}/{}/ids_all.txt'.format(args.dataset, s3t)
        else:
            dataset_ids = 'datasets/{}/{}/test_ids.txt'.format(args.dataset, s3t)
        
        with open(dataset_ids, 'r') as txt_file:
            ids = txt_file.read().splitlines()

        paths = []    
        train_patched =  dataset_patched + s3t 
        train_images_patched = train_patched + '/images/'
        train_masks_patched = train_patched + '/masks/'

        os.mkdir(train_patched)
        os.mkdir(train_images_patched)
        os.mkdir(train_masks_patched)

        patch_file = open('{}/patched.txt'.format(train_patched), 'w')

        for idx in ids:
            image_path, mask_path = idx.split(' ')
            image_name = image_path.split('/')[-1].split('.')[0]
            print(image_name)
            patch_file.write('begin_image\n')
            patch_file.write(image_name + '\n')
        
            image = cv2.imread(image_path)
            mask = cv2.imread(mask_path,0)

            print(np.unique(mask))
        
            height, width = mask.shape
            patch_file.write('{} {}\n'.format(height, width))
        
            patched_height = round(height/20)
            patched_width = round(width/20)

            for h in range(0, height, patched_height):
                #patch_file.write('begin_line\n')
                for w in range(0, width, patched_width):
                    patched_image = image[h:h+patched_height, w:w+patched_width]
                    patched_mask = mask[h:h+patched_height, w:w+patched_width]

                    i_im_path = train_images_patched + '{}_{}_{}.jpg'.format(image_name, h, w)
                    i_mk_path = train_masks_patched + '{}_{}_{}.png'.format(image_name, h, w)
                    patch_file.write('{} {}\n'.format(i_im_path, i_mk_path))
                    
                    cv2.imwrite(i_im_path, patched_image)
                    cv2.imwrite(i_mk_path, patched_mask)
                patch_file.write('end_line\n')
            patch_file.write('end_image\n')