#!/usr/bin/env python
import rospy
from pal_web_msgs.msg import WebGoTo
from pal_interaction_msgs.msg import Input
from std_msgs.msg import String
import wavingrobot, speakingrobot






#Define the function for publishing the webpage so it only happens once    
def publish_touch_page(page_name):
    #Create the publisher and node then wait for connection
    pub = rospy.Publisher('/web/go_to', WebGoTo, queue_size=1)
    rospy.init_node('touchpage_publisher', anonymous=True)
    rospy.sleep(1.0)
    #Create the msg we are sending to ARI
    msg = WebGoTo()
    msg.type = WebGoTo.TOUCH_PAGE
    msg.value = page_name

    #Publish the message
    pub.publish(msg)
    rospy.sleep(1.0)
    #rospy.wait_for_service("/user_input")

#Function to happen when the button is detected as pressed
def callback(txt):
    global count
    count = 0
    rospy.loginfo("Button Pressed")
    # speakingrobot.greetings()

#Need to add a listener and publisher that detects when the button is pressed to add to a count
#This will mean we know how many times people have interacted with the robot's touchscreen?
#I'm not sure how much we need this since it will be impossible to tell if people are clicking more than once.
#But I can bring it up in the next meeting perhaps


def timesup():
    pub2 = rospy.Publisher("/touchpage_publisher", String, queue_size=1)
    rospy.sleep(0.5)
    signal = "signal"
    pub2.publish(signal)


#Function for listening to the button press and executing previous function
def listener():
    global count
    rospy.Subscriber("/user_input", Input, callback)
    while not rospy.is_shutdown():
        if count < 10:
            count += 1
            print(count)
            print(len(hri.faces))
            rospy.sleep(1)
            
        else:
            timesup()
            count = 0 
        


    
#roslaunch rosbridge_server rosbridge_websocket.launch

if __name__ == '__main__':
    try:
        global count
        count = 0
        publish_touch_page("auroratesting2")
        print("Published")
        listener()
        

    except rospy.ROSInterruptException:
        pass
