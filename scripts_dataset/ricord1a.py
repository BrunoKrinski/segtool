import os
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

os.mkdir('all/')
os.mkdir('all/images/')
os.mkdir('all/masks/')

i = 0
ids = []
for image in images:
    ds = PDCM.dcmread(image)
    idx = ds.SOPInstanceUID

    anns = df.loc[df['SOPInstanceUID'] == idx]
    if len(anns) > 0:
        print(i)
        
        #Output_Image, Instance_Number = Dicom_to_Image(image)
        image_2d = ds.pixel_array.astype(float)
        image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0
        Output_Image = np.uint8(image_2d_scaled)
        cv2.imwrite('all/images/' + str(i).zfill(6) + '.jpg', Output_Image)

        shape = ds.pixel_array.shape
        mask = np.zeros((shape[0], shape[1]), dtype=np.uint8)

        for row in anns.iterrows():
            #print(row[1])
            if row[1]["data"] is not None:
                mask = toMask(row[1], mask)

        cv2.imwrite('all/masks/' + str(i).zfill(6) + '.png', mask)
        i += 1