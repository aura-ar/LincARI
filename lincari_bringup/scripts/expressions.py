#!/usr/bin/env python

import rospy
from hri_msgs.msg import Expression


def neutral():
    

    #define the publisher
    pub = rospy.Publisher("/robot_face/expression", Expression , queue_size=10)

    #wait 0.5 seconds because ros is stupid
    rospy.sleep(0.5)

    #define the expression
    msg = Expression()
    msg.expression = "neutral"

    # rospy.loginfo("Here is the msg")
    # rospy.loginfo(msg)
    
    #publish the expression to ari
    pub.publish(msg)
    rospy.loginfo("ari is " + msg.expression)



def excited():

    #define the publisher
    pub = rospy.Publisher("/robot_face/expression", Expression , queue_size=10)

    #wait 0.5 seconds because ros is stupid
    rospy.sleep(0.5)

    #define the expression
    msg = Expression()
    msg.expression = "excited"

    #publish the expression to ari
    pub.publish(msg)
    rospy.loginfo("ari is " + msg.expression)
    # rospy.loginfo("Setting Expression")
    # rospy.loginfo(msg)
    



    
    # while not rospy.is_shutdown():
    #     pub.publish(msg)
    #     print("Subscribers connected:", pub.get_num_connections())
    #     rate.sleep()
    #     rospy.loginfo(msg)


def main():
    #initialise the rosnode. You need it here and not inside the functions if you want to call the function in a different script otherwise the two nodes conflict
    rospy.init_node("expressioning")

    neutral()  

if __name__ == "__main__":
    try:
  
        main()
    except rospy.ROSInterruptException:
        pass

