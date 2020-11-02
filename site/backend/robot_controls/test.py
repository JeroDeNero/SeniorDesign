# Face Follower for Nvidia Jetson Nano by Neurotek
# Code based on JetsonHacks article for the camera access : https://www.jetsonhacks.com/2019/04/02/jetson-nano-raspberry-pi-camera/
# WORK IN PROGRESS

from sys import exit
from signal import signal, SIGINT

import Jetson.GPIO as GPIO
import Adafruit_PCA9685
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
    print('x')


def yCallback(pin):
    global yCount
    yCount = yCount + 1
    print('y')


def xCallback2(pin):
    global xCount2
    xCount2 = xCount2 + 1


def yCallback2(pin):
    global yCount2
    yCount2 = yCount2 + 1


signal(SIGINT, handler)

GPIO.setmode(GPIO.BOARD)

safeNumber = 7

DIR = 40
DIR2 = 38
safeNumber = 7

xEncoderPin = 13
yEncoderPin = 15
xEncoderPin2 = 11
yEncoderPin2 = 12

xCount = 0
yCount = 0
xCount2 = 0
yCount2 = 0

GPIO.setup(safeNumber, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(xEncoderPin, GPIO.IN)
GPIO.setup(yEncoderPin, GPIO.IN)
GPIO.setup(xEncoderPin2, GPIO.IN)
GPIO.setup(yEncoderPin2, GPIO.IN)

GPIO.output(safeNumber, GPIO.HIGH)

# pull the values from the board output for SCL and SDA and plug in

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

top_servo_min = 303
top_servo_max = 438

bot_servo_min = 246
bot_servo_max = 360


time.sleep(1)

print('moving servo on channel 0, press Ctrl-C to quit...')

GPIO.add_event_detect(xEncoderPin, GPIO.RISING, callback=xCallback)
GPIO.add_event_detect(yEncoderPin, GPIO.RISING, callback=yCallback)
GPIO.add_event_detect(xEncoderPin2, GPIO.RISING, callback=xCallback2)
GPIO.add_event_detect(yEncoderPin2, GPIO.RISING, callback=yCallback2)

signal(SIGINT, handler)

try:
    GPIO.output(safeNumber, GPIO.LOW)
    while True:
        start = time.time()

        timer = 20

#        pwm2.set_pwm(0,0,botServoMin)
#        pwm2.set_pwm(1,0,topServoMin)
#
#        GPIO.output(DIR, GPIO.LOW)
#        GPIO.output(DIR2, GPIO.LOW)
#
#
#        pwm.set_pwm(0,2000,0)
#        pwm.set_pwm(1,2000,0)
#
#        time.sleep(timer)
#
#        print('DIR changeed')
#
#        pwm2.set_pwm(0,0,botServoMax)
#        pwm2.set_pwm(1,0,topServoMax)
#
#        GPIO.output(DIR, GPIO.HIGH)
#        GPIO.output(DIR2, GPIO.HIGH)
#
#        time.sleep(timer)
#
        print('Power to Max')

        pwm2.set_pwm(0, 0, servosRest)
        pwm2.set_pwm(1, 0, topServoMax)

        pwm.set_pwm(0, 4096, 0)
        pwm.set_pwm(1, 4096, 0)

        time.sleep(timer)

#        print('DIR changed')
#
#        pwm2.set_pwm(1,0,topServoMin)
#
#        GPIO.output(DIR, GPIO.LOW)
#        GPIO.output(DIR2, GPIO.LOW)
#
#        time.sleep(timer)
        end = (time.time() - start)/60

        print(end)

        print(xCount)
        print(yCount)
        print(xCount2)
        print(yCount2)

        print('x1 = ' + str((xCount / 1440) / end))
        print('y1 = ' + str((yCount / 1440) / end))
        print('x2 = ' + str((xCount2 / 1440) / end))
        print('y2 = ' + str((yCount2 / 1440) / end))
        print('Stopping')

        pwm2.set_pwm(0, 0, servosRest)
        pwm2.set_pwm(1, 0, servosRest)

        pwm.set_pwm(0, 0, 0)
        pwm.set_pwm(1, 0, 0)
        time.sleep(timer)

except:

    print('error')

    GPIO.output(safeNumber, GPIO.HIGH)
    GPIO.cleanup()
