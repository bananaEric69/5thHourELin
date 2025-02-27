#Name: Eric Lin
#Class: 5th
#Assigment: Playground

import random
from traceback import print_tb

#The icon signs of the slot machine

cherry = 1
plum = 2
bells = 3
clover = 4
lemon = 5
gold_coin = 6
seven = 7
bar = 8
apple = 9
heart = 10
grape = 11
diamond = 12
orange = 13
horse_shoe = 14
watermelon = 15
def slot_machine():
    print("Enter a coin to start gambling")
    player = int(input("Press 1 to start, Change your mind press 2"))
    if player == 1:
        luck1 = random.randint(1,15)
        luck2 = random.randint(1,15)
        luck3 = random.randint(1,15)
        print(luck1)
        print(luck2)
        print(luck3)
    if luck1 == 7 and luck2 and luck3 == 7:
            print("You hit a JACKPOT!!")
    elif player == 2:
        print("Good bye")
        exit()
    replay()


def replay():
    letsplay = int(input("If you wold like to play again press 3 if not press 4"))
    if letsplay == "3":
        slot_machine()
    else:
        exit()

slot_machine()



