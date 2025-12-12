import math
import time

import rclpy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from tf_transformations import euler_from_quaternion, quaternion_from_euler
from turtlesim.msg import Pose


class LazerClass(Node):

	def __init__(self):
		super().__init__('tiago_node_laser')
		
		# Subscriber
		self.create_subscription(LaserScan, '/scan_raw', self.laser_cb, 1)
		

		
		
	def laser_cb(self, msg):
		self.get_logger().info(str(msg))
		min_range = min(msg.ranges)
				
		self.get_logger().info("Min range: " + str(min_range))
		#calculate the angle of the minimum range
		min_index = msg.ranges.index(min_range)
		
        # this work because the ranges are in order of angle from min to max
		angle = msg.angle_min + min_index * msg.angle_increment
		
        #transform in cartesian coordinates
		x = min_range * math.cos(angle)
		y = min_range * math.sin(angle)
		
        #transforme chartesian to polar
		radius = math.sqrt(x**2 + y**2)
		theta = math.atan2(y, x)
		
		
	def test_twist(self):
		# Start
		self.twist_cmd.linear.x = 0.2	
		self.twist_pub.publish(self.twist_cmd)
		
		time.sleep(1)
		
		# Stop
		self.twist_cmd.linear.x = 0.0	
		self.twist_pub.publish(self.twist_cmd)
		
def main(args=None):
    rclpy.init(args=args)

    tiago = LazerClass()

    rclpy.spin(tiago)
    #tiago.test_twist()


    tiago.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
		