from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, value, make, model, year, maxSpeed):
        super().__init__(value, make, model, year)
        self.maxSpeed = maxSpeed
        self.numWheels = 4

    def getValue(self):
        '''Returns the current value of the Car'''
        return self.value

    def getMaxSpeed(self):
        '''Returns max speed of the Car'''
        print(f"my max speed is {self.maxSpeed}")

    def getSpeedPerWheel(self):
        '''Calculates and prints speed per wheel --dont ask-- '''
        speedPerWheel = int(self.maxSpeed / self.numWheels)
        print(f"this vehicle gets {speedPerWheel} MPH per wheel!")
