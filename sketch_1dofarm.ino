#include <Servo.h>
Servo servo1;
Servo servo2;

const int MIN_ANGLE = 20;
const int MAX_ANGLE = 175;

const int OPEN_ANGLE = 20;
const int CLOSE_ANGLE = 105;

int servo1Angle = MIN_ANGLE;
int servo2Angle = CLOSE_ANGLE;

void setup() {
  // set baudrate
  Serial.begin(115200);
  Serial.setTimeout(1);
  servo1.attach(10);  // whatever pin we use
  servo2.attach(9);  // whatever pin we use

  // CODE FOR POKER TEST ONLY
  // init servo angles
  //servo1.write(MAX_ANGLE);
  // delay(1000);
  // for (int i = MAX_ANGLE; i > MIN_ANGLE; i--) {
  //   delay(30);
  //   servo1.write(i);
  // }
  // delay(1000);
  // for (int i = MIN_ANGLE; i < MAX_ANGLE; i++) {
  //   delay(30);
  //   servo1.write(i);
  // }
  //delay(3000);
  //servo1.write(MIN_ANGLE);
  // delay(3000);

  // CODE FOR GRIPPER TEST ONLY
  servo1.write(MAX_ANGLE);
  servo2.write(OPEN_ANGLE);
  delay(5000);
  servo2.write(servo2Angle);
  delay(5000);
  servo1.write(servo1Angle);
}
void loop() {
  while (!Serial.available())
    ;
  int x = Serial.readString().toInt();
  Serial.print(x);
  // SERVO 1 - ARM
  if (x == 3 || x == -3) {  // Right-Left on Dpad
    x = x / 3;
    x = x * 2;
    Serial.print(servo1Angle);
    if (servo1Angle > MAX_ANGLE) {
      Serial.print("MAX ANGLE REACHED");
      if (x == -1) {
        servo1Angle += x;
      }
    } else if (servo1Angle < MIN_ANGLE) {
      Serial.print("MIN ANGLE REACHED");
      if (x == 1) {
        servo1Angle += x;
      }
    } else {
      servo1Angle += x;
    }
    if (servo1Angle < MAX_ANGLE && servo1Angle > MIN_ANGLE) {
      servo1.write(servo1Angle);
    }
    Serial.print("Servo 1 angle is: ");
    Serial.print(servo1Angle);
    delay(2);
  }
  // SERVO 2 - GRIPPER
  if (x == 4 || x == -4) { // Up-Down on Dpad
    x = x / 4;
    Serial.print(servo2Angle);
    if (servo2Angle > MAX_ANGLE) {
      Serial.print("MAX ANGLE REACHED");
      if (x == -1) {
        servo2Angle += x;
      }
    } else if (servo2Angle < MIN_ANGLE) {
      Serial.print("MIN ANGLE REACHED");
      if (x == 1) {
        servo2Angle += x;
      }
    } else {
      servo2Angle += x;
    }
    if (servo2Angle < MAX_ANGLE && servo2Angle > MIN_ANGLE) {
      servo2.write(servo2Angle);
    }
    if (x == 1) {
      servo2Angle = CLOSE_ANGLE;
    }
    if (x == -1) {
      servo2Angle = OPEN_ANGLE;
    }
    servo2.write(servo2Angle);
    Serial.print("Servo 2 angle is: ");
    Serial.print(servo2Angle);
    delay(5);
  }
}