x = 10
print (x)

#list
#           0       1       2       3
names = ["arina","sachin","jyoti","roshini"]
print(names)
print(names[3])

#list stores the value by index
city = ["newroad","yetkha","sanepa","naradevi"]
print(city[2])


#Number of element in the list
#Program 1
fruits = ["apple", "mango", "banana", "grapes"]
print (len(fruits))

#Program 2
#How to update the value in the list
animals = ["tiger","lion","cat","dog","rat"]
animals[0] = "snake"
print(animals)

#Program 3
#           0          1     2      3       4
country = ["nepal","india","usa","italy","china"]

# for loop
# for loop with range()
# while loop

for x in range(5):
    #print(x)
    print(country[x])

    # x = 0
    # x = 1
    # x = 2
    # x = 3
    # x = 4

    # Program 4
    # Print in reverse
    country2 = ["india","japan","mauritius","mexico","portugal"]
    for y in range (len(country2)-1,-1,-1):
        #print(y)
        print(country2[y])

     # Program 5  

        city = ["pune", "hyderabad", "mysore", "delhi"] 
        for item in city :
            print(item)

    # Program 6
    # while loop
            
       #           0      1         2       3
    flowers = ["rose","tulip","marigold","lily"]      
    print(flowers)     

    i1 = 0
    while (i1 < len(flowers)):
        #print (i1) 
        print (flowers[i1]) 
        i1 = i1 + 1         

    i2 = len (flowers)-1
    while (i2 >= 0):
        print(flowers[i2])    
        i2 = i2 -1  
        

    # Program 6
    # Check if any element is present in the list??

    names = ["arina", "sony", "sachin","esha"]  
    print ("esha" in names)       