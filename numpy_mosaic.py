# This file times np usage vs iterative

import numpy as np
from skimage import (io)
from time import time
from numpy import savetxt

def create_rgb_small_img_list(pictures):
    rgb_small_imgs = []
    # print(pictures[0].shape)
    for i in range(len(pictures)):
        rgb_small_imgs.append(get_rgb_small_img(pictures[i]))
    return np.array(rgb_small_imgs)

def get_rgb_small_img(img):
    return np.array(img).mean(axis=(0,1), dtype=int)

def blockshaped(img_path, kernel_size: tuple):
    img = io.imread(img_path)
    h, w, c = img.shape
    tile_h, tile_w = kernel_size

    tiled_arr = img.reshape(h // tile_h, tile_h,
                            w // tile_w, tile_w,
                            c)

    tiled_arr = tiled_arr.swapaxes(1, 2)
    tiled_arr_2 = np.mean(tiled_arr, axis=(1,3), dtype=int)
    return tiled_arr

def apply_vec_func(arr):
    get_rgb_small_img_vectorized = np.vectorize(get_rgb_small_img)
    result = get_rgb_small_img_vectorized(arr)
    print(result.shape)

small_images_path = './images/*.jpg'
input_image_path = 'lion.jpg'
pictures = io.imread_collection(small_images_path)

if __name__ == '__main__':
    a = create_rgb_small_img_list(pictures)
    b = blockshaped(input_image_path, (20,20))
    # print(a.shape)
    # print(b.shape)
    # apply_vec_func(b)


