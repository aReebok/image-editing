# mosaifyer
🖼️ An image mosaic maker using python's libraries NumPy, scikit-image to create a mosaic output of a given image from small images of flowers.

Hoping to speed up this software to create an API for it for the purpose of adding it to a Discord bot or something!

### Past Run Times (2022)

| Date | Runtime (s) | Changes | 
| ---- | ------------| ------- |
Aug 10 | 9 | Using NumPy vectorization operations with a 5D array
Aug 9 | 104 | Code from Spring '19 that used like 5 nested for-loops

## Contribution Guide
1. Fork the repository.
1. Unzip only the images.zip.
1. Set up working env given the requirements.txt file (PyCharm does it automatically).
1. Run numpy_mosaic.py just to make sure that everything is working!
1. Make code ULTRA FAST! And submit a pull request :D

## Possible routes to speeding up the app
1. Cache previous color matches values.
1. Reduce the precision by dividing all RGB values by 10: giving us a better chance of utilizing caching.
1. Try getting rid of the nested for-loops at the end of the program when matching images.
