# ps3-controller-2-servo
- Quick and dirty solution for actuating servos with a PS3 controller. Read at your own risk &amp; no guarantees it will work for your project.   
- PS3 controller registered to Windows PC with [DsHidMini](https://github.com/ViGEm/DsHidMini) and converted to XInput.  
- This code worked with an Arduino Uno, and a 1-dof arm with one servo for the arm and one servo for the gripper.  
- This scheme could potentially work for up to 6 servos (1 for each button + L1/R1 trigger. We lose L2/R2 triggers due to being recognized as an XBox 360 controller).  
- Also be warned: `controller.py` connection occasionally drops.

# Libraries used
- Python: pyserial, pygame
- Arduino IDE: Servo.h
- Original PS4 pygame class & connection credit to: https://gist.github.com/claymcleod/028386b860b75e4f5472
- Pyserial - Arduino connection credit to: https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0

# to run
1. Connect your Arduino and controller via USB to PC or controller
2. Check your COM port for Arduino and COM port, baudrate in `controller.py` if needed
3. Open Arduino IDE
4. Write `.ino` code for your servos. make sure you're using the right pins in `setup`
5. Check your `.ino` code to make sure it compiles, then upload to Arduino
6. Close out of the Arduino IDE or the `controller.py` script won't be able to connect
7. Run `controller.py`
8. Use your controller to actuate your servos!
