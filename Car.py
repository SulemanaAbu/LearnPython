# Car class
class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"This {self.make} is moving")

    def stop(self):
        print(f"This {self.make} has stopped")
