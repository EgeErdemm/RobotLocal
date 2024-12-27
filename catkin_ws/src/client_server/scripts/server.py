#!/usr/bin/env python3

import rospy
from std_srvs.srv import SetBool,SetBoolResponse


def callback(request):
    #Create response message for service using std_srvs.srv
    response = SetBoolResponse()
    
    #exacution
    if request.data ==True:
        response.success = True
        response.message = "The device was enabled"
    else:
        response.success = True
        response.message = "The device was disabled"
       
    #return    
    return response
        
#node initilaization
rospy.init_node("server_node")
rospy.Service("test_service",SetBool,callback)

rospy.spin() 
