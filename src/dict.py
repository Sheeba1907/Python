D = {"brand": "Ford", "year": 1996, "model": "SUV"}
print(D)

D = {"brand": "Ford", "year": 1996, "model": "SUV"}
print(len(D))

D = dict(brand= "Ford", year= 1996, model= "SUV")
print(D)

D = {"brand": "Ford", "year": 1996, "model": "SUV"}
x = D.get("brand")
y = D.keys()
z = D.values()
a = D.items()
print(x)
print(y)
print(z)
print(a)

D = {"brand": "Ford", "year": 1996, "model": "SUV"}
if "model" in D:
    print("YES")

D = {"brand": "Ford", "year": 1996, "model": "SUV"}
D["year"] = 1997
print(D)
D = {"brand": "Ford", "year": 1996, "model": "SUV"}
D.update({"year": 1998})
print(D)

D = {"brand": "Ford", "year": 1996, "model": "SUV"}
D["color"] = "Black"
print(D)
D = {"brand": "Ford", "year": 1996, "model": "SUV"}
D.update({"color": "Black"})
print(D)

D = {"brand": "Ford", "year": 1996, "model": "SUV", "color": "Black"}
D.pop("color")
print(D)
D = {"brand": "Ford", "year": 1996, "model": "SUV", "color": "Black"}
D.popitem()
print(D)

D = {"brand": "Ford", "year": 1996, "model": "SUV"}
for x in D:
    print(x)

D = {"brand": "Ford", "year": 1996, "model": "SUV"}
for x,y in D.items():
    print(x,y)

D = {"brand": "Ford", "year": 1996, "model": "SUV"}
M = D.copy()
print(M)