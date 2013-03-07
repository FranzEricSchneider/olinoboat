#!/usr/bin/env python
import roslib; roslib.load_manifest('olinoboat')
import rospy
from std_msgs.msg import String
pub = 0


def initialize(topic_to_publish_to):
    global pub 
    pub = rospy.Publisher(topic_to_publish_to, String)

def publish(message):
    global pub
    if pub: 
        rospy.loginfo(message)
        pub.publish(message)
    else:
        print "you must initialize before publishing"

if __name__ == '__main__':
    try:
        print("look at me, yeaaaa")
        initialize("talker","chatter")
    except rospy.ROSInterruptException:
        pass
