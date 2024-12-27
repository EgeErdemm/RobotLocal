#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64

# Callback function
def callback(msg):
    print(msg)

# Node + subscriber initialization
rospy.init_node("subscriber_node")
rospy.Subscriber("topic", Int64, callback)

# Spinning
rospy.spin()
