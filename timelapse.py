#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from time import sleep
from picamera import PiCamera
from config import plant_type

camera 				= PiCamera()
camera.framerate 		= 30
camera.iso 			= 800 		# The higher the ISO the brighter the image, for bright daylight captures 100-200 are sufficient
camera.resolution 		= (1920, 1080) 	# 2592 x 1944 is the max resolution for RPI Cam Modules v1, if you are using v2 (which supports 8MP) you might want to change this to 3280 × 2464 pixels
camera.start_preview()
# Wait for the automatic gain control to settle
sleep(2)
# Then affix the values
camera.shutter_speed 		= camera.exposure_speed
camera.exposure_mode 		= 'off'
gains 				= camera.awb_gains
camera.awb_mode 		= 'off'
camera.awb_gains 		= gains
camera.sharpness 		= 0
camera.contrast 		= 0
camera.brightness 		= 60
camera.saturation 		= 0
camera.video_stabilization 	= False
camera.exposure_compensation 	= 0
camera.meter_mode 		= 'average'
camera.image_effect 		= 'none'
camera.color_effects 		= None
camera.rotation 		= 0
camera.hflip 			= False
camera.vflip 			= False
camera.crop 			= (0.0, 0.0, 1.0, 1.0)

while True:
	timestamp 		= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	overlay			= 'EnviroPi ' + plant_type + ' ' + timestamp
	camera.annotate_text 	= overlay
	filename 		= next(camera.capture_continuous('assets/timelapse/' + plant_type + '_' + '{timestamp:%Y-%m-%d_%H:%M:%S}' + '.jpg'))
	print('Captured %s' % filename)
	sleep(1200) 		# wait 20 minutes (=1200s)

