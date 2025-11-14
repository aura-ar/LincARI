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
    pubb = rospy.Publisher("/FaceDetection", String, queue_size=10)
    response = set_policy(2 , "") # policy 2 empty frame 2 tracks people with eyes3 
    expressions.neutral()
    # rospy.wait_for_service("/gaze_manager/enable_neck", timeout = 5)
    # neck_on = rospy.ServiceProxy("/gaze_manager/enable_neck", )
    while not rospy.is_shutdown():
        pubb.publish(f"Face Detected: {hri.faces}")
        rospy.sleep(1)
        # if len(hri.faces) != 0:
        #     speak()



# /humans/faces/string/aligned prints a bunch of random numbers in an array? No idea what's going on there.
#                     /cropped does as well      Possibly images might not record that data.
#                     /landmarks seems to give positional data
#                     /roi likewise to landmarks



#/humans/persons/ldbtc/face_id  seems to track the ids of every face that appears? But these are different to what can be found in persons/known
#                     /location_confidence is either empty or a 1.0 ?
# /humans/persons/known
# /humans/persons/tracked
# /humans/persons/zkeen/alias
# /humans/persons/zkeen/anonymous
# /humans/persons/zkeen/body_id
# /humans/persons/zkeen/engagement_status
# /humans/persons/zkeen/face_id
# /humans/persons/zkeen/location_confidence
# /humans/persons/zkeen/voice_id
# /hri_face_detect/ready
# /hri_face_identification/ready
# /humans/bodies/bmgez/cropped
# /humans/bodies/bmgez/joint_states
# /humans/bodies/bmgez/position
# /humans/bodies/bmgez/roi
# /humans/bodies/bmgez/skeleton2d
# /humans/bodies/bmgez/velocity
# /humans/bodies/tracked
# /humans/candidate_matches
# /humans/faces/tracked
# /humans/graph
# /humans/persons/anonymous_person_ffgha/alias
# /humans/persons/anonymous_person_ffgha/anonymous
# /humans/persons/anonymous_person_ffgha/body_id
# /humans/persons/anonymous_person_ffgha/engagement_status
# /humans/persons/anonymous_person_ffgha/face_id
# /humans/persons/anonymous_person_ffgha/location_confidence
# /humans/persons/anonymous_person_ffgha/voice_id
# /humans/persons/anonymous_person_hicai/alias
# /humans/persons/anonymous_person_hicai/anonymous
# /humans/persons/anonymous_person_hicai/body_id
# /humans/persons/anonymous_person_hicai/engagement_status
# /humans/persons/anonymous_person_hicai/face_id
# /humans/persons/anonymous_person_hicai/location_confidence
# /humans/persons/anonymous_person_hicai/voice_id
# /humans/persons/hcyvm/alias
# /humans/persons/hcyvm/anonymous
# /humans/persons/hcyvm/body_id
# /humans/persons/hcyvm/engagement_status
# /humans/persons/hcyvm/face_id
# /humans/persons/hcyvm/location_confidence
# /humans/persons/hcyvm/voice_id

if __name__ == '__main__':
    try:
        rospy.init_node("FaceDetection")
        hri = HRIListener()
        main()
    except rospy.ROSInterruptException:
        pass
