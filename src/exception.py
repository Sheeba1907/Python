#Simple try and except
try:
    num = int('abc')
except ValueError:
    print("Invalid input for int")
    
#Exception using functions
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError: 
        return "Cannot divide by zero"
print(divide(4,2))

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError: 
        return "Cannot divide by zero"
print(divide(4,0))

#Multiple exceptions
try:
    a = 10/2
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Division is impossible with zero")
    
#Using else and finally also
try:
    num = int(100)
except ValueError:
    print("Invalid input")
else:
    print("Successful code, the number is:", num)
finally:
    print("This always runs")
    
#Raising exceptions
def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b
try:
    print(divide(10,0))
except ZeroDivisionError as e:
    print("ERROR:", e)
