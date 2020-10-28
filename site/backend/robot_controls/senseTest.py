# coding: utf-8
## @package faboMPU9250
#  This is a library for the FaBo 9AXIS I2C Brick.
#
#  http://fabo.io/202.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

import FaBo9Axis_MPU9250
import time
import sys
import math

mpu9250 = FaBo9Axis_MPU9250.MPU9250()

    ## Read magneto
try:
    while True:
        #accel = mpu9250.readAccel()
        #print(" ax = " , ( accel['x'] ))
        #print(" ay = " , ( accel['y'] ))
        #print(" az = " , ( accel['z'] ))

        #gyro = mpu9250.readGyro()
        #print(" gx = " , ( gyro['x'] ))
        #print(" gy = " , ( gyro['y'] ))
        #print(" gz = " , ( gyro['z'] ))

        mag = mpu9250.readMagnet()
        #print(" mx = " , ( mag['x'] ))
        #print(" my = " , ( mag['y'] ))
        #print(" mz = " , ( mag['z'] ))

        x = (mag["x"] + 45)  * (math.pi / 180) * 0.48828125
        y = (mag["y"] + 45)  * (math.pi / 180) *0.48828125

        d = 0

        if (x == 0):
            if (y < 0):
                d = 90
            else:
                d = 0
        else :
            d = math.atan(y/x) * (180/math.pi)

        answer = d

        if (answer > 360):
            answer = answer - 360
        elif (answer < 0):
            answer = answer + 360

        print("bearing = " , answer)

        time.sleep(0.5)

except KeyboardInterrupt:
    sys.exit()

