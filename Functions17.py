#Functions

# int as a parameter and int as a return type
def addOne(x,y):
    return x+y
e = addOne(10,24)
print(e)


# float as a parameter and float as a return type
def subTwo(x,y):
    return x-y
f = subTwo(12.23,1.1)
print(f)


# boolean as a parameter and boolean as return type
def canDrive(age,haveVehicle):
    if age > 18 and haveVehicle:
        return True
    else:
        return False
g = canDrive (35,True)    
print(g)


# string as parameter and string as return type
def greet(name):
    return ("welcome " + name)
j = greet("arina")
print(j)


# list as parameter and list as return type
names = ["ari","sachin","ram","sam"]
def addName(lst):
    lst.append("sohan")
    return lst
k = addName(names)
print(k)


# dictionary as a parameter and dictionary as return type 

info = {
    "firstName" : "arina",
    "lastName" : "joshi"
}
def addCity(information):
    information['city'] = "kathmandu"
    return information
l = addCity(info)
print(l)


# tuple as parameter and tuple as return type

numbers = (11,22,33)
def addValue(tupA):
    # (11,22,33)
    tupA = list(tupA)   #[11,22,33]
    tupA.append(44)     #[11,22,33]
    tupA = tuple(tupA)  #[11,22,33]
    return tupA
l = addValue(numbers)
print(l)


# set as parameter and set as return type
setA = {11,22,33}
def addElement(setA):
    setA.add(44)
    return setA
z = addElement(setA)
print(z)


