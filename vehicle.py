class Vehicle():
    def __init__(self, value, make, model, year, maxSpeed, numWheels):
        self.value = value # these values are public because they are used to print
        self.make = make
        self.model = model
        self.year = year
        self.maxSpeed = maxSpeed
        self.numWheels = 4

    def getValue(self):
        '''Returns the current value of the Motorcycle'''
        return self.value

    def getInfo(self):
        '''Returns the Vehicle information in a readable string'''
        print(f"{self.make} {self.model} {self.year} is worth ${self.value}")
        return

    def depreciate(self):
        '''Sets the value of a vehicle to a depreciated value'''
        self.value -= int(self.value * .15) # linear depreciation, could use real data but....effort

    def getMaxSpeed(self):
        '''Returns max speed of the Car'''
        my_str = f"my max speed is {self.maxSpeed}"
        print(my_str.ljust(45) + "|")
    
    def getSpeedPerWheel(self):
        '''Calculates and prints speed per wheel --dont ask-- '''
        speedPerWheel = int(self.maxSpeed / self.numWheels)
        my_str = f"this vehicle gets {speedPerWheel} MPH per wheel!"
        print(my_str.ljust(45) + "|")

    def __str__ (self):
        my_str = f"{self.make} {self.model} {self.year} worth ${self.value}"
        return my_str.ljust(45) + "|"

    

