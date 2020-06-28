int pin=10;
int inc;
void setup() {
  Serial.begin(9600);
  pinMode(pin,OUTPUT);
  digitalWrite(pin,LOW);
  //Serial.println("Hey Are You Python ! I am Ardiuno Uno");
  
}

void loop() {
  if(Serial.available()>0)
  {
    inc=Serial.read();
    if(inc=='1'){
      digitalWrite(pin,HIGH);
      }  
    if(inc=='0'){
      digitalWrite(pin,LOW);
      }
  }

}
