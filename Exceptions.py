senior_ages = [65, 70, 75]
try:
    print("Second senior's age:", senior_ages[1])
    
    print("Fourth senior's age:", senior_ages[3])

except:
    print("An error occurred: Index out of range")

print()


group_one = [75, 70, 65]
group_two = [65, 70, 75]

try:
    group_one == group_two  
except:
    print("The groups are not equal")
else:
    print("Both groups are equal")

print()

try:
    retirement_fund = 100000 / 0
    print(retirement_fund)
except ZeroDivisionError:
    print("Error: Can't divide by zero")
finally:
    print("This block always executes")  
