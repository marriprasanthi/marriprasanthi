
   class Person:
    def __init__(self):
        self.name = "ARJUN" 

    def print_person(self):
        print("Class Person Name:", self.name)

class Employee(Person):
    def __init__(self):
        super().__init__() 
        self.name = "RAHUL"  

    def print_employee(self):
        print("Class Employee Name:", self.name)


objPerson = Person()
objPerson.print_person()

objEmployee = Employee()
objEmployee.print_employee()



class Student:
    name = None
    _roll = None  
    __course = None  

    def __init__(self, name, roll, course):
        self.name = name  
        self._roll = roll 
        self.__course = course  

    def displayName(self):  
        print("Name:", self.name)

    def _displayRoll(self): 
        print("Roll:", self._roll)

    def __displayCourse(self): 
        print("Course:", self.__course)

    def access_displayCourse(self):  
        self.__displayCourse()



class Graduate(Student):
    def __init__(self, name, roll, course):
        super().__init__(name, roll, course)

    def access_displayRoll(self):  
        self._displayRoll()


objGraduate = Graduate("VIKRAM", 10, "Computer Science")


objGraduate.displayName()  
objGraduate.access_displayRoll() 
objGraduate.access_displayCourse()  
