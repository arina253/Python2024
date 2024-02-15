
# while loop
# initialization
# while (condition):
# statement
# increment

#Program 1
# Print 1 to 3
t1 = 1
while (t1 <= 3):
    print(t1)     # 1 #2 #3
    t1 = t1 + 1

# Program 2
# Print 1 to 5
t2 = 1
while (t2 <= 5):
    print(t2)
    t2 = t2 +1

# Program 3
# Table of 2
t3 = 2
while (t3 <= 20):
    print(t3)
    t3 = t3 + 2  

# Program 4
# Table of 5
    t4 = 50
    while (t4 >= 5):
        print(t4)
        t4 = t4 - 5 

# break statement with while loop
        
# Program 5
        t5 = 1
        while (t5 <= 5):
            if t5 == 3:
                break
            print (t5)    #1 #2
            t5 = t5 + 1   #2 #3

# Program 6
            t6 = 5  
            while t6 >= 1:
                print(t6) #5 #4 #3
                if t6 == 3:
                    break
                t6 = t6 -1  #4 #3


# while loop with continue

# Program 7
            t7 = 1
            while t7 <= 5:
                t7 = t7 + 1 #4
                if t7 == 3:
                    continue
                print(t7)    #1 #2 #4 #5
                t7 = t7 + 1  #2 #3 #5 #6  
                                



