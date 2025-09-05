T = tuple(('apple', 'banana', 'cherry'))
print(T)

T = ('apple', 'banana', 'cherry')
print(T[1])

x = (1,2,3)
y = list(x)
y[1] = 0
x = tuple(y)        
print(x)

T = ('apple', 'banana', 'cherry')
y = ('kiwi',)
T += y
print(T)

T = ('apple', 'banana', 'cherry')
y = list(T)
y.remove('banana')
T = tuple(y)

#unpacking
fruits = ('apple', 'banana', 'cherry')  
(green, yellow, red) = fruits
print(green)    
print(yellow)
print(red)

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

