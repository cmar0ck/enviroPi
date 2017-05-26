#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import datetime
import sqlite3 as lite
import sys

from envirophat import light, motion, weather, leds, analog
from config import plant_type

interval 		= 12 	#Interval in seconds in which the sensor data will be read and written into the database
con 			= lite.connect('assets/db/enviro.db')

try:
    while True:

	timestamp 	= datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        lux 		= light.light()
        leds.on()
        rgb 		= str(light.rgb())[1:-1].replace(' ', '')
        leds.off()
        acc 		= str(motion.accelerometer())[1:-1].replace(' ', '')
        heading 	= motion.heading()
        temp 		= (weather.temperature() - 10)
        press 		= weather.pressure()
        altitude 	= weather.altitude()
        moisture 	= analog.read(0) 
	
	writeout = (
	    (timestamp, lux, rgb, acc, heading, temp, press, altitude, moisture),
	)

	with con:
		
    		cur 	= con.cursor()    
    		cur.execute("CREATE TABLE IF NOT EXISTS " + plant_type + " (Date DATETIME, Brightness INT, LightColor TEXT, Motion FLOAT, Heading INT, Temperature FLOAT, Pressure FLOAT, Altitude INT, Moisture FLOAT)")
    		cur.executemany("INSERT INTO " + plant_type + " VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", writeout)
        
	time.sleep(interval)

finally:
    leds.off()
