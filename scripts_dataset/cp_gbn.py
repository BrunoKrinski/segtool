import os
import glob

train_directories = ['DerGemeindebote/',
                     'DerJugendfreund/train/',
                     'DerPionier/train/',
                     'DerSandwirt/train/',
                     'EvLuthKirchenblatt/train/',
                     'KolonieZeitung/train/']

valid_directories = ['DerJugendfreund/test/',
                     'DerPionier/test/',
                     'DerSandwirt/test/',
                     'EvLuthKirchenblatt/test/',
                     'Gemeindeblatt/test/',
                     'Heimatbote/test/',
                     'KolonieZeitung/test/']

os.mkdir('train')
os.mkdir('train/images')
os.mkdir('train/masks')

os.mkdir('valid')
os.mkdir('valid/images')
os.mkdir('valid/masks')

for directory in train_directories:
    print(directory)
    paths = glob.glob(directory + '/*.jpg')
    for path in paths:
        if '_verify_' in path:
            image_path = path
            image_name = image_path.split('/')[-1]
            new_path = 'train/images/' + image_name.replace('_verify_','')
            os.system('cp {} {}'.format(image_path, new_path))

            mask_path = path.replace('_verify_.jpg','_gt_mask_region.png')
            mask_name = mask_path.split('/')[-1]
            new_path = 'train/masks/' + mask_name.replace('_gt_mask_region','')
            os.system('cp {} {}'.format(mask_path, new_path))

for directory in valid_directories:
    print(directory)
    paths = glob.glob(directory + '/*.jpg')
    for path in paths:
        if '_verify_' in path:
            image_path = path
            image_name = image_path.split('/')[-1]
            new_path = 'valid/images/' + image_name.replace('_verify_','')
            os.system('cp {} {}'.format(image_path, new_path))

            mask_path = path.replace('_verify_.jpg','_gt_mask_region.png')
            mask_name = mask_path.split('/')[-1]
            new_path = 'valid/masks/' + mask_name.replace('_gt_mask_region','')
            os.system('cp {} {}'.format(mask_path, new_path))