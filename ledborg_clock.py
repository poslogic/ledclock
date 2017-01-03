#! /usr/bin/env python

# ledborg_clock ------ By Cathal Stewart Feb 2014
# 
# Raspberry Pi from - http://www.raspberrypi.org/
#
# Led's from PiBorg - http://www.piborg.org/ledborg/
#
# Import moduals and define function

import time, os, sys
from time import localtime, strftime
import wiringpi
wiringpi.wiringPiSetup()

# Setup the LedBorg GPIO pins
PIN_RED = 0
PIN_GREEN = 2
PIN_BLUE = 3
wiringpi.pinMode(PIN_RED, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(PIN_GREEN, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(PIN_BLUE, wiringpi.GPIO.OUTPUT)

# A function to set the LedBorg colours
def setledborg(red, green, blue):
    wiringpi.digitalWrite(PIN_RED, red)
    wiringpi.digitalWrite(PIN_GREEN, green)
    wiringpi.digitalWrite(PIN_BLUE, blue)

# A function to turn the LedBorg off
def ledborgoff():
    setledborg(0, 0, 0)


def ledborg_clock (count, sequence, speed, repeat, sleep_interval):
	while (count <= int(repeat)):
		for sequence_code in sequence:
			setledborg(sequence_code[0], sequence_code[1], sequence_code[2])
			time.sleep(speed)
		
		time.sleep(sleep_interval)
		count += 1	




# Get hour and min numbers
time_h = strftime("%I", localtime())
time_m = strftime("%M", localtime())

if time_h == '01':
	hour_colour = [2, 2, 2] # white
elif time_h == '02':
	hour_colour = [0, 1, 0] # orange
elif time_h == '03':
	hour_colour = [0, 0, 1] # pink
elif time_h == '04':
	hour_colour = [0, 0, 2] # blue
elif time_h == '05':
	hour_colour = [0, 2, 0] # yellow
elif time_h == '06':
	hour_colour = [0, 1, 1] # blue red
elif time_h == '07':
	hour_colour = [0, 2, 0] # green
elif time_h == '08':
	hour_colour = [0, 0, 2] # blue
elif time_h == '09':
	hour_colour = [0, 1, 0] # red
elif time_h == '10':
	hour_colour = [0, 2, 2] # pea green
elif time_h == '11':
	hour_colour = [2, 2, 2] # white
elif time_h == '12':
	hour_colour = [0, 0, 2] # purple
else:
	hour_colour = [0, 2, 1] # 

if time_m == '15':
	min_flash = 1
elif time_m == '30':
	min_flash = 2
elif time_m == '45':
	min_flash = 3
else:
	min_flash = 4
	
# Set basic colours for use in sequence
black = [0, 0, 0]
red = [2, 0, 0]
blue = [0, 0, 2]

# Setup sqeuence list
quarter_hour_sequence = [black, red, blue, black, red, blue, black, red, blue, black, hour_colour, black]
hour_sequnce = [hour_colour, black, hour_colour, black, hour_colour, black]

# Setup led flash speeds
quarter_hour_led_speed = 0.07
hour_led_speed = 0.03
sleep_speed = 0.75

# Set counter
counter = 1	

# Run the clock	
ledborg_clock(counter, quarter_hour_sequence, quarter_hour_led_speed, min_flash, sleep_speed)
time.sleep(1)
ledborg_clock(counter, hour_sequnce, hour_led_speed, time_h, sleep_speed)
