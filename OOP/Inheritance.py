# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_details(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#
# class Child (Person):
#     def __init__(self, name, age,address):
#         Person.__init__(self,name, age)
#         self.address = address
#     def print_details(self):
#         print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")
#
# x = Person("John", 36)
# ch = Child("Jane", 25,"Pune")
# ch.print_details()
# x.print_details()


class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name

    def print_details(self):
        print(f"Name: {self.name}\nPrice: {self.price}")


class Volvo:
    def __init__(self, model, rent):
        self.model = model
        self.rent = rent

    def show_details(self):
        print(f'Model: {self.model}, Rent: {self.rent}')


v1 = Volvo("MK12", 1200)
print(v1)
v1.show_details()