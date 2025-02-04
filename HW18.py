#Name: Eric Lin
#Class: 5th Hour
#Assignment: HW18
import random

#1. Import the "random" library and create a def function that prints "Hello World!"
def hello_world():
    print("Hello World!")
hello_world()
#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = ["OrangeBean","PurpleBean","RedBean","BlueBean","GreenBean"]
#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def beans():
    if not beanBag:
        print("Bag is empty")
        exit()
    else:
        beangrabber = random.choice(beanBag)
        print(beangrabber)
        beanBag.remove(beangrabber)





    repeat_bean()




#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def repeat_bean():
    repeat = int(input("1 for yes 2 for no"))
    if repeat == 1:
        beans()
    else:
        exit()
#5. Call the #3 function at the bottom.
beans()