/*
  Contorl Arduino LED using voice in an android app
*/
String Incoming_value;
void setup() {

  Serial.begin(9600);
  pinMode(8, OUTPUT);

}

void loop() {
  if (Serial.available() > 0)
  {
    Incoming_value = Serial.readString();
    Serial.print(Incoming_value);
    Serial.print("\n");
    if (Incoming_value == "turn on")
      digitalWrite(8, HIGH);
    else if (Incoming_value == "turn off")
      digitalWrite(8, LOW);
  }
}
