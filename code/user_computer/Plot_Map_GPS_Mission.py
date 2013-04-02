from pylab import *
try:
    from PIL import Image
except ImportError:
    raise SystemExit("PIL must be installed to run this example")

# Use the animation library (inside matplotlib)
# Google matplotlib animation example
# Perhaps nest subplots or create a large subplot
# Close to GUI
# Use tkinter, gtk, Qt?

def plot_boat(pos, d_angle, boat_length): # pos is position in lat-lon, d_angle is the angle of the boat, and boat_length is in meters
	angle = -((d_angle * (pi/180)) - pi/2) #TODO - Make sure we're actually indexing clockwise from 0 North
	boat_r = boat_length/2

	posx = pos[0]
	posy = pos[1]

	x = [posx + cos(angle)*boat_r, posx + cos(angle+(pi/2))*boat_r*0.3, posx + cos(angle+(95*pi)/100)*boat_r, posx + cos(angle+(105*pi)/100)*boat_r, posx+ cos(angle+(3*pi/2))*boat_r*0.3, posx + cos(angle)*boat_r]
	y = [posy - sin(angle)*boat_r, posy - sin(angle+(pi/2))*boat_r*0.3, posy - sin(angle+(95*pi)/100)*boat_r, posy - sin(angle+(105*pi)/100)*boat_r, posy - sin(angle+(3*pi/2))*boat_r*0.3, posy - sin(angle)*boat_r]
	plot(x, y, linewidth = 2)
	return void

datafile = 'test_pic.jpg'
map_picture = Image.open(datafile)
dpi = rcParams['figure.dpi']
figsize = map_picture.size[0]/dpi, map_picture.size[1]/dpi

figure(figsize=figsize)
ax = axes([0,0,1,1], frameon=False)
ax.set_axis_off()
im = imshow(map_picture)

# plot([10, 50], [50, 100])
plot_boat([1000, 300], 315, 50)

show()