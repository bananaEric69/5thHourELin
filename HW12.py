#Name:Eric
#Class: 5th Hour
#Assignment: HW12

import time

#1. Create a for loop with variable i that counts down from 5 to 1
#and then prints "Hello World!" at the end.
"""
for h in range  (5,0,-1):
    time.sleep(0.4)
    print(h)
else:
    print("HELLO WORLD!!!!!")
   
#2. Create a for loop that counts up and prints only even numbers
#between 1 and 30.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)

for i in range (0,31,2):
    time.sleep(0.4)
    print(i)

#3. Create a for loop that prints 5 different animals from a list.
animal = ["Tiger", "Lion", "Turtle", "Fish", "Fox"]
for i in animal:
    print(i)
    """
#4. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")

e = input("Please enter a word")[::-1]
for e in e:
    print(e)