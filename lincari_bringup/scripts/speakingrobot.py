#!/usr/bin/env python

import rospy
from actionlib import SimpleActionClient
from pal_interaction_msgs.msg import TtsAction, TtsGoal


def greetings():
    talking_client = SimpleActionClient("/tts", TtsAction)

    rospy.loginfo("Looking for tts node")
    talking_client.wait_for_server()
    rospy.loginfo("Tts Ready!")

    goal = TtsGoal()
    goal.rawtext.text = "Hello!"
    goal.rawtext.lang_id = "en_AU"
    talking_client.send_goal_and_wait(goal)
    rospy.loginfo("Speech Complete")

def main():
    rospy.init_node("talking_node", anonymous=True)
    greetings()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass

