#Source https://www.youtube.com/watch?v=OHEsy9oJEi0

from gpiozero import LED
import paho.mqtt.client as mqtt

led = LED(2)

def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("/test/topic")

def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        message = str(msg.payload)
        if(message=="0" or message == "255"):
            print("Max or Min")
            led.on()
        else:
            led.off()
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)

client.publish("/test/topic","Online")

client.loop_forever()

