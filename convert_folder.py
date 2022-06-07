from convert_one import convert_all, convert_cluster, define_borders, enhance
import os
import sys
#Want to get similar colors to manga page, not just grayscale

def main(args):
    originalDir = args[0] if len(args) > 0 else 'pages/mainstream'
    newDir = args[1] if len(args) > 1 else 'pages/mainstream_gray'
    conversionType = args[2] if len(args) > 2 else 'all'
    cluster = max(int(args[3]), 1) if len(args) > 3 else 5

    if not (os.path.exists(newDir) and os.path.isdir(newDir)):
        os.makedirs(newDir)

    pages = [f for f in os.listdir(originalDir) if f.lower().endswith(('jpg', '.jpeg'))]
    for p in pages:
        originalPath = os.path.join(originalDir, p)
        newPath = os.path.join(newDir, p)
        if (conversionType.lower() == 'gray'):
            convert_cluster(originalPath, newPath, cluster) #2.98s
        elif (conversionType.lower() == 'standard'):
            convert_all(originalPath, newPath) #0.77s
        elif (conversionType.lower() == 'define'):
            define_borders(originalPath, newPath)
        elif (conversionType.lower() == 'detail' or
            conversionType.lower() == 'edge_enhance' or
            conversionType.lower() == 'sharpen' or
            conversionType.lower() == 'smooth'):
            enhance(originalPath, newPath, conversionType.lower(), cluster)
        else:
            print('Instruction format ' + conversionType + ' not recognized. See README for format types.')
            break
        
if __name__ == '__main__':
    main(sys.argv[1:])
