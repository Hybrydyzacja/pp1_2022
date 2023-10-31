import random


class Temperature():
    def __init__(self):
        self.is_on = False
        self.temp = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_status(self):
        if self.is_on == True:
            if self.temp > 37.0 and self.temp < 41.0:
                print(f"{self.temp}C (fever)")
            elif self.temp >= 41.0 and self.temp <= 42.0:
                print(f"{self.temp}C (CRITICAL TEMPERATURE)")
            elif self.temp > 34.0 and self.temp < 37.0:
                print(f"{self.temp}C")
            else:
                print("Thermometer is on, ready to measure")
        else:
            print("Thermometer is off")

    def measure(self):
        self.temp = round(random.uniform(34.0, 42.0),1)


# temp1 = Temperature()

# # temp1.show_status()
# temp1.turn_on()
# temp1.measure()
# temp1.show_status()
# temp1.turn_off()
# # temp1.show_status()
