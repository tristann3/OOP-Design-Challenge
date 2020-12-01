from vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, value, make, model, year, maxSpeed):
        super.__init__(value, make, model, year)
        self.maxSpeed = maxSpeed

    def getMaxSpeed(self):
        print(f"my max speed is {self.maxSpeed}")