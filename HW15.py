#Name: Eric Lin
#Class: 5th Hour
#Assignment: HW15
import random


#1. Create a def function that prints out "Hello World!"

def hello_world():
    print("Hello world")


#2. Create a def function that calculates the average of three numbers.
def calculate(a, b, c):
    print(a + b + c / 2)



#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animal(*creature):
    print("The Third animal is", creature[2])


#4. Create a def function that loops from 1 to the number put in the argument.
def number(x):
    for x in range(1, x + 1):
        print(x)






#5. Call all of the functions created in 1 - 4 with relevant arguments
hello_world()
calculate(24, 12, 4)
animal("Zebra","Lion","Flamingo","Monkey","Hippo")
number(x = int(input("Please enter number")))