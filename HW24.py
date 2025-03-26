#Name:
#Class: 5th Hour
#Assignment: HW24

import random, time




#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.
class Stat:
    def __init__(self, health, damage, speed,max_health):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.max_health = max_health

    def attack(self):
        for x in range(1,11):
            self.health -= random.randint(1,6)
            time.sleep(1)
            print(f'health is now {self.health}')


    def heal(self):
        self.health += 30
        if self.health > 100:
            self.health = 100
            print(self.health)
        else:
            print(f"health is {self.health}")



#2. Create a fourth attribute in the class called max_health that has the same values as health

#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute values: thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)
Warrior = Stat(100, 20, 30, 100)
Healer = Stat(60, 10, 30, 60)
Thief = Stat(50, 30, 40, 50)
Mage = Stat(45, 35, 25, 45)
#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
losing_Hp = random.randint(1,4)

if losing_Hp == 1:
    Warrior.attack()
elif losing_Hp == 2:
    Healer.attack()
elif losing_Hp == 3:
    Thief.attack()
elif losing_Hp == 4:
    Mage.attack()


#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling your healing function to that object and then print their health afterward.

if Warrior.health < Warrior.max_health:
    Warrior.heal()
elif Healer.health < Healer.max_health:
    Healer.heal()
elif Thief.health < Thief.max_health:
    Thief.heal()
elif Mage.health < Mage.max_health:
    Mage.heal()