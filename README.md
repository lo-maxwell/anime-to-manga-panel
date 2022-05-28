# anime-to-manga-panel



```
python3 convert_folder.py ORIGINALFOLDER NEWFOLDER CLUSTER? CLUSTER#
```

ie.
```
python3 convert_folder.py pages/mainstream pages/mainstream_gray cluster 1
```

will convert every .jpg file in pages/mainstream to grayscale (using the color shifting method) and place the results in pages/mainstream_gray.

```
CLUSTER? = cluster
```
will use the color shifting, any other value (or blank) will use the default grayscale conversion with no changes.

```
CLUSTER# = 5
```
will round every grayscale value to the nearest 5

Files in panels/ are for reference. 
