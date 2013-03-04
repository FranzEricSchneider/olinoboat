#!/usr/bin/env python
import roslib; roslib.load_manifest('olinoboat')
import rospy
from std_msgs.msg import String



def initialize(node_name,topic_to_publish_to,publish_loop):
    pub = rospy.Publisher(topic_to_publish_to, String)
    rospy.init_node(node_name)
    r = rospy.Rate(1)

    while not rospy.is_shutdown():
        str = publish_loop()
        rospy.loginfo("now publishing: "+str)
        pub.publish(String(str))
        r.sleep()

def _test_publish_loop():
    return "hey there worldy world"

if __name__ == '__main__':
    try:
        print("look at me, yeaaaa")
        initialize("talker","chatter",_test_publish_loop)
    except rospy.ROSInterruptException:
        pass
