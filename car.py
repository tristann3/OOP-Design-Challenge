from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, value, make, model, year, maxSpeed):
        super.__init__(value, make, model, year)
        self.maxSpeed = maxSpeed
        self.numWheels = 4

    def getMaxSpeed(self):
        '''Returns max speed of the Car'''
        print(f"my max speed is {self.maxSpeed}")

    