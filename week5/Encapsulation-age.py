# Encapsulation + Property Decorators
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = None
        self.age = age  # use setter

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        if value > 120:
            raise ValueError("Age cannot be greater than 120")
        self.__age = value

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

if __name__ == "__main__":
    p = Person("Nahal", 32)
    p.info()

    p.age = 30
    p.info()