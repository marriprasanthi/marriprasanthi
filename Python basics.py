print ("prasanthi") 
print("Multi-line commenting")
a = -5
print("Type of a: ", type(a))
b = False
print("Type of b: ", type(b))
c = 5.0
print("Type of c: ", type(c))
String = 'Hello'
print("Type of String: ", type(String))
a = 5
def f():
    print('Inside f() : ', a)

def g():
    a = 2
    print('Inside g() : ', a) 
# Uses global keyword to modify global 'a'
def h():
    global a
    a = 4      #Value of 'a' modified
    print('Inside h() : ', a)  
# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)