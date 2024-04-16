# Import Dependencies
import rospy 
from geometry_msgs.msg import Twist 
import time 

def move_turtle_square(): 
    rospy.init_node('turtlesim_square_node', anonymous=True)
    
    # Init publisher
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) 
    rospy.loginfo("Turtles are great at drawing squares!")

    ########## YOUR CODE GOES HERE ##########
    # Set the linear and angular velocities
    linear_velocity = 2.0  # meters per second
    angular_velocity = 1.57  # radians per second (90 degrees)

    # Draw a square
    while(True):
        # Move forward
        twist = Twist()
        twist.linear.x = linear_velocity
        twist.angular.z = 0
        velocity_publisher.publish(twist)
        time.sleep(2)  # Move for 2 seconds

        # Rotate 90 degrees
        twist = Twist()
        twist.linear.x = 0
        twist.angular.z = angular_velocity
        velocity_publisher.publish(twist)
        time.sleep(1)  # Rotate for 1 second

    # Stop the turtle
    twist = Twist()
    twist.linear.x = 0
    twist.angular.z = 0
    velocity_publisher.publish(twist)
    ###########################################

if __name__ == '__main__': 

    try: 
        move_turtle_square() 
    except rospy.ROSInterruptException: 
        pass
