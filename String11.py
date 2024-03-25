x = 10
print(x)

# String

first_name = "arina"
print(type(first_name))         #<class 'str'>


last_name = "joshi"
print(type(last_name))


middle_name = """shirish"""
print(type(middle_name))


info = ''' I am learning javascript '''
print(info)

#Program 2
city = "pune"
# 0  1  2  3
# p  u  n  e
print(city[0])
print (city[1])
#print(city[5])      IndexError: string index out of range


#Program 3
city4 = "chandrapur"
# 0   1  2  3  4  5  6  7  8  9
# c   h  a  n  d  r  a  p  u  r
#-10 -9 -8 -7 -6 -5 -4 -3 -2 -1

#string[startIndex:EndIndex(not included):stepSize]

e1 = city4[5::]
print(e1)          #rapur

e2 = city4[-7::]
print(e2)          #ndrapur

e3 = city4[1:7:]
print(e3)          #handra

e4 = city4[1:-2:]
print(e4)          #handrap

e5 = city4[-7:-2:]
print(e5)          #ndrap

e6 = city4[-7:9:]
print(e6)          #ndrapu

e7 = city4[0:10:3]
print(e7)         #cnar

e8 = city4[::-1]
print(e8)         #rupardnahc


#e9 = city4[-1:-4]
#print(e9)

#Program 4
#upper()
city = "nagpur"
e9 = city.upper()
print(e9)

#Program 5
# lower()
city2 = "Kathmandu"
e10 = city2.lower()
print(e10)

#Program 6
#count()
city3 = "chandrapur"
e11 = city3.count('a')
print(e11)

