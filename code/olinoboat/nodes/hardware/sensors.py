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
        self.angle = 0

        #initialize node if not running from the think code
        if node == 0:
            rospy.init_node('data_listener', anonymous=False)

        #set up subscribers to ("topic", DataType, callback_function)
        rospy.Subscriber("offset", UInt16, self.__set_offset)
        rospy.Subscriber("pwm_duration", UInt16, self.__pwm_to_wind_angle)
        rospy.loginfo("WindAngle initialized")

    def __set_offset(self, data):
        rospy.loginfo("Servo got offset signal: %i" % (data.data))
        self.offset = data.data

    def __pwm_to_wind_angle(self, data):
        rospy.loginfo("Servo got pwm signal: %i" % (data.data))
        phigh = data.data
        self.angle = (360*(phigh - self.__offset)/1024.)%360


class GPS():

    def __init__(self, node = 0):
        self.current_location = [0,0,0]

        #initialize node if not loading from think code
        if node == 0:
            rospy.init_node('data_listener', anonymous=False)

        rospy.Subscriber("GPS_output", UInt16, self.__set_current_position)
        rospy.loginfo("GPS initialized")

    def __set_current_position(self, data):
        rospy.loginfo("GPS sent %i" % (data.data))
        self.current_location = data.data


class Compass():

    def __init__(self, node = 0):
        self.angle = 0             
    
        #initialize node if not loading from think code     
        if node == 0:
            rospy.init_node('data_listener', anonymous=False)
    
        rospy.Subscriber("heading", UInt16, self.__set_angle)
        rospy.loginfo("Compass initialized")

    def __set_angle(self, data):
        rospy.loginfo("Compass sent %i" % (data.data))

        self.compass_angle = data.data

class LeakDetector():
    def __init__(self, node=0, leak_callback=0,):
        self.leak_detected = 0 
        self.leak_callback = leak_callback or self.__default_leak_callback          

        if node == 0:
            rospy.init_node('data_listener', anonymous=False)

        rospy.Subscriber("leak",UInt16,self.__check_for_leak)
        rospy.loginfo("Leak detector initialized")

    def __check_for_leak(self,data):
        if data.data > 1:
            self.leak_detected = 1
            self.leak_callback()
        else:
            rospy.loginfo("clear, no leak")
            self.leak = 0

    def __default_leak_callback(self):
        rospy.loginfo("Leak detected, but no callback registered")


def init(node):
    compass=None
    gps=None
    wind_angle=None
    leak_detector=None
    wind_angle = WindAngle(0,node)
    gps = GPS(node)
    compass = Compass(node)
    leak_detector = LeakDetector(node)



 
if __name__ == '__main__':
   pass