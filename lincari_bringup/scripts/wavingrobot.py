#!/usr/bin/env python

import rospy
from actionlib import SimpleActionClient
from play_motion_msgs.msg import PlayMotionAction, PlayMotionGoal


def waving():

    client = SimpleActionClient("/play_motion", PlayMotionAction)

    rospy.loginfo("Looking for Node")
    client.wait_for_server()
    rospy.loginfo("Node ready!")

    
    goal = PlayMotionGoal()
    goal.motion_name = "wave"
    goal.skip_planning = False

    client.send_goal_and_wait(goal)

    
    rospy.loginfo("Movement Complete")
    
    
def main():
    rospy.init_node("test_node", anonymous=True)
    waving()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
