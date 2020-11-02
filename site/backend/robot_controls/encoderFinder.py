#Face Follower for Nvidia Jetson Nano by Neurotek
#Code based on JetsonHacks article for the camera access : https://www.jetsonhacks.com/2019/04/02/jetson-nano-raspberry-pi-camera/  
#WORK IN PROGRESS 

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

def yCallback(pin):
    global yCount
    yCount = yCount + 1

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

#pull the values from the board output for SCL and SDA and plug in

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

print('starting')

count = 0

while True:
    GPIO.output(DIR, GPIO.HIGH)
    pwm.set_pwm(0, 4096, 0)
    #GPIO.wait_for_edge(xEncoderPin, GPIO.RISING)

    count = count + 1
    print(count)
    
    

    input()
