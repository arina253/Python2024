# Collection

# names = ["ram","sam","hari"]

# info = {
# "firstName" : "hari",
# "lastName" : "joshi"
# }

# tupleA = (22,33,44)

# set = {11,22,33,55,66,77}

# firstName = "arina"

# CRUD operation
# Methods
# Loop
# element present,duplicates



class Person:
    first_name = "arina"
    last_name = "joshi"

    # instance methods
    def walk(self):
        print("I am walking")

    def talk(self):
        print("I am talking")

# Instantiation and method calls should be outside the class definition

arina = Person()
print(arina.first_name)
print(arina.last_name)
arina.walk()
arina.talk()

amol = Person()
print(amol.first_name)
print(amol.last_name)
amol.walk()
amol.talk()

amol.first_name = "amol"
amol.last_name = "rao"

print(amol.first_name)
print(amol.last_name)

# Program 2

class PersonB:
    # constructor
    def __init__(self,fn,ln):
        self.first_name = fn
        self.last_name = ln

        def talk(self):
            print("I am talking")

        def walk(self):
            print("I am walking")

# # Instantiation and method calls should be outside the class definition

amol = PersonB("amol","rao")
arina = PersonB("arina","joshi")

print(amol.first_name)
print(amol.last_name)

print(arina.first_name)
print(arina.last_name)

arina.city = "kathmandu"
print(arina.city)
# print(amol.city)

# Assignment
class Vehicle:
    def __init__(self,ty,mo):
        self.type = ty
        self.model = mo

    def start(self):
        print("Car can start")    

    def stop(self):
        print("Car can stop")

Toyota = Vehicle("sedane","toyota") 
Honda = Vehicle("SUV","honda")     

print(Toyota.type)
print(Toyota.model)
Toyota.start()
Toyota.stop()

print(Honda.type)
print(Honda.model)
Honda.start()
Honda.stop()

    
                           


