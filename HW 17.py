#Name:Eric
#Class: 5th Hour
#Assignment: HW17
import random


#1. Import the "random" library and create a def function that prints "Hello World!"
def hello():
    print("hello world!")

#2. Create two empty integer variables named "heads" and "tails"
heads = 0
tails = 0
coin = 0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def coin_flip():
    global heads
    global tails
    global coin
    global flip
    while not coin == 100:
        coin += 1
        flip = random.randint(1, 2)
        if flip == 1:
            heads += 1
        elif flip == 2:
            tails += 1



#4. Call the "Hello world" and "Coin Flip" functions here
hello()
coin_flip()
#5. Print the final result of heads and tails here
print(heads)
print(tails)