import Jetson.GPIO as GPIO
import Adafruit_PCA9685
import busio
import time
import sys

from pynput.keyboard import Key, Listener
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

servo_centered = 303

top_servo_min = 303
top_servo_max = 438

bot_servo_min = 246
bot_servo_max = 360

maxDCMotor = 4096

time.sleep(1)

def on_press(key):

    speed = 1

    if(str(key) == 'w'):
        GPIO.output(DIR, GPIO.HIGH)
        GPIO.output(DIR2, GPIO.HIGH)
        pwm.set_pwm(0, maxDCMotor * speed, 0)
        pwm.set_pwm(1, maxDCMotor * speed, 0)

    if(str(key) == 'a'):            
        GPIO.output(DIR, GPIO.LOW)
        GPIO.output(DIR2, GPIO.HIGH)
        pwm.set_pwm(0, maxDCMotor * speed, 0)
        pwm.set_pwm(1, maxDCMotor * speed, 0)

    if(str(key) == 'd'):
        GPIO.output(DIR, GPIO.HIGH)
        GPIO.output(DIR2, GPIO.LOW)
        pwm.set_pwm(0, maxDCMotor * speed, 0)
        pwm.set_pwm(1, maxDCMotor * speed, 0)

    if(str(key) == 's'):
        GPIO.output(DIR, GPIO.LOW)
        GPIO.output(DIR2, GPIO.LOW)
        pwm.set_pwm(0, maxDCMotor * speed, 0)
        pwm.set_pwm(1, maxDCMotor * speed, 0)

    print(key)
    print(type(key))


def on_release(key):
    if(key == 'w' or key == 'a' or key == 'd' or key == 's'):
        pwm.set_pwm(0, 0, 0)
        pwm.set_pwm(1, 0, 0)

    print(key)

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
