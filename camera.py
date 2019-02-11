#!/usr/bin/env python
import numpy as np
import rospy
import cv2
import sys
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

br=CvBridge()
cap=cv2.VideoCapture(0)
#cap1=cv2.VideoCapture(0)
cap.set(3,120)
cap.set(4,100)
#cap.set(5,15)
def talker():
    pub=rospy.Publisher('video_topic',Image,queue_size=10)
    rospy.init_node('transmiter',anonymous = True)
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        #ret1, frame1 = cap1.read()
        pub.publish(br.cv2_to_imgmsg(frame,"bgr8"))
        #cv2.imshow("frame",frame)
        #cv2.imshow("frame1",frame1)
        cv2.waitKey(1)

if __name__ == '__main__':
    try:
        talker()
        #cap.release()
        #cv2.destroyAllWindows()
    except rospy.ROSInterruptException:
        pass
