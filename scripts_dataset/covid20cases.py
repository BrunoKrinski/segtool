import os
import cv2
import glob
import numpy as np
import nibabel as nib
from nibabel.testing import data_path

sets = ['train/', 'valid/']

for s3t in sets:
    images_path = s3t + 'images/'
    masks_path = s3t + 'masks/'

    for item in glob.glob(masks_path + '*'):
        name = item.split('/')[-1]
        image_item = images_path + name
        mask_item = masks_path + name

        name = name.split('.')[0]

        images = nib.load(image_item) 
        images = images.get_fdata()
        images = images.transpose(2, 0, 1)
        
        masks = nib.load(mask_item)
        masks = masks.get_fdata()
        masks = masks.transpose(2, 0, 1)

        num_images = len(images)

        for i, image, mask in zip(range(num_images), images, masks):
            #if np.count_nonzero(mask) == 0:
            #    continue
            #else:
            image_name = s3t + 'images/' + name + '_{}.jpg'.format(i)
            mask_name = s3t + 'masks/' + name + '_{}.png'.format(i)
            cv2.imwrite(image_name, image)
            cv2.imwrite(mask_name, mask)