import rospy
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import OccupancyGrid

def laser_callback(data):
    pass

def main():
    rospy.init_node('slam_node', anonymous=True)
    rospy.Subscriber("/scan", LaserScan, laser_callback)
    slam_pub = rospy.Publisher('/map', OccupancyGrid, queue_size=10)
    
    rospy.spin()

if __name__ == '__main__':
    main()
