#input: a single image from an anime in jpg/jpeg
#output: a single image grayscaled in jpg/jpeg


import cv2
import time
import os
import sys
from PIL import Image, ImageOps, ImageFilter
import matplotlib.pyplot as plt

def builtin_hsv(originalPath, newPath):
    img = cv2.imread(originalPath)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv_img)
    cv2.imwrite(newPath, v)

def colorShift(value, upThreshold, downThreshold):
    newValue = value
    if newValue >= upThreshold:
        newValue = min(newValue * 1.25 + 20, 255)
    if newValue <= downThreshold:
        newValue = max(newValue * 0.5 - 20, 0)
    newValue = min(newValue * 1.1, 255)
    return newValue

def getBrightnessDistribution(values):
    totalPixels = 0
    valueDistribution = [0 for _ in range(256)]
    for i in range(len(values)):
        for j in range(len(values[i])):
            totalPixels += 1
            valueDistribution[values[i][j]] += 1
    return (valueDistribution, totalPixels)

def getPercentile(sortedArray, totalElements, percentile = 0.5):
    count = 0
    index = 0
    while (count < totalElements*percentile):
        count += sortedArray[index]
        index += 1
    return index

def custom_hsv(originalPath, newPath):
    img = cv2.imread(originalPath)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hue = hsv_img[:,:,0]
    saturation = hsv_img[:,:,1]
    value = hsv_img[:,:,2]

    # saturation = saturation * 0
    for i in range(len(saturation)):
        for j in range(len(saturation[i])):
            saturation[i][j] = 0
    #magic numbers?
    valueDistribution, totalPixels = getBrightnessDistribution(value)
    median = getPercentile(valueDistribution, totalPixels, 0.5)
    upperQuartile = getPercentile(valueDistribution, totalPixels, 0.8)
    lowerQuartile = getPercentile(valueDistribution, totalPixels, 0.2)
    for i in range(len(value)):
        for j in range(len(value[i])):
            #value[i][j] = colorShift(value[i][j], upperQuartile, lowerQuartile)
            #Using hardcoded values seems to work out better, couldn't find a good range for the dynamic version
            value[i][j] = colorShift(value[i][j], 200, 40)

    gray_hsv_img = cv2.merge((hue, saturation, value))
    gray_bgr_img = cv2.cvtColor(gray_hsv_img, cv2.COLOR_HSV2BGR)
    cv2.imwrite(newPath, gray_bgr_img)
