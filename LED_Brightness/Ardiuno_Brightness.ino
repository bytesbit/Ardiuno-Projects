int led = 10;           
int br = 0;    
int fa;    
void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  analogWrite(led,br);
}
void loop() {
  
 while(!Serial.available())
 {
  analogWrite(led,br);
  //fa=Serial.read();
  //br= br + fa;
  //if (br == 0 || br == 255) {
   //fa = -fa ; 
   }
   
 
 // delay(30);
}
