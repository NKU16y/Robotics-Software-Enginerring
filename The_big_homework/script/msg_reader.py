#!/usr/bin/python

import rospy
from std_msgs.msg import String
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
import time

soundhandle=SoundClient()

class msg_reader:

    def __init__(self):
        rospy.init_node("msg_reader")
        self.msg=" "
        self.isstart=True
        self.isend=False
        self.flag_1=True
        self.flag_2=False
        self.flag_3=False
        self.msg_sub=rospy.Subscriber("/rec_result",String,self.msg_Callback)
        self.end_pub=rospy.Publisher("/finished",String,queue_size=15)
        rospy.Rate(1)
        rospy.spin()
    
    def msg_Callback(self,msg):

        if self.isstart and ~self.isend:
            recoder=open('report.txt','w')
            self.msg=msg
            Msg=str(self.msg)
            print(Msg)
            if self.flag_1:
                soundhandle.say("Here is your medicine , please take it on time.")
                self.flag_1=False
                self.flag_2=True
                time.sleep(15)
            
            if self.flag_2:
                soundhandle.say("Now we start the daily inspection")
                self.flag_2=False
                self.flag_3=True
                time.sleep(15)

            if self.flag_3:
                soundhandle.say("Have you taken your tempeture?What is it?")

                if "thirty-six" in Msg or "thirty-seven" in Msg or "thirty-eight" in Msg or "thirty-nine" in Msg or "forty" in Msg:
                    recoder.write('The body tempereture:'+Msg+'\n')
                time.sleep(15)
                soundhandle.say("How about the blood pressure?")

                if "one hundred and twenty and ninty" in Msg:
                    recoder.write('The blood pressure:\nSystolic blood pressure:120\nDiastoic blood pressure:90\n')
                time.sleep(15)
                soundhandle.say("I have sent the report to the doctor.What else do you need?")
                self.flag_3=False

            if "no thank you very much" in Msg:
                soundhandle.say('Bye')
                self.isend=True
                self.end_pub.publish("finished")
                recoder.close()

    def startCallback(self):
        self.isstart=True

if __name__ == '__main__':
    msg_reader()   