#!/usr/bin/env python
import roslib; roslib.load_manifest('olinoboat')
import rospy
from std_msgs.msg import UInt16

compass=None
gps=None
wind_angle=None
leak_detector=None

class WindAngle():

    def __init__(self, offset = 0, node = 0):
       self.__offset = offset
       self.wind_angle = 0

        #initialize node if not running from the think code
        if node == 0:
            rospy.init_node('data_listener', anonymous=False)
    
        #set up subscribers to ("topic", DataType, callback_function)
        rospy.Subscriber("offset", UInt16, self.__set_offset)
        rospy.Subscriber("pwm_duration", UInt16, self.__pwm_to_wind_angle)

    def __set_offset(self, data):
        self.offset = data.data

    def __pwm_to_wind_angle(self, data):
        phigh = data.data
        self.wind_angle = (360*(phigh - self.__offset)/1024.)%360


class GPS():

    def __init__(self, node = 0):
	    self.current_location = [0,0,0]

    	#initialize node if not loading from think code
        if node == 0:
            rospy.init_node('data_listener', anonymous=False)
	
        rospy.Subscriber("GPS_output", UInt16, self.__set_current_position)

    def __set_current_position(self, data):
        self.current_location = data.data


class Compass():

    def __init__(self, node = 0):
        self.angle = 0             
    
        #initialize node if not loading from think code     
        if node == 0:
            rospy.init_node('data_listener', anonymous=False)
    
        rospy.Subscriber("heading", UInt16, self.__set_angle)

    def __set_angle(self, data):
        self.compass_angle = data.data

class LeakDetector():
    def __init__(self, leak_callback, node=0):
        self.leak_detected = 0             

        if node == 0:
            rospy.init_node('data_listener', anonymous=False)

        rospy.Subscriber("leak",UInt16,leak_callback)


def init():
    compass=None
    gps=None
    wind_angle=None
    leak_detector=None

 
if __name__ == '__main__':
   pass