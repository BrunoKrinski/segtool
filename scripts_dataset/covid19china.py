import os
import glob

masks = glob.glob('mask/**/*.png', recursive=True)

i = 0
for mask in masks:
    print(mask)
    image = mask.replace('mask/','image/').replace('.png','.jpg')
    

    i_path = 'train/images/' + str(i).zfill(6) + '.jpg'
    m_path = 'train/masks/' + str(i).zfill(6) + '.png'

    os.system('cp {} {}'.format(image, i_path))
    os.system('cp {} {}'.format(mask, m_path))
    i += 1