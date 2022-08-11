# This file times np usage vs iterative

import numpy as np
from skimage import (io)
from time import time

def time_np(pictures):
    start = time()
    for i in range(len(pictures)):
        print_img_info_vectorized(pictures[i])
    stop = time()
    print("NP vectorized code took time of " + str(stop-start) + " s")


def time_it(pictures):
    start = time()
    for i in range(len(pictures)):
        print_img_info_iteratively(pictures[i])
    stop = time()
    print("Iterative code took time of " + str(stop-start) + " s")

def print_img_info_vectorized(img):
    avg_rgb = np.array(img).mean(axis=(0,1), dtype=int)

def print_img_info_iteratively(img):
    rgb_avg = []
    for k in range(2,-1,-1):
        sum = 0
        for i in range(20):
            for j in  range (20):
                sum += img[i][j][k]
        rgb_avg.append(int(sum/400))

if __name__ == '__main__':
    path = './images/*.jpg'
    pictures = io.imread_collection(path)

    time_it(pictures)
    time_np(pictures)
