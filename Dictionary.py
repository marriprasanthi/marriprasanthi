
Dict = dict([(1,'Kashish'), (2,'Kritika'), (3,'Aastha'), (4,'Vaishali'), (5,'Muskan')])
print("Dictionary with each item as a pair:",Dict) #printing dictionary

Dict[6] = 'prasanthi'
print("\n Dictionary with new item added:",Dict)
Dict[3] = 'prasanthi'
print("\n Dictionary with updated values:",Dict)

print("\n Accessing one value in Dictionary:",Dict[1])

del Dict[6]
print("\n Delete a value from a Dictionary:",Dict)

Dict1 = {1: 'prasanthi', 2: 'lakshmi',
        3:{'Age' : 20, 'Branch' : 'bsc', 'Year' : 'Third Year'}}
print("\n Nested loop Dictionary:",Dict1)

print("\n Accessing an element of a Nested Dictionary:",Dict1[2])
