# This file times np usage vs iterative

import numpy as np
from skimage import (io)
from time import time

def create_rgb_small_img_list(pictures):
    rgb_small_imgs = []
    for i in range(len(pictures)):
        rgb_small_imgs.append(get_rgb_small_img(pictures[i]))
    return np.array(rgb_small_imgs)

def get_rgb_small_img(img):
    return np.array(img).mean(axis=(0,1), dtype=int)

def unblockshaped(img_arr_5d):
    h, w, t_h, t_w, c = img_arr_5d.shape
    img_arr_5d = img_arr_5d.swapaxes(2, 1)
    return img_arr_5d.reshape(h*t_h, w*t_w, c)

def blockshaped(img_path, kernel_size: tuple):
    img = io.imread(img_path)
    h, w, c = img.shape
    tile_h, tile_w = kernel_size

    tiled_arr = img.reshape(h // tile_h, tile_h,
                            w // tile_w, tile_w,
                            c)

    tiled_arr = tiled_arr.swapaxes(1, 2)
    return tiled_arr

def avg_rgb_channels_5D_arr(arr_5d):
    return np.mean(arr_5d, axis=(2,3), dtype=int)

def trunc_rgb(arr, fac):
    return np.around(arr*fac).astype(int)

def closest(colors, target):
    distances = np.sqrt(np.sum((colors-target)**2, axis=1))
    index_of_smallest = np.where(distances==np.amin(distances))
    return index_of_smallest[0][0]

def run():
    small_images_path = './images/*.jpg'
    input_image_path = 'lion.jpg'
    pictures = io.imread_collection(small_images_path)
    a = create_rgb_small_img_list(pictures)
    b = blockshaped(input_image_path, (20, 20))
    c = avg_rgb_channels_5D_arr(b)

    # map
    height, width, channels = c.shape
    cache =  {}
    for i in range(height):
        for j in range(width):
            if str(c[i][j]) in cache:
                b[i][j] = pictures[str(c[i][j])]
                continue
            k = closest(a, c[i][j])
            b[i][j] = pictures[k]
            cache[str(b[i][j])] = k


    d = unblockshaped(b)
    io.imsave('testlion.jpg', d)


if __name__ == '__main__':
    start = time()
    run()
    stop = time()
    print("Time NP usage: " + str(stop - start))

