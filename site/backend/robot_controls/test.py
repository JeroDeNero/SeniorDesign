#Face Follower for Nvidia Jetson Nano by Neurotek
#Code based on JetsonHacks article for the camera access : https://www.jetsonhacks.com/2019/04/02/jetson-nano-raspberry-pi-camera/  
#WORK IN PROGRESS 

from __future__ import division
import sys
import time
import Adafruit_PCA9685
#import adafruit_servokit as ServoKit
import Jetson.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

targ = 35
DIR = 40
DIR2 = 38

GPIO.setup(targ, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(DIR2, GPIO.OUT)

pwm1 = Adafruit_PCA9685.PCA9685(address=0x41, busnum=1)
#pwm2 = ServoKit(address=0x41, busnum=1)

pwm1.set_pwm_freq(1600)
#pwm2.set_pwm_freq(50)
servo_min = 1500
servo_max = 10000

time.sleep(1)

print('moving servo on channel 0, press Ctrl-C to quit...')


#def setDirectin(direction):
#    duty = a / 180 * direction + b
#    pwm2.setDuty(channel, duty)
#    print("direction = {} -> duty = {}".format(direction, duty))
#    time.sleep(1) # allow to settle

def testMotors():
    while True:
        timer = 5
        GPIO.output(DIR, GPIO.LOW)
        GPIO.output(DIR2, GPIO.LOW)
        pwm1.set_pwm(0,2000,0)
        pwm1.set_pwm(1,2000,0)
        time.sleep(timer)
        print('DIR changeed')
        GPIO.output(DIR, GPIO.HIGH)
        GPIO.output(DIR2, GPIO.HIGH)
        time.sleep(timer)
        print('Power to Max')
        pwm1.set_pwm(0, 4096, 0)
        pwm1.set_pwm(1, 4096, 0)
        time.sleep(timer)
        print('DIR changed')
        GPIO.output(DIR, GPIO.LOW)
        GPIO.output(DIR2, GPIO.LOW)
        time.sleep(timer)
        print('Stopping')
        pwm1.set_pwm(0,0,0)
        pwm1.set_pwm(1,0,0)
        time.sleep(timer)

#def sweep():
#    sweep = range(30,150)
#    for degree in sweep :
#        pwm2.servo[0].angle=degree
#        pwm2.servo[1].angle=degree

testMotors()
