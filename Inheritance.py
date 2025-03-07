class Senior():  
    def display(self):
        print("Display inside Senior class")
 
    def show(self):
        print("Show inside Senior class")
     
class Manager(Senior): 
    def print_info(self):
        print("Print inside Manager class")    

    def show(self):
        print("Show inside Manager class")
    
 
class Director(Manager): 
    def show(self):
        print("Show inside Director class")         


senior_obj = Senior()
senior_obj.display()

manager_obj = Manager()
manager_obj.print_info()

director_obj = Director()   
director_obj.show()
