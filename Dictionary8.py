 # list

# Program 1

#          0        1        2       3         4
names = ["arina","sachin","jyoti","roshini","poorva"]

# retrieve
print(names[0])
print(names[4])

# update
names[0] = "siddhi"
print(names)

# add
names.append("santosh")
print(names)
names.insert(2,"sony")
print(names)

# delete
names.pop()
print(names)
names.pop(1)
print(names)
names.remove("jyoti")
print(names)

# in
print ("siddhi" in names)

# Program 2

# Dictionary - as document.Store key - value, also known as property value.
# Start with {} - key and value in single or double quote
# Do not store the value by index.

vehicle = {
    "color" : "red",
    "type" : 'sedane',
    "color" : "blue"
}
print (type(vehicle))         #<class 'dict'>

# len()
print(len(vehicle))

#in
print("color" in vehicle)

# duplicate values
print(vehicle)

# retrieve
vehicle ['color']
vehicle ['color'] = "red"
print(vehicle)
vehicle['regNo'] = '123'
print(vehicle)

del vehicle
# print(vehicle)