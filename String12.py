
# String stores the value in index.
# Reverse indexing is possible in python
# Range: when working with index


# Program1

first_name = 'arina'
last_name = "joshi"
middle_name = """ great"""
info = '''
   I am learning 
'''
print(middle_name)
print(info)
print(type(info))

# Program 2

city = "chandrapur"
#print(city[startIndex:EndIndex(not included):stepSize])

print(city[1::])
print(city[2:7:])
print(city[-8:])
print(city[-8:-2])
print(city[1:-1:])
print(city[0:10:2])
print(city[-1:3])        # blank


# Program 3
# String stores the value by index.

city3 = "pune"

# p  u  n  e
# 0  1  2  3

print(city3[0])
print(city3[1])
print(city3[2])
print(city3[3])


# Print reverse
for x in range(len(city3)-1, -1,-1):
    #print(x)
    print(city3[x])


for x in range(50,4,-5):
    print(x)


city4 = "nagpur"

for x in range(len(city4)):
    print(city4[x])

for char in city4:
    print(char)


# Program 4
print("in" in "chinmay")    


# Program 5
city5 = "wardha"

# w  a  r  d  h  a
# 0  1  2  3  4  5

# Using while loop (Reverse)

i1 = 0
while (i1 < len(city5)):
    # print(i1)
    print(city5[i1])
    i1 = i1+1


i2 = len(city5)-1
while (i2 >= 0):
    print(city5[i2])
    i2 = i2 -1

# Using for loop (Forward)
    for x in city5:
        print(x)    

    for x in range(0,len(city5),1):
        print(city5[x])  



