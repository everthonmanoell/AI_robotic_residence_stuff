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
		ranges = msg.ranges
		min_range = float('inf')
		#taking the minimum range
		for r in ranges:
			if r < min_range:
				min_range = r
				
		self.get_logger().info("Min range: " + str(min_range))
		#calculate the angle of the minimum range
		min_index = ranges.index(min_range)
		angle = msg.angle_min + min_index * msg.angle_increment
		self.get_logger().info("Angle: " + str(angle))
		
		
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
		