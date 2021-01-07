import os
import cv2
import glob
import numpy as np

if __name__ == '__main__':
    s3ts = ['train/', 'valid/', 'test/']

    rgb_colors = [
        np.array([ 64, 128,  64]),
        np.array([128,   0, 192]),
        np.array([192, 128,   0]),
        np.array([ 64, 128,   0]),
        np.array([  0,   0, 128]),
        np.array([128,   0,  64]),
        np.array([192,   0,  64]),
        np.array([ 64, 128, 192]),
        np.array([128, 192, 192]),
        np.array([128,  64,  64]),
        np.array([192,   0, 128]),
        np.array([ 64,   0, 192]),
        np.array([ 64, 128, 128]),
        np.array([192,   0, 192]),
        np.array([ 64,  64, 128]),
        np.array([128, 192,  64]),
        np.array([  0,  64,  64]),
        np.array([128,  64, 128]),
        np.array([192, 128, 128]),
        np.array([192,   0,   0]),
        np.array([128, 128, 192]),
        np.array([128, 128, 128]),
        np.array([192, 128,  64]),
        np.array([ 64,   0,   0]),
        np.array([ 64,  64,   0]),
        np.array([128,  64, 192]),
        np.array([  0, 128, 128]),
        np.array([192, 128, 192]),
        np.array([ 64,   0,  64]),
        np.array([  0, 192, 192]),
        np.array([  0, 192,  64])
    ]

    for s3t in s3ts:
        cimages_path = glob.glob(s3t + 'cimages/*.png')

        images_path = s3t + '/images/'
        masks_path = s3t + '/masks/'

        if os.path.isdir(images_path):
            os.system('rm -rf {}'.format(images_path))
        
        if os.path.isdir(masks_path):
            os.system('rm -rf {}'.format(masks_path))

        os.mkdir(images_path)
        os.mkdir(masks_path)

        for cimage_path in cimages_path:
            image_name = cimage_path.split('/')[-1].replace('.png','')
            print(image_name)

            cimage = cv2.imread(cimage_path)

            image_path = images_path + image_name + '.jpg'
            cv2.imwrite(image_path, cimage)

            cmask_path = cimage_path.replace('/cimages/','/cmasks/').replace('.png','_L.png')
            cmask = cv2.imread(cmask_path)
            
            height, width, _ = cmask.shape
            mask = np.zeros((height, width))
            for i in range(len(rgb_colors)):
                #mask = np.where(cmask == rgb_colors[i], i, 0)
                mask[(cmask == rgb_colors[i]).all(axis=2)] = i

            #print(np.unique(mask))
            mask_path = masks_path + image_name + '.png'
            cv2.imwrite(mask_path, mask)