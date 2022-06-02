#input: a single image from an anime in jpg/jpeg
#output: a single image grayscaled in jpg/jpeg


import cv2
import time
import os
import sys
from PIL import Image, ImageOps

#input: RGB of type int
#output: RGB shifted to be more mangalike
def grayscaleShift(color):
    gray = color
    if gray < 35:
        gray = 0
    if gray > 150:
        gray = 255
    if gray > 0:
        gray = min(int((gray)*1.1), 255)
    return gray

#Input: RGB of type tuple
#Output: RGB converted to grayscale of type tuple
def colorToGrayscale(color, cluster=1):
    #get gray color
    gray = 0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2]
    #round to nearest cluster
    gray = int((gray//cluster)*cluster)

    #shift for manga coloration
    gray = grayscaleShift(gray)
    return (gray, gray, gray)

def colorShift(color, cluster=1):
    if (color[0] + color[1] + color[2] > 500):
        color = (255,255,255)
    if (color[0] + color[1] + color[2] < 100):
        color = (0,0,0)
    return color

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
        pixels[i] = colorShift(pixels[i], cluster)
        pixels[i] = colorToGrayscale(pixels[i], cluster)
    gray_image = Image.new(image.mode, image.size)
    gray_image.putdata(pixels)
    gray_image.save(newPath)
