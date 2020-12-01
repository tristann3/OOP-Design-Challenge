class Vehicle():
    def __init__(self, value, make, model, year):
        self.value = value
        self.make = make
        self.model = model
        self.year = year


    def getInfo(self):
        print(f"{self.make} {self.model} {self.year} is worth ${self.value}")
        return

    def depreciate(self):
        self.value -= self.value * .15
