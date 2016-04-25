import RPi.GPIO as GPIO

class ShifRegister:
 
    def __init__(self, data_pin, latch_pin, clock_pin):
        self.data_pin = data_pin    #    data_pin => pin 14 on the 74HC595
        self.latch_pin = latch_pin  #    latch_pin => pin 12 on the 74HC595
        self.clock_pin = clock_pin  #    clock_pin => pin 11 on the 74HC595
        GPIO.setup(self.data_pin, GPIO.OUT)
        GPIO.setup(self.latch_pin, GPIO.OUT)
        GPIO.setup(self.clock_pin, GPIO.OUT)
        #     output_number => Value from 0 to n pointing to the output pin on the 74HC595
        #     0 => Q0 pin 15 on the 74HC595
        #     1 => Q1 pin 1 on the 74HC595
        #     2 => Q2 pin 2 on the 74HC595
        #     3 => Q3 pin 3 on the 74HC595
        #     4 => Q4 pin 4 on the 74HC595
        #     5 => Q5 pin 5 on the 74HC595
        #     6 => Q6 pin 6 on the 74HC595
        #     7 => Q7 pin 7 on the 74HC595
        #     n => Qn pin n ...
        #     value => a state to pass to the pin, could be HIGH or LOW
        self.outputs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def setOutputWithCommit(self, output_number, value):
        self.setOutput(output_number, value)
        self.setCommit()

    #    Definir la valeur de pin dans le registre sans commit
    def setOutput(self, output_number, value):
        try:
            self.outputs[output_number] = value
        except IndexError:
            raise ValueError("Numero de sortie invalide, la valeur doit etre comprise entre 0 et 23")

        GPIO.output(self.latch_pin, GPIO.LOW)
        for output in range(23, -1, -1):
            GPIO.output(self.clock_pin, GPIO.LOW)
            value = self.outputs[output]
            GPIO.output(self.data_pin, value)
            GPIO.output(self.clock_pin, GPIO.HIGH)

    #    Commit les valeurs sasies dans les registres des CI
    def setCommit(self):
        GPIO.output(self.latch_pin, GPIO.HIGH)


