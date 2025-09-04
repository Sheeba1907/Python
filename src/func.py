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

