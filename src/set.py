# Creating a set
S = set((1, 2, 3))
print(S)

# Access items
S = {1, 2, 3, 4, 5}
for i in S:
    print(i)

# Check if item exists
S = {1, 2, 3, 4, 5}
print(3 in S)

# Add items
S = {1, 2, 3, 4, 5}
S.add(6)
print(S)

# Add multiple items
S = {1, 2, 3}
T = {4, 5, 6}
S.update(T) 

#set also accepts lists and tuples  
S = {1, 2, 3}
R = [4, 5, 6]
S.update(R)
print(S)

# Remove items
S = {1, 2, 3, 4, 5}
S.remove(3) 
print(S)

#discard
S = {1, 2, 3, 4, 5}
S.discard(3)
print(S)

#pop
S = {1, 2, 3, 4, 5}
S.pop() 
print(S)

#Loop through a set
S = {1, 2, 3, 4, 5}
L = list(S)
i = 0
for i in range(len(L)):
    print(L[i]) 
    i += 1

#join two sets
#Union
S1 = {1, 2, 3}  
S2 = {4, 5, 6}
S3 = S1.union(S2)   
print(S3)

#Update
S1 = {1, 2, 3}
S2 = {4, 5, 6}
S1.update(S2)   
print(S1)

#Intersection
S1 = {1, 2, 3, 4}
S2 = {3, 4, 5, 6}
S3 = S1.intersection(S2)
print(S3)

#difference
S1 = {1, 2, 3, 4}
S2 = {3, 4, 5, 6}
S3 = S1.difference(S2)
print(S3)

#symmetric difference
S1 = {1, 2, 3, 4}
S2 = {3, 4, 5, 6}
S3 = S1.symmetric_difference(S2)
print(S3)

#subset
S1 = {1, 2, 3}
S2 = {1, 2, 3, 4, 5}    
print(S1.issubset(S2))

#superset
S1 = {1, 2, 3, 4, 5}
S2 = {1, 2, 3}
print(S1.issuperset(S2))

#disjoint
S1 = {1, 2, 3}
S2 = {4, 5, 6}
print(S1.isdisjoint(S2))
S3 = {1, 2, 3}
print(S1.isdisjoint(S3))

#copy
S1 = {1, 2, 3}  
S2 = S1.copy()  
print(S2)

#clear
S = {1, 2, 3, 4, 5} 
S.clear()
print(S)    

#frozenset
S = frozenset((1, 2, 3, 4, 5))
print(S)    