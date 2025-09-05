#List constructor
L = list((1,2,3,4))
print(L)

#change items
L = [1,2,3,4]
L[1] = 0
print(L)

#insert and append
L = [1,2,3,4]
L.insert(2, 0)
print(L)

L = [1,2,3,4]
L.append(5) 
print(L)

#exend
L = [1,2,3,4]  
L2 = [5,6,7]
L.extend(L2)    
print(L)

L = [1,2,3,4]
M = (0, 5, 6)
L.extend(M)
print(L)

#remove
L = [1,2,3,4]   
L.remove(2)
print(L)

#pop
L = [1,2,3,4]
L.pop(1)
print(L)

#clear
L = [1,2,3,4]
L.clear()
print(L)

#count
L = [1,2,3,4,2,2]
print(L.count(2))

#Loop through a list
L = [1,2,3,4]
for item in L:
    print(item) 

#list comprehension
L = [1,2,3,4]   
N = [x*2 for x in L if x%2==0]
print(N)

#list slicing
L = [1,2,3,4,5,6,7,8,9]
print(L[2:5]) 

#sorting a list
L = [5,2,9,1,5,6]
L.sort()
print(L)

L = [5,2,9,1,5,6]
L.sort(reverse=True)
print(L)

#sort using function
def func(n):
    return abs(n-50)
L = [100, 50, 65, 82, 23]
L.sort(key=func)
print(L)

L = ['Apple', 'orange', 'banana', 'Kiwi', 'Pear', 'grape']
L.sort()
print(L)  #case sensitive sorting

L = ['Apple', 'orange', 'banana', 'Kiwi', 'Pear', 'grape']
L.sort(key=str.lower)
print(L)

#copy a list
L = [1,2,3,4]
M = L.copy()
print(M)    

L = [1,2,3,4]
M = list(L) #copy using list constructor
print(M)    

#join two lists
L = [1,2,3]
M = [4,5,6]
N = L + M   
print(N)

L = [1,2,3]
M = [4,5,6]
L.extend(M) 
print(L)

L = [1,2,3]
M = [4,5,6]
for item in M:
    L.append(item)  
print(L)
