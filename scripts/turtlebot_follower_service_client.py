#!/usr/bin/env python
from turtlebot_msgs.srv import SetFollowState
import rospy
def turtle_follower_client(msg):
    rospy.wait_for_service('/turtlebot_follower/change_state')
    try:
        change_state = rospy.ServiceProxy('/turtlebot_follower/change_state', SetFollowState)
        return change_state(msg)
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e
def keyboard_control():
    command=' '
    while command != 'q':
        try:
            command = raw_input('next_command:')
            if command == 'w':
                turtle_follower_client(1)
            elif command == 's':
                turtle_follower_client(0)
            else:
                print "Invalid Command!"
        except EOFError:
            print "error!"
if __name__ == "__main__":
    keyboard_control()


