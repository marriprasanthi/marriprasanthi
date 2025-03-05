class OverloadExample:
    def add(self, a, b=None):
        if b is not None:
            print(f"Sum: {a + b}")
        else:
            print(f"Single parameter: {a}")

    
    def show(self, a, b=None):
        if isinstance(a, str) and b is None:
            print(f"String input: {a}")
        elif isinstance(a, int) and isinstance(b, int):
            print(f"Sum of integers: {a + b}")
        else:
            print("Invalid parameters")

    
    def display(self, a, b):
        print(f"Display method called: {b}, {a}")  
obj = OverloadExample()


print("\nMethod Overloading - Same Name, Different Parameters:")
obj.add(10)       
obj.add(10, 20)

print("\nMethod Overloading - Different Parameter Types:")
obj.show("Hello")       
obj.show(10, 20)  

print("\nMethod Overloading - Same Name, Same Parameters (Last One Overrides):")
obj.display(5, 10)  
