void setup()                               // Built-in initialization block
{
  tone(4, 3000, 1000);                    // Play tone for 1 second
  delay(1000);                            // Delay to finish tone
  pinMode(10, INPUT);  pinMode(9, OUTPUT);   // Left IR LED & Receiver
  Serial.begin(9600);                     // Set data rate to 9600 bps
} 

void loop()                               // Main loop auto-repeats
{
  int irLeft = irDetect(9, 10, 38000);    // Check for object
  Serial.println(irLeft);                 // Display 1/0 no detect/detect
  delay(100);                             // 0.1 second delay
}

// IR Object Detection Function

int irDetect(int irLedPin, int irReceiverPin, long frequency)
{
  tone(irLedPin, frequency, 8);           // IRLED 38 kHz for at least 1 ms
  delay(1);                               // Wait 1 ms
  int ir = digitalRead(irReceiverPin);    // IR receiver -> ir variable
  delay(1);                               // Down time before recheck
  return ir;                              // Return 1 no detect, 0 detect
}  





Infrared Controlled Moving:
#include <Servo.h>

Servo servoRight;
Servo servoLeft;

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

void setup(){                                 
  tone(4, 3000, 1000);                       
  delay(1000);                               
  servoLeft.attach(13);  
  servoRight.attach(12); 
  pinMode(10, INPUT);  pinMode(9, OUTPUT);   
  pinMode (3, INPUT); pinMode (2, OUTPUT);
  Serial.begin(9600);                        
}  

int irDetect(int irLedPin, int irReceiverPin, long frequency){
  tone(irLedPin, frequency, 8);              
  delay(1);                                  
  int ir = digitalRead(irReceiverPin);       
  delay(1);                                  
  return ir;                                 
}  

void loop() { 
  int irLeft = irDetect(9, 10, 38000);  
  int irRight = irDetect (2, 3, 38000);
  
  if (irLeft == 1 && irRight == 1){
    Serial.println("forward");
    forward(3);
  } else if (irLeft == 0 && irRight == 1){
    Serial.println("right");
    turnRight(50);
  } else if (irLeft == 1 && irRight == 0){
    Serial.println("left");
    turnLeft(50);
  }else if (irRight == 0 && irLeft == 0){
    Serial.println("back");
    reverse(3);

}
