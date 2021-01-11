import os
#os.environ['CUDA_VISIBLE_DEVICES'] = '0'

import cv2
import yaml
import json
import time
import torch
import shutil
import random
import argparse
import numpy as np
import albumentations as albu
import segmentation_models_pytorch as smp

from tqdm import trange, tqdm
from datetime import datetime
from torch.utils.data import DataLoader
from torch.utils.data import Dataset as BaseDataset

############################## DATASET ##############################
class Dataset(BaseDataset):
    
    def __init__(self, ids, num_classes, augmentation=None, preprocessing=None, mode=None):
        
        with open(ids, 'r') as ids_file:
            self.ids = ids_file.read().splitlines()
        
        self.images = []
        self.masks = []

        for idx in self.ids:
            image_path, mask_path = idx.split(' ')
            self.images.append(image_path)
            self.masks.append(mask_path)

        self.num_classes = num_classes
        self.augmentation = augmentation
        self.preprocessing = preprocessing
        self.mode = mode
    
    def __getitem__(self, i):
        
        image_path = self.images[i]
        mask_path = self.masks[i]
        #print(image_path)
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        mask = cv2.imread(mask_path, 0)
        
        height = mask.shape[0]
        width = mask.shape[1]
    
        masks = np.zeros((height, width, self.num_classes))
        for i, unique_value in enumerate(np.unique(mask)):
            masks[:, :, unique_value][mask == unique_value] = 1
                
        if self.augmentation:
            sample = self.augmentation(image=image, mask=masks)
            image, masks = sample['image'], sample['mask']

        if self.preprocessing:
            sample = self.preprocessing(image=image, mask=masks)
            image, masks = sample['image'], sample['mask']

        if self.mode == 'test':
            return image, masks, image_path, mask_path
        return image, masks
    
    def __len__(self):
        return len(self.ids)

############################## AUGMENTATION ##############################
def get_training_augmentation(height=256, width=256):
    if (height > width):
        max_size = height
    else:
        max_size = width
    
    train_transform = [
        #albu.Resize(height, width, interpolation=cv2.INTER_NEAREST, p=1),
        albu.LongestMaxSize(max_size, interpolation=cv2.INTER_NEAREST, p=1),
        albu.PadIfNeeded(min_height=height, min_width=width, always_apply=True, border_mode=cv2.BORDER_CONSTANT, value=0, mask_value=0),
        
        albu.CLAHE(p=0.5),
        #albu.HorizontalFlip(p=0.5),

        #albu.ShiftScaleRotate(scale_limit=0.5, rotate_limit=0, shift_limit=0.1, p=1, border_mode=0),

        #albu.PadIfNeeded(min_height=image_size, min_width=image_size, always_apply=True, border_mode=0),
        #albu.RandomCrop(height=image_size, width=image_size, always_apply=True),

        #albu.IAAAdditiveGaussianNoise(p=0.2),
        #albu.IAAPerspective(p=0.5),

        #albu.OneOf(
        #    [
        #        albu.CLAHE(p=1),
        #        albu.RandomBrightness(p=1),
        #        albu.RandomGamma(p=1),
        #    ],
        #    p=0.9,
        #),

        #albu.OneOf(
        #    [
        #        albu.IAASharpen(p=1),
        #        albu.Blur(blur_limit=3, p=1),
        #        albu.MotionBlur(blur_limit=3, p=1),
        #    ],
        #    p=0.9,
        #),

        #albu.OneOf(
        #    [
        #        albu.RandomContrast(p=1),
        #        albu.HueSaturationValue(p=1),
        #    ],
        #    p=0.9,
        #),
    ]
    return albu.Compose(train_transform)

def get_validation_augmentation(height=256, width=256):
    if (height > width):
        max_size = height
    else:
        max_size = width

    test_transform = [
        albu.LongestMaxSize(max_size, interpolation=cv2.INTER_NEAREST, p=1),
        albu.PadIfNeeded(min_height=height, min_width=width, always_apply=True, border_mode=cv2.BORDER_CONSTANT, value=0, mask_value=0),
    ]
    return albu.Compose(test_transform)

def to_tensor(x, **kwargs):
    return x.transpose(2, 0, 1).astype('float32')

def get_preprocessing(preprocessing_fn):    
    _transform = [
        albu.Lambda(image=preprocessing_fn),
        albu.Lambda(image=to_tensor,mask=to_tensor)
    ]
    return albu.Compose(_transform)

############################## MAIN ##############################
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--configs', type=str, required='true')
    args = parser.parse_args()

    with open(args.configs) as configs_file:
        configs = yaml.load(configs_file, Loader=yaml.FullLoader)

    with open(configs['dataset']['labels'], 'r') as classes_file:
        classes = classes_file.read().splitlines()

    device = 'cuda'
    num_classes = len(classes)
    
    resize_width = configs['model']['width']
    resize_height = configs['model']['height']
    batch_size = configs['model']['batch_size']
    
    dataset = configs['general']['dataset']
    experiment = configs['general']['experiment']
    num_workers = configs['general']['num_workers']
    
    encoder = configs['model']['encoder']
    preprocessing_fn = smp.encoders.get_preprocessing_fn(encoder, 'imagenet')
    
    loss = smp.utils.losses.DiceLoss()
    metrics = [smp.utils.metrics.Fscore(threshold=0.9)] 
    individual_metrics = [smp.utils.metrics.Fscore(threshold=0.9, num_classes=num_classes)] 
    
    #============================== TRAIN ==============================#
    if configs['general']['mode'] == 'train':

        num_epochs = configs['model']['num_epochs']
        learning_rate = configs['model']['learning_rate']

        runs_dir = 'RUNS/'
        os.makedirs(runs_dir, exist_ok='True')

        runs_dir += '/' + experiment
        os.makedirs(runs_dir, exist_ok='True')

        runs_dir += '/' + dataset
        os.makedirs(runs_dir, exist_ok='True')
        
        out_dir = args.configs.replace('.yml','').split('/')[-1]
        out_dir = runs_dir + '/' + out_dir
        
        date = str(datetime.now()).replace(' ', '_')

        out_dir = out_dir + '_' + date
        os.mkdir(out_dir) 

        os.system('cp {} {}'.format(args.configs, out_dir))
                
        activation = 'softmax2d'
        
        if configs['model']['decoder'] == 'fpn':
            model = smp.FPN(encoder_name=encoder, classes=num_classes, encoder_weights='imagenet', activation=activation)
        elif configs['model']['decoder'] == 'unet':
            model = smp.Unet(encoder_name=encoder, classes=num_classes, encoder_weights='imagenet', activation=activation)
        elif configs['model']['decoder'] == 'linknet':
            model = smp.Linknet(encoder_name=encoder, classes=num_classes, encoder_weights='imagenet', activation=activation)
        elif configs['model']['decoder'] == 'pspnet':
            model = smp.PSPNet(encoder_name=encoder, classes=num_classes, encoder_weights='imagenet', activation=activation)
        
        train_dataset = Dataset(configs['dataset']['train'], num_classes,
                                augmentation=get_training_augmentation(resize_height, resize_width),
                                preprocessing=get_preprocessing(preprocessing_fn))
        valid_dataset = Dataset(configs['dataset']['valid'], num_classes,
                                augmentation=get_validation_augmentation(resize_height, resize_width),
                                preprocessing=get_preprocessing(preprocessing_fn))

        train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=num_workers)
        valid_loader = DataLoader(valid_dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers)
        
        optimizer = torch.optim.Adam([dict(params=model.parameters(), lr=learning_rate),])

        train_epoch = smp.utils.train.TrainEpoch(model, loss=loss, metrics=metrics, individual_metrics=individual_metrics, 
                                                 labels=classes, optimizer=optimizer, device=device, verbose=True,)

        valid_epoch = smp.utils.train.ValidEpoch(model, loss=loss, metrics=metrics, individual_metrics=individual_metrics, 
                                                 labels=classes, device=device, verbose=True,)

        checkpoints = out_dir + '/checkpoints'
        os.mkdir(checkpoints)

        logs = {}
        logs['train'] = []
        logs['valid'] = []
        
        max_score = 0
        for i in range(num_epochs):
            print('\nEpoch: {}'.format(i))
            train_init = time.time()
            train_logs, individual_train_logs = train_epoch.run(train_loader)
            train_end = time.time()
            train_time = (train_end - train_init)

            valid_init = time.time()
            valid_logs, individual_valid_logs = valid_epoch.run(valid_loader)
            valid_end = time.time()
            valid_time = (valid_end - valid_init)
            
            individual_train_logs['Epoch'] = i
            individual_valid_logs['Epoch'] = i
            individual_train_logs['Time'] = train_time
            individual_valid_logs['Time'] = valid_time
            logs['train'].append(individual_train_logs)
            logs['valid'].append(individual_valid_logs)

            #torch.save(model, '{}/epoch{}.pth'.format(checkpoints, i))
            torch.save(model, '{}/last.pth'.format(checkpoints))
    
            if max_score < valid_logs['Fscore']:
                max_score = valid_logs['Fscore']
                torch.save(model, '{}/best.pth'.format(checkpoints))

            with open(out_dir + '/train_logs.json', 'w') as log_file:
                json.dump(logs, log_file, indent=4)
        
            if i > 0 and (i % 10 == 0):
                print('Learning rate decreased!')
                optimizer.param_groups[0]['lr'] = learning_rate / 10
        
    #============================== EVAL ==============================#
    elif configs['general']['mode'] == 'eval':

        project_path = configs['general']['path']

        masks_path = project_path + '/predicted_masks'
        images_path = project_path + '/segmented_images'

        if os.path.isdir(masks_path):
            shutil.rmtree(masks_path)

        if os.path.isdir(images_path):
            shutil.rmtree(images_path)

        os.mkdir(masks_path)
        os.mkdir(images_path)
        
        model_path = project_path + '/checkpoints/' + configs['model']['type'] + '.pth'

        model = torch.load(model_path)

        test_dataset = Dataset(configs['dataset']['test'], num_classes,
                                augmentation=get_validation_augmentation(resize_height, resize_width),
                                preprocessing=get_preprocessing(preprocessing_fn))
        
        test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers)

        test_epoch = smp.utils.train.ValidEpoch(model=model, loss=loss, metrics=metrics, 
                                                individual_metrics=individual_metrics, labels=classes, device=device)
        
        test_logs = test_epoch.run(test_loader)

        logs = {}
        logs['test'] = [test_logs]

        with open(project_path + '/test_logs.json', 'w') as log_file:
            json.dump(logs, log_file, indent=4)
            
        colors = []
        #for i in range(num_classes):
        #    if i == 0:
        #        colors.append([0, 0, 0])
        #    else:
        #        colors.append([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
        #colors.append([0, 0, 0])
        #colors.append([0, 50, 0])
        #colors.append([0, 100, 0])
        #colors.append([200, 0, 0])
        colors_path = 'colors.txt'
        with open(colors_path, 'r') as colors_file:
            colors = colors_file.read().splitlines()

        colors_str = colors[0:num_classes]
    
        colors = []
        for c in colors_str:
            color = []
            c = c.split(',')
            for item in c:
                color.append(int(item))
            colors.append(color)

        test_dataset = Dataset(configs['dataset']['test'], num_classes,
                               augmentation=get_validation_augmentation(resize_height, resize_width),
                               preprocessing=get_preprocessing(preprocessing_fn), mode='test')

        for i in trange(len(test_dataset)):
            image, gt_mask, image_path, mask_path = test_dataset[i]
            #gt_mask = gt_mask.squeeze()
            
            idx = image_path.replace('.jpg','').split('/')[-1]
            
            x_tensor = torch.from_numpy(image).to(device).unsqueeze(0)
            pr_masks = model.predict(x_tensor)
            pr_masks = torch.argmax(pr_masks, dim=1)
            pr_masks = (pr_masks.squeeze().cpu().numpy())

            original_image = cv2.imread(image_path)
            original_height, original_width, _ = original_image.shape

            if (resize_height > resize_width):
                max_size = resize_height
            else:
                max_size = resize_width
            
            transform = albu.LongestMaxSize(max_size, interpolation=cv2.INTER_NEAREST, p=1)
            image = transform(image=original_image)['image']
            
            image_height, image_width, _ = image.shape
            transform = albu.CenterCrop(height=image_height, width=image_width, p=1)
            pr_masks = transform(image=pr_masks)['image']

            if (original_height > original_width):
                max_size = original_height
            else:
                max_size = original_width

            transform = albu.LongestMaxSize(max_size, interpolation=cv2.INTER_NEAREST, p=1)
            pr_masks = transform(image=pr_masks)['image']
            
            mask_height, mask_width = pr_masks.shape
            
            if mask_width < original_width:
                transform = albu.Resize(height=original_height,width=original_width, interpolation=cv2.INTER_NEAREST, p=1)
                pr_masks = transform(image=pr_masks)['image']
            
            elif mask_width > original_width:
                transform = albu.CenterCrop(height=original_height,width=original_width, p=1)
                pr_masks = transform(image=pr_masks)['image']
            
            mask_height, mask_width = pr_masks.shape
            final_mask = np.zeros((mask_height, mask_width, 3))
            final_mask[:,:,0] = pr_masks
            final_mask[:,:,1] = pr_masks
            final_mask[:,:,2] = pr_masks
            
            for i, unique_value in enumerate(np.unique(pr_masks)):
                final_mask = np.where(final_mask == [unique_value, unique_value, unique_value], colors[unique_value], final_mask)
            
            image = original_image.astype('float32')
            final_mask = final_mask.astype('float32')

            pred_image = cv2.addWeighted(image, 0.9, final_mask, 0.8, 0.0)

            image_path = images_path + '/{}.jpg'.format(idx)
            mask_path = masks_path + '/{}.png'.format(idx)
            
            cv2.imwrite(image_path, pred_image)
            cv2.imwrite(mask_path, final_mask)
