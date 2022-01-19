import cv2
import os
import shutil
import pythonmosaic

video_name = '00_video.avi'
image_folder = 'images'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 25, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

outpath = os.path.join(os.getcwd(), r'output')
if os.path.exists(outpath) and os.path.isdir(outpath):
    shutil.rmtree(outpath)
os.makedirs(outpath)



cv2.destroyAllWindows()
video.release()

