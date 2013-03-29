import os, sys, inspect

parent_folder = "/".join(os.path.realpath(os.path.dirname(inspect.getfile(inspect.currentframe()))).split("/")[0:-1])
if parent_folder not in sys.path:
     sys.path.insert(0, parent_folder)

from hardware import sensors
import rospy

name = rospy.get_param('name')
print(name)
current_node = rospy.init_node(name,anonymous=True)
sensors.init(current_node)
sensors.wind_angle.set_callback(on_wind_direction_change)

def on_wind_direction_change(angle):
	rospy.loginfo("Compass sent %i" % (angle))
	



