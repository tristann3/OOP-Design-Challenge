from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, value, make, model, year, maxSpeed, numWheels, nitrous, selfDrive):
        super().__init__(value, make, model, year, maxSpeed, numWheels)
        self.nitrous = nitrous      # this value is private because it is only used in this class
        self.selfDrive = selfDrive

    def zoom(self):
        if self.nitrous == True:
            my_str = "I can use nitrous!"
            print(my_str.ljust(45) + "|")

    def canSelfDrive(self):
        if self.selfDrive == True:
            my_str = "I can self drive"
            print(my_str.ljust(45) + "|")
        



    
