# This file times np usage vs iterative

import numpy as np
from skimage import (io)
from time import time

def create_rgb_small_img_list(pictures):
    rgb_small_imgs = []
    for i in range(len(pictures)):
        rgb_small_imgs.append(rgb_small_img_vectorized(pictures[i]))
    return np.array(rgb_small_imgs)

def rgb_small_img_vectorized(img):
    return np.array(img).mean(axis=(0,1), dtype=int)

def blockshaped(img_path, kernel_size: tuple):
    img = io.imread(img_path)
    h, w, c = img.shape
    tile_h, tile_w = kernel_size

    tiled_arr = img.reshape(h // tile_h, tile_h,
                            w // tile_w, tile_w,
                            c)
    tiled_arr = tiled_arr.swapaxes(1,2)
    return tiled_arr

small_images_path = './images/*.jpg'
input_image_path = 'lion.jpg'
pictures = io.imread_collection(small_images_path)

if __name__ == '__main__':
    a = create_rgb_small_img_list(pictures)
    b = blockshaped(input_image_path, (20,20))
    print(a.shape)
    print(b.shape)


