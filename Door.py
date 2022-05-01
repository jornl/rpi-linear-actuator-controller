import RPi.GPIO as gpio
from decouple import config
from time import sleep
from Sensor import Sensor

# input_pin1 = 23
# input_pin2 = 24
class Door:
    def __init__(self, motorPin1, motorPin2, delay):
        self.pin1 = motorPin1
        self.pin2 = motorPin2
        self.delay = delay

        gpio.setmode(gpio.BCM)

        self.state = "initial"
        if (bool(config("USE_SENSOR")) == True):
            self.sensor = Sensor(int(config("SENSOR_PIN")))            

        print("Door initiated on {} and {}".format(self.pin1, self.pin2))

        gpio.setup(self.pin1, gpio.OUT)
        gpio.setup(self.pin2, gpio.OUT)

        gpio.output(self.pin1, 0)
        gpio.output(self.pin2, 0)

        print("Ensuring door is initially closed.")
        self.open()
        self.close()


    def __del__(self):
        print("Destrucing Door")
        gpio.cleanup()
        

    def handle(self, payload):
        if (str(payload) == "b'close'"):
            self.close()
        elif (str(payload) == "b'open'"):
            self.open()
        else:
            print("I dont understand what you mean.")
        

    def open(self):
        if (self.state != "opened"):
            self.state = "opened"
            print("Open door.")
            gpio.output(self.pin1, 1)
            gpio.output(self.pin2, 0)
            print("{} set to HIGH".format(self.pin1))
            sleep(self.delay)
            gpio.output(self.pin1, 0)
            print("{} set to LOW".format(self.pin1))
        else:
            print("Door is already open.")

    def close(self):
        if (self.state != "closed" and self.sensor.get_status() == 0):
            self.state = "closed"
            print("Close door.")
            gpio.output(self.pin1, 0)
            gpio.output(self.pin2, 1)
            print("{} set to HIGH".format(self.pin2))
            sleep(self.delay)
            gpio.output(self.pin2, 0)
            print("{} set to LOW".format(self.pin2))
        elif (self.state != "closed" and self.sensor.get_status() == 1):
            print("Vacuum missing.")
        else:
            print("Door is already closed.")