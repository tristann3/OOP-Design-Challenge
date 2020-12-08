from vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, value, make, model, year, maxSpeed, numWheels):
        super().__init__(value, make, model, year, maxSpeed, numWheels)
