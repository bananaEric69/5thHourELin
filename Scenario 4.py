#Name:Eric Lin
#Class: 5th Hour
#Assignment: Scenario 4
from lib2to3.fixes.fix_input import context

#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
x = 0

print("Hello world")
while 5 < 3:

player = int(input())
print(player)
print("add how many player you need that is more than 0")
if player <= 12:
    print("more than 0 please")

player = int(input())
print(player)
if player < 5:
    print("Give a rating more than 0")
