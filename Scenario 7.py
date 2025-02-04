#Name:Eric Lin
#Class: 5th Hour
#Assignment: Scenario 7
from Scenario_6 import *
#Import all of Scenario 6 here

listAverage = 0

def final_average():
    global listAverage
    listAverage = sum(stats)/len(stats)#Calculate the sum of the list by the length of the list here
    return listAverage

final_average()

print(listAverage)