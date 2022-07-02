# anime-to-manga-panel

Dependencies: cv2, pillow

```
python3 convert_folder.py FORMAT ORIGINALFOLDER NEWFOLDER VALUE
```

ie.
```
python3 convert_folder.py gray pages/mainstream pages/mainstream_gray 1
```

will convert every .jpg file in pages/mainstream to grayscale (using the color shifting method) and place the results in pages/mainstream_gray.

```
Formats = gray, standard_gray, hsv, standard_hsv, detail, edge_enhance, sharpen, smooth
```

```
VALUE = clustering for grayscale, or # of times filter is applied
```
Files in panels/ are for reference.

To get current best images:
```
python3 convert_folder.py hsv pages/mainstream pages/mainstream_gray/hsv 1
python3 convert_folder.py sharpen pages/mainstream/hsv pages/mainstream_gray/hsv_sh 1
```
Images will be in pages/mainstream_gray/hsv_sh
