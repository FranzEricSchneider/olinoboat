#include <Wire.h>
#include <LSM303.h>
#include <ros.h>
#include <std_msgs/UInt16.h>
#include "std_msgs/MultiArrayLayout.h"
#include "std_msgs/MultiArrayDimension.h"
#include "std_msgs/UInt16MultiArray.h"



LSM303 compass;
LSM303::vector running_min = {2047, 2047, 2047}, running_max = {-2048, -2048, -2048};


ros::NodeHandle nh;
std_msgs:: UInt16 xmin;
std_msgs:: UInt16MultiArray maxmin_array;
ros::Publisher pub_xmin("xmin", &xmin);
ros::Publisher pub_array("compass_calibration", &maxmin_array);

void setup() {
  //nh.initNode();
  Serial.begin(57600);
  Wire.begin();
  compass.init();
  compass.enableDefault();
  
  //maxmin_array.layout.dim = (std_msgs::MultiArrayDimension *)
  //maxmin_array.layout.dim_length = 1;
  maxmin_array.layout.dim[0].size = 6;
  maxmin_array.layout.dim[0].stride = 1;
  maxmin_array.layout.data_offset = 0;
  maxmin_array.layout.dim[0].label = "xmin, xmax, ymin, ymax, zmin, zmax";
  maxmin_array.data_length = 6;

  //maxmin_array.data.resize(6);
  nh.advertise(pub_xmin);
  nh.advertise(pub_array);
}

void loop() {  
  compass.read();

  maxmin_array.data[1] = min(running_min.x, compass.m.x);
  maxmin_array.data[2] = min(running_min.y, compass.m.y);
  maxmin_array.data[3] = min(running_min.z, compass.m.z);

  maxmin_array.data[4] = max(running_max.x, compass.m.x);
  maxmin_array.data[5] = max(running_max.y, compass.m.y);
  maxmin_array.data[6] = max(running_max.z, compass.m.z);  

  nh.spinOnce();
  
  delay(50);
}

