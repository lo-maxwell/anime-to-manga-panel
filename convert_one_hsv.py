#input: a single image from an anime in jpg/jpeg
#output: a single image grayscaled in jpg/jpeg


import cv2
import time
import os
import sys
from PIL import Image, ImageOps, ImageFilter

def builtin_hsv(originalPath, newPath):
    img = cv2.imread(originalPath)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    print(originalPath)
    print(hsv_img)
    #convert back to image
    bgr_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
    cv2.imwrite(newPath, bgr_img)

def custom_hsv(originalPath, newPath):
    img = cv2.imread(originalPath)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for i in hsv_img:
        #do something with the hsv array?
        break
    print(originalPath)
    print(hsv_img)
    #convert back to image
    bgr_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
    cv2.imwrite(newPath, bgr_img)
