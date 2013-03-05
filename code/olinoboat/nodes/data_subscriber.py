#!/usr/bin/env python
import roslib; roslib.load_manifest('beginner_tutorials')
import rospy
from std_msgs.msg import UInt16

offset = 0	#need to add offset pub and subscribe to it
		# in the meantime, use 'rostopic pub -r 1 /offset std_msgs/UInt16 25' for an offset of 25 degrees
 
class datalistener():

    def __init__(self, offset = 0):
        self.offset = offset
        rospy.init_node('data_listener', anonymous=False)
        rospy.Subscriber("offset", UInt16, self.offset_callback)
        rospy.Subscriber("pwm_duration", UInt16, self.pwm_callback)

    def offset_callback(self, data):
        self.offset = data.data

    def pwm_callback(self, data):
        phigh = data.data
        angle = (360*(phigh - self.offset)/1024.)%360
        rospy.loginfo(rospy.get_name() + ": pwm is %s, offset is %s" %(phigh, self.offset))
        rospy.loginfo(rospy.get_name() + ": Encoder reads %s degrees" % angle)
 
 
if __name__ == '__main__':
    listener = datalistener()
    rospy.spin()
