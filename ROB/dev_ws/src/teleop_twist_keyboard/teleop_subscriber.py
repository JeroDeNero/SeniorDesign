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


def testMotors(speed):
    self.get_logger().info('speed: %s' % speed)

    if speed == 'low_foward':
        # set GPIO.HIGH
        # GPIO.output(DIR, GPIO.HIGH)
        # GPIO.output(DIR2, GPIO.HIGH)
        # pwm1.set_pwm(0,2000,0)
        # pwm1.set_pwm(1,2000,0)
        print('forward: GPIO.HIGH, pwm: 2000')
    if speed == 'high_foward':
        # GPIO.output(DIR, GPIO.HIGH)
        # GPIO.output(DIR2, GPIO.HIGH)
        # pwm1.set_pwm(0,4096,0)
        # pwm1.set_pwm(1,4096,0)
        print('forward: GPIO.HIGH, pwm: 4096')
    if speed == 'low_backward':
        # GPIO.output(DIR, GPIO.LOW)
        # GPIO.output(DIR2, GPIO.LOW)
        # pwm1.set_pwm(0,2000,0)
        # pwm1.set_pwm(1,2000,0)
        print('backward: GPIO.LOW, pwm: 2000')
     if speed == 'high_backward':
        # GPIO.output(DIR, GPIO.LOW)
        # GPIO.output(DIR2, GPIO.LOW)
        # pwm1.set_pwm(0,4096,0)
        # pwm1.set_pwm(1,4096,0)
        print('backward: GPIO.LOW, pwm: 4096')
    if speed == 'stopped':
        # pwm1.set_pwm(0,0,0)
        # pwm1.set_pwm(1,0,0)  
        print('pwm: 0')  
    

    # while True:
        # timer = 5
        # GPIO.output(DIR, GPIO.LOW)
        # GPIO.output(DIR2, GPIO.LOW)
        # pwm1.set_pwm(0,2000,0)
        # pwm1.set_pwm(1,2000,0)
        # time.sleep(timer)
        # print('DIR changed1')
        # GPIO.output(DIR, GPIO.HIGH)
        # GPIO.output(DIR2, GPIO.HIGH)
        # time.sleep(timer)
        # print('Power to Max')
        # pwm1.set_pwm(0, 4096, 0)
        # pwm1.set_pwm(1, 4096, 0)
        # time.sleep(timer)
        # print('DIR changed2')
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
        self.get_logger().info("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
        self.get_logger().info("Angular Components: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))

        targ = 35
        DIR = 40
        DIR2 = 38
        safeNumber = 7
        speed = ''
        print('before assign speed: ', speed)

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

        print('before testMotors() speed: ', speed)
        testMotors(speed)
        # time.sleep(1)
        # signal(SIGINT, handler)

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
