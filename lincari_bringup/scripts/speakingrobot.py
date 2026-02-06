#!/usr/bin/env python

import rospy
from actionlib import SimpleActionClient
from pal_interaction_msgs.msg import TtsAction, TtsGoal
from pyhri import HRIListener
import expressions


def introduce():

    talking_client = SimpleActionClient("/tts", TtsAction)

    # rospy.loginfo("Looking for tts node")
    talking_client.wait_for_server()
    rospy.loginfo("Hello")

    goal = TtsGoal()
    goal.rawtext.text = "Hello! I am ARI a sustainable eating robot!"
    goal.rawtext.lang_id = "en_AU"
    talking_client.send_goal_and_wait(goal)
    rospy.loginfo("Speech Complete")


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
    goal.rawtext.text = "Hello! Welcome to our cafeteria!"
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


def tofu():

    talking_client = SimpleActionClient("/tts", TtsAction)

    # rospy.loginfo("Looking for tts node")
    talking_client.wait_for_server()
    rospy.loginfo("Tofu")

    goal = TtsGoal()
    goal.rawtext.text = "Mushroom noodles are my favourite!"
    goal.rawtext.lang_id = "en_AU"
    expressions.excited
    talking_client.send_goal_and_wait(goal)
    expressions.neutral
    rospy.loginfo("Speech Complete")

def happy():

    talking_client = SimpleActionClient("/tts", TtsAction)

    # rospy.loginfo("Looking for tts node")
    talking_client.wait_for_server()
    rospy.loginfo("Happy")

    goal = TtsGoal()
    goal.rawtext.text = "Thank you for your interest!"
    goal.rawtext.lang_id = "en_AU"
    expressions.excited
    talking_client.send_goal_and_wait(goal)
    expressions.neutral
    rospy.loginfo("Speech Complete")

def green():

    talking_client = SimpleActionClient("/tts", TtsAction)

    # rospy.loginfo("Looking for tts node")
    talking_client.wait_for_server()
    rospy.loginfo("Green")

    goal = TtsGoal()
    goal.rawtext.text = "Let's help our planet together!"
    goal.rawtext.lang_id = "en_AU"
    expressions.excited
    talking_client.send_goal_and_wait(goal)
    expressions.neutral
    rospy.loginfo("Speech Complete")

def dailyfood():
    
    talking_client = SimpleActionClient("/tts", TtsAction)

    # rospy.loginfo("Looking for tts node")
    talking_client.wait_for_server()
    rospy.loginfo("Daily")

    goal = TtsGoal()
    goal.rawtext.text = "The vegan options are delicious"
    goal.rawtext.lang_id = "en_AU"
    expressions.excited
    talking_client.send_goal_and_wait(goal)
    expressions.neutral
    rospy.loginfo("Speech Complete")

def potatoing():

    talking_client = SimpleActionClient("/tts", TtsAction)

    # rospy.loginfo("Looking for tts node")
    talking_client.wait_for_server()
    rospy.loginfo("Potation")

    goal = TtsGoal()
    goal.rawtext.text = "Vegan curry potatos are the best!"
    goal.rawtext.lang_id = "en_AU"
    expressions.excited
    talking_client.send_goal_and_wait(goal)
    expressions.neutral
    rospy.loginfo("Speech Complete")


def alsopotatoing():

    talking_client = SimpleActionClient("/tts", TtsAction)

    # rospy.loginfo("Looking for tts node")
    talking_client.wait_for_server()
    rospy.loginfo("Potation2")

    goal = TtsGoal()
    goal.rawtext.text = "We have Tuna Mayo Potatos!"
    goal.rawtext.lang_id = "en_AU"
    expressions.excited
    talking_client.send_goal_and_wait(goal)
    expressions.neutral
    rospy.loginfo("Speech Complete")


def test():

    talking_client = SimpleActionClient("/tts", TtsAction)

    # rospy.loginfo("Looking for tts node")
    talking_client.wait_for_server()
    rospy.loginfo("testing")

    goal = TtsGoal()
    goal.rawtext.text = "Hello"
    goal.rawtext.lang_id = "en_AU"
    expressions.excited
    talking_client.send_goal_and_wait(goal)
    expressions.neutral
    rospy.loginfo("Speech Complete")


# def asking():

#     talking_client = SimpleActionClient("/tts", TtsAction)

#     # rospy.loginfo("Looking for tts node")
#     talking_client.wait_for_server()
#     # rospy.loginfo("asking")

#     goal = TtsGoal()
#     goal.rawtext.text = "Are you still there?"
#     goal.rawtext.lang_id = "en_AU"
#     expressions.excited
#     talking_client.send_goal_and_wait(goal)
#     expressions.neutral
#     rospy.loginfo("Speech Complete")

def main():
    rospy.init_node("talking_node", anonymous=True)
    greetings()

if __name__ == "__main__":
    try:
        test()
    except rospy.ROSInterruptException:
        pass

