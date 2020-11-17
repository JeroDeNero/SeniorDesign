#!/usr/bin/env python2
import rospy
from movement.msg import messageTest
import random

pub = rospy.Publisher('test_topic', messageTest, queue_size=10)

rospy.init_node('pub_custom_msg_node', anonymous=True)

rate = rospy.Rate(0.5)

i = 0
while not rospy.is_shutdown():
    customMessage = messageTest()
    customMessage.name = "stormBot_data1"
    customMessage.id = 1
    customMessage.xLin = 5 + (random.random() * 2)
    customMessage.xAng = 0
    customMessage.yAng = 0
    rospy.loginfo("I publish: ")
    rospy.loginfo(customMessage)
    pub.publish(customMessage)
    rate.sleep()
    i = i + 1