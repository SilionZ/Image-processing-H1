#Silion Zhang

#Import library
import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

#create a class for outside cite
class Homework:
    #Create three function for each problem solving
        #1.Gray_level
        #2.Median_threshold
        #3.Power_trans

    #define function name with two paramters,
    #img: input img,r: adjust number
    def grayLevel_modification(img,r):
        #data for read img, 
        #px is function to modify each pixels in imgae
        #use np.clip limit number in range 0,255
        data = cv2.imread(img,0)
        px = np.clip([i+int(16*np.sqrt(r))for i in data],0,255)
        
        #display two image together
        output = cv2.hconcat([data,px])
        cv2.imshow('Output',output)
       
        #press any keys to close window
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        #----------Histogram for checking----------#
        # hist = plt.hist(px.ravel(),256,[0,256])
        # plt.show()
        # hist2 = plt.hist(data.ravel(),256,[0,256])
        # plt.show()
        #----------Histogram for checking----------#

    def median_threshold(img):
        #data for read img, 
        #px is function to modify each pixels in imgae
        #use np.median calculate the median value in image
        data = cv2.imread(img, 0)
        median = int(np.median(data))
        ret,px = cv2.threshold(data, median, 255, cv2.THRESH_BINARY)
       
        #display two image together
        output = cv2.hconcat([data,px])
        cv2.imshow('Output',output)

        #press any keys to close window
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        #----------Histogram for checking----------#
        # hist = plt.hist(px.ravel(),256,[0,256])
        # plt.show()
        # hist2 = plt.hist(data.ravel(),256,[0,256])
        # plt.show()
        #----------Histogram for checking----------#


    def power_transform(img,y):
        #data for read img, 
        #px is function to modify each pixels in imgae
        #binding px data type as unit8
        data = cv2.imread(img,0)
        px = np.array([255*(i/255)**y for i in data],dtype=np.uint8)

        #display two image together
        output = cv2.hconcat([data,px])
        cv2.imshow('Output',output)

        #press any keys to close window
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        #----------Histogram for checking----------#
        # hist = plt.hist(px.ravel(),256,[0,256])
        # plt.show()
        # hist2 = plt.hist(data.ravel(),256,[0,256])
        # plt.show()
        #----------Histogram for checking----------#