import time
import picamera
import datetime

camera = picamera.PiCamera()

camera.start_preview(alpha=50)

time.sleep(1)

camera.capture(datetime.datetime.now().strftime("%m-%d-%y_%H-%M-%S") + ".jpg")

camera.stop_preview()
