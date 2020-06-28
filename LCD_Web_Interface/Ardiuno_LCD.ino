#include <LiquidCrystal.h> 
int Contrast=70,l,op;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
String str;
void setup() 
{
 
 
 analogWrite(6,Contrast);
 Serial.begin(9600); 
    
 lcd.begin(16,2);
}

void loop() 
{
while(Serial.available())
{

 str=Serial.readString();
 l=str.length();
 lcd_string(); 
   
}

}


//STRING DISPLAY

void lcd_string() {
  if (l<=16)
  {
   lcd.clear();
   lcd.setCursor(0,0);
   lcd.print(str);
  }
  else  {
    if(l>32)
    {
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("ERROR:RANGE 16X2");
      
      }
      else {
   lcd.setCursor(0,0);
   for(int i=0;i<=16;i++)
    {
     lcd.print(str[i]);
     }
    lcd.setCursor(0,1);
    
    for (int j=16;j<l;j++)
    {
      
      lcd.print(str[j]);
      }
  }
  
}
}
