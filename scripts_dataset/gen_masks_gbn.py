#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Classes: 
# 0 - TextRegion      [255 0 0] 
# 1 - ImageRegion     [255 255 0]
# 2 - GraphicRegion   [0 255 0]   
# 3 - SeparatorRegion [255 0 255] 

# vri08:
# python gt_masks.py -d '/home/alessandra/GBNLAdatabase/GBNLA/<NEWSPAPER>/train/'
# python gt_masks.py -d '/home/alessandra/GBNLAdatabase/GBNLA/<NEWSPAPER>/test/'

import os
import cv2
import glob
import argparse
import numpy as np
from PIL import Image

#Parameters
#ap = argparse.ArgumentParser()
#ap.add_argument("-d", "--directory", required = True, help = "Directory of files XML.")
#args = vars(ap.parse_args())

directories = ['DerGemeindebote/',
               'DerJugendfreund/train/',
               'DerPionier/train/',
               'DerSandwirt/train/',
               'EvLuthKirchenblatt/train/',
               'KolonieZeitung/train/',
               'DerJugendfreund/test/',
               'DerPionier/test/',
               'DerSandwirt/test/',
               'EvLuthKirchenblatt/test/',
               'Gemeindeblatt/test/',
               'Heimatbote/test/',
               'KolonieZeitung/test/']

#directories = ['Gemeindeblatt/test/',
#               'Heimatbote/test/']

log = open('log.txt','w')

for directory in directories:
    print(directory)
    log.write('directory: {}\n'.format(directory))
    for file in glob.glob(directory+'*.xml'):
        dir_img_title = file[:-4]
        print('-----',file,'-----')
        log.write('file: {}\n'.format(file))
        
        os.system('convert {} -quality 100 {}'.format(dir_img_title + '.png', dir_img_title + '.jpg'))

        im = cv2.imread(dir_img_title + '.png')
        try:
            cv2.imwrite(dir_img_title + '_verify_.jpg', im)
        except:
            print('ERRO NA IMAGEM: ' + dir_img_title)
            log.write('ERRO NA IMAGEM: {}\n'.format(dir_img_title))
            continue

        arq = open(dir_img_title+'.xml', 'r')
        xml = arq.readlines()

        img = cv2.imread(dir_img_title+'-bw.png')
    
        l,c,ch = img.shape
        mask = np.zeros((l,c,ch))

        for i in range (0,len(xml)):
            if ('<TextRegion' in xml[i]) or ('<ImageRegion' in xml[i]) or ('<GraphicRegion' in xml[i]) or ('<SeparatorRegion' in xml[i]):
                #print xml[i]
                #print xml[i+1]
                string_pts = xml[i+1].split('"') #quebra a string nas aspas
                string_pts_pair = string_pts[1].split(" ") #pega a segunda parte quebrada da string e quebra nos espacamentos em branco 
                
                points = [] #points.dtype => 'int64'

                for pair in string_pts_pair:
                    p = pair.split(',')
                    list_temp = []
                    list_temp.append(p[0])
                    list_temp.append(p[1])

                    points.append(list_temp)

                #Para desenhar somente os contornos:
                #cv2.polylines(mask, np.int32([points]), 1, (0,255,0))

                if ('<TextRegion' in xml[i]):
                    cv2.fillPoly(mask,np.int32([points]),(255,0,0))
                elif ('<GraphicRegion' in xml[i]):
                    cv2.fillPoly(mask,np.int32([points]),(0,255,0))
                elif ('<SeparatorRegion' in xml[i]): 
                    cv2.fillPoly(mask,np.int32([points]),(255,0,255))
                elif ('<ImageRegion' in xml[i]):
                    cv2.fillPoly(mask,np.int32([points]),(255,255,0))
        arq.close()

        #print(dir_img_title+'_CARACT_MASK.png')
        cv2.imwrite(dir_img_title+'_REGION_MASK.png',mask) 
        cv2.imwrite(dir_img_title+'_CARACT_MASK.png',mask+img)

        region_mask = mask
        caract_mask = mask+img
        height, width, _ = caract_mask.shape
        bin_caract_mask = np.zeros((height, width))
        bin_region_mask = np.zeros((height, width))
        
        for h in range(height):
            for w in range(width):
                element = caract_mask[h, w]
                a = element[0]
                b = element[1]
                c = element[2]
                if a == 255 and b == 0 and c == 0:
                    bin_caract_mask[h, w] = 1
                if a == 0 and b == 255 and c == 0:
                    bin_caract_mask[h, w] = 2
                if a == 255 and b == 0 and c == 255:
                    bin_caract_mask[h, w] = 3
                if a == 255 and b == 255 and c == 0:
                    bin_caract_mask[h, w] = 4
                
                element = region_mask[h, w]
                a = element[0]
                b = element[1]
                c = element[2]
                if a == 255 and b == 0 and c == 0:
                    bin_region_mask[h, w] = 1
                if a == 0 and b == 255 and c == 0:
                    bin_region_mask[h, w] = 2
                if a == 255 and b == 0 and c == 255:
                    bin_region_mask[h, w] = 3
                if a == 255 and b == 255 and c == 0:
                    bin_region_mask[h, w] = 4

        cv2.imwrite(dir_img_title+'_gt_mask_caract.png',bin_caract_mask)
        cv2.imwrite(dir_img_title+'_gt_mask_region.png',bin_region_mask)
log.close()

#DerSandwirt_1937_02-p036_5719_4240.jpg
