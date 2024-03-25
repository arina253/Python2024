# Single inheritance

class Father:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)  

class Son(Father):
    def __init__(self,fn,ln,sn):
       super(). __init__(fn,ln)
       self.sonName = sn

    def displaySName(self):
        print(self.sonName + self.lastName) 

niresh = Son("ramesh","maskey","niresh")
print(niresh.firstName)
print(niresh.lastName)
niresh.displayName()
niresh.displaySName()


# Multilevel Inheritance

class GrandFather:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayGName(self):
        print(self.firstName + " " + self.lastName)  

class Father(GrandFather):
    def __init__(self,fn,ln,ffn):
        super(). __init__(fn,ln)
        self.fatherName = ffn

    def displayFName(self):
        print(self.fatherName + " " + self.lastName) 

class Son(Father):
    def __init__(self,fn,ln,ffn,ssn):
        super().__init__(fn,ln,ffn)  
        self.sonName = ssn

    def displaySName(self):
        print(self.sonName + " " + self.lastName)

sri = Son("hari","shrestha","sachin","sri")        

print(sri.firstName)     
print(sri.lastName)   
print(sri.fatherName)
print(sri.sonName)   

sri.displayGName()
sri.displayFName()
sri.displaySName()


# Hierarchial Inheritance

class Mother:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayMName(self):  
        print(self.firstName + " " + self.lastName)  

class Son(Mother):
    def __init__(self,fn,ln,sfn):
        super(). __init__(fn,ln)
        self.sonName = sfn

    def displaySonName(self):
        print(self.sonName + " " + self.lastName)

class Daughter(Mother):
    def __init__(self,fn,ln,ddn):
        super().__init__(fn,ln)
        self.daughterName = ddn

    def displayDName(self):
        print(self.daughterName + " " + self.lastName)

keerti = Daughter("jyoti","pradhan","keerti")
print(keerti.firstName)
print(keerti.lastName)
print(keerti.daughterName)

keerti.displayMName()
keerti.displayDName()

nivish = Son ("roshini","amatya","nivish")
print(nivish.firstName)
print(nivish.lastName)
print(nivish.sonName)

nivish.displayMName()
nivish.displaySonName()



                 