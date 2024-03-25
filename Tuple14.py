# Tuple - Defined in round bracket

# Python Datatypes: String, List , Dictionary

str = "amol"
print(str)
print(type(str))

names = ["arina","jyoti","sony"]
print(names)
print(type(names))

info = {
    "firstName" : "arina",
    "lastName" : "joshi"
}
print(info)
print(type(info))


# Program 2
# We cannot update the value of tuple.
flowers = ["lily","lotus","rose"]
flowersB = ("lily","lotus","rose")
print(type(flowersB))       #<class 'tuple'>
#flowersB[1] = "sunflower"
print(flowersB)


# Program 3
# Tuple is fixed. Tuple stores the value by index
tupleA = ("A","B","C")
print(tupleA)
print(type(tupleA))
print(tupleA[0])


# for with range
for x in range(3):
   # print(x)
    print(tupleA[x])

# for without range
    for item in tupleA:
        print(item)    

# while loop
        i=0
        while(i<3):
            print(tupleA[i])       #A #B #C 
            i=i+1                  #1 #2 #3


# Program 4
        tupleB = 12,23
        print(type(tupleB))
        #tupleB[0]=88

        tupleC = (11,22,33)
        a,b,c = tupleC
        print(a)
        print(b)
        print(c)


# Program 5
# We cannot update the value of tuple.
# Unpacking: Converting tuple to list to add value and converting back to tuple.
        tupleF = (11,22,33)
        len(tupleF)
        e = list(tupleF)
        print(e)
        e.append(44)
        e = tuple(e)
        print(e)


# Program 6
        d = (11,22,33,44,44)
        print(d)
        e2 = d.count(44)
        print(e2)

        e3 = d.index(22)
        print(e3)
        print(33 in d)


# how to create tuple with constructor
        e4 = ([11,22,33], [33,44,55],[55,66,77])        

