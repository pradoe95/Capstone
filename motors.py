#!/usr/bin/env python
from __future__ import division
import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
pwm_A1 = GPIO.PWM(2,490)
pwm_B1 = GPIO.PWM(3,490)
pwm_A2 = GPIO.PWM(4,490)
pwm_B2 = GPIO.PWM(17,490)
pwm_A1.start(0)
pwm_B1.start(0)
pwm_A2.start(0)
pwm_B2.start(0)

MQTT_SERVER = "192.168.0.100"
MQTT_PATH = "joystick_topic"

def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_PATH)

def on_message(client,userdata, msg):
    cmd = msg.payload.split("/")

    V1 = int(int(cmd[0])*(60/150))
    V2 = int(int(cmd[1])*(60/150))
    V3 = int(int(cmd[2])*(60/150))
    V4 = int(int(cmd[3])*(60/150))
    #print msg.payload
    print V1, V2, V3, V4

    pwm_A1.ChangeDutyCycle(V1)
    pwm_B1.ChangeDutyCycle(V2)
    pwm_A2.ChangeDutyCycle(V3)
    pwm_B2.ChangeDutyCycle(V4)

client = mqtt.Client()
client.connect(MQTT_SERVER, 1883, 60)

client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
