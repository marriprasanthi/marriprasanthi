from abc import ABC, abstractmethod
 
class Vehicle(ABC):  
 
    @abstractmethod
    def number_of_wheels(self):
        pass
 
class Bicycle(Vehicle):  
 
   
    def number_of_wheels(self):
        print("Bicycle: I have 2 wheels")
 
class Car(Vehicle):  
 
  
    def number_of_wheels(self):
        print("Car: I have 4 wheels")
 
class Truck(Vehicle): 
 
 
    def number_of_wheels(self):
        print("Truck: I have 6 wheels")
 
class Motorcycle(Vehicle): 
 
 
    def number_of_wheels(self):
        print("Motorcycle: I have 2 wheels")
 

obj1 = Bicycle()
obj1.number_of_wheels()
 
obj2 = Car()
obj2.number_of_wheels()
 
obj3 = Truck()
obj3.number_of_wheels()
 
obj4 = Motorcycle()
obj4.number_of_wheels()
