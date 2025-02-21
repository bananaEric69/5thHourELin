#Name:Eric Lin
#Class: 5th Hour
#Assignment: HW20
#from multiprocessing.managers import Value
from logging import raiseExceptions
from multiprocessing.managers import Value
from sys import prefix, excepthook
from traceback import print_tb

#1. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.

try:
    print(x)
except:
    print("Hello world")

#2. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    y = int(input())
    print(100/y)
except ZeroDivisionError:
    print("cant divide by zero")



#3. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.


try:
    z = int(input())
    print(z)
except ValueError:
    print("Not a integer")






#4. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.

i = 5
while i >= 0:
    print(i)
    i -= 1
    if i < 0:
        raise Exception("Cannot go below 0")




