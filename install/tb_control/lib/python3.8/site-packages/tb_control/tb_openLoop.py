#!/usr/bin/env python3

import sys
import rclpy
from rclpy.node import Node

#Import message type
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class tb_openLoop(Node):
  
  def __init__(self):
    super().__init__('tb_openLoop')
    self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
    self.publisher = self.create_publisher(String, 'topic', 10)
    timer_period = 1.0 # seconds
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.i = 0
    self.run_flag = 0
    self.scenario = 0
    self.base_vel = 0.05
    self.step_vel = 0.05
    
  def timer_callback(self):
    msg = String()
    #msg.data = 'Hello World: %d' % self.i
    #self.publisher.publish(msg)
    #self.get_logger().info('Publishing: "%s"' % msg.data)
    #self.i += 1
    if self.scenario == 1:
      if(self.i <= 20):
        if(self.run_flag != 1):
          twist = Twist()
          twist.linear.x = 0.1
          twist.linear.y = 0.0
          twist.linear.z = 0.0

          twist.angular.x = 0.0
          twist.angular.y = 0.0
          twist.angular.z = 0.0
    
          self.cmd_vel_pub.publish(twist)
          self.run_flag = 1
      else:
        twist = Twist()
        twist.linear.x = 0.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0

        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0
    
        self.cmd_vel_pub.publish(twist)
        msg.data = 'Target reached!'
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

    elif self.scenario == 2:
      if(self.i <= 7):
        self.base_vel += self.step_vel
        twist = Twist()
        twist.linear.x = self.base_vel
        twist.linear.y = 0.0
        twist.linear.z = 0.0

        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0
    
        self.cmd_vel_pub.publish(twist)
      elif(self.i > 7 and self.i <=14):
        twist = Twist()
        twist.linear.x = self.base_vel
        twist.linear.y = 0.0
        twist.linear.z = 0.0

        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0
        
        self.cmd_vel_pub.publish(twist)
      elif(self.i > 14 and self.i <=21):
        self.base_vel -= self.step_vel
        twist = Twist()
        twist.linear.x = self.base_vel
        twist.linear.y = 0.0
        twist.linear.z = 0.0

        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0
        
        self.cmd_vel_pub.publish(twist)
      else:
        twist = Twist()
        twist.linear.x = 0.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0

        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0
        
        self.cmd_vel_pub.publish(twist)
        
    else:
      print("Invalid Scenario Choice")
    
    self.i += 1

def main():
# print('Hi from tb_control.')

  rclpy.init()
  openLoop = tb_openLoop()

  print("Please choose your scenario:")
  print("1: Constant Velocity")
  print("2: Accel/Deaccel")
  openLoop.scenario = int(input("Selection (as int): "))
  
  rclpy.spin(openLoop)
  
  # Destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  openLoop.destroy_node()
  rclpy.shutdown()


if __name__ == '__main__':
    main()
