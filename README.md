# pi-parking-sensor
Raspberry Pi ultrasonic parking sensor project


Use this to wire up your ultrasonic sensor:
https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi

I'm using a 330 and 470ohm resistor instead.

Here's the ultrasonic sensor you'll need, can also be purchased from ebay for much cheaper, but on the slow boat from China:
http://www.microcenter.com/product/453103/Ultrasonic_Sensor_Module

You'll also need one, two or several large LEDs, or alternatively you can use RGB LED, or even strips.


Configure your warn/stop and +/- threshold distances in the top of the script.


GPIO:

5V -- power rail

GND -- ground rail

GPIO15 -- GREEN LED +

GPIO18 -- RED LED +

GPIO23 -- TRIGGER (HC-SR04 sensor)

GPIO24 -- ECHO (HC-SR04 sensor) (after 330ohm resistor coming off sensor, then 470ohm resistor connecting to GND)
