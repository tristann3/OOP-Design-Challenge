from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
import os

class Person():
    def __init__(self, name, money):
        self.__name = name
        self.__money = money
    garage = list() # will contain a list of vehicles

    def getVehicles(self):
        '''Returns all vehicles in Person's garage'''
        if not self.garage: # if list is empty
            print("Tristan's garage is empty!")
        else:
            print(f"{self.__name}'s Garage: \n------------------------------------------")
            for vehicle in self.garage:
                print("")
                print(vehicle)
                if isinstance(vehicle, Car):
                    vehicle.zoom()
                    vehicle.canSelfDrive()
                elif isinstance(vehicle, Motorcycle):
                    vehicle.hasWheelieBar()
                vehicle.getMaxSpeed()
                vehicle.getSpeedPerWheel()
                print("")

            print("------------------------------------------")
    
    def getMoney(self):
        '''Returns the current amount of money the person object has'''
        return f"${self.__money}"
    
    def getAssets(self):
        assets = self.__money
        for vehicle in self.garage:
            assets += vehicle.getValue()
        return str(assets)

    def buyVehicle(self, Vehicle):
        '''Adds a vehicle to the garage'''
        self.__money -= float(Vehicle.getValue())
        self.garage.append(Vehicle)

    def sellVehicle(self, Vehicle):
        '''Removes a vehicle from the garage'''
        Vehicle.getInfo()
        self.__money += float(Vehicle.getValue())
        self.garage.remove(Vehicle)

if __name__ == "__main__":
    os.system("clear")

    tesla = Car(38045, "Telsa", "Tesla Series X", "2020", 130, 4, False, True)
    honda = Car(38045, "Honda", "WRX", "2020", 174, 4, True, False)
    kawasaki = Motorcycle(4999, "Kawasaki", "Ninja 400", "2020", 105, 2, True)
    harley = Motorcycle(11499, "Harley Davidson", "Roadster", "2020", 110, 2, False)

    Tristan = Person("Tristan", 100000)

    tesla.getInfo()
    kawasaki.getInfo()
    honda.getInfo()
    harley.getInfo()

    print("\nCurrent money: " + Tristan.getMoney())

    print("\nTristan buys all the cars\n")
    Tristan.buyVehicle(kawasaki)
    Tristan.buyVehicle(harley)
    Tristan.buyVehicle(tesla)
    Tristan.buyVehicle(honda)
    print("Current money " + Tristan.getMoney() + "\n")
    Tristan.getVehicles()

    print("\n\n1 year has passed and you decide to sell some cars\n\n")
    tesla.depreciate()
    kawasaki.depreciate()

    Tristan.sellVehicle(kawasaki)
    Tristan.sellVehicle(tesla)
    print("\n")

    
    Tristan.getVehicles()


    print("\nEnding money " + Tristan.getMoney())
    print("Assets " + Tristan.getAssets())

    