#Name:Eric Lin
#Class: 5th Hour
#Assignment: Scenario 4


#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.
player = int(input("Enter a amount of players"))
i = 1
rating_sum = 0
while i <= player:
    rate = int(input("Rate 1-5"))
    if rate > 5 or rate < 1:
        print("error")
    else:
        rating_sum += rate
        i += 1
average = rating_sum / player
print(average)