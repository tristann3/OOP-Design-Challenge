from vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, value, make, model, year, maxSpeed, numWheels, wheelieBar):
        super().__init__(value, make, model, year, maxSpeed, numWheels)
        self.__wheelieBar = wheelieBar # this value is private because it is only used in this class
    
    def hasWheelieBar(self):
        if self.__wheelieBar == True:
            my_str = "I can do wheelies"
            print(my_str.ljust(45) + "|")
        else:
            my_str = "I can't do wheelies"
            print(my_str.ljust(45) + "|")

