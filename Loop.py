from tkinter import N
a = "Bright IT Career"

for i in range(10):
    print(a)

i = 1

while(i<=20):
    print(i)
    i+= 1 



a = 5
b = 10
print(a ==b) 
print(a != b) 



Numbers = [1,2,3,4,5,6,7,8,9,10]
print("Even Numbers: ")  
for i in Numbers:     
    if i % 2 == 0:       
        print(i, end =" ")    
print("\nOdd Numbers:")
for i in Numbers:
    if i % 2 != 0:
        print(i, end =" ")
print()



k = 40
a = 50
s = 90
if k >= a and k >= s:
    largest = k
elif a >= k and a >= s:
    largest = a
else:
    largest = s
print("Largest number is: ",largest)  

a = 10
b = 20
print("Even Numbers Between 10 to 20: ",end=" ")
while a <= b:
    if(a % 2 == 0):
        print("{0}".format(a),end=" ")
    a = a + 1
print()

a = 1
print("Print 1 to 10 using the do-while loop statement:",end=" ")
while True:
    print(a,end=" ")
    a = a + 1
    if(a > 10):
        break 
print()

a = int(input('Enter a number to check if its armstrong or not: '))
sum = 0
temp = 0
temp = a
while temp > 0:
    r = temp % 10
    sum += r ** 3
    temp //= 10
if a == sum:
    print(a," is an amstrong number")
else:
    print(a," is not an amstrong number")

number = int(input("Enter any number to check prime number or not: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")


n = int(input("Enter number to check palindrome or not:"))
temp = n
rev = 0
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if(temp == rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!") 

a = int(input('Enter Number to check is EVEN or ODD: '))
if a % 2 == 0:
    print("{0} is Even ".format(a))
else:
    print("{0} is Odd ".format(a))  
