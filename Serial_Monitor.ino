voud setup()
{
  pinMode(13, OUTPUT);
  Serial.begin(9600);
  while(!Serial);
  Serial.print1n("Input 1 to Turn LED 13 on and 2 to off");
  pinMode(12, OUTPUT);
  Serial.begin(9600);
  while(!Serial);
  Serial.print1n("Input 3 to Turn LED 12 on and 4 to off");
  pinMode(11, OUTPUT);
  Serial.begin(9600);
  while(!Serial);
  Serial.print1n("Input 5 to Turn LED 11 on and 6 to off");
  pinMode(10, OUTPUT);
  Serial.begin(9600);
  while(!Serial);
  Serial.print1n("Input 7 to Turn LED 10 on and 8 to off");
  pinMode(9, OUTPUT);
  Serial.begin(9600);
  while(!Serial);
  Serial.print1n("Input 9 to Turn LED 9 on and 10 to off");
 
}

void loop(){
 if (Serial.available() > 0) {
   incomingByte = Serial.read();
   if (incomingByte == '1') {
     digitalWrite(13, HIGH);
   } 
   
   if (incomingByte == '2') {
     digitalWrite(13, LOW);
   }  
   
   if (incomingByte == '3') {
     digitalWrite(12, HIGH);
   } 
   
   if (incomingByte == '4') {
     digitalWrite(12, LOW);
   }

   if (incomingByte =='5'){
     digitalWrite(11, HIGH);       
   }
   
   if (incomingByte == '6') {
     digitalWrite(11, LOW);
   }
    
   if (incomingByte == '7') {
     digitalWrite(10, HIGH);   
   }
  
   if (incomingByte =='8') {
     digitalWrite(10, LOW);
   }      
      
   if (incomingByte == '9') {
     digitalWrite(9, HIGH);     
   }
      
   if (incomingByte =='10') {
     digitalWrite(9, LOW);
    
   }
    if (incomingByte =='0') {
     digitalWrite(13, LOW); 
     digitalWrite(12, LOW);
     digitalWrite(11, LOW);
     digitalWrite(10, LOW);   
   }
   if (incomingByte =='9') {
     digitalWrite(13, HIGH); 
     digitalWrite(12, HIGH);
     digitalWrite(11, HIGH);
     digitalWrite(10, HIGH); 
   }
   void forward(int time) {
  servoLeft.write(0);
  servoRight.write(180);
  delay(time);
}

void reverse(int time) {
  servoLeft.write(180);
  servoRight.write(0);
  delay(time);
}

void turnRight(int time) {
  servoLeft.write(180);
  servoRight.write(180);
  delay(time);
}

void turnLeft(int time) {
  servoLeft.write(0);
  servoRight.write(0);
  delay(time);
}

void stopRobot() {
  servoLeft.write(90);
  servoRight.write(90);
}

  void setup() {
    servoLeft.attach(13);  // Set left servo to digital pin 10
    servoRight.attach(12);  // Set right servo to digital pin 9
  }
  void loop () {  
if (infrared sensor far away from something)
{
  forward(100);
}
else
{
  turnLeft();
}
}
