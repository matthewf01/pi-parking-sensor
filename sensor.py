#!/usr/bin/python
#modified script from http://www.raspberrypi-spy.co.uk/2012/12/ultrasonic-distance-measurement-using-python-part-1/

#Import required Python libraries
import time
import RPi.GPIO as GPIO

#GPIO setup
GPIO.setmode(GPIO.BCM)
#ultrasonic sensor
GPIO_TRIGGER = 23
GPIO_ECHO = 24
LED_RED = 18
LED_GREEN = 15

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo
red = GPIO.setup(LED_RED,GPIO.OUT)
green = GPIO.setup(LED_GREEN,GPIO.OUT)

#parking distances
dist_warn= 30
dist_stop= 15
#Maximum allowable centimeters to exceed the exact stop distance "dist_stop"
dist_stop_tolerance=0


def slowblink(color):
  GPIO.output(color,True)
  time.sleep(0.4)
  GPIO.output(color,False)
  time.sleep(0.5)
  
def fastblink(color):
  GPIO.output(color,True)
  time.sleep(0.2)
  GPIO.output(color,False)
  time.sleep(0.1)

def hyperblink(color):
  GPIO.output(color,True)
  time.sleep(0.1)
  GPIO.output(color,False)
  time.sleep(0.06)
  GPIO.output(color,True)
  time.sleep(0.1)
  GPIO.output(color,False)
  time.sleep(0.06)
  GPIO.output(color,True)
  time.sleep(0.1)
  GPIO.output(color,False)
  time.sleep(0.06)
  GPIO.output(color,True)
  time.sleep(0.1)
  GPIO.output(color,False)
  time.sleep(0.06)
  
def lightsoff():
  GPIO.output(LED_GREEN,False)
  GPIO.output(LED_RED, False)

def measure():
  # This function measures a distance
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()
  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()
  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()
  elapsed = stop-start
  distance = (elapsed * 34300)/2
  return distance
  
def calculate_average():
  # This function takes 3 measurements and returns the average.
  distance1=measure()
  time.sleep(0.1)
  distance2=measure()
  time.sleep(0.1)
  distance3=measure()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)
lightsoff()

#Light test
GPIO.output(LED_RED, True)
time.sleep(0.5)
GPIO.output(LED_GREEN,True)
time.sleep(0.5)
GPIO.output(LED_RED, False)
time.sleep(0.5)
GPIO.output(LED_GREEN,False)

print "Starting ultrasonic distance measure"

try:
  
  while True:
    distance = calculate_average()
    print "Distance : %.1f" % distance
    if distance > dist_warn:
     slowblink(LED_GREEN)
    time.sleep(0.5)
    

#  elseif distance <= distwarn or

except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  lightsoff()
  GPIO.cleanup()
