import rospy 
from attention_manager_msgs.srv import SetPolicy
from pal_web_msgs.msg import WebGoTo

# rosservice call /gaze_manager/enable_neck
# rosservice call /gaze_manager/disable_neck

rospy.wait_for_service("/attention_manager/set_policy", timeout = 5)
set_policy = rospy.ServiceProxy("/attention_manager/set_policy", SetPolicy)
response = set_policy(2 , "") # policy 2 empty frame 2 tracks people with eyes3 
# rospy.wait_for_service("/gaze_manager/enable_neck", timeout = 5)
# neck_on = rospy.ServiceProxy("/gaze_manager/enable_neck", )