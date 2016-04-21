#Source: https://www.youtube.com/watch?v=PgsH43Tpqjc

import serial, time, mosquitto
import paho.mqtt.publish as publish
ser = serial.Serial('/dev/ttyACM0', 9600)
print("go now")

publish.single("/test/topic","Lets Go", hostname="localhost")

while 1 :
    recivedString = ser.readline()
    myNumberAsString = ""
    myString = str(recivedString)
    for i in range(len(myString)):
        theChar = myString[i]
        if(theChar == '0' or theChar == '1' or theChar == '2' or theChar == '3' or theChar == '4' or theChar == '5' or theChar == '6' or theChar == '7' or theChar == '8' or theChar == '9'):
            myNumberAsString = myNumberAsString + theChar
    print(myNumberAsString)
    publish.single("/test/topic",myNumberAsString, hostname="localhost")
    time.sleep(0.5)
