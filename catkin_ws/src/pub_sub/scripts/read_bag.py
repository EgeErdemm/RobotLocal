#!/usr/bin/env python3

import rospy
import rosbag

rospy.init_node("read_bag")
bag = rosbag.Bag("/home/yagiz/catkin_ws/src/pub_sub/bag/kayit.bag")


# birden fazla dinleyeceksen  ==> topics= ["/yagiz","/gur"] yoksa sadece "/tapik_edilecek_node_adı"
for topic, msg, time in bag.read_messages(topics= ["/yagiz","/gur"]):
    if topic == "/yagiz":
        print("Yagiz info:")
        print(msg)
        print(time)
        print("--------------------------------------------------")
    if topic == "/gur":
        print("GUR info:")
        print(msg)
        print(time)
        print("--------------------------------------------------")
   
    else:
        print("nothing")

