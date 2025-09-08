#Decorators
def div(a, b):
    print(a / b)
def smart(func):
    def smd(a, b):
        if(a < b):
            a, b = b, a
            return func(a, b)
    return smd    
div = smart(div)
div(2, 4)

def logging(func):
    def wrapper(*args):
        print("Start logging..")
        func(*args)
        print("End log..")
    return wrapper
@logging
def add(n1, n2):
    print(n1+n2)
add(10, 2)
#without @logging
def sub(n1, n2):
    print(n1-n2)
log = logging(sub)
log(10,2)

#Generators

#If using return
#def countdown(n):
#   while n > 0:
#      #return n
#     n -= 1                    '''ERROR! Traceback (most recent call last): TypeError: 'int' object is not iterable'''
#for i in countdown(5):
    #print(i)
    
#With yield
def countdown(n):
    while n > 0:
        yield n
        n -= 1
for i in countdown(5):
    print(i)
    
def my_generator():
    yield 1
    yield 2
    yield 3
gen = my_generator()
print(next(gen))  
print(next(gen))  
print(next(gen)) 

gen_exp = (x * x for x in range(5))
for val in gen_exp:
    print(val)

#Higher order functions
#Takes another function as an argument
def gmail(username, domain = "gmail.com"):
    return f"{username}@{domain}"
def ymail(username, domain = "ymail.com"):
    return f"{username}@{domain}"
def hotmail(username, domain = "hotmail.com"):
    return f"{username}@{domain}"
def build_email(username, email_func):
    return email_func(username)
print(build_email(username = "Sheeba", email_func = gmail))
print(build_email(username = "Sheeba", email_func = ymail))
print(build_email(username = "Sheeba", email_func = hotmail))

print()

#Returning function as an output
def email_builder(domain):
    def build_email(username):
        return f"{username}@{domain}"
    return build_email
gmail = email_builder('gmail.com')
ymail = email_builder('ymail.com')
hotmail = email_builder('hotmail.com')
print(gmail("Sheeba"))
print(ymail("Sheeba"))
print(hotmail("Sheeba"))

#lambda functions
add = lambda x,y : x+y
print(add(4,5))
even_square = lambda a : a*a if a%2==0 else "Invalid"
print(even_square(5))

#map
fruits = ["apple", "mango", "kiwi"]
result = list(map(lambda fruit: fruit.upper(), fruits))
print(result)
numbers = [1,2,3,4]
r = list(map(lambda x : x ** 3, numbers))
print(r)

#filter
nums = [1,2,3,4,5,6,7,8]
c = list(filter(lambda x : x%2 == 0, nums))
print(c)
num = [10, 15, 20, 23, 13, 25]
d = list(filter(lambda x : x%5 == 0, num))
print(d)

#reduce
from functools import reduce
add = [1,2,3,4]
ans = reduce(lambda a,b : a+b, add)
print(ans)
lst = [1, 2, 3, 4, 5]
multi = reduce(lambda a,b : a*b, lst)
print(multi)
T = [100, 22, 40, 23, 20, 126]
max = reduce(lambda a,b : a if a>b else b, T)
print(max)

#Practise combos
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x : x%2 == 0, nums))
squares = list(map(lambda y : y*y, even))
print(squares)

from functools import reduce
num = [3, 6, 8, 10, 15, 21, 28]
by3 = list(filter(lambda x : x%3 == 0, num))
sums = reduce(lambda a,b : a+b, by3)
print(sums)

from functools import reduce
lst = [1, 2, 3, 4]
double = list(map(lambda a : a*2, lst))
product = reduce(lambda a,b : a*b, double)
print(product)

from functools import reduce
l = [5, 12, 17, 18, 24, 32]
even1 = list(filter(lambda x : x%2 == 0, l))
cubes = list(map(lambda y : y**3, even1))
sum1 = reduce(lambda a,b : a+b, cubes)
print(sum1)