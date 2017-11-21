void setup() {
  // put your setup code here, to run once:
  pinMode(9, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  char val;
  if(Serial.available()>0){
    val=(char)Serial.read();
    Serial.println(val);
    if(val=='a')
      analogWrite(9, 255);
    else if (val=='b')
      analogWrite(9, 63);
    else
      analogWrite(9, 0);
  }
  
}
