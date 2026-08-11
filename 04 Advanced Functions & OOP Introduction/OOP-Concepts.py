# Introduce
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} & I'm {self.age} years old.\n\n"

p = Person("Yadi", 105)
print(p.introduce())


# BankAccount
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Balance after deposit: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Balance after withraw: {self.balance}"

    def show_balance(self):
        return f"Balance: {self.balance}\n"

acc = BankAccount("Yadi", 1000)
print(acc.deposit(250))
print(acc.withdraw(400))
print(acc.show_balance())


# student person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def info(self):
        return f"Name: {self.name}, Age: {self.age}, Student_id: {self.student_id}"

s = Student("Yadi", 106, "Anine")
print(s.info())