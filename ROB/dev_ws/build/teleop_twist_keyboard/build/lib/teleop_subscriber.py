from __future__ import division
import sys
from sys import exit
from signal import signal, SIGINT
import time
# uncomment for Nano
# import Jetson.GPIO as GPIO
# import Adafruit_PCA9685
# test.py above
from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node

# example import file
# import sys
# insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, '../../../site/backend/robot_controls/')
# import test.py

# cal suggests for import
# from robotcontroler/-pat-to-directory- import function/class-name
# from ./-pat-to-directory- import function/class-name

# DIR = motor1, DIR2 = motor2, GPIO.LOW = forward, GPIO.HIGH = backward


def testMotors(speed):
    print('speed: %s' % speed)
    # for turning, will need to expand params to (leftSpeed, rightSpeed)
    # ex. turn left, leftSpeed = 0 or stopped, rightSpeed = 0.5 or low
    # pwm1.set_pwm(0,2000,0) = left motor low
    # pwm1.set_pwm(1, 4096, 0) = right motor high

    # while True:
    #timer = 5
    # GPIO.output(DIR, GPIO.LOW)
    # GPIO.output(DIR2, GPIO.LOW)
    # pwm1.set_pwm(0,2000,0)
    # pwm1.set_pwm(1,2000,0)
    # time.sleep(timer)
    #print('DIR changed1')
    # GPIO.output(DIR, GPIO.HIGH)
    # GPIO.output(DIR2, GPIO.HIGH)
    # time.sleep(timer)
    #print('Power to Max')
    # pwm1.set_pwm(0, 4096, 0)
    # pwm1.set_pwm(1, 4096, 0)
    # time.sleep(timer)
    #print('DIR changed2')
    # GPIO.output(DIR, GPIO.LOW)
    # GPIO.output(DIR2, GPIO.LOW)
    # time.sleep(timer)
    # print('Stopping')
    # pwm1.set_pwm(0,0,0)
    # pwm1.set_pwm(1,0,0)
    # time.sleep(timer)
    # signal(SIGINT, handler)


class KeyboardSubscriber(Node):

    def __init__(self):
        super().__init__('keyboard_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        # self.get_logger().info("receiving keyboard commands: ")
        self.get_logger().info("Linear Components: [%f, %f, %f]" % (
            msg.linear.x, msg.linear.y, msg.linear.z))
        self.get_logger().info("Angular Components: [%f, %f, %f]" % (
            msg.angular.x, msg.angular.y, msg.angular.z))

        targ = 35
        DIR = 40
        DIR2 = 38
        safeNumber = 7

        if msg.linear.x > 0 and msg.linear.x <= 0.5:
            speed = 'low_forward'
        elif msg.linear.x > 0.5:
            speed = 'high_forward'
        elif msg.linear.x < 0 and msg.linear.x >= -0.5:
            speed = 'low_backward'
        elif msg.linear.x < -0.5:
            speed = 'high_backward'
        else:
            speed = 'stopped'

        # testMotors(speed)
        time.sleep(1)
        #signal(SIGINT, handler)


def main(args=None):
    rclpy.init(args=args)

    keyboard_subscriber = KeyboardSubscriber()

    rclpy.spin(keyboard_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    keyboard_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
