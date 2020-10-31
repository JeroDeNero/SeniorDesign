#Face Follower for Nvidia Jetson Nano by Neurotek
#Code based on JetsonHacks article for the camera access : https://www.jetsonhacks.com/2019/04/02/jetson-nano-raspberry-pi-camera/  
#WORK IN PROGRESS 

import Jetson.GPIO as GPIO
import Adafruit_PCA9685
import busio
import time
import sys

from signal import signal, SIGINT
from sys import exit

def handler(signalRecieved, frame):
    print("exiting with grace")

    safeNumber = 7

    GPIO.output(safeNumber, GPIO.HIGH)
    
    exit(0)

GPIO.setmode(GPIO.BOARD)
targ = 35
DIR = 40
DIR2 = 38
safeNumber = 7

GPIO.setup(targ, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(safeNumber, GPIO.OUT)

pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=1)
pwm2 = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)

time.sleep(3)
pwm.set_pwm_freq(1600)
pwm2.set_pwm_freq(50)

top_servo_min = 303
top_servo_max = 438

bot_servo_min = 246
bot_servo_max = 360


time.sleep(1)

print('moving servo on channel 0, press Ctrl-C to quit...')

signal(SIGINT, handler)

while True:

    timer = 5

    GPIO.output(safeNumber, GPIO.LOW)

    GPIO.output(DIR, GPIO.LOW)
    GPIO.output(DIR2, GPIO.LOW)

    pwm.set_pwm(0,2000,0)
    pwm.set_pwm(1,2000,0)

    pwm2.set_pwm(0, 0, bot_servo_min)
    pwm2.set_pwm(1, 0, top_servo_min)

    time.sleep(timer)

    print('DIR changeed')

    GPIO.output(DIR, GPIO.HIGH)
    GPIO.output(DIR2, GPIO.HIGH)

    pwm2.set_pwm(0, 0, bot_servo_max)

    time.sleep(timer)

    print('Power to Max')

    pwm.set_pwm(0, 4096, 0)
    pwm.set_pwm(1, 4096, 0)

    pwm2.set_pwm(1, 0, top_servo_max)

    time.sleep(timer)

    print('DIR changed')

    GPIO.output(DIR, GPIO.LOW)
    GPIO.output(DIR2, GPIO.LOW)

    pwm2.set_pwm(0, 0, bot_servo_min)

    time.sleep(timer)

    print('Stopping')
    
    pwm.set_pwm(0,0,0)
    pwm.set_pwm(1,0,0)

    pwm2.set_pwm(0, 0, 303)
    pwm2.set_pwm(1, 0, 303)

    time.sleep(timer) 
