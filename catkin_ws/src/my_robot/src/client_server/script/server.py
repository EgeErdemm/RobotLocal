#!/usr/bin/env python3

import rospy
from std_srvs.srv import SetBool,SetBoolResponse

def callback(req):
 response = SetBoolResponse()
 if req.data == True:
  response.success=True
  response.message="The device was enabled"
 else:
  response.success=True
  response.message="The device was disenabled"
  
 return response 

rospy.init_node("server")
rospy.Service("test_service", SetBool, callback)

rospy.spin()

