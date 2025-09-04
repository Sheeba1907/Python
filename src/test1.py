x = "He is 'Johny'"
print(x)

#String indexing
a = "Hello"
print(a[2])

#Looping through strings
for x in 'banana':
    print(x)              #Can add end after x to avoid new line

#check string
txt = "The best things in life are free!"
if 'free' in txt:
    print('Yes')

txt = "The best things in life are free!"
if 'yes' not in txt:
    print('Yes')

#Slicing
b = "Hello"
print(b[2:4])
print(b[:3])
print(b[2:])

#Negative indexing
c = 'banana'
print(c[-5:-2])

#Modify strings
t = " Palindrome"
print(t.upper())
print(t.lower())
print(t.strip())
print(t.replace("P", "p"))
print(t.split("|"))

#Concatenation
a = "Python"
b = "is"
c = "good"
print(a+b+c)

#Formatting
age = 35
print(f"John and I am {age} years old  ")

#Evaluate using bool
print(bool("Hello"))
print(bool(15))
print(bool(""))
print(bool(" "))
print(bool(0))
print(bool(None))
print(bool([]))
print(bool(()))

x = 200
print(isinstance(x, int))
