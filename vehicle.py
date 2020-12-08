class Vehicle():
    def __init__(self, value, make, model, year, maxSpeed, numWheels):
        self.__value = value # these values are private because they are used only in the class, and not in the subclasss
        self.__make = make
        self.__model = model
        self.__year = year
        self.__maxSpeed = maxSpeed
        self.__numWheels = 4

    def getValue(self):
        '''Returns the current value of the Motorcycle'''
        return self.__value

    def getInfo(self):
        '''Returns the Vehicle information in a readable string'''
        print(f"{self.__make} {self.__model} {self.__year} is worth ${self.__value}")
        return

    def depreciate(self):
        '''Sets the value of a vehicle to a depreciated value'''
        self.__value -= int(self.__value * .15) # linear depreciation, could use real data but....effort

    def getMaxSpeed(self):
        '''Returns max speed of the Car'''
        my_str = f"my max speed is {self.__maxSpeed}"
        print(my_str.ljust(45) + "|")
    
    def getSpeedPerWheel(self):
        '''Calculates and prints speed per wheel --dont ask-- '''
        speedPerWheel = int(self.__maxSpeed / self.__numWheels)
        my_str = f"this vehicle gets {speedPerWheel} MPH per wheel!"
        print(my_str.ljust(45) + "|")

    def __str__ (self):
        my_str = f"{self.__make} {self.__model} {self.__year} worth ${self.__value}"
        return my_str.ljust(45) + "|"

    

