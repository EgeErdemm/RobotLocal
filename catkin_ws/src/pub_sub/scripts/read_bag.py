#!/usr/bin/env python3

import rospy
import rosbag

rospy.init_node("read_bag")
bag = rosbag.Bag("/home/zekiye/catkin_ws/src/pub_sub/bag/test.bag")

for topic, msg, t in bag.read_messages(topics = ["/sam", "/jenny"]):
  if topic == "/sam":
    print("sam's data is:")
    print(msg.data)
    print("and it was recorded at:")
    print(t)
     
  if topic == "/jenny":
    print("jenny's data is:")
    print(msg.data)
    print("and it was recorded at:")
    print(t)

