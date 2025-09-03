print("Hello world frpm python script!")

''' This is a multi-line comment
    which spans multiple lines
    and is used to explain the code below. '''

x,y,z = 1,2,3
print(x+y+z)
a = "Python"
b = "is"
c = "fun!"
print(a + " " + b + " " + c)

#Global Variables
x = "Sheeba"
def func():
    x  = "Me"
    print("Name: ", x)
func()                      #Prints Name: Me

x = "Sheeba"
def func():
    x  = "Me"
    print("Name: ", x)
func() 
print("Name: ", x)         #Prints Name: Sheeba

def func1():
    global x
    x = "Print name"      #Prints Print name
func1()
print(x)

x = 5
def func1():
    x = 7
func1()
print(x)                    #Prints 5

x = 5
def func1():
    global x
    x = 7
func1()
print(x)                  #Prints 7

x = 5
y = "Hello"
print(type(x))               
print(type(y))