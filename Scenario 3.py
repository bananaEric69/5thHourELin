#Name: Eric Lin
#Class: 5th Hour
#Assignment: Scenario 3
from pprint import PrettyPrinter
from random import randint

print("Hello WORLD!!!!!!!!!!!!!!!!!!!!!!!!!")

#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Step 1: Copy enemy dictionary from SC1

#Step 2: Copy party dictionary from SC2

#Step 3: Make sure every enemy and party member has health points (fixed)

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4

#Step 4: Make sure every enemy and party member has an attack modifier (fixed)

#Step 5: Make sure every enemy and party member has an armor class (AC) (fixed)

#Step 6: Make every enemy and party member has a damage roll (random)
import random

#Party Dictionary Goes Here
partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Damage" : random.randint(1,6) +  random.randint(1,6) + 3,
        "attack Mod": 4,
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damage" : random.randint(1,6) + 2,
         "attack Mod": 4,
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damage" : random.randint(1,10),
        "attack Mod": 4,
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Damage" : random.randint(1,6) + 4,
        "attack Mod": 4,
    }
}
#Enemy Dictionary Goes Here
enemies = {
    "Pirate_Monkey" : {
        "Health" : 20,
        "Damage" : random.randint(1,6) + random.randint(1,6) + 1,
        "AC" : 14,
        "attack Mod": 4,
    },
    "Farmer" : {
        "Health" : 10,
        "Damage" : random.randint(1,6),
        "AC" : 10,
        "attack Mod" : 4,
},
    "Wizard" : {
        "Health" : 25,
        "Damage" : random.randint(1,6) + 3,
        "AC" : 16,
        "attack Mod": 4,
},
    "Knight" : {
        "Health" : 15,
        "Damage" : random.randint(1,6) + 2,
        "AC" : 10,
        "attack Mod": 4,
},
}

#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#Step 7: Pick a party member

#Step 8: Pick an ememy

#Step 9: Create an attack roll for party member

#Step 10: Compare the party member attack roll to the enemy AC

#Step 11: Subtract damage from enemy health if it hits

#Step 12: Check to see if enemy is still alive

#Step 13: Step 9 through 12, but enemy attacks party member if still alive

#Combat Code Goes Here

if random.randint(1,20) + partyDictionary['Shadowheart']['attack Mod'] >= (enemies["Pirate_Monkey"]["AC"]):
    enemies['Pirate_Monkey']["Health"] -= partyDictionary['Shadowheart']['Damage']
    if enemies['Pirate_Monkey']['Health'] <=0:
        print("Pirate_Monkey has fallen ")
        exit()
    else:
        print("Pirate_MOnkey is still alive")
else:
    print("Missed")
print('enemy Attacks')
if random.randint(1,20) + enemies['Pirate_Monkey']['attack Mod'] >= (partyDictionary["Shadowheart"]["AC"]):
    partyDictionary['Shadowheart']["Health"] -= enemies["Pirate_Monkey"]["Damage"]
    if partyDictionary['Shadowheart']['Health'] <=0:
        print("Shadowheart has fallen ")
        exit()
    else:
        print("Shadow heart is still alive")
else:
    print("Missed")











