#

class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving...")

class Car(Vehicle):
    def __init__(self, name, fuel_type):
        super().__init__(name)
        self.fuel_type = fuel_type

    def fuel(self):
        print(f"{self.name} uses {self.fuel_type} fuel.")

class ElectricCar(Car):
    def __init__(self, name, battery_capacity):
        super().__init__(name, fuel_type="electric")
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"{self.name} is charging. Battery: {self.battery_capacity}")

    def fuel(self):
        print(f"{self.name} does not use fuel, it uses electricity")

if __name__ == "__main__":
    v = Vehicle("Generic Vehicle")
    c = Car("Gas Car", "gasoline")
    e = ElectricCar("Tesla", 75)

    v.move()
    c.move()
    c.fuel()
    e.move()
    e.fuel()
    e.charge()