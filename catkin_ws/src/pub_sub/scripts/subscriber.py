#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64

#callback function
def callback(msg):
    print("data ==> ", msg)

# Node and Subscriber initialization
rospy.init_node("subscriber")
rospy.Subscriber("topic", Int64, callback)

#spinning
rospy.spin() # same as while not rospy.is_
