#Name:Eric Lin
#Class: 5th Hour
#Assignment: HW11

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)

i = 1
while i <= 100:

    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")

    elif i % 3 == 0:
        print("fizz")

    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

    i += 1