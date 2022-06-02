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
def colorToGrayscale(color, shift = False, cluster=1):
    #get gray color
    gray = 0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2]
    #round to nearest cluster
    gray = int((gray//cluster)*cluster)

    #shift for manga coloration
    if shift:
        gray = grayscaleShift(gray)
    return (gray, gray, gray)

def increaseContrast(color, cluster=1):
    if (color[0] + color[1] + color[2] > 500):
        color = (255,255,255)
    if (color[0] + color[1] + color[2] < 100):
        color = (0,0,0)
    color = colorShift(color, 350, 1.1, 0, 250, 0.9, 0)
    return color

def colorShift(color, upThreshold, upPercent, upFlat, downThreshold, downPercent, downFlat):
    colorSum = color[0] + color[1] + color[2]
    if (colorSum >= upThreshold):
        color = (min(int((color[0])*upPercent + upFlat), 255), min(int((color[1])*upPercent + upFlat), 255), min(int((color[2])*upPercent + upFlat), 255))
    if (colorSum <= downThreshold):
        color = (max(int((color[0])*downPercent - downFlat), 0), max(int((color[1])*downPercent - downFlat), 0), max(int((color[2])*downPercent - downFlat), 0))
    if upThreshold > downThreshold:
        mid = downThreshold + (upThreshold - downThreshold)/2
        if (colorSum <= mid):
            shiftPercent = (2+min((mid - colorSum)/mid, 1)*downPercent)/3
            color = (max(int((color[0])*shiftPercent), 0), max(int((color[1])*shiftPercent), 0), max(int((color[2])*shiftPercent), 0))
        else:
            shiftPercent = (2+max((colorSum - mid)/mid, 1)*upPercent)/3
            color = (min(int((color[0])*shiftPercent), 255),min(int((color[1])*shiftPercent), 255), min(int((color[2])*shiftPercent), 255))
    return color

def convert_all(originalPath, newPath):
    image = Image.open(originalPath, 'r')
    gray_image = ImageOps.grayscale(image)
    gray_image.save(newPath)

def setRCToBlack(matrix, row, col):
    matrix[row*col + col] = (0,0,0)

def setSurrounding(originalPixels, element, rows, cols):
    row = element//rows
    col = element%rows
    for i in range(-1, 1):
        for j in range(-1, 1):
            if (row + i == -1 or row + i == rows + 1 or col + j == -1 or col + j == cols + 1):
                continue
            setRCToBlack(originalPixels, row + i, col + j)

def define_borders(originalPath, newPath):
    image = Image.open(originalPath, 'r')
    pixels = list(image.getdata())
    width, height = image.size
    for i in range(len(pixels)):
        if isinstance(pixels[i], int):
            pixels[i] = (pixels[i], pixels[i], pixels[i])
        if pixels[i] == (0,0,0):
            setSurrounding(pixels, i, height, width)
    new_image = Image.new(image.mode, image.size)
    new_image.putdata(pixels)
    new_image.save(newPath)

def convert_cluster(originalPath, newPath, cluster=1):
    image = Image.open(originalPath, 'r')
    pixels = list(image.getdata())
    for i in range(len(pixels)):
        if isinstance(pixels[i], int):
            pixels[i] = (pixels[i], pixels[i], pixels[i])
        pixels[i] = increaseContrast(pixels[i], cluster)
        pixels[i] = colorToGrayscale(pixels[i], False, cluster)
    gray_image = Image.new(image.mode, image.size)
    gray_image.putdata(pixels)
    gray_image.save(newPath)
