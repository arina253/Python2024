info3 = {
    "firstName": "ram",
    "lastName": "joshi",
    "rollNo" : 34,
    "age" : 40
}

print (info3['firstName'])
print(info3.get('firstName'))

y = info3.setdefault('city', 'pune')
print(y)
print(info3)

#info4 = dict.fromkeys(["keyone","keytwo","keythree"])
#print(info4)


# Program 1

students = [
{ "firstName" : "ram",
  "lastName" : "deshpande",
   "age": 34,
   "skills": ["html","css","js"]
},

{
"firstName" : "raj",
"lastName" : "joshi",
"age": 32,
"skills": ["html","css","js","python"]
},

{
"firstName" : "ramita",
"lastName" : "rao",
"age": 24,
"skills": ["html","css","js"]
}]

print(students)

print(type(students))

print(students[2]['firstName'])


# Print firstname only
for x in students:
    print(x['firstName'])


# Print user with python skills
    for x in students:
        print(x['skills']) 
        if "python" in x["skills"]:
            print(x['firstName'])  


# Print user with python skills and age > 30
            for x in students:
                if x['age'] > 30 and "python" in x['skills']:
                    print(x['firstName'], x['age'],x["skills"])


#   Print name and number of skills
                    for x in students:
                        print(x['firstName'] + ":" + str(len(x['skills'])))    # converted integer to string str


#  Print average age of all the students

total = 0
for x in students:
 total = total + x['age']
print(total/len(students))