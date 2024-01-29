int LED_BUILTIN = 2;
void setup() {
  Serial.begin(115200);  // Set the baud rate to match the Raspberry Pi
  pinMode(LED_BUILTIN,OUTPUT);
}

void loop() {
  // Check if data is available from the Raspberry Pi
  if (Serial.available() > 0) {
    char incomeData = Serial.read();
    if (int(incomeData)%2 ==0){
      Serial.println("the integer is even!");
      digitalWrite(LED_BUILTIN,HIGH);
      }
     else{
      Serial.println(incomeData);
      digitalWrite(LED_BUILTIN,LOW);
     }

  }
    
  
  delay(1000);  // Add a delay to control the data sending rate
}
