import os
import cv2
import glob
import  pylab
import numpy as np
import nibabel as nib
import  matplotlib.cm as cm
from nibabel.testing import data_path

os.mkdir('all/')
os.mkdir('all/images/')
os.mkdir('all/masks/')

masks = glob.glob('masks/*.nii')

i = 0
for mask in masks:
    image = mask.replace('masks/','studies/').replace('_mask','')

    name = mask.split('/')[-1].replace('_mask.nii','')

    images = nib.load(image) 
    images = images.get_fdata()
    images = images.transpose(2, 0, 1)

    masks = nib.load(mask)
    masks = masks.get_fdata()
    masks = masks.transpose(2, 0, 1)

    for img, msk in zip(images, masks):
        img_path = 'all/images/' + name + '_' + str(i).zfill(6) + '.jpg'
        msk_path = 'all/masks/' + name + '_' + str(i).zfill(6) + '.png'
        
        #cv2.imwrite(img_path, img)
        cv2.imwrite(msk_path, msk)
        pylab.imsave(img_path, np.rot90(img), format='jpg', cmap=cm.Greys_r)
        i += 1