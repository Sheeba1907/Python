class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person("Sheeba",19)
print(p1.name)
print(p1.age)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
p1 = Person("Sheeba",19)
p1.age = 20
print(p1)

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        return f"Hello {self.firstname} {self.lastname}"
p1 = Person("Sheeba","doll")
print(p1.printname())

#Inheritance
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        return f"Hello {self.firstname} {self.lastname}"
class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.year = year
    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} of {self.year}")
p1 = Student("Sheeba","doll", 2018)
p1.welcome()

class Bike:
    def __init__(self,model,year):
        self.model = model
        self.year = year
class Splendor(Bike):
    def __init__(self,model,year,color):
        super().__init__(model,year)
        self.color = color
    def speed(self):
        print(self.color, self.model, "released in the year", self.year, "runs at 50kmhr")
p1 = Splendor("Hero Splendor Plus", 2009, "Black")
p1.speed()

class Animal:
    def speak(self):
        print("This is an animal")
class Dog(Animal):
    def speak(self):
        print("Woof!")
a = Animal()
d = Dog()
a.speak()
d.speak()

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id
class GraduateStudent(student):
    def __init__(self,name,age,student_id,degree):
        super().__init__(name,age,student_id)
        self.degree = degree     
    def greeting(self):
        print(self.name, "of", (self.age), "holding student ID number", self.student_id, "is from", self.degree)
g = GraduateStudent("Sheeba", 25, 1802211, "ECE")
g.greeting()

#Polymorphism
class Apple:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def taste(self):
        print("All apples are not sweet everytime")
class Mango:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def taste(self):
        print("Mangoes are loved by eveyone even if it's not sweet everytime")
class Grapes:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def taste(self):
        print("Grapes are sweet sometimes")
a = Apple("Apple","Red")
m = Mango("Mango","Yellow")
g = Grapes("Grapes","Green")
for i in (a,m,g):
    i.taste()
    
class Vehicle:
    def travel_time(self,distance):
        speed = 0
        return distance/speed
class Car(Vehicle):
    def travel_time(self,distance):
        speed = 60
        return distance/speed
class Train(Vehicle):
    def travel_time(self,distance):
        speed = 120
        return distance/speed
class Plane(Vehicle):
    def travel_time(self,distance):
        speed = 600
        return distance/speed
c = Car()
t = Train()
p = Plane()
distance = 300
for i in (c,t,p):
    print(f"{i.__class__.__name__} will take {i.travel_time(distance)} hours")

#Method overriding
class number:
    def add(self,a,b):
        print(a+b)
class number1(number):
    def add(self,a,b):
        print(a*b)
n = number()
n1 = number1()
n.add(4,5)
n1.add(2,5)

#Encapsulation
class bankaccount:
    def __init__(self,opening_bal = float):
        self.__balance = float(opening_bal)
    def deposit(self,amount = float):
        if amount<=0:
            raise ValueError("Deposit should not be negative")
        self.__balance += amount
    def withdraw(self,amount = float):
        if amount<=0:
            raise ValueError("Witdrawal should be positive")
        elif amount>self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
    def balance(self):
        return self.__balance
acct = bankaccount(1000.26)
acct.deposit(400)
acct.withdraw(100)
print(acct.balance())
#print(acct.__balance)