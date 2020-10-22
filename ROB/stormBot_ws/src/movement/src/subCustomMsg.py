#!/usr/bin/env python2
import rospy
from movement.msg import messageTest

def messageTestCallback(messageTest):
    rospy.loginfo("new messageTest received: (%s, %d, %.2f, %.2f, %.2f)", 
    messageTest.name, messageTest.id, messageTest.xLin, messageTest.xAng, messageTest.yAng)

rospy. init_node('sub_custom_msg_node', anonymous=True)

sub = rospy.Subscriber('test_topic', messageTest, messageTestCallback)

rospy.spin()