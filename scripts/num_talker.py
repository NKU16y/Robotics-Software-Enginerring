#!/usr/bin/env python

import rospy
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
from std_msgs.msg import Int8
soundhandle = SoundClient()
Str=" "
def callback(data):
    if data.data == 1:
        Str = "I see "+ str(data.data)+ " person"
    else:
        Str = "I see "+ str(data.data)+ " people"
    soundhandle.say(Str)

    rospy.loginfo(rospy.get_caller_id() + "I heard %s",Str )
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("say", Int8 , callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
