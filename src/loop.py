#For loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == 'banana':
        break  

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == 'banana':
        break  
    print(x) 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#range
for x in range(10):
   print(x)

for x in range(2, 10):
   print(x)

for x in range(2, 10, 2):
   print(x)

#Else with for
for x in range(6):
    print(x)    
else:
   print("Nothing")

for x in range(6):
  if x == 3: 
    break
  print(x)
else:
  print("Finally finished!")

#Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

count = 5
for i in range(count):
   print(f"Countdown: {count}")
   count -= 1
print("Blastoff!")

#While loop
i = 1
while(i < 6):
   print(i)
   i += 1  

i = 1
while i < 5:
   print(i)
   i += 1
   if i == 3:
      break

i = 0
while i < 5:
   i += 1
   if i == 3:
      continue    
   print(i)

items = []
while True:
   item = input("Enter the item (or done to finish): ")
   if item.lower() == 'done':
      break
   items.append(item)
print("You ordered ", items)


correct_pin = '7869'
entered_pin = ''
while entered_pin != correct_pin:
   entered_pin = input("Enter you pin: ")
print("Access enabled")

