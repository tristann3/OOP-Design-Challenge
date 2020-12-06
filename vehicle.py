class Vehicle():
    def __init__(self, value, make, model, year):
        self.value = value
        self.make = make
        self.model = model
        self.year = year


    def getInfo(self):
        '''Returns the Vehicle information in a readable string'''
        print(f"{self.make} {self.model} {self.year} is worth ${self.value}")
        return

    def depreciate(self):
        '''Sets the value of a vehicle to a depreciated value'''
        self.value -= self.value * .15
