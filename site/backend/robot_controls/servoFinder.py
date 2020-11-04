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

pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=1)
pwm2 = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)

time.sleep(3)
pwm.set_pwm_freq(1600)
pwm2.set_pwm_freq(50)
servo_min = 1500
servo_max = 10000
pulselen_1 = 300 

while True:

    print(pulselen_1)

    pwm2.set_pwm(1, 0, 246);
    pwm2.set_pwm(0, 0, 438);
    pulselen_1 = pulselen_1 - 1

    input()
