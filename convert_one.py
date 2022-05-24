#input: a single image from an anime in jpg/jpeg
#output: a single image grayscaled in jpg/jpeg


import cv2
import time
import os
import sys
from PIL import Image, ImageOps

#Input: RCB of type tuple
#Output: RGB converted to grayscale of type tuple
def colorToGrayscale(color, cluster=1):
    #get gray color
    gray = 0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2]
    #round to nearest cluster
    gray = int((gray//cluster)*cluster)
    return (gray, gray, gray)

def convert_all(originalPath, newPath):
    image = Image.open(originalPath, 'r')
    gray_image = ImageOps.grayscale(image)
    gray_image.save(newPath)

def convert_cluster(originalPath, newPath, cluster=1):
    image = Image.open(originalPath, 'r')
    pixels = list(image.getdata())
    for i in range(len(pixels)):
        if isinstance(pixels[i], int):
            pixels[i] = (pixels[i], pixels[i], pixels[i])
        pixels[i] = colorToGrayscale(pixels[i], cluster)
    gray_image = Image.new(image.mode, image.size)
    gray_image.putdata(pixels)
    gray_image.save(newPath)
