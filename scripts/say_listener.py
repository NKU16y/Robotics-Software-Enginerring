#!/usr/bin/env python
import rospy
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
from std_msgs.msg import String
soundhandle = SoundClient()
def callback(data):
    soundhandle.say(data.data)
    
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("say", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()

