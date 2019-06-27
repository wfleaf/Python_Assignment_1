#This program will display the word FUN in a specific pattern
'''
FFFFFFF  U     U  NN   NN
FF       U     U  NNN  NN
FFFFFFF  U     U  NN N NN
FF        U   U   NN  NNN
FF         UUU    NN   NN
'''


#Printing the F
for row in range (5):
    for col in range (7):
        if (col<2)  or ((row==0) or (row==2) and col>0):
            print ("F", end='')
        else:
            print(end=" ")
    print()


#Printing the U
for row in range (5):
    for col in range (7):
        if ((col==0) or (col==6)) and (row <3):
            print ("U", end='')
        elif ((col==1) or (col==5)) and (row==3):
            print ("U", end='')
        elif ((col>1) and (col<5)) and row==4:
            print ("U", end='')
        else:
            print (end=" ")
    print()


#Print the N

for row in range (5):
    for col in range (7):
        if (col<2 or col>4) or((row==(col-1)) and (col>0 and col<5)):
            print ("N", end='')
        else:
            print (end=" ")
    print()
