import RPi.GPIO as gpio

class Sensor:
    def __init__(self, sensorPin):
        self.sensorPin = sensorPin
        gpio.setup(self.sensorPin, gpio.IN)
        print("Sensor initiated on {}, the initial state is {}".format(self.sensorPin, self.get_status()))

    def get_status(self):
        return gpio.input(self.sensorPin)
