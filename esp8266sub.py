from umqtt.simple import MQTTClient
from machine import Pin
led=Pin(5, Pin.OUT)
led.value(1)



def msg(a,b):
    data=(str(b,'utf-8'))
    print(data)
    if "LED on" in data:
        led.value(0)
    if "LED off" in data:
        led.value(1)

        

    
    
def client():
    server="test.mosquitto.org"
    c = MQTTClient("umqtt_client", server)
    c.set_callback(msg)
    c.connect()
    c.subscribe("test2")
    c.wait_msg()
    c.check_msg()
    c.disconnect()
while True:    
     client()    

