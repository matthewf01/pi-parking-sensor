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
GPIO.setup(LED_RED,GPIO.OUT)
GPIO.setup(LED_GREEN,GPIO.OUT)

def lightsoff():
  GPIO.output(LED_GREEN,False)
  GPIO.output(LED_RED, False)

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

lightsoff()

# Allow module to settle
time.sleep(0.5)

'''
#Light test
GPIO.output(LED_RED, True)
time.sleep(1)
GPIO.output(LED_GREEN,True)
time.sleep(1)
GPIO.output(LED_RED, False)
time.sleep(1)
GPIO.output(LED_GREEN,False)
'''

print "Starting ultrasonic distance measure"

while True:
    # Send 10us pulse to trigger 
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()
    while GPIO.input(GPIO_ECHO)==0:
      start = time.time()
      GPIO.output(LED_GREEN,True)

    while GPIO.input(GPIO_ECHO)==1:
      stop = time.time()
      GPIO.output(LED_GREEN,False)
      GPIO.output(LED_RED, True)

    # Calculate pulse length
    elapsed = stop-start

    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * 34000

    # That was the distance there and back so halve the value
    distance = distance / 2

    print "Distance : %.1f" % distance
    lightsoff()
    time.sleep(1)

# Reset GPIO settings
lightsoff()
GPIO.cleanup()

