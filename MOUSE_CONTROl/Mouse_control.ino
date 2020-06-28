int datareceived[5] {0,0,0,0};          // To store byte from phone
int in_byte = 0;
int array_index = 0;

void setup() {
Serial.begin (9600); // starts the serial monitor
}

 int height=0,width=0;
 int lcount=0,rcount=0;
void loop() {
  int clicks=0;
  int sensitivity=20;       // you can adjust the sensitivity
  int xpos=0,ypos=0;
if (Serial.available() > 0) {  //recieve byte from phone
  in_byte= Serial.read(); //store in byte into a variable
  if (in_byte == (255)) { // if the variable is 0 stet the array inxed to 0.
    array_index = 0;
  }
  datareceived[array_index] = in_byte;  //store number into array
  array_index = array_index +1;
  
if(datareceived[1]>=110)
xpos=map(datareceived[1],110,172,0,sensitivity);       // When moved right
if(datareceived[1]<=70)
xpos=map(datareceived[1],60,1,0,-sensitivity);        // When moved left
if(datareceived[2]>=110)
ypos=map(datareceived[2],110,255,0,sensitivity);     // When moved down
if(datareceived[2]<=60)
ypos=map(datareceived[2],70,1,0,-sensitivity);       // When moved up


if(datareceived[3]==1)      // TO recognise a single button press
{
  lcount+=1;
  if(lcount>3)
  {
    clicks=1;
    lcount=0;
  }
}
else if(datareceived[3]==2)
{
  rcount+=1;
  if(rcount>3)
  {
    clicks=2;
    rcount=0;
  }
}       // to recognise the scroll


if(xpos!=0 or ypos!=0 or clicks!=0)       // when either of the joystick is moved or the button is pressed
{
height=height+ypos;
width=width+xpos;
if(height>=799)
height=799;
if(height<=0)
height=0;
if(width>=1279)
width=1279;
if(width<=0)
width=0;
Serial.print(width);
Serial.print(":");
Serial.print(height);
Serial.print(":");
Serial.println(clicks);
clicks=0;
}
}
}
