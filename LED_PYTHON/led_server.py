import socket
import sys
import os
import time
import serial
ar=serial.Serial('/dev/ttyACM0',9600)
time.sleep(2)
sys.setrecursionlimit(10**6) 
#message from Ardiuno
#armsg=ar.readline()

os.system('clear')
def create_socket():
  try:
      global host
      global port
      global s
      host=""
      port=4444
      s=socket.socket()


  except  socket.error as msg:
      print ("Error While Creating Socket->  " + str(msg))

def bind_socket():
 try:
      global host
      global port
      global s
      print("***Server is Started on port->> " + str(port))
      #s.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
      s.bind((host,port))
      s.listen(5)
 except socket.error as msg:
      print ("Binding Error "+ str(msg) + "\n" + " chill Retrying...")
      bind_socket()  #Recursion So server Started Always

def socket_accept():
       c,a=s.accept()
       print("Connnected To  "+" |IP "+a[0]+" ||port "+str(a[1]))
       send_command(c)
       c.close()

def send_command(c):
         msg ="***[Connected|Ardiuno Controlling Server|LED CONTROLLER] "
         c.send(str.encode(msg))
         time.sleep(1)
         m1="Enter 1 For ON & 0 For OFF 2 For Exit"
         c.send(str.encode(m1))
         while 1:
          inc=c.recv(1024)

          if (inc =='1'):
            ar.write('1')
            on="LED TURNED ON "
            print(on)
            c.send(on)
            time.sleep(1)

          if (inc =='0'):
            ar.write('0')
            off="LED TURNED OFF"
            print(off)
            c.send(off)
            time.sleep(1)
      #   if (inc =='2'):
       #   print("Conncection Close By User")
        #  s.close()
      
def main():
 create_socket()
 bind_socket()
 socket_accept()

main()
