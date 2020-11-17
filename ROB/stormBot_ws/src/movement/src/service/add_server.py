#!/usr/bin/env python

from movement.srv import serviceTest
from movement.srv import serviceTestRequest
from movement.srv import serviceTestResponse

import rospy

def handle_add_two_ints(req):
    print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))
    return serviceTestResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('test_two_ints', serviceTest, handle_add_two_ints)
    print "Ready to add two ints."
    rospy.spin()
    
if __name__ == "__main__":
    add_two_ints_server()