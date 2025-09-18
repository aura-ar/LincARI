#!/usr/bin/env python
import rospy
from pal_web_msgs.msg import WebGoTo
from pal_interaction_msgs.msg import Input
import wavingrobot




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
def callback():
    rospy.loginfo("Button Pressed")
    wavingrobot.waving()

#Function for listening to the button press and executing previous function
def listener():
    
    rospy.Subscriber("/user_input", Input, callback)
    print("Listening")
    #rospy.spin() because it needs to keep running to detect button presses in the future
    rospy.spin()
    
#roslaunch rosbridge_server rosbridge_websocket.launch

if __name__ == '__main__':
    try:
        publish_touch_page("auroratesting2")
        print("Published")
        listener()

    except rospy.ROSInterruptException:
        pass
