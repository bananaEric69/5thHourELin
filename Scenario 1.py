#Name: Eric Lin
#Class: 5th hour
#Assignment: Scenario 1
from dataclasses import replace
from fileinput import filename
from linecache import updatecache

#You are a programmer for a fledgling game developer. Your team lead
#has asked you to create a nested dictionary containing five enemy
#creatures (and their properties) for combat testing. Additionally,
#the testers are asking for a way to input changes to the enemy's print those changes to
#confirm they went through.
#damage for balancing, as well as having it

#It is up to you to decide what properties
#are important and the theme of the game.

#UPDATE: The testers have run into some bugs with your code. Some of the
#code seems to not work correctly. For example, one of the testers changed
#the damage for an enemy to 30 per attack, but when they attacked the player
#character, the health went from 100 to 10030 instead of the intended 70.
#Your team lead has asked you to fix the bug.
#(HINT: The player's health is stored as an integer.)

print("Hello World")

enemies = {
    "Pirate_Monkey" : {
        "Health" : 50,
        "Damage" : 5,
        "Armor" : 10,
    },
    "Farmer" : {
        "Health" : 40,
        "Damage" : 5,
        "Armor" : 0,
},
    "Wizard" : {
        "Health" : 80,
        "Damage" : 15,
        "Armor" : 50,
},
    "Lil_Timmy" : {
        "Health" : 300,
        "Damage" : 5,
        "Armor" : 50,
},
     "Jesus" : {
        "Health" : 600,
        "Damage" : 15,
        "Armor" : 100,
}
}

print(enemies['Pirate_Monkey']['Damage'],enemies['Farmer']['Damage'],enemies['Wizard']['Damage'],enemies['Lil_Timmy']['Damage'],enemies['Jesus']['Damage'])

enemies['Pirate_Monkey']['Damage'] = int(input('monster1'))
enemies['Farmer']['Damage'] = int(input('monster2'))
enemies['Wizard']['Damage'] = int(input('monster3'))
enemies['Lil_Timmy']['Damage'] = int(input('monster4'))
enemies['Jesus']['Damage'] = int(input('monster5'))

print(enemies['Pirate_Monkey']['Damage'],enemies['Farmer']['Damage'],enemies['Wizard']['Damage'],enemies['Lil_Timmy']['Damage'],enemies['Jesus']['Damage'])