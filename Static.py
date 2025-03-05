class Python:
 staticVariable = 8
print(Python.staticVariable)


Python.staticVariable = 12
print(Python.staticVariable) 


instance = Python()
print(instance.staticVariable) 

#Change within an instance
instance.staticVariable = 15
print(instance.staticVariable) 
print(Python.staticVariable) 