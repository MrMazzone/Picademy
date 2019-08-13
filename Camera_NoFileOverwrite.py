import time
import picamera
import os

camera = picamera.PiCamera()

camera.start_preview(alpha=50)

num_pics = 0
count = 1
filename = "image" # Change filename to what you want, no need for file extension

while num_pics < 5: # Change 5 to the number of pictures you want to take 
    if os.path.isfile('{}{:03d}.jpg'.format(filename, count)):
        count += 1
    else:
        camera.capture('{}{:03d}.jpg'.format(filename, count))
        print('{}{:03d}.jpg'.format(filename, count))
        num_pics += 1
        time.sleep(1)

camera.stop_preview()

