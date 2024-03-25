# Program 1
names = ["ari","ram","sam","hari"]
print(names)


# Program 2
info = {
    "firstName" : "ari",
    "lastName" : "joshi",
    "rollNo" : 12,
    "age" : 12
}

# Program 3
numbers = (11,22,33,44)
print(numbers)

# Program 4
# Program 2
info = {
    "firstName" : "ari",
    "lastName" : "joshi",
    "rollNo" : 12,
    "age" : 12
}
print(info)
lastName = "shrestha"
print(lastName)
print(info)


# Set
# Store unique values
# Set is defined in curly braces
# Doesn't allow duplicate values.
# Insertion order is not maintained.
# Does not store the value by index.
# Cannot update the value
# As it doesn't store the value by index, we cannot use loop by range but can use a simple for loop

setA = {11,22,33,44}
print(type(setA))           # <class 'set'>


# Set do not allow duplicate values
# Insertion order is not maintained.
setB = {11,22,33,44,44,55,55}
print(setB)
print(len(setB))


# Set do not store the value by index
 # print(setB[0])

# As it doesn't store the value by index, we cannot use loop by range but can use a simple for loop
for i in setB:
    print(i)


# Program 2
# add()
    setC = {11,22,33,44,55}
    setC.add(66)  
    print(setC)  

    # pop()
    setC.pop()
    print(setC)

    # remove()
    setC.remove(22)
    print(setC)