#!/usr/bin/env python
import rospy
from pal_web_msgs.msg import WebGoTo



# rospy.wait_for_service("/web/go_to")
# rospy.loginfo("Service Reached")
# rospy.init_node("Publisher")

# pub = rospy.Publisher("/web/go_to", WebGoTo, queue_size=10)
# rospy.sleep(1)
# rospy.Rate(1)
    
    

def publish_touch_page(page_name):
    pub = rospy.Publisher('/web/go_to', WebGoTo, queue_size=1)
    rospy.init_node('touchpage_publisher_once')
    # Give ROS publishers/subscribers time to connect
    rospy.sleep(1.0)
    msg = WebGoTo()
    msg.type = WebGoTo.TOUCH_PAGE
    msg.value = page_name
    rospy.loginfo("Publishing TOUCH_PAGE for page: %s", page_name)
    pub.publish(msg)
    # Optionally wait a bit and then shutdown
    rospy.sleep(1.0)

if __name__ == '__main__':
    try:
        publish_touch_page("auroratest")
    except rospy.ROSInterruptException:
        pass
