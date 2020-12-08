from vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, value, make, model, year, maxSpeed, numWheels, wheelieBar):
        super().__init__(value, make, model, year, maxSpeed, numWheels)
        self.wheelieBar = wheelieBar
    
    def hasWheelieBar(self):
        if self.wheelieBar == True:
            my_str = "I can do wheelies"
            print(my_str.ljust(45) + "|")
        else:
            my_str = "I can't do wheelies"
            print(my_str.ljust(45) + "|")

