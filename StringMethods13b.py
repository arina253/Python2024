# REVISION

first_name = "Suraj"

print(first_name.upper())
print(first_name.lower())
print(first_name.isupper())
print(first_name.islower())

# Program 2
first_name = " sachin "
print(len(first_name))
print(len(first_name.rstrip()))
print(len(first_name.lstrip()))
print(len(first_name.strip()))


# Program 3
last_name = "shrestha"
print(last_name.startswith("s"))
print(last_name.startswith("sh"))

print(last_name.endswith('a'))
print(last_name.endswith('nh'))


# Program 4
marks = "123"
print(marks.isdigit())       # 0-9
print(marks.isalpha())       # A-Z     a-z
print(marks.isalnum())       # do not allow special characters
print(type(marks))


# Program 5
# isspace()----Return True if the string is a whitespace string, False otherwise.
full_name = " a"
e3 = full_name.isspace()
print(e3)


# Program 6
# capitalize()----make the first character have upper case and the rest lower case.
firstN = "arina"
e4 = firstN.capitalize()
print(e4)


# istitle()---Return True if the string is a title-cased string, False otherwise.
e4 = "I Am Learning Javascript"
print(e4.istitle())


# Program 7
# join()
info = ["arina","joshi", "9803753479"]
e5 = "@".join(info)
print(e5)


# Program 8
# split()
email = "arina@gmail.com"
e6 = email.split('@')      # info = ["arina","joshi", "9803753479"]
print(e6)


# Program 9
# find()
emailaddress = "chinmaya"
print(emailaddress.find('a',6))    #7   
#firstargument=first occurence, secondarg = afterindex
print(emailaddress.find('a',8))      #-1


## Program 10
# removeprefix()
email2 = "gmail.com@arina"
email3 = "gmail.com@sachin"
email4 = "gmail.com@samay"

print(email4.removeprefix('gmail.com@'))

# Print output as ["arina", "sachin", "samay"]

students = [email2,email3,email4]
lista = []
for x in students:
     # print(x)
   q1 =  x.removeprefix("gmail.com@")
   lista.append(q1)
   print(lista)


# Program 11
# removesuffix()
   students = {
      "1" : "chinmayadmin",
      "2" : "poorvaceo",
      "3" : "shamcustomer",
      "4" : "nirnaymanager"
   }

   roles = ["admin","ceo","customer","manager"]
   names = []

   # Print names = ["chinmay","poorva","sham","nirnay"]
   for name in students.values():
      #print(name)
      for role in roles:
         if role in name:
            q2 = name.removesuffix(role)
            names.append(q2)
            print(names)


# Program 12            
# swapcase() ---- change upper case to lowercase and lowercase to uppercase
            a = "hello"
            print(a.swapcase())


# Program 13            
# zfill() ---- filled with zero
            name = "arina"
            name2  = "sachin"

            print(name.zfill(10))            #00000arina
            print(name2.zfill(10))            