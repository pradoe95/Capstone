#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import rospy
import sys
from std_msgs.msg import Bool

GPIO.setmode(GPIO.BOARD)
PIN_TRIGGER = 7
PIN_ECHO = 11
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)
GPIO.output(PIN_TRIGGER, GPIO.LOW)
time.sleep(0.01)

def talker():
    pub=rospy.Publisher('distance_topic',Bool,queue_size=10)
    rospy.init_node('ultrasound',anonymous = True)
    while not rospy.is_shutdown():
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECHO)==0:
                pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO)==1:
                pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time

        distance = round(pulse_duration * 17150, 2)

        if distance < 20:
                pub.publish(1)
        else:
                pub.publish(0)

        time.sleep(.3)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        GPIO.cleanup()
        pass
