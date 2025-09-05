# Creating a tuple
T = tuple(('apple', 'banana', 'cherry'))
print(T)

# Access items
T = ('apple', 'banana', 'cherry')
print(T[1])

# Change tuple values
# Tuples are immutable, so we convert to a list and back to a tuple
x = (1,2,3)
y = list(x)
y[1] = 0
x = tuple(y)        
print(x)

# Add items
T = ('apple', 'banana', 'cherry')
y = ('kiwi',)
T += y
print(T)

# Remove items
T = ('apple', 'banana', 'cherry')
y = list(T)
y.remove('banana')
T = tuple(y)
print(T)

#unpacking
fruits = ('apple', 'banana', 'cherry')  
(green, yellow, red) = fruits
print(green)    
print(yellow)
print(red)

#using asterisk* to collect remaining values
fruits = ('apple', 'banana', 'cherry', 'strawberry', 'raspberry')
(green, yellow, *red) = fruits
print(green)
print(yellow)   
print(red)

#loop through a tuple
T = ('apple', 'banana', 'cherry')   
for i in range(len(T)):
    print(T[i])

T = ('apple', 'banana', 'cherry')
i = 0
while i < len(T):
    print(T[i])
    i += 1

#join two tuples
T1 = ('a', 'b', 'c')    
T2 = (1, 2, 3)
T3 = T1 + T2
print(T3)

#multiply tuples
T = ('apple', 'banana', 'cherry')   
T2 = T * 2
print(T2)

