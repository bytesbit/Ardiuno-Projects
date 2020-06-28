import time
import serial
from Adafruit_IO import Client, Feed, RequestError
ADAFRUIT_IO_KEY = 'aio_Gide65PCPSj0B1GWVLnZJ2l4Gdr5'
ar=serial.Serial("/dev/ttyACM0",9600)

ADAFRUIT_IO_USERNAME = 'ARUNku7042'
 
a_c = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)



#digital = a_c.feeds('LED  BUTTON')
try: # if we have a 'digital' feed
    digital = a_c.feeds('led-button')
except RequestError: # create a digital feed
    feed = Feed(name="led-button")
    digital = a_c.create_feed(feed)
 
while True:
    data = a_c.receive(digital.key)
    ds= data.value
    
    if str(data.value) == "on":
    
        ar.write('1'.encode())
        print('received <- ON\n')
    elif str(data.value) ==  "off":
        ar.write('0'.encode())
        print('received <- OFF\n')

    # timeout so we dont flood adafruit-io with requests
    time.sleep(0.5)


ar.close()
