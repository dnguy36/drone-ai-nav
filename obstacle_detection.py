import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def image_callback(data):
    bridge = CvBridge()
    frame = bridge.imgmsg_to_cv2(data, "bgr8")
    
    # Detect obstacles
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    
    # Show the result
    cv2.imshow("Obstacle Detection", thresh)
    cv2.waitKey(1)

def main():
    rospy.init_node('obstacle_detection_node', anonymous=True)
    rospy.Subscriber("/camera/rgb/image_raw", Image, image_callback)
    
    rospy.spin()

if __name__ == '__main__':
    main()
