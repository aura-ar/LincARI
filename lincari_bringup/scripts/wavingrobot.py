#!/usr/bin/env python

import rospy
from actionlib import SimpleActionClient
from play_motion_msgs.msg import PlayMotionAction, PlayMotionGoal
import speakingrobot, expressions


def waving():
    
    client = SimpleActionClient("/play_motion", PlayMotionAction)

    rospy.loginfo("Looking for Play_Motion Node")
    client.wait_for_server()
    rospy.loginfo("Play_Motion Node ready!")

    goal = PlayMotionGoal()
    goal.motion_name = "wave"
    goal.skip_planning = False
    rospy.loginfo("Executing Movement")
    client.send_goal_and_wait(goal)

    rospy.loginfo("Movement Complete")
    
    
def main():
    rospy.init_node("test_node", anonymous=True)
    #speakingrobot.greetings()
    #expressions.excited()
    #waving()
    expressions.neutral()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
