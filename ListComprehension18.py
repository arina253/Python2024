
# List comprehension
# Written with []
# By default, output of list comprehension is list

lst = [1989,1990,1991,1992]
# [35,34,33,32]
ages = []
for x in lst:
    ages.append(2024-x)
    print(ages)


# Program 2
# list comprehension - [expression-loop-condition]   
    a = [2024 - x for x in lst]
    print(a)    


# Program 3
number = [1,2,3,4,5,6,7,8,9,10]
c = [ x * x for x in number]
print(c)


# Program 4
d = [x for x in number if x % 2 == 0]
print(d)


#Program 5
number = [1,2,3,4,5]
#["odd","even","odd","even","odd"]

# if multiple condition, use ternary statement in left side
e = ["even" if x % 2 == 0 else "odd" for x in number]
print(e)


# Program 6
names = ["arina","jyoti","roshini","sony","rita"]
f = ["Mr/Mrs" + x for x in names if len(x) > 5]
print(f)