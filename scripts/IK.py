#!/usr/bin/env python
import math
import rospy
from std_msgs.msg import Float64

class IK():
    def __init__(self,x,y):
        rospy.init_node("IK")
        self.pub_IK_theta1 = rospy.Publisher('/shoulder_controller/command',Float64,queue_size=15)
        self.pub_IK_theta2 = rospy.Publisher('/shoulder_controller/command',Float64,queue_size=15)
        self.l1=0.145
        self.l2=0.15
        self.theta1=0.0
        self.theta2=0.0
    def cal_theta(self):
        theta1=Float64
        theta2=Float64
        theta2=math.acos((x*x+y*y-self.l1*self.l1-self.l2*self.l2)/(2*self.l1*self.l2))
        A=self.l1+self.l2*math.cos(theta2)
        B=self.l2*math.sin(theta2)
        theta1=math.acos((x)/math.sqrt(A*A+B*B))-math.atan2(B,A)
        self.theta1=theta1
        self.theta2=theta2
    def pub_theta(self):   
        print (self.theta1)
        print ('\n')
        print (self.theta2)
        print ('\n')
        self.pub_IK_theta1.publish(self.theta1)
        self.pub_IK_theta2.publish(self.theta2)

if __name__ == "__main__":
    x=input('please input x :')
    y=input('please input y :')
    ik=IK(x,y)
    ik.cal_theta()
while True:
    ik.pub_theta()
    
    
