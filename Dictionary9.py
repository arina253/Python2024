info = ["arina","joshi",34, 56]  #.....information is not clear.
print(type (info))

info2 = {
    "firstName" : "arina",
    "lastName" : "joshi",
    "age" : 34,
    "rollNo" : 56
}
print(type(info2))

# retrieve
print (info2['firstName'])

# update
info2['firstName'] = "sita"
print(info2)

#add
info2['city'] = "pune"
print(info2)

#delete
info2.pop('firstName')
print(info2)

#in
print("firstName" in info2)

# Program 1

vehicle = {
    'color' : "red",
    'type' : 'sedane'
}

print(vehicle)
print(len(vehicle))

print("hello")
print(vehicle['color'])
q1 = vehicle.get('color')
print(q1)


# Program 2

vehicle = {
    'color' : 'blue',
    'type' : 'sedane'
}

#vehicle.clear()         #{}
print(type(vehicle))
print(vehicle)

# del vehicle
# print(vehicle2)

#vehicle.pop('color')
# popitem()
e = vehicle.popitem()
print (e)
print(vehicle)

# Program 3

animals = {
    "legs" : 4,
    "color" : "black"
}

# update()
animals.update({"cityFound" : "chandrapur"})
print(animals)


# Program 4

info3 = {
    'firstName' : "arina",
    'lastName' : "joshi",
    'rollNo' : 23,
    'age': 38
}

for key in info3.keys():
    print(key)

for val in info3.values():
    print(val)    

for k,v in info3.items():
    print(k,v)    

print(info3['firstName'])    
for x in info3:
    print(x,info3[x])
