import cv2
import os
import shutil

# code from
# https://www.programcreek.com/python/example/72134/cv2.VideoWriter

def join():
    video_name = '08_output.mp4'
    image_folder = 'output_backup'

    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    # video = cv2.VideoWriter(video_name, fourcc, 25, (width,height))
    video = cv2.VideoWriter(video_name, 0x00000021, 25, (width,height))

    count = 0
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))


    cv2.destroyAllWindows()
    video.release()