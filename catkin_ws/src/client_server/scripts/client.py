#!/usr/bin/env python3

import rospy
from std_srvs.srv import SetBool, SetBoolRequest

#initialize client node
rospy.init_node("client_node")

#define client and wait for service
# test_service ismi server.py dosyasında geliyor
client = rospy.ServiceProxy("test_service",SetBool)
client.wait_for_service()

#create response message
request = SetBoolRequest()
request.data = False


#get response store in response variable
response = client(request)


print(response)
