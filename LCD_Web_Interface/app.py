from flask import Flask,render_template,request
import serial
app=Flask(__name__)
ar=serial.Serial("/dev/ttyACM0",9600)
@app.route('/',methods=['POST','GET'])
def home():
  if request.method=='POST':
    msg=request.form['msg']
    print 'Sending'
    ar.write(msg.encode())

  return render_template('main.html')
    


if __name__=='__main__':
 app.run(host=" 0.0.0.0",port =444,debug=True)

