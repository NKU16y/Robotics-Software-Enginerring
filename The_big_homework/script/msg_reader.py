#!/usr/bin/python
# -*- encoding: UTF-8 -*-
import rospy
import os
from std_msgs.msg import String
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
import time

soundhandle=SoundClient()

class msg_reader:

    def __init__(self):
        
        rospy.init_node("msg_reader")
        self.msg=" "
        self.isstart=False
        self.isend=False
        self.flag_1=True
        self.flag_2=False
        self.flag_3=False
        self.start_sub=rospy.Subscriber("/dialog",String,self.startCallback)
        self.msg_sub=rospy.Subscriber("/rec_result",String,self.msg_Callback)
        self.end_pub=rospy.Publisher("/finished",String,queue_size=15)
        rospy.Rate(1)
        rospy.spin()
    
    def msg_Callback(self,msg):

        if self.isstart and ~self.isend:
            self.msg=msg.data
            Msg=str(self.msg)
            print(Msg)
            if self.flag_1:
                recoder=open('report.txt','w')
                recoder.write("Name:xxx"+'\n')
                recoder.write("Gender:Man"+'\n')
                recoder.write('Age:20'+'\n')
                recoder.write('Date:'+time.strftime("%Y/%m/%d")+'\n')
                recoder.close()
                soundhandle.say("Here is your medicine , please take it on time.")
                self.flag_1=False
                self.flag_2=True
                time.sleep(10)
            
            if self.flag_2:
                soundhandle.say("Now we start the daily inspection")
                self.flag_2=False
                self.flag_3=True
                time.sleep(5)
                soundhandle.say("Have you taken your tempeture?What is it?")

            if self.flag_3:
                if "36" in Msg or "37" in Msg or "38" in Msg or "39" in Msg or "40" in Msg:
                    recoder=open('report.txt','a')
                    recoder.write('The body tempereture:'+Msg[0:2]+'℃'+'\n')
                    recoder.close()
                    time.sleep(15)
                    soundhandle.say("How about the blood pressure?")

                if "120 and 90" in Msg:
                    time.sleep(15)
                    recoder=open('report.txt','a')
                    recoder.write('The blood pressure:\nSystolic blood pressure:120mmHg\nDiastoic blood pressure:90mmHg\n')
                    recoder.close()
                    soundhandle.say("I have sent the report to the doctor.What else do you need?")

                if "thanks" in Msg:
                    soundhandle.say('Bye. Hope that you will recover soon.')
                    self.isend=True
                    os.rename('report.txt','Report.txt')
                    self.end_pub.publish("finished")
        
                
                    exit()

    def startCallback(self):
        
        self.isstart=True

if __name__ == '__main__':
    msg_reader()   
