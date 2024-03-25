# loop------for loop and while loop

# for loop with range()
# for x in range (startIndex, EndIndex (not included),stepSize);
# statements
# default ----- 0 as startIndex

#Print 0 to 9
for  x in range(10):  #if startIndex is not mentioned, zero is default.
    print(x)

# Print 1 to 5
for x in range(1,6,1):
    print(x)    

# Print 2 to 9
for x in range (2,10,1):
    print(x)    

# table of 2
# 2,4,6,8,10,12,14,16,18,20
for x in range (2,21,2):
    print(x) 

#Table of 3
for x in range (3,31,3):
    print(x)   

# Table of 5 in reverse
for x in range (50,4,-5):
    print(x)     

# Table of 10 in reverse
    for x in range (100,9,-10):
        print(x) 


# break statement with for loop
        for x in range (1,6): #2,3
            if (x == 3):
                break
            print(x)      #1 #2   


        for  x in range (1,6):
            print(x)
            if x == 3:
                break  

        for x in range (30,2,-3):
            print(x)
            if x == 3:
                break     


 # continue with for loop 
        for x in range (1,6):
            if x == 3:
                continue
            print(x)  # 1,2,4,5


            for x in range (6,1,-1):
                if x == 3:
                    continue
                print(x)  # 6,5,4,2

# CTRL + C to stop loop
