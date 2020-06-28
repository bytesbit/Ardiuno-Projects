int inc;
int pin=8;                
void setup() 
{
  Serial.begin(9600);         
  pinMode(pin, OUTPUT);       
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
