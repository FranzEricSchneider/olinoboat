/*
 * rosserial PWM reader
 * rosserial Servo Control
 *
 * This sketch combines olinoboat's ROS publishers and subscribers
 * 
 */

#include <Arduino.h>
#include <Servo.h>
#include <ros.h>
#include <std_msgs/UInt16.h>

ros::NodeHandle  nh;

// Setting up the encoder PWM signal
    // The message type for our encoder publisher
    std_msgs:: UInt16 pwm_msg;
    
    // Setting up Arduino subscribers
    ros::Publisher pub_pwm("pwm_duration", &pwm_msg);
    
    int encoder_pin = 8;                  //pin 8 is encoder input
    unsigned long duration;
  
// Setting up the servo control
    Servo servo1;
    Servo servo2;
    
    // Callback response for servo1
    void servo1_cb( const std_msgs::UInt16& cmd_msg){
      servo1.write(cmd_msg.data); //set servo angle, should be from 0-180  
      digitalWrite(13, HIGH-digitalRead(13));  //toggle led  
    }
  
    // Callback response for servo2  
    void servo2_cb( const std_msgs::UInt16& cmd_msg){
      servo2.write(cmd_msg.data); //set servo angle, should be from 0-180  
      digitalWrite(13, HIGH-digitalRead(13));  //toggle led  
    }
    
    //Setting up Arduino subscribers
    ros::Subscriber<std_msgs::UInt16> sub1("servo1", servo1_cb);
    ros::Subscriber<std_msgs::UInt16> sub2("servo2", servo2_cb);


void setup(){
  // Initializing the Arduino as a fake node
  nh.initNode();
  
  // Setting up the encoder PWM signal
      pinMode(encoder_pin, INPUT);		
      nh.advertise(pub_pwm);
      
  // Setting up the servo control
      nh.subscribe(sub1);
      nh.subscribe(sub2);
      servo1.attach(9); //attach servo1 to pin 9
      servo2.attach(10); //attach servo2 to pin 10
}

void loop(){
  nh.spinOnce();

  // Collecting the encoder PWM signal
      pwm_msg.data = pulseIn(encoder_pin, HIGH);
      pub_pwm.publish(&pwm_msg);

  delay(1);
}


