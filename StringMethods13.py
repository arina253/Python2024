# Program 1
# upper()
first_name = "arina"
print(len(first_name))
e = first_name.upper()
print(e)


# lower()
last_name = "joshi"
e2 = last_name.lower()
print(e2)

# isupper()
middle_name = "GREAT"
e3 = middle_name.isupper()
print(e3)
# checks if all characters in the string "GREAT" are uppercase and prints True because they are.

# islower()
e4 = e2.islower()
print(e4)

# lower(),upper(),islower(),isupper()


# Program 2

# staryswith()
city = "pune"
e5 = city.startswith ("pu")
e6 = city.startswith("P")
print(e5)
print(e6)

# endswith()
e7 = city.endswith('e')
e8 = city.endswith('une')
print(e7)
print(e8)

# count()
city2 = "kathmandu"
e9 = city2.count('a')
print(e9)


# Program 3

# lstrip() - remove front space
city3 = " wardha"
print(len(city3))
e10 = city3.lstrip()
print(e10)
print(len(e10))

# rstrip() - remove space from last
city4 = " wardha "
print(len(city4))
e11 = city4.rstrip()
print(len(e11))

# strip() - remove space from front and back
city5 = " wardha "
e12 = city5.strip()
print(len(e12))


# Program 3
# replace()-------will not change original string
info = "I am learning javascript"
e13 = info.replace("javascript","python")
print(e13)
print(info)


# Program 4
e14 = "123".isdigit()  # 0-9
print(e14)                # True

e15 = "123#"
e16 = e15.isalpha()
print(e16)                # False

e17 = e15.isalnum()
print(e17)                # False