
# Program 1
names = ["arina","sachin","santosh"]
names2 = names
names2[0]="raj"
print(names)
print(names2)
# names and names2 are different address but stored in the same memory.

# Program 2
#append() - add element at last

fruits = ["apple","mango","banana"]
fruits.append("grapes")
print(fruits)

# Program 3
# pop() - remove element at last
# pop (index) - remove element at specified index
# remove()

#                0        1          2       3
vegetables = ["carrot","cabbage","tomato","potato"]
vegetables.pop()
print(vegetables)
vegetables.pop(1)
print(vegetables)

vegetables.remove("tomato")
print(vegetables)

# Program 4
# clear() - clear the list
animals = ["tiger","rabbit","tiger","lion","panthar"]
#animals.clear()
#print(animals)

# Program 5
# count()
animals = ["tiger","lion","elephant","rat","tiger","lion"]
q1 = animals.count("tiger")
print(q1)

# Program 6
# reverse()
city = ["pune","nagpur","hyderabad","delhi"]
city.reverse()
print(city)

# Program 7
# insert() - add element at the specified index
#           0          1       2        3       4
country = ["nepal","india","america","china","japan"]
country.insert(2,"norway")
print(country)


# Program 8
# sort()
district = ["kathmandu","pokhara","biratnagar"]
district.sort()
print(district)

# Program 9
# copy

listA = [11,22,33]
listB = listA
listB[0] = 88
print(listB)
print(listA)

# copy will make different address and different memory.
listD = listA.copy()
listD[1] = 111
print(listD)
print(listA)

# Program 10
# extend()
listA = [11,22,33]
listA.extend([44,55,66])
print(listA)

q1 = listA.index(44)
print(q1)


