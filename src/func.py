#*args
def function(*numbers):
    print("The number is: ", numbers[2])
function(1,2,3,4)

#*Kwargs
def func(c1,c2,c3):
    print("Cars are:", c1+","+c2+","+c3)
func(c1="BMW", c2="Audi", c3="Ferrari")
    
#**kwargs
def func1(**number):
    print("Number: ", number['sum'])
func1(sum='1', num='2', val='3')

#Default parameter value
def num(n=19):
    print("I choose: ", n)
num(20)
num(30)
num()

#Passing datatype as argument
def func2(mylist):
    for item in mylist:
        print(item)
mylist = ["Bat", "Ball", "Cup"]
func2(mylist)

#Return values
def add(a, b):
    return a + b
result = add(5, 3)
print("The sum is:", result)

#what if return is replaced with print
def add(a, b):
    print(a + b)
result1 = add(5, 3)
print("The sum is:", result1)

def square(n):
    return n * n
result2 = square(4)+10
print("The square is:", result2)

def square(n):
    print(n * n)
#result3 = square(4)+10
#print("The square is:", result3)

#Recursion
#normal function
def sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i  
    return total
r = sum(5)
print("The sum is:", r)

#recursive function
def sum(n):
    if n == 1:         #base condition
        return 1
    return n + sum(n - 1)
print(sum(5))


#Modules
import math
print(math.sqrt(16))
print(math.pi)

import random
print(random.randint(1, 100))

from math import sqrt
print(sqrt(25))