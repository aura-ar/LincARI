#!/usr/bin/env python

import rospy
from actionlib import SimpleActionClient
from pal_interaction_msgs.msg import TtsAction, TtsGoal
from pyhri import HRIListener
import expressions


def hello():
    talking_client = SimpleActionClient("/tts", TtsAction)

    # rospy.loginfo("Looking for tts node")
    talking_client.wait_for_server()
    rospy.loginfo("Hello")

    goal = TtsGoal()
    goal.rawtext.text = "Hello!"
    goal.rawtext.lang_id = "en_AU"
    talking_client.send_goal_and_wait(goal)
    rospy.loginfo("Speech Complete")


def greetings():
    talking_client = SimpleActionClient("/tts", TtsAction)

    # rospy.loginfo("Looking for tts node")
    talking_client.wait_for_server()
    rospy.loginfo("Greetings")

    goal = TtsGoal()
    goal.rawtext.text = "Hello! Welcome to FoodLinks"
    goal.rawtext.lang_id = "en_AU"
    expressions.excited
    talking_client.send_goal_and_wait(goal)
    expressions.neutral
    rospy.loginfo("Speech Complete")


def encourage():

    talking_client = SimpleActionClient("/tts", TtsAction)

    # rospy.loginfo("Looking for tts node")
    talking_client.wait_for_server()
    rospy.loginfo("Encourage")

    goal = TtsGoal()
    goal.rawtext.text = "Check out the average carbon emissions for each protein"
    goal.rawtext.lang_id = "en_AU"
    expressions.excited
    talking_client.send_goal_and_wait(goal)
    expressions.neutral
    rospy.loginfo("Speech Complete")


def guilt():

    talking_client = SimpleActionClient("/tts", TtsAction)

    # rospy.loginfo("Looking for tts node")
    talking_client.wait_for_server()
    rospy.loginfo("Guilt")

    goal = TtsGoal()
    goal.rawtext.text = "How often do you think about sustainable eating?"
    goal.rawtext.lang_id = "en_AU"
    expressions.excited
    talking_client.send_goal_and_wait(goal)
    expressions.neutral
    rospy.loginfo("Speech Complete")

def asking():

    talking_client = SimpleActionClient("/tts", TtsAction)

    # rospy.loginfo("Looking for tts node")
    talking_client.wait_for_server()
    rospy.loginfo("Guilt")

    goal = TtsGoal()
    goal.rawtext.text = "Are you still there?"
    goal.rawtext.lang_id = "en_AU"
    expressions.excited
    talking_client.send_goal_and_wait(goal)
    expressions.neutral
    rospy.loginfo("Speech Complete")

def main():
    rospy.init_node("talking_node", anonymous=True)
    greetings()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass

