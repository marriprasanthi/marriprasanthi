
class ClassOne:
    def __init__(self):
        print("ClassOne Constructor Called")

    def display(self):
        print("Method from ClassOne")


class ClassTwo:
    def __init__(self):
        print("ClassTwo Constructor Called")

    def show(self):
        print("Method from ClassTwo")

mypackage = {
    "ClassOne": ClassOne,
    "ClassTwo": ClassTwo
}
ClassOneImported = mypackage["ClassOne"]
ClassTwoImported = mypackage["ClassTwo"]


obj1 = ClassOneImported()
obj1.display()

obj2 = ClassTwoImported()
obj2.show()
