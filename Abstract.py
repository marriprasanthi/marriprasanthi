from abc import ABC, abstractmethod
 
class Vehicle(ABC):  # Base class / Superclass
 
    @abstractmethod
    def number_of_wheels(self):
        pass
 
class Bicycle(Vehicle):  # Subclass
 
    # Overriding abstract method
    def number_of_wheels(self):
        print("Bicycle: I have 2 wheels")
 
class Car(Vehicle):  # Subclass
 
    # Overriding abstract method
    def number_of_wheels(self):
        print("Car: I have 4 wheels")
 
class Truck(Vehicle):  # Subclass
 
    # Overriding abstract method
    def number_of_wheels(self):
        print("Truck: I have 6 wheels")
 
class Motorcycle(Vehicle):  # Subclass
 
    # Overriding abstract method
    def number_of_wheels(self):
        print("Motorcycle: I have 2 wheels")
 
# Driver code
# Creating the objects to call the abstract method.
obj1 = Bicycle()
obj1.number_of_wheels()
 
obj2 = Car()
obj2.number_of_wheels()
 
obj3 = Truck()
obj3.number_of_wheels()
 
obj4 = Motorcycle()
obj4.number_of_wheels()
