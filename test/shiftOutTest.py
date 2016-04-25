import unittest

from time import sleep
import RPi.GPIO as GPIO

from src.elec.shiftOut import ShifRegister

class ShiftOutTest(unittest.TestCase):
    
    def __init__(self):
        data_pin = 3 #pin 14 on the 75HC595
        latch_pin = 5 #pin 12 on the 75HC595
        clock_pin = 7 #pin 11 on the 75HC595
        GPIO.setmode(GPIO.BOARD)
        self.shift_register = ShifRegister(data_pin, latch_pin, clock_pin)
    
    #    Clignotement des diodes 0 à 7 par 4 fois
    def test_Clignote_0A7_5x(self):
        i = 0
        while i < 5:
            self.shift_register.setOutput(0, GPIO.HIGH)
            self.shift_register.setOutput(1, GPIO.HIGH)
            self.shift_register.setOutput(2, GPIO.HIGH)
            self.shift_register.setOutput(3, GPIO.HIGH)
            self.shift_register.setOutput(4, GPIO.HIGH)
            self.shift_register.setOutput(5, GPIO.HIGH)
            self.shift_register.setOutput(6, GPIO.HIGH)
            self.shift_register.setOutput(7, GPIO.HIGH)
            self.shift_register.setCommit()
            sleep(1)
            self.shift_register.setOutput(0, GPIO.LOW)
            self.shift_register.setOutput(1, GPIO.LOW)
            self.shift_register.setOutput(2, GPIO.LOW)
            self.shift_register.setOutput(3, GPIO.LOW)
            self.shift_register.setOutput(4, GPIO.LOW)
            self.shift_register.setOutput(5, GPIO.LOW)
            self.shift_register.setOutput(6, GPIO.LOW)
            self.shift_register.setOutput(7, GPIO.LOW)
            self.shift_register.setCommit()
            sleep(1)
            i = i +1

#         i=0
#         shift_register.setOutputWithCommit(i, GPIO.HIGH)
#         sleep(0.05)
#         while i<23:
#                 i=i+1
#                 shift_register.setOutputWithCommit(i-1, GPIO.LOW)
#                 shift_register.setOutputWithCommit(i, GPIO.HIGH)
#                 sleep(0.05)
#         shift_register.setOutputWithCommit(23, GPIO.LOW)
