#Face Follower for Nvidia Jetson Nano by Neurotek
#Code based on JetsonHacks article for the camera access : https://www.jetsonhacks.com/2019/04/02/jetson-nano-raspberry-pi-camera/  
#WORK IN PROGRESS 

from adafruit_servokit import ServoKit
from __future__ import division
from sys import exit

import Jetson.GPIO as GPIO
import Adafruit_PCA9685
import signal
import busio
import time
import sys

def handler(signalRecieved, frame):
    print("exiting with grace")

    safeNumber = 7
    GPIO.output(safeNumber, GPIO.HIGH)

    GPIO.cleanup()

    exit(0)

def xCallback(pin):
    global xCount
    xCount = xCount + 1

def yCallback(pin):
    global yCount
    yCount = yCount + 1

signal(SIGINT, handler)

GPIO.setmode(GPIO.BOARD)

safeNumber = 7

DIR = 40
DIR2 = 38

xEncoderPin = 11
yEncoderPin = 12

GPIO.setup(safeNumber, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(xEncoderPin, GPIO.IN)
GPIO.setup(yEncoderPin, GPIO.IN)

GPIO.output(safeNumber, GPIO.HIGH)

#pull the values from the board output for SCL and SDA and plug in
i2c_bus0=(busio.I2C(board.SCL, board.SDA))
kit = ServoKit(channels=16, i2c=i2c_bus0)

pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=1)
pwm2 = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)

time.sleep(3)
pwm.set_pwm_freq(1600)
pwm2.set_pwm_freq(60)

servosRest = 303

topServoMin = 303
topServoMax = 438

botServoMin = 246
botServoMax = 360

time.sleep(1)

def setServoPulse(channel, pulse):
    pulseLength = 1000000
    pulseLength //= 60
    print('{}us per perios'.format(pulseLength))
    pulseLength //= 4096
    print('{}us per bit'.format(pulseLength))
    pulse *= 1000
    pulse //= pulseLength
    pwm.set_pwm(channel, 0, pulse)


print('moving servo on channel 0, press Ctrl-C to quit...')

GPIO.add_event_detect(xEncoderPin, GPIO.RISING, callback=xCallback)
GPIO.add_event_detect(yEncoderPin, GPIO.RISING, callback=yCallback)

signal(SIGINT, handler)

try:
    GPIO.output(safeNumber, GPIO.LOW)
    while True:

        timer = 5

        pwm2.set_pwm(0,0,botServoMin)
        pwm2.set_pwm(1,0,topServoMin)

        GPIO.output(DIR, GPIO.LOW)
        GPIO.output(DIR2, GPIO.LOW)

        start = time.time()

        pwm.set_pwm(0,2000,0)
        pwm.set_pwm(1,2000,0)

        time.sleep(timer)

        print('DIR changeed')

        pwm2.set_pwm(0,0,botServoMax)
        pwm2.set_pwm(1,0,topServoMax)

        GPIO.output(DIR, GPIO.HIGH)
        GPIO.output(DIR2, GPIO.HIGH)

        time.sleep(timer)

        print('Power to Max')

        pwm2.set_pwm(0,0,servosRest)
        pwm2.set_pwm(1,0,topServoMax)

        pwm.set_pwm(0, 4096, 0)
        pwm.set_pwm(1, 4096, 0)

        time.sleep(timer)

        print('DIR changed')

        pwm2.set_pwm(1,0,topServoMin)

        GPIO.output(DIR, GPIO.LOW)
        GPIO.output(DIR2, GPIO.LOW)

        time.sleep(timer)

        print(start - time.time())

        print('Stopping')
        
        pwm2.set_pwm(1,0,servosRest)

        pwm.set_pwm(0,0,0)
        pwm.set_pwm(1,0,0)
        time.sleep(timer)

    except

        print('error')

        GPIO.output(safeNumber, GPIO.HIGH)
        GPIO.cleanup()

# def 
