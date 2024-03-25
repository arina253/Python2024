# Program 1

class Person:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def display_name(self):
         print(self.firstName  + self.lastName)

amol = Person ("amol","rao")
arina = Person ("arina", "joshi")
print(amol.firstName)
print(arina.firstName)
print(amol.lastName)
print(arina.lastName)
amol.display_name()
arina.display_name()


# Program 2

class Person2 :
    country = "bharat"
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    def displayName(self):
        print(self.firstName + self.lastName)

    @classmethod
    def changeCountry(cls,cnty):
        cls.country = cnty

amol = Person2("amol","rao")
arina = Person2 ("arina", "joshi")  
ninad = Person2 ("ninad","dani")

print(amol.firstName)
print(amol.lastName)
print(amol.country)
print(arina.country)

amol.country = "india"
print(amol.country)     # india
print(arina.country)    # bharat
print(ninad.country)    # bharat

Person2.changeCountry("Hindustan")
print(amol.country)      # india
print(arina.country)     # Hindustan 
print(ninad.country)     # Hindustan


# Whatever is common in all the object will be written in Class level.
# Things that are not common is written in Constructor.
# Constructor : def __init__(self,fn,ln) 
# @classMethod will be called on the name of class.mho                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      