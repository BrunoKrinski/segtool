import cv2
import numpy as np
from alive_progress import alive_bar

setts = ['train','valid']
datasets = ['ricord1a', 'medseg','mosmed','covid19china','covid20cases']

for dataset in datasets:
    print(dataset)
    lesion_sizes = [0] * 10
    for sett in setts:
        print(sett)
        dataset_path = f'datasets/{dataset}/{sett}/'
        ids_file_path = dataset_path + 'ids.txt'
        images_path = dataset_path + 'images/'
        masks_path = dataset_path + 'masks/'

        ids_file = open(ids_file_path, 'r')
        ids = ids_file.readlines()
        
        with alive_bar(len(ids)) as bar:
            for id in ids:
                #print(id)
                id = id.replace('\n','')
                image_path = images_path + id + '.jpg'
                mask_path = masks_path + id + '.png'

                #print(mask_path)

                mask = cv2.imread(mask_path,0)            
                height, width = mask.shape
                tot_size = height * width
          
                contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                for i, contour in enumerate(contours):
                    contour_mask = np.zeros((height, width, 3), dtype=np.uint8)
                    cv2.fillPoly(contour_mask, pts =[contour], color=(255,255,255))
                    nwp = np.sum(contour_mask == 255)
                    id = ((nwp * 100) // tot_size) // 10
                    lesion_sizes[id] += 1
                bar()
    print(lesion_sizes)