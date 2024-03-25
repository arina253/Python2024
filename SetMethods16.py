# Set Methods

# union()
setA = {1,2,3}
setB = {11,22,33}
setC = setA.union(setB)
print(setC)

#intersection()
setE ={11,33,44}
setF = {44,55,66}
setG = setE.intersection(setF)
print(setG)

# intersection_update()
#setE.intersection_update(setF)
#print(setE)     # {44}
setF.intersection_update(setE)
print(setF)       # {44}


# Program 2 
# symmetric_difference()
# symmetric_difference_update()

setQ = {11,22,33}
setE = {45,66,77,33}

setR = setQ.symmetric_difference(setE)
print(setR)       # 66, 11, 45, 77, 22}
setQ.symmetric_difference_update(setE)
print(setQ)       # {66, 11, 45, 77, 22}
print(setE)


# Program 3
# difference()
# difference_update()
setQ = {11,22,33}
setE = {45,66,77,33}

setW = setQ.difference(setE)      #{11, 22}
print(setW)
setQ.difference_update(setE)
print(setQ)                       # {11, 22}

setE.difference_update(setQ)
print(setQ)


# Program 4
# issubset()
# issuperset()
setQ = {11,22,33}
setE = {11,22,33,44}
q = setQ.issubset(setE)
q2 = setE.issuperset(setQ)
print(q)
print(q2)

# isdisjoint()
setQ = {11,22,33,44,88}
setF = {55,66,77,88}
e = setQ.isdisjoint(setF)
print(e)


# Program 5

# add()
setW = {11,22,33,44}
setW.add(55)
print(setW)

# clear()
# setW.clear()
 # print(setW)      #set()

# pop()
# remove()
setW.pop()
print(setW)
setW.remove(44)
print(setW)

# update()
setW.update({5,6,7,8,3})
print(setW)

# discard()
r = setW.discard(58)
print(setW)