import mouse, sys
import time 
import serial

mouse.FAILSAFE=False
ArduinoSerial=serial.Serial('/dev/ttyACM0',9600)  #
time.sleep(1)                             #delay of 1 second

while 1:
   data=str(ArduinoSerial.readline().decode('ascii'))
   (x,y,z)=data.split(":")  # read the x and y axis data
   (x,y)=(int(x),int(y))   # convert to int
   mouse.move(x,y)         # move the cursor to desired coordinates
   if '1' in z:                       
      mouse.click(button="left")     #clicks mouse button
   elif '2' in z:
      mouse.click(button="right")
   elif '3' in z:
      mouse.wheel(delta=-1)       # Scroll down
   elif '4' in z:
      mouse.wheel(delta=1)       # Scroll up
    
     

