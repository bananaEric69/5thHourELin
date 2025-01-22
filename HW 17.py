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

#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def coin_flip():
    global heads
    global tails

while not 100:
    coin = random.randint(1, 101)
    print(coin)
    heads += 1
    tails += 1





coin_flip()

#4. Call the "Hello world" and "Coin Flip" functions here

#5. Print the final result of heads and tails here