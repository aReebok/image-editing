import numpy as np
from skimage import (io)
from time import time

def create_rgb_small_img_list(pictures):
    rgb_small_imgs = []
    for i in range(len(pictures)):
        rgb_small_imgs.append(get_rgb_small_img(pictures[i]))
    return np.array(rgb_small_imgs)

def get_rgb_small_img(img):
    return np.around(np.array(img).mean(axis=(0,1), dtype=int)*0.1).astype(int)

def closest(colors, target):
    distances = np.sqrt(np.sum((colors-target)**2, axis=1))
    index_of_smallest = np.where(distances==np.amin(distances))
    return index_of_smallest[0][0]


def createMatrix(arr):
    # arr given:
    target = [0,0,0]
    i = closest(arr, target)
    color = arr[i]
    rgb = [26,26,26] #111

    # print(rgb)

    gen_list = {}
    index_count = 0
    for i in range(target[0], rgb[0]+1):
        for j in range(target[1], rgb[1]+1):
            for k in range(target[2], rgb[2]+1):
                # gen_list.append([i,j,k])
                col = np.array([i,j,k])
                gen_list[str(col)] = index_count 
                index_count += 1
    
    # rgb = np.array(arr[i]) # 111
    # gen_list = np.array(gen_list)
    # j = np.where(gen_list == rgb)    
    
    fin = gen_list["[1 1 1]"]
    print (fin)
    print ( list(gen_list.keys())
      [list(gen_list.values()).index(fin)])

    
    




def main():
    small_images_path = './images/*.jpg'
    pictures = io.imread_collection(small_images_path)
    a = create_rgb_small_img_list(pictures)
    createMatrix(a)

if __name__ == "__main__":
    main()
    # print(rgb_to_hex(255,165,1))
    # print(hex_to_rgb(rgb_to_hex(255,165,1)))


# first: 
# [0,0,0] in a (all avg rgb values)
# we get [1,1,1]'s index: but we also need the list itself
# write in file 
# 
#
# [0,0,0] 2836
# 3 for loops 
# [1,0,0] 2836
# [1,1,1]
