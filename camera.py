#!/usr/bin/python
from picamera import PiCamera
from time import sleep
import sys

sleep(5)
camera = PiCamera()
camera.rotation = 180
camera.resolution = (640, 480)
camera.framerate = 30
#for effect in camera.IMAGE_EFFECTS:
#    camera.image_effect = effect
#    camera.annotate_text = "Effect = %s" % effect
#    sleep(5)
camera.start_recording('/home/pi/putirepo/buatputi/5sec_30fps.h264')
sleep(5)
camera.stop_recording()
sys.exit(0)
#camera.stop_preview()
