#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose

def poseCallback(pose_message):
    #get_caller_id(): Get fully resolved name of local node
    # rospy.loginfo(rospy.get_caller_id() + "I'm at %s", message.data)
    print "pose callback"
    print ('x = %f' %pose_message.x)
    # print ('x = '.%)
    print ('y = %f' %pose_message.y) #used in python 2
    # print ('y = %f' %)
    print ('theta = %f' %pose_message.theta) # no yaw for pose object, theta in radians

# def position():
if __name__ == '__main__':
    try:

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
        rospy.init_node('position', anonymous=True)
        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

# if __name__ == '__main__':
#     position()
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")