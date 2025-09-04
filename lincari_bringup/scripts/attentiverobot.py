import rospy 
from attention_manager.srv import SetPolicy

rospy.wait_for_service("/attention_manager/set_policy", timeout = 5)
set_policy = rospy.ServiceProxy("/attention_manager/set_policy", SetPolicy)
response = set_policy(3 , "") # policy 3 empty frame
