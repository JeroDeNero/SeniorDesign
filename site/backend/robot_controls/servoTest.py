# SDA = pin.SDA_1
# SCL = pin.SCL_1
# SDA_1 = pin.SDA
# SCL_1 = pin.SCL

from adafruit_servokit import ServoKit
import board
import busio
import time

# On the Jetson Nano
# Bus 0 (pins 28,27) is board SCL_1, SDA_1 in the jetson board definition file
# Bus 1 (pins 5, 3) is board SCL, SDA in the jetson definition file
# Default is to Bus 1; We are using Bus 0, so we need to construct the busio first ...
print("Initializing Servos")
print(board.SDA)
print(board.SCL)
i2c_bus0=(busio.I2C(board.SCL, board.SDA))
print("Initializing ServoKit")
kit = ServoKit(channels=16, i2c=i2c_bus0)
# kit[0] is the bottom servo
# kit[1] is the top servo
print("Done initializing")
sweep = range(5,180)

while 0:
    for degree in sweep :
        kit.servo[0].angle=degree
        kit.servo[1].angle=degree

    time.sleep(0.5)
    p = range(180,0, -1)
    sweep = range(180,0, -1)
    sweep = range(180,5, -1)
    
    for degree in sweep :
        kit.servo[0].angle=degree
        kit.servo[1].angle=degree

    sweep = range(0,180)
    sweep = range(5,180)

    for degree in sweep :
        kit.servo[0].angle=degree
        kit.servo[1].angle=180 - degree

    sweep = range(0,180)
    sweep = range(5,180)

    for degree in sweep :
        kit.servo[0].angle=180 - degree
        kit.servo[1].angle=degree

kit.servo[0].angle = 0

time.sleep(5)

kit.servo[1].angle = 0

time.sleep(5)

kit.servo[0].angle = 180
kit.servo[1].angle = 180

time.sleep(5)

kit.servo[0].angle = 0
kit.servo[1].angle = 180

time.sleep(5)

kit.servo[0].angle = 180
kit.servo[1].angle = 0

time.sleep(5)

kit.servo[0].angle = 90
kit.servo[1].angle = 90
