# Composition vs Inheritance for Car
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            print(f"Engine started with {self.horsepower} HP.")
        else:
            print("Engine is already running.")

    def stop(self):
        if self.running:
            self.running = False
            print("Engine stopped.")
        else:
            print("Engine is already off.")

class Car:
    def __init__(self, model, horsepower):
        self.model = model
        self.engine = Engine(horsepower)  #composition

    def drive(self):
        if not self.engine.running:
            self.engine.start()
        print(f"{self.model} is driving...")

    def park(self):
        print(f"{self.model} is parking...")
        self.engine.stop()


if __name__ == "__main__":
    car = Car("Mercedes", 2000)
    car.drive()
    car.park()