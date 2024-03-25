# Inheritance

# Program 1
# Single Inheritance
# Parent constructor, Child - no constructor

class Student:
    def __init__(self,fn,ln,adharNo):
        self.firstName = fn
        self.lastName = ln
        self.adharNo = adharNo

    def displayName(self):
        print(self.firstName + self.lastName)    

arina = Student("arina", "joshi", 2345) 
print(arina.firstName)
print(arina.lastName)
print(arina.adharNo)       
arina.displayName()

class Teacher(Student):
    salary = 500000
    def displaySalary(self):
        print(self.salary)

arinaT = Teacher ("arinaT", "joshiT", 2345)    
print(arinaT.firstName)
print(arinaT.lastName)  
print(arinaT.adharNo)
print(arinaT.salary)  

arinaT.displayName()


# Program 2
# Single inheritance
# Parent Constructor, Child Constructor

class Student:
    def __init__(self,fn,ln,adharNo):
        self.firstName = fn
        self.lastName = ln
        self.adharNo = adharNo

    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):
    def __init__(self,fn,ln,adharNo,salary):
        super().__init__(fn,ln,adharNo)    
        self.salary = salary

    def displaySalary(self):
        print(self.salary)      

arinaT = Teacher ("arina","joshi",12345,70000)
print(arinaT.firstName)
print(arinaT.lastName)
print(arinaT.adharNo)
print(arinaT.salary)

arinaT.displayName()
arinaT.displaySalary()


# Program 3
# Multi level inheritance

class Student:
    def __init__(self,fn,ln,adharNo):
        self.firstName = fn
        self.lastName = ln
        self.adharNo = adharNo

    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):
    def __init__(self,fn,ln,adharNo,salary):
        super(). __init__(fn,ln,adharNo)
        self.salary = salary

    def displaySalary(self):
        print(self.salary)  


class Professor(Teacher): 
    def __init__(self,fn,ln,adharNo,salary,specialization):
        super(). __init__(fn,ln,adharNo,salary)  
        self.specialization = specialization

    def displaySpecialization(self):
        print(self.specialization)      

arina = Professor ("arina","joshi",12345,700000,"Micro")    
print(arina.firstName)
print(arina.lastName)
print(arina.adharNo)
print(arina.salary)
print(arina.specialization)

arina.displayName()
arina.displaySalary()
arina.displaySpecialization()
                     



    