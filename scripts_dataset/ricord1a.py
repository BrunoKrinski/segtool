import cv2
import png
import json
import mdai
import glob
import numpy as np
import pandas as pd
import pydicom as PDCM

from PIL import Image
from scipy.ndimage.interpolation import zoom
from pydicom.pixel_data_handlers.util import apply_voi_lut

def Dicom_to_Image(Path):
    DCM_Img = PDCM.read_file(Path)

    rows = DCM_Img.get(0x00280010).value #Get number of rows from tag (0028, 0010)
    cols = DCM_Img.get(0x00280011).value #Get number of cols from tag (0028, 0011)

    Instance_Number = int(DCM_Img.get(0x00200013).value) #Get actual slice instance number from tag (0020, 0013)
    Window_Center = int(ds.WindowCenter) if (type(ds.WindowCenter) == PDCM.valuerep.DSfloat) else int(ds.WindowCenter[0])
    Window_Width = int(ds.WindowWidth) if (type(ds.WindowWidth) == PDCM.valuerep.DSfloat) else int(ds.WindowWidth[0])

    Window_Max = int(Window_Center + Window_Width / 2)
    Window_Min = int(Window_Center - Window_Width / 2)

    if (DCM_Img.get(0x00281052) is None):
        Rescale_Intercept = 0
    else:
        Rescale_Intercept = int(DCM_Img.get(0x00281052).value)

    if (DCM_Img.get(0x00281053) is None):
        Rescale_Slope = 1
    else:
        Rescale_Slope = int(DCM_Img.get(0x00281053).value)

    New_Img = np.zeros((rows, cols), np.uint8)
    Pixels = DCM_Img.pixel_array

    for i in range(0, rows):
        for j in range(0, cols):
            Pix_Val = Pixels[i][j]
            Rescale_Pix_Val = Pix_Val * Rescale_Slope + Rescale_Intercept

            if (Rescale_Pix_Val > Window_Max): #if intensity is greater than max window
                New_Img[i][j] = 255
            elif (Rescale_Pix_Val < Window_Min): #if intensity is less than min window
                New_Img[i][j] = 0
            else:
                New_Img[i][j] = int(((Rescale_Pix_Val - Window_Min) / (Window_Max - Window_Min)) * 255) #Normalize the intensities

    return New_Img, Instance_Number

def toMask(row, mask):
    vertices = np.array(row["data"]["vertices"])
    vertices = vertices.reshape((-1, 2))
    mask_instance = mask[:,:].copy()
    cv2.fillPoly(mask_instance, np.int32([vertices]), 1)
    mask[:,:] = mask_instance
    return mask

json_path = 'MIDRC-RICORD-1a_annotations_labelgroup_all_2020-Dec-8.json'

results = mdai.common_utils.json_to_dataframe(json_path)
df = results['annotations']

images = glob.glob('**/*.dcm', recursive=True)
#images = ['1-001.dcm']

i = 0
ids = []
for image in images:
    ds = PDCM.dcmread(image)
    idx = ds.SOPInstanceUID

    anns = df.loc[df['SOPInstanceUID'] == idx]
    if len(anns) > 0:
        print(i)
        #print(image)
        #print(anns)
        
        #Output_Image, Instance_Number = Dicom_to_Image(image)
        image_2d = ds.pixel_array.astype(float)
        image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0
        Output_Image = np.uint8(image_2d_scaled)
        cv2.imwrite('train/images/' + str(i).zfill(6) + '.jpg', Output_Image)

        shape = ds.pixel_array.shape
        mask = np.zeros((shape[0], shape[1]), dtype=np.uint8)

        for row in anns.iterrows():
            #print(row[1])
            if row[1]["data"] is not None:
                mask = toMask(row[1], mask)

        cv2.imwrite('train/masks/' + str(i).zfill(6) + '.png', mask)
        i += 1
        #exit()    
    #
    #
    
    #windowed = apply_voi_lut(ds.pixel_array, ds)
    #image_2d_scaled = np.uint8(windowed)
    #
    #print(wl, ww)
    #img = convert_ct_dicom_to_8bit(ds, windows = [[ww,wl]], imsize=(512.,512.), should_remove_padding = True)
    #image_2d = ds.pixel_array.astype(float)
    #image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0
    #image_2d_scaled = np.uint8(image_2d_scaled)
    #cv2.imwrite('images/{}.jpg'.format(i), image_2d_scaled)
    #with open('images/{}.png'.format(i), 'wb') as png_file:
    #    w = png.Writer(shape[1], shape[0], greyscale=True)
    #    w.write(png_file, image_2d_scaled)
    #img = Image.fromarray(img)
    #img.save('images/{}.jpg'.format(i))
    #
    #break

    #
    #
    #
    #
    #    print(anns)
    
    #ids.append(ds.SOPInstanceUID)






#with open(json_path) as json_file:
#    data = json.load(json_file)
#
#anns = data["datasets"][0]["annotations"]

#c = 0
#for ann in anns:
#    print(ann['SOPInstanceUID'])
#    print(ann)
#    print('--------------------------------------------------------------------------------')
#    c += 1
#    if c == 20:
#        break

#ids = []
#c = 0
#for row in df.iterrows():
#   #print(row[0])
#   #break
#   x = row[1]['SOPInstanceUID']
#   if type(x) == type('a'):
#        print(x)
#        ids.append(x)
#
#print(len(ids))    
#ids = list(set(ids))
##
#print(len(ids))



'''
images = glob.glob('**/*.dcm', recursive=True)

for image in images:
    fs = image.split('/')
    home = fs[0]
    name = fs[-1]
    
    print(name)
    new_path = home + '/' + fs[1].split('.')[-1] + '_' + fs[2].split('.')[-1] + '_' + name
    
    ds = dcmread(image)
    img = ds.pixel_array.astype(float)

    img = (np.maximum(img,0) / img.max()) * 255.0
    img = np.uint8(image_2d_scaled)

    jpg_path = new_path.replace('.dcm','.jpg')
    cv2.imwrite(jpg_path, img)
'''