from hardware import servos, sensors
import rospy

current_node = rospy.init_node("think_v1",anonymous=True)
sensors.init(current_node)
servos.init(current_node)

rospy.Rate(10)

'''
servos:
	sail - servos.sail.set_position(angle)
	rudder - servos.sail.set_position(angle)

sensors: 
	compass - sensors.compass.angle
	gps - sensors.gps.current_location
	wind_angle - sensors.wind_angle.angle
	leak_detector - sensors.leak_detector.leak_callback = callback_function
					sensors.leak_detector.leak_detected
'''

loop_count = 0
next_tack = 100

while not rospy.is_shutdown():
	if loop_count > next_tack:
		print("tacking")
		servos.rudder.set_position(-1*servos.rudder.current_position)
		servos.sail.set_position(-1*servos.sail.current_position)
	else:	
		servos.sail.set_position(sensors.wind_angle.angle/2)

	rospy.sleep()