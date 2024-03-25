 # class instance method
 # Program 1

class Person:

    # constructor
    def __init__(self,fn,ln):
        # instance variables
        self.firstName = fn
        self.lastName = ln

    # instance method
    def displayName(self):
        print(self.firstName + self.lastName)

    # Method to update last name
    def updateName(self,ln):
        self.lastName = ln

# Creating an instance 'arina' of the Person class
arina = Person("arina","joshi")
print(arina.firstName)
print(arina.lastName)
arina.displayName() 

# Updating last name
arina.updateName("shrestha")     
print(arina.lastName)  
arina.displayName()    


# class instance,class method
# Program 2

class PersonB:
    # Class attribute
    country = "India"

    # constructor
    def __init__(self,fn,ln):
        # instance variables
        self.firstName = fn
        self.lastName = ln

     # instance method
    def updateName (self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    # class method
    @classmethod
    def updateCountry(cls,cnty):
        cls.country = cnty

# Create an instance 'h'of the PersonB class
h = PersonB("Jyoti","Pradhan")   
print(h.firstName)
print(h.lastName)
print(h.country)  

h.country = "bharat"  # Create a new instance attribute 'country' specific to 'h'


# Create another instance 'h2' of the PersonB class
h2 = PersonB("Jyoti2","Pradhan2")
print(h2.country)  # Output: India (not affected by the change made to 'h')

# Update the class attribute 'country' using the class method
PersonB.updateCountry('India B')

print(h.country)   # # Output: bharat (instance attribute specific to 'h')
print(h2.country)  # Output: India B (updated because it's referencing the class attribute)


# static method
# count number of objects
# Program 3

class PersonC:
    # class attributes
    count = 0
    country = "Bharat"

   # constructor
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
        PersonC.count = PersonC.count + 1

    # instance method
    def displayName(self):
        print(self.firstName + self.lastName)   

    # class method
    @classmethod
    def updateCountry(cls,cnty):
        cls.country = cnty     


    # static method
    @staticmethod
    def countObj():
        return PersonC.count  

# Creating instances    
arina = PersonC("arina","joshi")
sachin = PersonC("sachin","shrestha")    

# Calling the static method to get the count of objects
a = PersonC.countObj()
print(a)

# Static method is called on the name of class
# Do not pass paramaeter to static()
# Use static method for constant
