#Name:
#Class: 5th Hour
#Assignment: Scenario8
import random

#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.
class Game:
    def __init__(self,health,ac,damage,attack_mod):
        self.health = health
        self.ac = ac
        self.damage = damage
        self.attack_mod = attack_mod

LaeZel = Game(12,17,random.randint(1,6) +  random.randint(1,6) + 3,4 )
ShadowHeart = Game(10,14,random.randint(1,6) + 2,4 )
Gale = Game(8,14,random.randint(1,6),4 )
Astarion = Game(10,14,random.randint(1,6) + 4,4 )

Pirate_Monkey = Game(20,14,random.randint(1,6) +  random.randint(1,6) + 1,4 )
Farmer = Game(10, 10,random.randint(1,6),4 )
Wizard = Game(10,10,random.randint(1,6),4 )
Knight = Game(15,10,random.randint(1,6) + 2,4 )

#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)
