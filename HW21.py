#Name:Eric Lin
#Class: 5th Hour
#Assignment: HW21


#1. Make a nested dictionary with three entries called "sport1", "sport2", and "sport3" containing
#the name a sport the school partakes in, the amount of players a typical team uses during gameplay
#(ex: Basketball has 5 players), and if the sport uses a ball or not (as a boolean).
sports = {
    "sport1" : {
    "sport": "basketball",
    "player": 5,
    "ball": True,
},
    "sport2" : {
    "sport" : "soccer",
    "player" : 11,
    "ball" : True,
},
    "sport3" : {
    "sport" : "baseball",
    "player" : 9,
    "ball" : True,
},
}




#2. Create a def function that pulls the values from the dictionary as arguments, adds together the
#players of all three sports, and prints the sum
def sportsum(a,b,c):
    sum = a+b+c
    print(sum)


#3. Call the function with arguments here
sportsum(sports["sport1"]["player"],sports["sport2"]["player"],sports["sport3"]["player"])