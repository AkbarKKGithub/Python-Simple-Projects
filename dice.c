
void setup() {
Serial.begin(9600);
Serial.println("Welcome");
pinMode(13, INPUT_PULLUP);
pinMode(2, OUTPUT);
pinMode(3, OUTPUT);
}

void loop() {
  Serial.println("Roll:");
  while(true)
  {
    if(digitalRead(13)==0)
    {
      break;
    }
  }
  int x=random(1,6);
  Serial.println("output=");
  Serial.println(x);
  digitalWrite(x, HIGH);
  delay(1000);
   digitalWrite(x, LOW);
}
