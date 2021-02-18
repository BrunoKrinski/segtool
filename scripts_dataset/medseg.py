import os
import cv2
import glob
import  pylab
import numpy as np
import nibabel as nib
import  matplotlib.cm as cm
from nibabel.testing import data_path

images_path = 'images/'
masks_path = 'masks/'

os.mkdir('all/')
os.mkdir('all/images/')
os.mkdir('all/masks/')

i = 0
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

    for image, mask in zip(images, masks):

        image_name = 'all/images/' + name + '_' + str(i).zfill(6) + '.jpg'
        mask_name = 'all/masks/' + name + '_' + str(i).zfill(6) + '.png'

        #cv2.imwrite(image_name, image)
        cv2.imwrite(mask_name, np.rot90(mask))
        pylab.imsave(image_name, np.rot90(image), format='jpg', cmap=cm.Greys_r)
        #pylab.imsave(mask_name, np.rot90(mask), format='png')
        i += 1