#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64
 
# Node and Topic initialization
rospy.init_node("publisher_node")
pub =  rospy.Publisher("yagiz", Int64, queue_size= 1)
pub2 =  rospy.Publisher("/gur", Int64, queue_size= 1)




# looping mesages
while not rospy.is_shutdown():
    pub.publish(1013)
    pub2.publish(1218)
    rospy.sleep(1)
    
