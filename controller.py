#controller.py adapted from Clay McLeod's PS4 Controller class:
#https://gist.github.com/claymcleod/028386b860b75e4f5472

#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file presents an interface for interacting with the Playstation 4 Controller
# in Python. Simply plug your PS4 controller into your computer using USB and run this
# script!
#
# NOTE: I assume in this script that the only joystick plugged in is the PS4 controller.
#       if this is not the case, you will need to change the class accordingly.
#
# Copyright © 2015 Clay L. McLeod <clay.l.mcleod@gmail.com>
#
# Distributed under terms of the MIT license.

import pygame
import serial 
import time

# make sure servo commands not sent when initialized
cmd = "888"

class XBOX360Controller(object):
    """Class representing the PS4 controller. Pretty straightforward functionality."""
    
    #changed to XBOX360 class as Windows recognizes controller as such

    controller = None
    axis_data = None
    button_data = None
    hat_data = None

    def init(self):
        """Initialize the joystick components"""
        
        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def listen(self):
        """Listen for events to happen"""

        if not self.axis_data:
            self.axis_data = {}

        if not self.button_data:
            self.button_data = {}
            for i in range(self.controller.get_numbuttons()):
                self.button_data[i] = False

        if not self.hat_data:
            self.hat_data = {}
            for i in range(self.controller.get_numhats()):
                self.hat_data[i] = (0, 0)

        servo = 0
        cmd = "888"
        while True:
            for event in pygame.event.get():
                # not used. final number of servos reduced to 2
                if event.type == pygame.JOYBUTTONDOWN:
                    #print(event.button)
                    if event.button == 0: # X Button
                        #arduino code
                        servo = "8" # servo 1
                        #res = write_read(cmd)
                        #print(res)
                    elif event.button == 1: # O Button
                        #arduino code
                        servo = "9" # servo 2
                        #res = write_read(cmd)
                        #print(res)
                    elif event.button == 2: # SQUARE Button
                        #arduino code
                        servo = "10" # servo 3
                        #res = write_read(cmd)
                        #print(res)
                    elif event.button == 3: # TRIANGLE Buttton
                        #arduino code
                        servo = "0" # no servo
                        #res = write_read(cmd)
                        #print(res)
                    #elif event.button == 4: # LEFT Trigger
                        #arduino code
                        servo = "0" # no servo
                        #res = write_read(cmd)
                        #print(res)
                    #elif event.button == 5: # RIGHT Trigger
                        #arduino code
                        servo = "0" # no servo
                        #res = write_read(cmd)
                        #print(res)

                    #res = write_read(servo)
                    #print(res)
                elif event.type == pygame.JOYHATMOTION:
                    if event.hat == 0:
                        if event.value == (1, 0): # Servo 1
                            #print("DPAD-right")
                            cmd = "3"
                        if event.value == (-1, 0): # Servo 1
                            #print("DPAD-left")
                            cmd = "-3"
                        if event.value == (0, 1): # Servo 2
                            #print("DPAD-up")
                            cmd = "4"
                        if event.value == (0, -1): # Servo 2
                            #print("DPAD-down")
                            cmd = "-4"
                        if event.value == (0, 0): # Release DPAD
                            cmd = "888"

            # increases/decreases servo angle as long as DPAD held down
            if cmd != "888":
                res = write_read(cmd)
                print(res)

# arduino wrapper for pyserial adapted from arduino forums
# https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

if __name__ == "__main__":
    x360 = XBOX360Controller()
    x360.init()
    x360.listen()