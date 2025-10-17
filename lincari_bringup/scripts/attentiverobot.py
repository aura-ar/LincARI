import rospy 
from attention_manager_msgs.srv import SetPolicy
from pyhri import HRIListener
from std_msgs.msg import String
import expressions, speakingrobot, wavingrobot
from random import randint

# rosservice call /gaze_manager/enable_neck
# rosservice call /gaze_manager/disable_neck

def speak():
    number = randint(1,4)
    if number == 1:
        speakingrobot.greetings()

    elif number == 2:
        speakingrobot.greetings()

    elif number == 3:
        speakingrobot.greetings()

    elif number == 4:
        wavingrobot.waving()

    rospy.sleep(5)

def main():

    rospy.wait_for_service("/attention_manager/set_policy", timeout = 5)
    set_policy = rospy.ServiceProxy("/attention_manager/set_policy", SetPolicy)
    rospy.Subscriber("/FaceDetection", String)
    response = set_policy(2 , "") # policy 2 empty frame 2 tracks people with eyes3 
    expressions.neutral()
    # rospy.wait_for_service("/gaze_manager/enable_neck", timeout = 5)
    # neck_on = rospy.ServiceProxy("/gaze_manager/enable_neck", )
    while not rospy.is_shutdown():
        print(hri.faces)
        rospy.sleep(1)
        if len(hri.faces) != 0:
            speak()




if __name__ == '__main__':
    try:
        rospy.init_node("FaceDetection")
        hri = HRIListener()
        main()
    except rospy.ROSInterruptException:
        pass
