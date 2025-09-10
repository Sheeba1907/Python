'''Create a class Person with attributes name and age. Derive a class Student that adds roll_no and marks. Write methods to display details.'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def details(self):
        pass
class Student(Person):
    def __init__(self, name, age, marks, roll_no):
        super().__init__(name, age)
        self.marks = marks
        self.roll_no = roll_no
    def details(self):
        print(f"The Student {self.name} of age {self.age} with roll number {self.roll_no} has scored {self.marks} in the final examination")
p = Person("Sheeba", 25)
s = Student("Sheeba", 25, 85, 1802211)
s.details()

'''Create a class Vehicle. Derive Car from Vehicle and then ElectricCar from Car.
Each should have a method show_info() that prints relevant details.
Demonstrate method overriding.'''

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def show_info(self):
        pass
    
class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)
        self.year = year
    def show_info(self):
        print(f"The car {self.brand}'s {self.model} is from the year {self.year}")

class ElectricCar(Car):
    def __init__(self, brand, model, year, fuel):
        super().__init__(brand, model, year)
        self.fuel = fuel
    def show_info(self):
        print(f"The car {self.brand}'s {self.model} from the year {self.year} is of {self.fuel} type.")
        
c = Car("Suzuki", "S-cross", 2021)
ec = ElectricCar("Kia", "EV6", 2024, "no fuel")
c.show_info()
ec.show_info()



'''Create two classes Teacher and Athlete.
Derive a class Student from both, which can access attributes from both parents.
Show what happens if both parent classes have a method with the same name (MRO – Method Resolution Order).'''

class Teacher:
    def work(self):
        print("The teacher teaches!")
class Athelete:
    def work(self):
        print("Atheletes involve in sports")
class Student(Teacher, Athelete):
    pass

s = Student()
s.work()


'''Create a base class Animal with a method sound().
Derive Dog and Cat classes that override sound().
Call sound() from each object.'''

class Animal:
    def sound(self):
        print("Animals make sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks!")
class Cat(Animal):
    def sound(self):
        print("Cat Meows!!")
a = Animal()
d = Dog()
c = Cat()
a.sound()
d.sound()
c.sound()


'''Write a program where Employee is the parent class and Manager is the child class.
Manager should use super() to call the constructor of Employee.'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def display(self):
        print(self.name, self.salary, self.department)
        
m = Manager("John,", 45000, ",Sales")
m.display()

'''Create a base class Shape.
Derive two classes Rectangle and Circle.
Both should implement area() differently.
Demonstrate polymorphism by iterating over a list of shapes.'''

class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
    def area(self):
        return self.length * self.breadth
class Triangle(Shape):
    def __init__(self, b, h):
        self.base = b
        self.height = h
    def area(self):
        return 0.5 * self.base * self.height
        
r = Rectangle(4, 5)
t = Triangle(4, 5)

for i in r,t:
    print(i.area())