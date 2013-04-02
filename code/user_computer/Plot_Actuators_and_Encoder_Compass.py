from pylab import *


def init_polar_subgraph(plot_name, plot_num):
	plot_name = subplot(2, 2, plot_num, projection='polar')
	plot_name.set_theta_zero_location('N')
	plot_name.set_theta_direction(-1)

	yt = yticks()[0]
	yticks(yt, ['' for q in range(len(yt))])
	return void


def draw_polar_design(d_angle, rad, design): # d_angle is in degrees, rad is for scaling the outer diameter of boat
	rad = float(rad)
	angle = d_angle * (pi/180)

	if design == 'Boat':
		t = [0, angle, angle-(pi/2), angle-(9*pi/10), angle-(11*pi/10), angle-(3*pi/2), angle]
		y = [0, rad, 0.25*rad, 0.75*rad, 0.75*rad, 0.25*rad, rad]
	elif design == 'Wind':
		t = [0, angle, angle-(pi/30), angle, angle+(pi/30), angle, 0]
		y = [0, 0.9*rad, 0.7*rad, 0.95*rad, 0.7*rad, 0.9*rad, 0]
	elif design == 'Rudder':
		t = [angle, angle-(pi/15), angle, angle+(pi/15), angle]
		y = [0, 0.25*rad, 0.65*rad, 0.25*rad, 0]
	elif design == 'Sail':
		t = [pi+angle, angle+(pi/2), angle, angle-(pi/2), pi+angle, 0, angle]
		y = [0.5*rad, 0.05*rad, 1*rad, 0.05*rad, 0.5*rad, 0, 1*rad]
	else:
		t = 0
		y = 0

	polar(t, y, linewidth = 2)
	polar(0, rad)
	return void


rc('grid', color='#aaaaaa', linewidth = 1)
rc('ytick', labelsize = 2)
title_size = 13
fig = figure(figsize = [10,10])


#TODO - CHANGE THESE NAMES TO OUR OFFICIAL NAMES
boat_d_angle = 20;

init_polar_subgraph('plt1', 1)
draw_polar_design(boat_d_angle, 1, 'Boat')
title('Compass Direction', fontsize=title_size)


#TODO - CHANGE THESE NAMES TO OUR OFFICIAL NAMES
wind_d_angle = 315;

init_polar_subgraph('plt2', 2)
draw_polar_design(wind_d_angle, 1, 'Wind')
title('Wind Direction', fontsize=title_size)


#TODO - CHANGE THESE NAMES TO OUR OFFICIAL NAMES
rudder_d_angle = 150;

init_polar_subgraph('plt3', 3)
draw_polar_design(rudder_d_angle, 1, 'Rudder')
title('Rudder Position', fontsize=title_size)

#TODO - CHANGE THESE NAMES TO OUR OFFICIAL NAMES
sail_d_angle = 150;

init_polar_subgraph('plt4', 4)
draw_polar_design(sail_d_angle, 1, 'Sail')
title('Sail Direction', fontsize=title_size)


show()
