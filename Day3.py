# Conditional statements - one input and multiple outcome

# if condition:
# statements

# Program 1
# if numT > 0 and numT <= 5 -------10% discount
# if numT > 5 and numT <= 10 ------20% discount
# if numT > 10 --------------------30% discount

numT = 8

if numT > 0 and numT <= 5:
    print ("10% discount")

if numT > 5 and numT <= 10:
    print ("20% discount")

if numT > 10:
    print ("30% discount")  


# Program 2

if numT > 0 and numT <= 5:
    print("10% discount")

elif numT > 5 and numT <= 10:
    print ("20% discount")

elif numT > 10:
    print ("30% discount")
else:
    print ("incorrect input")   

# Program 3

marks = 95

if marks > 90:
    print ("Grade A")
if marks >= 75:
    print ("Grade B")
if marks >= 65:
    print ("Grade C")  

#Program 4

if marks > 90:
    print ("Grade A")
elif marks >=75:
    print ("Grade B")
elif marks >= 65:
    print("Grade C")
else:
    print("try again ....!")   


# Program 5

a = 10
b = 5
if a > b:
    print ("a is greater")
else :
    print ("b is greater")

#Program 6

x1 = 100
x2 = 200
x3 = 300

if x1 > x2 and x1 > x3:
    print ("x1 is greater")
elif x2 > x1 and x2 > x3:
    print ("x2 is greater")
else:
    print ("x3 is greater")

# if will check all the conditions even if the first condition is true.
# if elif will not check other conditions if the first condition is true.        
      

          
