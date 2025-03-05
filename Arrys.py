from audioop import avg
from operator import index
from turtle import position
from typing import final

arr = [10,20,30,40]
sum = 0
for i in range(0,len(arr)):
    sum = sum + arr[i]
print("Sum of all integer values in array: ",sum) 


def cal_average(num):
    sum_num = 0
    for i in num:
        sum_num = sum_num + i    
        avg = sum_num / len(num)
    return avg

print("The average is", cal_average([12,23,34,44,55]))

arr = [1,3,5,3,1,2,6,5,3,8,6,9]


index = arr.index(3)
print("Index of 3: ",index)

index = arr.index(9)
print("Index of 9: ",index)

index = arr.index(8)
print("Index of 8: ",index)
      
