
# Program 1
# Method 1
lst = [1989,1990,1991,1992]
ages = []

for i in lst:
    x = 2024 - i
    ages.append(x)
    print(ages)

# Method 2
a = list(map(lambda x:2024-x,lst))    
print(a)

# Method 3 
# Using list comprehension
print([2024-i for i in lst])



# Program 2
f = lambda x : 2024-x
f(lst[0])


# Program 3
names = ["arina","roshini","sony","hari"]
above5 = []
for x in names:
    if len(x) > 5:
        above5.append(x)
        print(above5)

# By using list comprehension
print ([x for x in names if len(x) > 5])    
e = list(filter(lambda x : len(x) > 5, names)) 
print(e)  


# Program 3
d = [34,23,-33,-56,444,400,-900]
transactions = []

for x in d:
    if x < 0:
        #print("withdrawl")
        transactions.append("withdraw")
    else:
        transactions.append("deposit")
print(transactions)     


# Using list comprehension and ternary operator

print(["withdrawl" if x < 0 else "deposit"  for x in d])
print (list(filter(lambda x : x > 0, d)))
print(list(filter(lambda x : x < 0 , d)))


# decorator , recursive function , generators , modules-------remaining