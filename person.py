from vehicle import Vehicle
class Person():
    def __init__(self, name, money):
        self.name = name
        self.money = money
    garage = list() # will contain a list of vehicles

    def getVehicles(self):
        '''Returns all vehicles in Person's garage'''
        for car in self.garage:
            print(f"{car.make} {car.model} {car.year} is worth ${car.value}")

    def buyVehicle(self, money, Vehicle):
        '''Adds a vehicle to the garage'''
        self.money -= money
        self.garage.append(Vehicle)

    def sellVehicle(self, money, Vehicle):
        '''Removes a vehicle from the garage'''
        self.money += money
        self.garage.remove(Vehicle)

if __name__ == "__main__":
    pass