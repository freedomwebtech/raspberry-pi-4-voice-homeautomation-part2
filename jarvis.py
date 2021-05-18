import paho.mqtt.client as mqtt
import time
from jarvis import audio


    
def pub():
    mqttBroker ="test.mosquitto.org"
    client = mqtt.Client("raspberry pi 40")
    client.connect(mqttBroker)
    a=audio()
    client.publish("test2",(bytes(a,'utf-8')))     

pub()    
