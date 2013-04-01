import roslib; roslib.load_manifest('beginner_tutorials')
import rospy
from std_msgs.msg import UInt16
from std_msgs.msg import UInt16MultiArray
import os
import multiprocessing
from threading import Timer
import time
import signal

compass_calibrate_path = '/home/trevor/groovy_workspace/sandbox/olinoboat/code/arduino/Calibrate'


def pwm_callback(data):
    offset = data.data
    print offset
    offset_publisher.publish(offset)

def timeout_wrapper():
    result = os.system('rosrun rosserial_python serial_node.py /dev/ttyACM0')


def kill_serial(proc):
    print "death to serial"
    pid = os.getpid()
    os.kill(pid, signal.SIGINT)

def set_compass():

    os.chdir('%s' %compass_calibrate_path)
    try: os.system('ino init')
    except:  pass
    #os.system('ino build')
    #os.system('ino upload')
    #os.system('rosrun rosserial_python serial_node.py /dev/ttyACM0')


    print 'init timer'
    proc = multiprocessing.Process(target=timeout_wrapper)
    t = Timer(6, kill_serial, args=[proc])
    t.start()
    proc.start()
    rospy.sleep(6)
    proc.terminate()
    print 'terminated'
    proc.is_alive()
    print 'well is it?'




def xmin_callback(data):
    xmin_publisher.publish(data.data)

if __name__ == "__main__":
    rospy.init_node('encoder_offset_setter')

    offset_publisher = rospy.Publisher("pwm_offset", UInt16, latch = True)
    xmin_publisher = rospy.Publisher("xmin_latch", UInt16, latch = True)
    xmax_publisher = rospy.Publisher("xmax_latch", UInt16, latch = True)
    ymin_publisher = rospy.Publisher("ymin_latch", UInt16, latch = True)
    ymax_publisher = rospy.Publisher("ymax_latch", UInt16, latch = True)
    zmin_publisher = rospy.Publisher("zmin_latch", UInt16, latch = True)
    zmax_publisher = rospy.Publisher("zmax_latch", UInt16, latch = True)
    rospy.Subscriber("pwm_duration", UInt16, pwm_callback)
    rospy.Subscriber("xmin", UInt16, xmin_callback)
    set_compass()
    

