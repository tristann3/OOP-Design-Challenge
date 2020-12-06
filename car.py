from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, value, make, model, year, maxSpeed):
        self.maxSpeed = maxSpeed
        self.numWheels = 4

    def getMaxSpeed(self):
        '''Returns max speed of the Car'''
        print(f"my max speed is {self.maxSpeed}")

    def getSpeedPerWheel(self):
        '''Calculates and prints speed per wheel --dont ask-- '''
        speedPerWheel = int(self.maxSpeed / self.numWheels)
        print(f"this vehicle gets {speedPerWheel} MPH per wheel!")

    if __name__ == "__main__":
        pass