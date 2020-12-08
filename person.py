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
            for car in self.garage:
                print("")
                print(car)
                car.getMaxSpeed()
                car.getSpeedPerWheel()
                print("")

            print("------------------------------------------")
    
    def getMoney(self):
        '''Returns the current amount of money the person object has'''
        return f"${self.__money}"

    def buyVehicle(self, Vehicle):
        '''Adds a vehicle to the garage'''
        self.__money -= float(Vehicle.getValue())
        self.garage.append(Vehicle)

    def sellVehicle(self, Vehicle):
        '''Removes a vehicle from the garage'''
        self.__money += float(Vehicle.getValue())
        self.garage.remove(Vehicle)

if __name__ == "__main__":
    os.system("clear")
    toyota = Car(38045, "Jeep", "Wrangler Rubicon", "2019", 112, 4)
    kawasaki = Motorcycle(4999, "Kawasaki", "Ninja 400", "2020", 105, 2)
    Tristan = Person("Tristan", 100000)

    toyota.getInfo()
    kawasaki.getInfo()

    print("\nStarting money: $" + Tristan.getMoney())

    print("Tristan has " + Tristan.getMoney())
    Tristan.buyVehicle(kawasaki)
    Tristan.buyVehicle(toyota)
    print("Tristan has " + Tristan.getMoney() + "\n")
    Tristan.getVehicles()

    print("\n\n1 year has passed and you decide to sell your cars\n\n")
    toyota.depreciate()
    kawasaki.depreciate()

    Tristan.sellVehicle(kawasaki)
    Tristan.sellVehicle(toyota)

    
    Tristan.getVehicles()


    print("\nEnding money " + Tristan.getMoney())

    