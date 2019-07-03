#! /usr/bin/env python
import rospy
from std_srvs.srv import *

def handle_terminate_service(req):
	resp = SetBoolResponse()
	if req.data:
		resp.success = True
		resp.message = "Plan terminated"
		print('Plan terminate message received')

	else:
		resp.success = False
		resp.message = "Plan not terminated"

	return resp


def terminate_service():
	rospy.init_node("terminate_service")
	s = rospy.Service('terminate_planning', SetBool, handle_terminate_service)
	rospy.spin()


if __name__=='__main__':
	terminate_service()