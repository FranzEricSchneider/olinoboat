#!/usr/bin/env python
import roslib; roslib.load_manifest('olinoboat')
import rospy
from std_msgs.msg import UInt16
import random

def random_servo_driver():
    pub1 = rospy.Publisher('servo1', UInt16)
    pub2 = rospy.Publisher('servo2', UInt16)
    rospy.init_node('random_servo_driver')
    while not rospy.is_shutdown():
        angle = random.randint(0,179)
        pub1.publish(angle)
        pub2.publish(angle)
        print angle
        rospy.sleep(2.0)

if __name__ == '__main__':
    try:
        random_servo_driver()
    except rospy.ROSInterruptException:
        pass
