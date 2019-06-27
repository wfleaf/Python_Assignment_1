# This program will display the message 'Welcome to Python' 5 times

'''
print ("Welcome to Python")
print ("Welcome to Python")
print ("Welcome to Python")
print ("Welcome to Python")
print ("Welcome to Python")
'''

# Assign the a number to the constant called printRepeat that equals number
# the nuner of time you wish to repeat the message

'''
printRepeat = 5

for row in range (printRepeat):
    print ("Welcome to Python")
    printRepeat -=1
'''

# This version allows the user to input the number of times to print the message

printRepeat = int (input ("How many times should I repeat the the message: "))

for row in range (printRepeat):
    print ("Welcome to Python")
    printRepeat -=1
