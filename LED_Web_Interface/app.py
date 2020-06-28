from flask import Flask,render_template,request
import serial
app = Flask(__name__)

ar=serial.Serial("/dev/ttyACM0",9600)
@app.route('/',methods=['POST','GET'])
def home():
    if request.method=='POST':
     if request.form['submit']=='Turn On':
          print 'TURN ON'
          ar.write('1')
     elif request.form['submit']=='Turn Off':
           print 'TURN OFF'
           ar.write('0')
    return render_template('main.html')
#@app.route('/turnon',methods=['GET'])
#def ledon():
#     ar.write('1')
#@app.route('/turnoff',methods=['GET'])
#def ledoff():
#     ar.write('0')


if __name__=='__main__':
 app.run(host=" 0.0.0.0",port =444,debug=True)
