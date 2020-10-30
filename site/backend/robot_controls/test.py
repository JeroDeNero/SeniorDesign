#Face Follower for Nvidia Jetson Nano by Neurotek
#Code based on JetsonHacks article for the camera access : https://www.jetsonhacks.com/2019/04/02/jetson-nano-raspberry-pi-camera/  
#WORK IN PROGRESS 

from adafruit_servokit import ServoKit
from __future__ import division
import Jetson.GPIO as GPIO
import Adafruit_PCA9685
import busio
import time
import sys

GPIO.setmode(GPIO.BOARD)
targ = 35
DIR = 40
DIR2 = 38

GPIO.setup(targ, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)

#pull the values from the board output for SCL and SDA and plug in
i2c_bus0=(busio.I2C(board.SCL, board.SDA))
kit = ServoKit(channels=16, i2c=i2c_bus0)

pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)
#pwm2 = Adafruit_PCA9685.PCA9685(address=0x38, busnum=1)

time.sleep(3)
pwm.set_pwm_freq(1600)
#pwm2.set_pwm_freq(1600)
servo_min = 1500
servo_max = 10000

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

while True:

    timer = 5

    kit.servo[0].angle = 0
    kit.servo[1].angle = 0

    GPIO.output(DIR, GPIO.LOW)
    GPIO.output(DIR2, GPIO.LOW)

    pwm.set_pwm(0,2000,0)
    pwm.set_pwm(1,2000,0)

    time.sleep(timer)

    print('DIR changeed')

    kit.servo[0].angle = 5
    kit.servo[1].angle = 0

    GPIO.output(DIR, GPIO.HIGH)
    GPIO.output(DIR2, GPIO.HIGH)

    time.sleep(timer)

    print('Power to Max')

    kit.servo[0].angle = 175
    kit.servo[1].angle = 180

    pwm.set_pwm(0, 4096, 0)
    pwm.set_pwm(1, 4096, 0)

    time.sleep(timer)

    print('DIR changed')

    kit.servo[0].angle = 5
    kit.servo[1].angle = 0

    GPIO.output(DIR, GPIO.LOW)
    GPIO.output(DIR2, GPIO.LOW)

    time.sleep(timer)

    print('Stopping')
    
    kit.servo[0].angle = 90
    kit.servo[1].angle = 90

    pwm.set_pwm(0,0,0)
    pwm.set_pwm(1,0,0)
    time.sleep(timer)

# def 
