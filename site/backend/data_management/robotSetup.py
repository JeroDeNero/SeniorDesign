# pylint: disable=bare-except
"""to stop pylint from complainign about any excepts"""

from signal import signal, SIGINT

import time
import math
import sys
import _thread

import Jetson.GPIO as GPIO
import Adafruit_PCA9685


def handler(_signalRecieved, _frame):
    print("exiting with grace")

    safeNumber = 7
    GPIO.output(safeNumber, GPIO.HIGH)

    GPIO.cleanup()

    sys.exit(0)


class Robot:
    safeNumber = 7

    motorEncoderPR = 570
    motorFrequency = 1600
    motorAddress = 0x41
    motorBusNum = 1

    # leftMotor
    leftMotorLoc = 0
    leftMotoReversed = False
    motor1DIR = 40
    motor1EncoderXPin = 13
    motor1EncoderYPin = 15

    # rightMotor
    rightMotorLoc = 1
    rightMotoReversed = False
    motor2DIR = 38
    motor2EncoderXPin = 11
    motor2EncoderYPin = 12

    servofrequency = 60
    servoAddress = 0x40
    servoBusNum = 1

    botServoPos = 0
    botServoMin = 246
    botServoRest = 293
    servoRest = 303

    botServoPos = 0
    botServoMin = 246
    botServoMax = 360

    topServoPos = 1
    topServoMin = 303
    topServoRest = 303
    topServoMax = 438

    def __init__(self):

        self.setupBot()

        self.leftMotor = Motor(self.motor1EncoderXPin, self.motor1EncoderYPin, self.motorEncoderPR, self.motorAddress,
                               self.motorBusNum, self.leftMotorLoc, self.motor1DIR, self.leftMotoReversed, self.motorFrequency)
        self.rightMotor = Motor(self.motor2EncoderXPin, self.motor2EncoderYPin, self.motorEncoderPR, self.motorAddress,
                                self.motorBusNum, self.rightMotorLoc, self.motor2DIR, self.rightMotoReversed, self.motorFrequency)

        self.botServo = Servo(self.botServoMin, self.botServoRest, self.botServoMax,
                              self.botServoPos, self.servoAddress, self.servoBusNum, self.servofrequency)
        self.topServo = Servo(self.topServoMin, self.topServoRest, self.topServoMax,
                              self.topServoPos, self.servoAddress, self.servoBusNum, self.servofrequency)

        self.stop()

        GPIO.output(self. safeNumber, GPIO.LOW)

    def setupBot(self):

        #signal(SIGINT, handler)

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.safeNumber, GPIO.OUT)

        GPIO.output(self. safeNumber, GPIO.HIGH)

        GPIO.setup(self.motor1DIR, GPIO.OUT)
        GPIO.setup(self.motor2DIR, GPIO.OUT)
        GPIO.setup(self.motor1EncoderXPin, GPIO.IN)
        GPIO.setup(self.motor1EncoderYPin, GPIO.IN)
        GPIO.setup(self.motor2EncoderXPin, GPIO.IN)
        GPIO.setup(self.motor2EncoderYPin, GPIO.IN)

        time.sleep(0.1)

    def moveCamera(self, state, value):
        print(state)
        if state == 'x':
            self.botServo.goto(value)
        else:
            self.topServo.goto(value)

    def stopCamera(self, *pos):
        print("stopping camera, ", pos)
        if pos is None:
            _thread.start_new_thread(self.botServo.stop())
            _thread.start_new_thread(self.topServo.stop())
        elif 'x' in pos:
            self.botServo.stop()
        else:
            self.topServo.stop()

    def holdCamera(self):
        self.botServo.servoHoldToggle()
        self.topServo.servoHoldToggle()

    def stop(self):
        self.leftMotor.stop()
        self.rightMotor.stop()

        self.botServo.rest()
        self.topServo.rest()

        GPIO.output(self. safeNumber, GPIO.HIGH)

    def releaseStop(self):
        GPIO.output(self.safeNumber, GPIO.LOW)

    def moveStraight(self, value):
        try:
            self.leftMotor.rotate(value)
            self.rightMotor.rotate(value)
        except:
            print("failed to move")
            self.stopMotor()

    def rotate(self, value):
        try:
            self.leftMotor.rotate(value)
            self.rightMotor.rotate(value * -1)
        except:
            print("failed to move")
            self.stopMotor()

    def stopMotor(self):
        try:
            distance1 = self.leftMotor.stop()
            distance2 = self.rightMotor.stop()

            print(distance)
            print(math.pi * 2 * 0.5 * distance)
        except:
            print("failed to stop")
            try:
                handler(0, 0)
            except:
                print("everything failed")


class Motor:

    maxSpeed = 4096

    encoderTotal = 0
    lastEncoder = ''

    def __init__(self, xEncoder, yEncoder, encoderRotation, address, busNum, motorPos, dirPin, reversedDir, frequency):

        GPIO.add_event_detect(xEncoder, GPIO.RISING,
                              callback=self.xCallback)
        GPIO.add_event_detect(yEncoder, GPIO.RISING,
                              callback=self.yCallback)

        self.encoderRot = encoderRotation

        self.pwmController = Adafruit_PCA9685.PCA9685(
            address=address, busnum=busNum)
        self.pwmController.set_pwm_freq(frequency)

        self.motorPos = motorPos
        self.dirPin = dirPin
        self.reversed = reversedDir

    def __delete__(self, instance):
        if self.reversed:
            GPIO.output(self.dirPin, GPIO.LOW)
        else:
            GPIO.output(self.dirPin, GPIO.HIGH)
        self.stop()

    def xCallback(self, _pin):
        if self.lastEncoder == 'x':
            self.encoderTotal += 2
        else:
            self.encoderTotal += 1

        self.lastEncoder = 'x'

    def yCallback(self, _pin):
        if self.lastEncoder == 'y':
            self.encoderTotal += 2
        else:
            self.encoderTotal += 1

        self.lastEncoder = 'y'

    def rotate(self, percent):
        if self.reversed:
            percent = percent * -1

        if percent > 0:
            GPIO.output(self.dirPin, GPIO.HIGH)
        elif percent < 0:
            GPIO.output(self.dirPin, GPIO.LOW)
        else:
            return

        self.pwmController.set_pwm(
            self.motorPos, round(self.maxSpeed * percent), 0)

        print(percent)

    def stop(self):
        self.pwmController.set_pwm(self.motorPos, 0, 0)
        return self.encoderTotal / self.encoderRot


class Servo:
    servoStop = False
    servoHold = False

    def __init__(self, servoMin, servoRest, servoMax, servoNum, address, busnum, frequency):
        self.servoMin = servoMin
        self.servoMax = servoMax
        self.servoRest = servoRest
        self.servoPos = servoRest
        self.servoNum = servoNum

        self.pwmController = Adafruit_PCA9685.PCA9685(
            address=address, busnum=busnum)
        self.pwmController.set_pwm_freq(frequency)

    def __delete__(self, instance):
        self.stop()
        self.rest()

    def goto(self, percent):
        if not self.servoHold:
            self.servoStop = True
            deviation = 0
            print(percent)
            if percent < 0:
                print(self.servoMin)
                deviation = (self.servoRest - self.servoMin) * percent
                print(deviation)
            elif percent > 0:
                deviation = (self.servoMax - self.servoRest) * percent
                print(self.servoMax)
                print(deviation)

            self.stop()

            self.travel(self.servoRest - deviation)

    def travel(self, target):
        if (self.servoPos - target) == 0:
            return
        interval = (self.servoPos - target) / abs(self.servoPos - target) * -1
        while not self.servoStop and not self.servoHold and self.servoPos != round(target):

            print('position ' + str(self.servoPos) + ' target: ' + str(target))

            self.servoPos += interval
            self.pwmController.set_pwm(self.servoNum, 0, round(self.servoPos))
            time.sleep(0.001)

    def rest(self):
        self.pwmController.set_pwm(self.servoNum, 0, self.servoRest)

    def stop(self):
        print("stopping servo " + str(self.servoNum))
        self.servoStop = True
        time.sleep(0.005)
        self.servoStop = False

    def servoHoldToggle(self):
        self.servoHold = not self.servoHold
