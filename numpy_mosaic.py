# This file times np usage vs iterative

import numpy as np
from skimage import (io)
from time import time
from numpy import savetxt

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

# def write_out_small_imgs(a):
#     c = trunc_rgb(a, 0.1)
#     h, c = c.shape
#     d = np.stack((np.arange(start=1, stop=h), c))
#     # print(d.shape)
#     np.savetxt('rgb_small_img.txt', trunc_rgb(a, 0.1), fmt='%d')

small_images_path = './images/*.jpg'
input_image_path = 'lion.jpg'
pictures = io.imread_collection(small_images_path)

def closest(colors, target):
    distances = np.sqrt(np.sum((colors-target)**2, axis=1))
    index_of_smallest = np.where(distances==np.amin(distances))
    # smallest_distance = colors[index_of_smallest]
    return index_of_smallest[0][0]




if __name__ == '__main__':
    a = create_rgb_small_img_list(pictures)
    b = blockshaped(input_image_path, (20, 20))
    c = avg_rgb_channels_5D_arr(b)

    #map
    height, width, channels = c.shape

    for i in range(height):
        for j in range(width):
            b[i][j] = pictures[closest(a, c[i][j])]

    d = unblockshaped(b)
    io.imsave('testlion.jpg', d)