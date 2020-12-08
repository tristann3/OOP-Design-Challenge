from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, value, make, model, year, maxSpeed, numWheels):
        super().__init__(value, make, model, year, maxSpeed, numWheels)
         # private variables. these attributes outside of the class, dont, and shouldn't need to be used elsewhere.


    
