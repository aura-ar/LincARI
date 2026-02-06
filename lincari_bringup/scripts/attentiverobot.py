import rospy 
from attention_manager_msgs.srv import SetPolicy
from pyhri import HRIListener
from std_msgs.msg import String
import expressions, speakingrobot, wavingrobot
from pal_interaction_msgs.msg import Input
from random import randint
import time
from pal_web_msgs.msg import WebGoTo


# rosservice call /gaze_manager/enable_neck
# rosservice call /gaze_manager/disable_neck

def message_reciever(txt):
    global Last_time, txet
    txet = txt.args[0].value
    publisher.publish(txet)

    Last_time = time.time() + 60

def speak():
    global Last_time
    number = randint(1,10)
    print(number)
    if number == 1:
        speakingrobot.greetings()

    elif number == 2:
        speakingrobot.encourage()

    elif number == 3:
        speakingrobot.guilt()

    elif number == 4:
        wavingrobot.waving()

    elif number == 5:
        speakingrobot.introduce()

    elif number == 6:
        speakingrobot.tofu()

    elif number == 7:
        speakingrobot.green()   

    elif number == 8:
        speakingrobot.dailyfood()

    elif number == 9:
        speakingrobot.potatoing()
    
    elif number == 10:
        speakingrobot.alsopotatoing()

    Last_time = time.time()

# def noodle():

#     number = randint(1,3)
#     if number == 1:
#         speakingrobot.tofu()
#     elif number == 2:
#         speakingrobot.happy()
#     elif number == 3:
#         speakingrobot.green()

# def homecomfort():
#     number = randint(1,3)
#     if number == 1:
#         speakingrobot.dailyfood()
#     elif number == 2:
#         speakingrobot.green()
#     elif number == 3:
#         speakingrobot.happy()

# def potato():
#     number = randint(1,4)
#     if number == 1: 
#         speakingrobot.green()
#     elif number == 2:
#         speakingrobot.happy()
#     elif number == 3:
#         speakingrobot.potatoing()
#     elif number == 4:
#         speakingrobot.alsopotatoing()
        


def timesup():

    signal = "signal"
    pub2.publish(signal)

def publish_touch_page(page_name):
    #Create the publisher and node then wait for connection
    pub = rospy.Publisher('/web/go_to', WebGoTo, queue_size=1)
    # rospy.init_node('touchpage_publisher', anonymous=True)
    rospy.sleep(1.0)
    #Create the msg we are sending to ARI
    msg = WebGoTo()
    msg.type = WebGoTo.TOUCH_PAGE
    msg.value = page_name

    #Publish the message
    pub.publish(msg)
    rospy.sleep(1.0)


def main():

    global Last_time
    rospy.wait_for_service("/attention_manager/set_policy", timeout = 5)
    set_policy = rospy.ServiceProxy("/attention_manager/set_policy", SetPolicy)
    pubb = rospy.Publisher("/humans/faces/FaceDetection", String, queue_size=10)
    response = set_policy(2, "") # policy 2 empty frame 2 tracks people with eyes3 
    expressions.neutral()
    rospy.Subscriber("/user_input", Input, message_reciever)

    # rospy.wait_for_service("/gaze_manager/enable_neck", timeout = 5)
    # neck_on = rospy.ServiceProxy("/gaze_manager/enable_neck", )
    while not rospy.is_shutdown():

        pubb.publish(f"Face Detected: {hri.faces}")
        print(time.time() - Last_time)
        rospy.sleep(1)
        # global txet 

        # if txet == "Main to Noodle Bar":
        #     noodle()
        # elif txet == "Main to Potato":
        #     potato()
        # elif txet == "Main to Home Comforts":
        #     homecomfort()

        if time.time() - Last_time >= 60:
            
            timesup()
            
            if len(hri.faces) != 0:
            
                speak()
                rospy.sleep(1)

        




# /humans/faces/string/aligned prints a bunch of random numbers in an array? No idea what's going on there.
#                     /cropped does as well      Possibly images might not record that data.
#                     /landmarks seems to give positional data
#                     /roi likewise to landmarks



if __name__ == '__main__':
    try:
        rospy.init_node("FaceDetection")
        publisher = rospy.Publisher("/humans/faces/InteractionLog", String, queue_size=10)
        pub2 = rospy.Publisher("/touchpage_publisher", String, queue_size=1)
        hri = HRIListener()
        global Last_time
        Last_time = time.time()
        publish_touch_page("auroratesting2")
        main()
    except rospy.ROSInterruptException as e:
        print(e)
