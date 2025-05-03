class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Child (Person):
    def __init__(self, name, age,address):
        Person.__init__(self,name, age)
        self.address = address
    def print_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

x = Person("John", 36)
ch = Child("Jane", 25,"Pune")
ch.print_details()
x.print_details()
