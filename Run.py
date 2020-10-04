import os
import cv2
from Allcodes import Homework

#read folder images
img1 = os.path.basename('../lena.jpg')
img2 = os.path.basename('../spine.jpg')


Homework.grayLevel_modification(img1,2)
Homework.median_threshold(img1)
Homework.power_transform(img2,0.45)