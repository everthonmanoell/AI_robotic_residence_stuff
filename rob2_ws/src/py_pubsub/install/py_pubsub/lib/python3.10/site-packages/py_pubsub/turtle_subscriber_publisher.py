import time
from math import atan2, sqrt

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node
from turtlesim.msg import Pose


class TurleClass(Node):
    def __init__(self):
        super().__init__('turtle_node') #nome do tópico
        #Subscriber
        self.subscription_ = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_cb, #definir a função que será chamada depois que receber a msg
            1
        )

        #Publisher
        self.twist_pub = self.create_publisher(
            Twist,
            '/turtle1/cms_vel',
            1
            )
        self.twist_cmd = Twist()

        #To detec the first loop
        self.first_loop = True

        # identifu the maneuver
        self.rotation_is_over = False

        


    def pose_cb(self, msg):
        print(msg)

        # w kw (o* - o) - orientação
        # v = k (x* - x) - distancia
        
        # goal x,y
        x_goal = 2
        y_goal = 3

        #save inicial pose (x)
        if self.first_loop:
            self.x_init = msg.x
            self.y_init = msg.y
                
            # computer desired orientaiton
            self.theta_goal = atan2(y_goal - self.y_init, x_goal - self.x_init)


            # computer desired distance 
            self.distance_goal = sqrt((x_goal - self.x_init)**2 + (y_goal - self.y_init)**2)

            #goal define (x*)
            self.x_goal = self.x_init + 1

            self.first_loop = False

        #update the current position
        self.x = msg.x
        self.y = msg.y
        self.theta = msg.theta
        print(f"x: {self.x} - y: {self.y} - theta: {self.theta}")
        



        # controller proportional
        k = 1 #(k)
        self.twist_cmd.linear.x = k * (self.x_goal - self.x)

        #controller
        if not self.rotation_is_over:
            self.twist_cmd.angular.z = k * (self.theta_goal - self.theta)
            # print(f"theta_goal: {self.theta_goal} - theta: {self.theta} ")

            #detect the end of the rotation
            if abs(self.theta_goal - self.theta) < 0.0001:
                self.rotation_is_over = True
                print("Rotation is over")
        else:
            print("Rotation is over")
            
            #compute the current distance
            distance_current = sqrt((self.x - self.x_init)**2 + (self.y - self.y_init)**2)
            k = 1
            self.twist_cmd.angular.z = 0.0
            self.twist_cmd.linear.x = k * (self.distance_goal - distance_current)

        #publish velocity
        self.twist_pub.publish(self.twist_cmd)

        

    def test_twist(self):
        #start
        self.twist_cmd.linear.x =0.2

        time.sleep(1)

        #stop
        self.twist_cmd.linear.x =0.0
        self.twist_pub.publish(self.twist_cmd)

        

def main(args=None):
    rclpy.init(args=args)

    my_turtle = TurleClass()

    rclpy.spin(my_turtle)

    #my_turtle.test_twist()

    # Destory the node explicitly
    #(iptional - otherwise it will be done automatically
    # whe the garbage )
    my_turtle.destroy_node()
    rclpy.shutdown()


if __name__=='__main__':
    main()