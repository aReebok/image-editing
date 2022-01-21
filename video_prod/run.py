import cv
import os
import shutil
from pythonmosaic import *

def run():
    images = [img for img in os.listdir('images') if img.endswith(".jpg")]
    len_img = len(images) - 1

    output_path = os.path.join(os.getcwd(), r'output')
    if os.path.exists(output_path) and os.path.isdir(output_path):
        shutil.rmtree(output_path)
    os.makedirs(output_path)

    count = 0
    for image in images:
        print("Working on img \t" + str(count) + "/" + str(len_img))
        save_as = '/output_' + str(count).zfill(3)
        mosaic(image, save_as, 1)
        count += 1