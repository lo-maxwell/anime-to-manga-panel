#input: a single image from an anime in jpg/jpeg
#output: a single image grayscaled in jpg/jpeg

import cv2
import time
import os
import sys
from PIL import Image, ImageOps, ImageFilter

#Input: RGB of type tuple
#Output: RGB converted to grayscale of type tuple
def colorToGrayscale(color, cluster=1):
    #get gray color
    gray = 0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2]
    #round to nearest cluster
    gray = int((gray//cluster)*cluster)
    return (gray, gray, gray)

def increaseContrast(color):
    if (    color[0] + color[1] > 380\
         or color[0] + color[2] > 380\
         or color[1] + color[2] > 380\
         or color[0] + color[1] + color[2] > 510):
        color = (255,255,255)
    if (color[0] + color[1] + color[2] < 100):
        color = (0,0,0)
    color = colorShift(color, 200, 1.1, 0, 200, 0.9, 0)
    return color

def colorShift(color, upThreshold, upPercent, upFlat, downThreshold, downPercent, downFlat):
    colorSum = color[0] + color[1] + color[2]
    if (colorSum >= upThreshold):
        color = (min(int((color[0])*upPercent + upFlat), 255), min(int((color[1])*upPercent + upFlat), 255), min(int((color[2])*upPercent + upFlat), 255))
    if (colorSum <= downThreshold):
        color = (max(int((color[0])*downPercent - downFlat), 0), max(int((color[1])*downPercent - downFlat), 0), max(int((color[2])*downPercent - downFlat), 0))
    return color

def builtin_grayscale(originalPath, newPath):
    image = Image.open(originalPath, 'r')
    gray_image = ImageOps.grayscale(image)
    gray_image.save(newPath)

def convert_cluster(originalPath, newPath, cluster=1):
    image = Image.open(originalPath, 'r')
    pixels = list(image.getdata())
    for i in range(len(pixels)):
        if isinstance(pixels[i], int):
            pixels[i] = (pixels[i], pixels[i], pixels[i])
        pixels[i] = increaseContrast(pixels[i])
        pixels[i] = colorToGrayscale(pixels[i], cluster)
    gray_image = Image.new(image.mode, image.size)
    gray_image.putdata(pixels)
    gray_image.save(newPath)

def enhance(originalPath, newPath, conversionType, value):
    image = Image.open(originalPath)
    if conversionType == 'sharpen':
        # Apply sharp filter
        for i in range(value):
            image = image.filter(ImageFilter.SHARPEN)
    elif conversionType == 'detail':
        # Apply detail filter
        for i in range(value):
            image = image.filter(ImageFilter.DETAIL)
    elif conversionType == 'edge_enhance':
        # Apply edge enhance filter
        for i in range(value):
            image = image.filter(ImageFilter.EDGE_ENHANCE)
    elif conversionType == 'smooth':
        # Apply smooth filter
        for i in range(value):
            image = image.filter(ImageFilter.SMOOTH)
    else:
        print('Instruction format ' + conversionType + ' not recognized. See README for format types.')
    image.save(newPath)
