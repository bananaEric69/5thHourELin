#Name: Eric Lin
#Class: 5th Hour
#Assignment: HW16
import random
from os import lseek

#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".

#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.

rock = 1
paper = 2
scissor = 3


def rock_paper_scissors():
    player = int(input("Game had started"))
    bot = random.randint(1,3)
    if player == 1 and bot == 3:
        print("player won")
    elif player == 1 and bot == 2:
        print("bot won")
    elif player == 1 and bot == 1:
        print("its a tie")
    elif player == 2 and bot == 1:
        print("player won")
    elif player == 2 and bot == 3:
        print("bot won")
    elif player == 2 and bot == 2:
        print("its a tie")
    elif player == 3 and bot == 2:
        print("player won")
    elif player == 3 and bot == 1:
        print("bot won")
    elif player == 3 and bot == 3:
        print("its a tie")
    repeat_player()

def repeat_player():
    repeat = int(input("1 for yes 2 for no"))
    if repeat == 1:
        rock_paper_scissors()
    else:
        exit()



rock_paper_scissors()




