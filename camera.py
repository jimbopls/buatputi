#!/usr/bin/python
from picamera import PiCamera
from time import sleep
import sys

sleep(5)
camera = PiCamera()
camera.rotation = 180
camera.resolution = (1280, 720)
camera.framerate = 30
#for effect in camera.IMAGE_EFFECTS:
#    camera.image_effect = effect
#    camera.annotate_text = "Effect = %s" % effect
#    sleep(5)
camera.start_recording('/home/pi/180_sec_recording_1280_720_30fps.h264')
sleep(180)
camera.stop_recording()
sys.exit(0)
#camera.stop_preview()
