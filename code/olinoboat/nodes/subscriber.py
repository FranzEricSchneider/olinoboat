#!/usr/bin/env python
import roslib; roslib.load_manifest('olinoboat')
import rospy
from std_msgs.msg import String

def _data_callback(data, parser_callback):
	rospy.loginfo("got %s" % data.data)
	parser_callback(data.data)

def initialize(node_name,topic_to_listen_to,parser_callback):
    rospy.init_node(node_name, anonymous=True)
    parse_data = lambda data: _data_callback(data,parser_callback)
    rospy.Subscriber(topic_to_listen_to, String, parse_data)
    rospy.spin()

def _test_callback(parsed_data):
	rospy.loginfo("now calling bacccccck with parsed data: "+parsed_data)


if __name__ == '__main__':
    initialize("listener","chatter",_test_callback)
