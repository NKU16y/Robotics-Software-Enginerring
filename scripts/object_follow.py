#! /usr/bin/env python
# -*- encoding: UTF-8 -*-
import cv2
import dlib
import time
import rospy
from opencv_apps.msg import RotatedRectStamped
from std_msgs.msg import String
from geometry_msgs.msg import Twist


class object_follow():
    def __init__(self):
        rospy.init_node("object_follow")
        self.pub_vel = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=15)
        self.sub_size = rospy.Subscriber("/camshift/track_box", RotatedRectStamped, self.size_callback)
        self.x = self.y = 0
        self.cam_width = 640
        self.cam_height = 480
        self.total_time = 0
        self.dir = "none"
        self.left = (self.cam_width / 2) - (self.cam_width / 10)
        self.right = (self.cam_width / 2) + (self.cam_width / 10)
        self.top = (self.cam_height / 2) - (self.cam_height / 5)
        self.bottom = (self.cam_height / 2) + (self.cam_height / 5)
        self.size_old = 0
        self.keyboard_control()

    def size_callback(self, msg):
        Twi = Twist()
        x = msg.rect.center.x
        y = msg.rect.center.y
        if x < self.left:
            Twi.angular.z = (self.cam_width / 2 - x) * .005
        elif x > self.right:
            Twi.angular.z = -(x - self.cam_width / 2) * .005
        if y < self.top:
            Twi.linear.x = (self.cam_height / 2 - y) * .0005
        elif y > self.bottom:
            Twi.linear.x = -(y - self.cam_height / 2) * .0005
        self.total_time += 1
        if self.total_time == 3:
            self.total_time = 0
            self.pub_vel.publish(Twi)


if __name__ == "__main__":
    object_follow()
