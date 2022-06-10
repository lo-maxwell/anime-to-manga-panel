from convert_one_rgb import custom_grayscale, builtin_grayscale, enhance
from convert_one_hsv import builtin_hsv, custom_hsv
import os
import sys
#Want to get similar colors to manga page, not just grayscale

def checkIfDirectoryExistsIfNotCreateOne(nameOfDirectory):
    if not (os.path.exists(nameOfDirectory) and os.path.isdir(nameOfDirectory)):
        os.makedirs(nameOfDirectory)

def main(args):
    conversionType = args[0].lower() if len(args) > 0 else 'ERROR'
    originalDir = args[1] if len(args) > 1 else 'pages/mainstream'
    newDir = args[2] if len(args) > 2 else 'pages/mainstream_gray'
    value = max(int(args[3]), 1) if len(args) > 3 else 1

    checkIfDirectoryExistsIfNotCreateOne(newDir)

    listOfPages = [imageFileName for imageFileName in os.listdir(originalDir) if imageFileName.lower().endswith(('jpg', '.jpeg'))]

    for page in listOfPages:
        originalPath = os.path.join(originalDir, page)
        newPath = os.path.join(newDir, page)
        if (conversionType == 'gray'):
            custom_grayscale(originalPath, newPath, value) #2.98s
        elif (conversionType == 'standard_gray'):
            builtin_grayscale(originalPath, newPath) #0.77s
        elif (conversionType == 'hsv'):
            custom_hsv(originalPath, newPath)
        elif (conversionType == 'standard_hsv'):
            builtin_hsv(originalPath, newPath)
        elif (conversionType == 'detail' or
            conversionType == 'edge_enhance' or
            conversionType == 'sharpen' or
            conversionType == 'smooth'):
            enhance(originalPath, newPath, conversionType, value)
        else:
            print('Instruction format ' + conversionType + ' not recognized. See README for format types.')
            break

if __name__ == '__main__':
    listOfArguments = sys.argv[1:]
    main(listOfArguments)
