from convert_one import convert_all, convert_cluster
import os
import sys

def main(args):
    originalDir = args[0] if len(args) > 0 else 'pages/mainstream'
    newDir = args[1] if len(args) > 1 else 'pages/mainstream_gray'
    conversionType = args[2] if len(args) > 2 else 'all'
    cluster = int(args[3]) if len(args) > 3 else 5

    if not os.path.isdir(newDir):
        os.system("mkdir {0}".format(newDir))

    pages = [f for f in os.listdir(originalDir) if f.lower().endswith(('jpg', '.jpeg'))]
    for p in pages:
        if (conversionType == 'cluster'):
            convert_cluster(os.path.join(originalDir, p), os.path.join(newDir, p), cluster) #2.98s
        else:
            convert_all(os.path.join(originalDir, p), os.path.join(newDir, p)) #0.77s

if __name__ == '__main__':
    main(sys.argv[1:])
