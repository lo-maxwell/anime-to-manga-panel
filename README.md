# anime-to-manga-panel



```
python3 convert_folder.py ORIGINALFOLDER NEWFOLDER FORMAT VALUE
```

ie.
```
python3 convert_folder.py pages/mainstream pages/mainstream_gray gray 1
```

will convert every .jpg file in pages/mainstream to grayscale (using the color shifting method) and place the results in pages/mainstream_gray.

```
Formats = gray, standard, detail, edge_enhance, sharpen, smooth
```

```
VALUE = clustering for grayscale, or # of times filter is applied
```
Files in panels/ are for reference.
