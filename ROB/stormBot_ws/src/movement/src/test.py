#! /usr/bin/env python

import rospy

rospy.init_node('test')
rate = rospy.Rate(1)

while not rospy.is_shutdown():
    print "Hello there"
    rate.sleep()