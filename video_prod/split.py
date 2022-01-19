import cv2
vidcap = cv2.VideoCapture('video.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("./images/frame_%s.jpg" % str(count).zfill(3), image)     # save frame as JPEG file      
  success,image = vidcap.read()
#   print('Read a new frame: ', success)
  count += 1
  if count == 1000:
      break