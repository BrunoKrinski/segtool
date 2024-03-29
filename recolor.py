import os
import cv2
import glob
import shutil
import random
import argparse
import numpy as np

probs = ['0p05/', '0p1/', '0p15/', '0p2/']
das = ['Stargan/','StarganFlip/','Stylegan/','StyleganFlip/']
das = ['noda/']
datasets = ['ricord1a/']

runs_path = 'RUNS/das4/'

for prob in probs:
    for da in das:
        for dataset in datasets:
            dataset_path = 'datasets/' + dataset + '/valid/ids.txt'
            ids = open(dataset_path).readlines()

            paths = runs_path + prob + da + dataset + 'unetplusplus/timm-regnetx_002/'
            runs = glob.glob(paths + '*')

            for run in runs:
                recolored_masks = run + '/recolored_masks/'
                if os.path.isdir(recolored_masks):
                    shutil.rmtree(recolored_masks)
                os.mkdir(recolored_masks)

                for id in ids:
                    id = id.replace('\n','')
                    print(id)
                    image_path = 'datasets/' + dataset + '/valid/images/' + id + '.jpg'
                    #print(image_path)
                    mask_path = run + '/predicted_masks/' + id + '.png'
                    #print(mask_path)
                    image = cv2.imread(image_path)
                    mask = cv2.imread(mask_path, 0)
                    mask = np.where(mask != 0, 255, 0)

                    height, width = mask.shape
                    colored_gt = np.zeros((height, width, 3))
                    colored_gt[:,:,0] = mask
                    colored_gt[:,:,1] = mask
                    colored_gt[:,:,2] = mask

                    for i, unique_value in enumerate(np.unique(mask)):
                        colored_gt = np.where(colored_gt == [255, 255, 255], [0, 0, 255], colored_gt)
                    
                    image = image.astype('float32')
                    colored_gt = colored_gt.astype('float32')

                    colored_gt = cv2.addWeighted(image, 0.9, colored_gt, 0.9, 0.0)

                    colored_gt_path = recolored_masks + id + '.jpg'
                    print(colored_gt_path)
                    cv2.imwrite(colored_gt_path, colored_gt)
                    

                





'''
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, required='true')
    parser.add_argument('--num_classes', type=int, required='true')
    args = parser.parse_args()

    sets = ['train', 'valid']
    #sets = ['train']
    colors_path = 'colors.txt'
    with open(colors_path, 'r') as colors_file:
        colors = colors_file.read().splitlines()

    colors_str = colors[0:args.num_classes]
    
    colors = []
    for c in colors_str:
        color = []
        c = c.split(',')
        for item in c:
            color.append(int(item))
        colors.append(color)
    print(colors)
    
    #c = []
    #for i, color in enumerate(colors):
    #    if i == 0:
    #        c.append([0, 0, 0])
    #    else:
    #        c.append(colors[1])
    #colors = c

    #for i in range(args.num_classes):
    #    if i == 0:
    #        colors.append([0, 0, 0])
    #    else:
    #        #random.seed(50)
    #        color1 = random.randint(0, 255)
    #        #random.seed(200)
    #        color2 = random.randint(0, 255)
    #        #random.seed(100)
    #        color3 = random.randint(0, 255)
    #        colors.append([color1, color2, color3])
    #        print(colors)

    for s3t in sets:
        if s3t == 'train':
            dataset_ids = 'datasets2/{}/{}/ids_all.txt'.format(args.dataset, s3t)
        else:
            dataset_ids = 'datasets2/{}/{}/test_ids.txt'.format(args.dataset, s3t)

        colored_path = 'datasets2/{}/{}/colored_gt/'.format(args.dataset, s3t)

        if os.path.isdir(colored_path):
            os.system('rm -rf {}'.format(colored_path))
    
        os.mkdir(colored_path)

        with open(dataset_ids, 'r') as txt_file:
            ids = txt_file.read().splitlines()

        num_classes = 0
        for idx in ids:
            #print(idx)
            image_path, mask_path = idx.split(' ')
            
            image_path = image_path.replace('datasets2/','datasets2/')
            mask_path = mask_path.replace('datasets2/','datasets2/')

            colored_gt_path = image_path.replace('/images/','/colored_gt/')
            image_name = image_path.split('/')[-1].split('.')[0]
            #print(image_name)
        
            image = cv2.imread(image_path)
            print(mask_path)
            mask = cv2.imread(mask_path,0)

            #print(np.unique(mask))
            if len(np.unique(mask)) > num_classes:
                num_classes += 1
                print(num_classes)
                print(np.unique(mask))
        
            height, width = mask.shape

            colored_gt = np.zeros((height, width, 3))
            colored_gt[:,:,0] = mask
            colored_gt[:,:,1] = mask
            colored_gt[:,:,2] = mask

            for i, unique_value in enumerate(np.unique(mask)):
                colored_gt = np.where(colored_gt == [unique_value, unique_value, unique_value], colors[unique_value], colored_gt)

            image = image.astype('float32')
            colored_gt = colored_gt.astype('float32')

            colored_gt = cv2.addWeighted(image, 0.9, colored_gt, 0.9, 0.0)
            
            cv2.imwrite(colored_gt_path, colored_gt)
'''