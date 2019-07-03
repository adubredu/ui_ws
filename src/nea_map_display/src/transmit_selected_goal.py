#! /usr/bin/env python
import rospy
from geometry_msgs.msg import PointStamped, Pose 
from nea_map_display.srv import *


class transmit_goal:
	def __init__(self):
		rospy.init_node('transmit_goal')
		rospy.Subscriber('/clicked_point', PointStamped, self.transmit_goal_service)
		rospy.spin()



	def transmit_goal_service(self, input_goal):
		pose = Pose()
		pose.position.x = input_goal.point.x
		pose.position.y = input_goal.point.y
		rospy.wait_for_service('goal_channel')

		try:
			channel = rospy.ServiceProxy('goal_channel', Goal)
			response = channel(pose)
			print("Goal sent")

			if response.status:
				rospy.loginfo('Goal has been reached!')
			else:
				rospy.loginfo('Something went wrong with service')

		except rospy.ServiceException as e:
			rospy.loginfo("Service call failed: %s"%e)

		return response.status


if __name__=='__main__':
    try:
        send_goal = transmit_goal()

    except rospy.ROSInterruptException: pass