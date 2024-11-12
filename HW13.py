#Name:Eric Lin
#Class: 5th Hour
#Assignment: HW13


#1. Create a list containing 10 integers of your choice.
numList = {2, 5, 10, 11, 18, 23, 20, 35, 46, 53,}
#2. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = {}

oddNumbers = {}
#3. Make a loop that counts the number of even and odd numbers in the list.
#(HINT: The way to see if a number is even is if it is divisible by 2).
for numList in numList:
   if numList % 2 == 0:
    print(numList)
# Print the total count of even and odd numbers.
