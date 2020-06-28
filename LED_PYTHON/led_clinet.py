import socket
import os
import subprocess
import sys

s=socket.socket()
host='192.168.43.28'
port=4444
s.connect((host,port))

m1=s.recv(1024)
print(m1) 
m2=s.recv(1024)
print(m2)
while 1:
  inc=raw_input('>')
  s.send(inc)
  an=s.recv(1024)
 # if (inc =='1' or inc =='0'):
  print(an)
  #if (inc =='2'):
   # print("Connection Closed")
    #s.close()
    #sys.exit()
